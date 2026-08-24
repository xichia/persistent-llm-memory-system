# Personal memory

Preferences, interests, recurring decisions, and knowledge that should follow you across chats — without living in a product's hidden memory feature.

## What belongs here

- Standing facts: location, role, constraints ([../structure/person/profile.md](../structure/person/profile.md))
- Defaults that should change model behavior ([../structure/person/preferences.md](../structure/person/preferences.md))
- Tone and format ([../structure/person/communication.md](../structure/person/communication.md))
- Recurring life or work decisions ("I don't use cloud X", "always prefer local-first")
- Interests and knowledge topics that keep coming back (`knowledge/<topic>/`)

## What does not

- Every chat about dinner or a one-off error
- Secrets
- Information that is already in a calendar, contacts app, or password manager

## Why a folder beats built-in "memory"

Vendor memory is tied to one account and one model family. It is hard to inspect, correct, or export. A `person/` directory is all of those things by default, and the same files work in ChatGPT, Claude, Grok, or a local model.

You can also *not* load personal files. A project-only session reads `.me/` or `projects/<name>/` and leaves the profile on disk.

## Retrieval pattern

For a general personal assistant session: `profile.md` + `preferences.md` + `communication.md`. That is usually a sufficient working set. Pull a knowledge topic only when the question is about that topic.

Update in place when the person changes their mind. A preference that flipped should not remain in the file as archaeology — put the flip in a log if you care, then change the preference.
