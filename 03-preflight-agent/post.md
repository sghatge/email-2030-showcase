Most campaign mistakes are visible before the send. Nobody checks until after.

I built a pre-flight agent for Adobe Campaign v8 deliveries. It reads delivery metadata and runs eight checks.

1. Rules decide the verdict: PASS, RISK, FAIL or NOT_READY. No LLM is involved in pass or fail.
2. It catches the boring killers: missing suppression, no unsubscribe or mirror page, an audience that silently shrank, a send time that is not valid.
3. A human can override, but only with a named approver and a written reason, recorded in an append-only audit log.

It is read-only and runs on synthetic data, with zero runtime dependencies and 28 tests.

By 2030, QA will be an agent step before every send. The sign-off will still be human.

Live demo: https://sghatge.github.io/campaign-v8-preflight-agent/app/demo.html

Agents check. Humans decide.
