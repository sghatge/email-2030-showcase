from demo import brief_to_spec

def test_empty_brief_needs_detail():
    assert brief_to_spec("")["status"] == "needs_detail"

def test_welcome_brief():
    s = brief_to_spec("Welcome email 1 day after signup, then reminder after 3 days if not opened")
    assert s["status"] == "ok"
    assert s["channel"] == "email"
    assert len(s["steps"]) == 2
