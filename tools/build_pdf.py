"""Render guide.md as a four-page field guide. Requires reportlab."""
from pathlib import Path
import os
import re
from html import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Flowable, Paragraph, Preformatted, Spacer
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'output/pdf/course-guide.pdf'
REPO = 'https://github.com/xichia/persistent-llm-memory-system/blob/main/'
W, H = A4
TEAL = colors.HexColor('#294f50')
GOLD = colors.HexColor('#e3cc8b')
INK = colors.HexColor('#192c2c')
MUTED = colors.HexColor('#5c6865')
PAPER = colors.HexColor('#f7f6f1')


def register_fonts():
    """Use the original Liberation faces when installed; metric equivalents otherwise."""
    roots = [Path(os.environ.get('PDF_FONT_DIR', '/usr/share/fonts/truetype/liberation2')),
             Path('/usr/share/fonts/truetype/liberation'), Path('/Library/Fonts')]
    roots += list((Path.home() / '.cache/codex-runtimes').glob(
        '*/dependencies/native/libreoffice-headless/libreoffice/*.app/Contents/Resources/fonts/truetype'))
    faces = {'Serif': ('LiberationSerif-Regular.ttf', 'Times-Roman'),
             'Italic': ('LiberationSerif-Italic.ttf', 'Times-Italic'),
             'Sans': ('LiberationSans-Regular.ttf', 'Helvetica'),
             'Bold': ('LiberationSans-Bold.ttf', 'Helvetica-Bold'),
             'Mono': ('LiberationMono-Regular.ttf', 'Courier')}
    names = {}
    for name, (filename, fallback) in faces.items():
        source = next((r / filename for r in roots if (r / filename).exists()), None)
        if source:
            pdfmetrics.registerFont(TTFont(name, str(source)))
            names[name] = name
        else:
            names[name] = fallback
    return names


FONT = register_fonts()
BODY = ParagraphStyle('body', fontName=FONT['Serif'], fontSize=11.5, leading=16.5,
                      textColor=INK, spaceAfter=12, alignment=TA_LEFT)
CODE = ParagraphStyle('code', fontName=FONT['Mono'], fontSize=9, leading=14,
                      textColor=TEAL)
LABEL = ParagraphStyle('label', fontName=FONT['Sans'], fontSize=9.5, leading=13,
                       textColor=MUTED)


def rich(text):
    text = escape(text)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', lambda m:
                  '<a href="' + (m[2] if '://' in m[2] else REPO + m[2]) +
                  '" color="#294f50"><u>' + m[1] + '</u></a>', text)
    text = re.sub(r'`([^`]+)`', lambda m:
                  '<font name="' + FONT['Mono'] + '" size="9.5">' + m[1] + '</font>', text)
    return re.sub(r'\*\*(.+?)\*\*', lambda m:
                  '<font name="' + FONT['Bold'] + '">' + m[1] + '</font>', text)


class CodeCard(Flowable):
    def __init__(self, text):
        super().__init__()
        # Keep portable box drawing even with PDF base fonts.
        text = text.translate(str.maketrans({'├': '+', '└': '+', '─': '-', '│': '|'}))
        self.text = text
        self.is_tree = '\n+-- ' in text

    def wrap(self, width, height):
        self.width = width
        # Compact tree labels; full meanings stay in the following paragraph.
        text = self.text
        if self.is_tree:
            text = re.sub(r'(?<=\S) {3,}[^\n]+', '', text)
        if any(pdfmetrics.stringWidth(line, FONT['Mono'], CODE.fontSize) > width - 28 for line in text.splitlines()):
            raise ValueError('Code line too wide; wrap the source prompt.')
        self.pre = Preformatted(text, CODE)
        _, self.inner_height = self.pre.wrap(width - 28, height)
        self.height = self.inner_height + 26
        return width, self.height

    def draw(self):
        c = self.canv
        c.setFillColor(PAPER)
        c.setStrokeColor(TEAL)
        c.setLineWidth(.65)
        c.roundRect(0, 0, self.width, self.height, 2, fill=1, stroke=1)
        self.pre.drawOn(c, 14, 13)


def flowables(markdown):
    items = []
    for n, block in enumerate(re.split(r'(```[^\n]*\n.*?```)', markdown, flags=re.S)):
        if n % 2:
            items += [CodeCard(block.split('\n', 1)[1].rsplit('```', 1)[0].rstrip()), Spacer(1, 14)]
        else:
            for paragraph in re.split(r'\n\s*\n', block.strip()):
                if paragraph:
                    items.append(Paragraph(rich(' '.join(paragraph.splitlines())), BODY))
    return items


def tracked(c, text, x, y, size=8, spacing=2, centered=False):
    c.saveState()
    t = c.beginText()
    t.setFont(FONT['Sans'], size)
    t.setCharSpace(spacing)
    width = pdfmetrics.stringWidth(text, FONT['Sans'], size) + spacing * (len(text) - 1)
    t.setTextOrigin(x - width / 2 if centered else x, y)
    t.textOut(text)
    c.drawText(t)
    c.restoreState()


def cover(c):
    c.setFillColor(TEAL)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setStrokeColor(colors.HexColor('#365b59'))
    c.setLineWidth(.25)
    for y in range(0, int(H), 5):
        c.line(0, y, W, y)
    c.setStrokeColor(GOLD)
    c.setLineWidth(.55)
    c.rect(49, 114, W - 98, H - 174, fill=0, stroke=1)
    c.setFillColor(GOLD)
    tracked(c, 'A PRACTICAL FIELD GUIDE', W / 2, H - 105, centered=True)
    c.setFont(FONT['Italic'], 24)
    c.drawCentredString(W / 2, H - 175, 'The')
    c.setFont(FONT['Serif'], 43)
    c.drawCentredString(W / 2, H - 224, 'LIVING')
    c.setFont(FONT['Serif'], 39)
    c.drawCentredString(W / 2, H - 276, 'REPOSITORY')
    c.setFont(FONT['Serif'], 17)
    c.drawCentredString(W / 2, H - 330, 'Project memory with Codex')
    tracked(c, 'READ  ·  SHAPE  ·  RETURN', W / 2, H - 396, centered=True)
    c.circle(368, 324, 39, fill=1, stroke=0)
    c.setFillColor(colors.HexColor('#71816b'))
    path = c.beginPath()
    path.moveTo(49, 300)
    path.curveTo(180, 330, 326, 275, W - 49, 308)
    path.lineTo(W - 49, 114)
    path.lineTo(49, 114)
    path.close()
    c.drawPath(path, fill=1, stroke=0)
    c.setFillColor(colors.HexColor('#4c655e'))
    path = c.beginPath()
    path.moveTo(49, 254)
    path.curveTo(206, 293, 370, 234, W - 49, 266)
    path.lineTo(W - 49, 114)
    path.lineTo(49, 114)
    path.close()
    c.drawPath(path, fill=1, stroke=0)
    c.setFillColor(colors.HexColor('#b2a371'))
    path = c.beginPath()
    path.moveTo(49, 136)
    path.curveTo(172, 140, 255, 246, 395, 286)
    path.curveTo(284, 239, 262, 151, 312, 114)
    path.lineTo(49, 114)
    path.close()
    c.drawPath(path, fill=1, stroke=0)
    c.setFillColor(GOLD)
    tracked(c, 'ONE FOLDER  ·  THREE PROJECT FILES', W / 2, 92, spacing=1, centered=True)
    c.showPage()


def frame(c, number, title):
    c.setFillColor(MUTED)
    c.setFont(FONT['Sans'], 8)
    c.drawString(45, H - 25, 'The Living Repository')
    c.setStrokeColor(colors.HexColor('#aaa79b'))
    c.setLineWidth(.45)
    c.line(45, H - 31, W - 45, H - 31)
    c.line(45, 28, W - 45, 28)
    c.setFont(FONT['Sans'], 7.5)
    c.drawString(45, 18, 'THE LIVING REPOSITORY  ·  FIELD GUIDE')
    c.drawRightString(W - 45, 18, str(number))
    c.setFillColor(TEAL)
    c.setFont(FONT['Serif'], 23)
    c.drawString(45, H - 64, title)


def put(c, items, y, floor=55):
    for item in items:
        _, height = item.wrap(W - 90, H)
        if y - height < floor:
            raise ValueError('Content overflow: shorten guide.md or adjust the page layout.')
        item.drawOn(c, 45, y - height)
        y -= height + item.getSpaceAfter()
    return y


def cycle(c, y):
    """A compact visual of the repeatable workflow; echoes the original map cards."""
    captions = [('READ', 'Relevant files'), ('SHAPE', 'One useful task'), ('CHECK', 'Saved result'), ('RETURN', 'Fresh chat')]
    gap = 9
    width = (W - 90 - gap * 3) / 4
    for i, (label, caption) in enumerate(captions):
        x = 45 + i * (width + gap)
        c.setFillColor(PAPER)
        c.setStrokeColor(TEAL)
        c.setLineWidth(.6)
        c.roundRect(x, y - 68, width, 68, 2, fill=1, stroke=1)
        c.setFillColor(TEAL)
        c.setFont(FONT['Bold'], 9)
        c.drawCentredString(x + width / 2, y - 26, label)
        c.setFont(FONT['Sans'], 8)
        c.drawCentredString(x + width / 2, y - 45, caption)


def main():
    source = (ROOT / 'guide.md').read_text()
    chunks = re.split(r'^## (\d\. .+)$', source, flags=re.M)
    if len(chunks) != 7:
        raise ValueError('Expected exactly three numbered guide sections.')
    intro = re.sub(r'^# .+\n', '', chunks[0]).strip()
    sections = [(chunks[i], chunks[i + 1].strip()) for i in (1, 3, 5)]
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(OUTPUT), pagesize=A4, pageCompression=1, invariant=1)
    c.setTitle('The Living Repository - Project memory with Codex')
    c.setAuthor('The Living Repository')
    c.setSubject('A concise guide to persistent project context in Markdown')
    cover(c)
    for page, (title, text) in enumerate(sections, start=2):
        frame(c, page, title)
        y = H - 88
        if page == 2:
            y = put(c, flowables(intro), y)
            y -= 4
        y = put(c, flowables(text), y)
        if page == 4:
            cycle(c, y - 28)
            put(c, [Paragraph('Read less old chat. Keep a clear next step.', LABEL)], y - 127)
            c.linkURL(REPO + 'guide.md', (45, 58, W - 45, 76), relative=0, thickness=0)
            c.setFillColor(TEAL)
            c.setFont(FONT['Sans'], 8)
            c.drawString(45, 62, 'Guide and starter: github.com/xichia/persistent-llm-memory-system')
        c.showPage()
    c.save()
    print(OUTPUT)


if __name__ == '__main__':
    main()
