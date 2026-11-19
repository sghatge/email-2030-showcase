from demo import pick_winner

def test_below_min_sample():
    assert pick_winner({"A": (100, 5), "B": (100, 9)})["status"] == "not_enough_data"

def test_zero_conversions():
    assert pick_winner({"A": (1000, 0), "B": (1000, 0)})["status"] == "not_enough_data"

def test_clear_winner():
    r = pick_winner({"A": (2000, 40), "B": (2000, 90)})
    assert r["status"] == "winner" and r["winner"] == "B"
