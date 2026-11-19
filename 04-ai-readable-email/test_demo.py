from demo import score_email

def test_image_only_email_scores_low():
    r = score_email('<html><body><img src="a.png"></body></html>')
    assert r["score"] < 30
    assert any("image" in x.lower() for x in r["reasons"])

def test_empty_html():
    assert score_email("")["score"] == 0

def test_clear_text_email():
    html = ('<html><body><h1>Your order has shipped</h1>'
            '<p>Your order 1042 left our warehouse today and arrives Friday.</p>'
            '<p><a href="https://x.test/track">Track your order</a></p></body></html>')
    assert score_email(html)["score"] >= 70
