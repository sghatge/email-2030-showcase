AI agents are coming into Campaign. Who checks what they do?

I built a gate that sits between an agent and Adobe Campaign. Every call is checked against a written policy before it runs.

1. Five outcomes: allow, mask PII, dry-run, send for human approval, or block.
2. In my synthetic Black Friday session, 28 agent calls led to 12 allowed, 5 sent for approval and 9 blocked, including a full-table DELETE and a 50,000-row PII export.
3. Every decision goes into a hash-chained audit log. Edit one entry and verification fails.

By 2030 the question will not be whether agents can operate campaigns. It will be what they are allowed to do, and whether you can prove it afterwards.

Demo (synthetic data, no real Adobe instance): https://sghatge.github.io/acc-agent-gate/

Agents propose. A gate decides.
