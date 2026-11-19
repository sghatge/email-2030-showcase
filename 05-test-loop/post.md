The best A/B test tool says "not enough data" more often than you expect.

Adobe's Experimentation Agent points toward testing that runs all the time. I built a tiny version of the core rule to see what it must refuse to do.

1. Two variants, each needs at least 500 sends before it can win.
2. Zero conversions on both sides: no winner, no crash.
3. 2.0% vs 4.5% on 2,000 sends each: winner declared, with the numbers shown.

Synthetic data, standard library only, tested.

By 2030, nobody will pick winners by eye. The edge will be a system that knows when to stay quiet and keep testing.

Demo and tests: https://github.com/sghatge/email-2030-showcas
