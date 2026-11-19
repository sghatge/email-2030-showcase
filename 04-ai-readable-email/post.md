Your next reader may be an AI inbox, not a person.

Inbox assistants are starting to summarize and prioritize mail before anyone opens it. An email that is one big image gives them nothing to summarize.

I built a small checker that scores an HTML email from 0 to 100 and says why.

1. Image-only banner: 0. No readable text, no heading, no alt text.
2. Vague "click here" link and missing heading: 65.
3. Clear heading, plain sentence, a link that says what it does: 100.

The rules are my own heuristic, not a standard. The point is the habit: write email that a machine can read as easily as a person.

By 2030, "does it render in Outlook" will share the checklist with "can an AI summarize it".

Demo and tests: https://github.com/sghatge/email-2030-showcas
