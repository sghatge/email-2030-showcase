# Post 4: Email for AI inboxes

2030 shift: inbox assistants summarize and prioritize messages before a person reads them, so structure and plain text matter more than pixels.

The checker scores an HTML email 0 to 100 with reasons: readable text, one heading, descriptive link text, alt text, a call to action. These rules are my own heuristic, not an industry standard.

Run: `python demo.py` (scores the three files in sample_emails) | Test: `python -m pytest -q`
