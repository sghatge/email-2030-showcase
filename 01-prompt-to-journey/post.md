In 2030, you will describe a journey. You will not drag boxes.

Adobe's Journey Agent already lets Journey Optimizer users create and optimize journeys in natural language. I wanted to see what the handoff looks like, so I built a tiny version.

1. Input: "Welcome email 1 day after signup, then reminder after 3 days if not opened."
2. Output: a structured spec with the channel, the steps, the delays, the condition, and a list of open questions.
3. A human reviews the spec before anything is built.

My demo is rule-based, not an LLM. It only shows the shape: plain-English brief in, reviewable spec out, questions flagged instead of guessed.

The skill that matters is not clicking. It is writing a brief that leaves no open questions.

Demo and tests: https://github.com/sghatge/email-2030-showcas
