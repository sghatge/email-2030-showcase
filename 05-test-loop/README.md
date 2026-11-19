# Post 5: Self-optimizing test loop

2030 shift: tests run continuously and the system only declares a winner when the data supports it.

Adobe's Experimentation Agent (AJO Experimentation Accelerator) works on this idea at scale. This demo is a tiny version on synthetic numbers: a two-proportion z-test that refuses to pick a winner below a minimum sample (default 500 sends per variant) or when the difference is not significant (p >= 0.05).

Run: `python demo.py` | Test: `python -m pytest -q`
