# Post 3: QA moves before the send

2030 shift: pre-send QA becomes an agent step, but the verdict stays rule-based and a human signs off.

Demo: [Campaign v8 Pre-flight Agent](https://github.com/sghatge/campaign-v8-preflight-agent). Eight deterministic checks (PF-01 to PF-08) return PASS, RISK, FAIL or NOT_READY. No LLM decides pass or fail. Any human override is logged with a named approver and a written reason.

Facts from the repo README: read-only, synthetic data, no send capability, zero runtime dependencies, 28 tests. Live demo: https://sghatge.github.io/campaign-v8-preflight-agent/app/demo.html
