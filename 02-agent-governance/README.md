# Post 2: Agents propose, a gate decides

2030 shift: AI agents will operate inside campaign platforms. The question moves from "can the agent do it" to "what is it allowed to do, and can we prove what happened".

Demo: [ACC Agent Gate](https://github.com/sghatge/acc-agent-gate), a governance layer between AI agents and Adobe Campaign. Every tool call is checked against a written policy (allow, allow_masked, dry_run, needs_approval, block) and logged in a hash-chained audit log.

Facts from the repo README (synthetic session, fictional brand): 28 agent calls, 12 allowed, 1 masked, 1 dry-run, 5 sent for approval, 9 blocked. 24 tests. Interactive demo: https://sghatge.github.io/acc-agent-gate/

Not claimed: this does not connect to a real Adobe instance in the demo.
