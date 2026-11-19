"""Heuristic AI-readability score for an HTML email (my own rules, not an industry standard)."""
from html.parser import HTMLParser

class _P(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text, self.imgs, self.imgs_no_alt, self.headings = [], 0, 0, 0
        self.links, self.bad_links, self._a, self._abuf = 0, 0, False, []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "img":
            self.imgs += 1
            if not (a.get("alt") or "").strip():
                self.imgs_no_alt += 1
        elif tag in ("h1", "h2", "h3"):
            self.headings += 1
        elif tag == "a":
            self._a, self._abuf = True, []
            self.links += 1
    def handle_endtag(self, tag):
        if tag == "a" and self._a:
            label = "".join(self._abuf).strip().lower()
            if label in ("", "click here", "here", "link", "read more"):
                self.bad_links += 1
            self._a = False
    def handle_data(self, data):
        s = data.strip()
        if s:
            self.text.append(s)
            if self._a:
                self._abuf.append(s)

def score_email(html: str) -> dict:
    if not (html or "").strip():
        return {"score": 0, "reasons": ["Empty email: nothing for an AI inbox to read."],
                "has_plain_text_alt": False}
    p = _P()
    p.feed(html)
    words = sum(len(t.split()) for t in p.text)
    reasons, score = [], 100
    if words < 10:
        score -= 70
        reasons.append("Almost no readable text; content is mostly image.")
    if p.imgs and words < 10:
        reasons.append("Image-only content cannot be summarized by an AI inbox.")
    if p.headings == 0:
        score -= 15
        reasons.append("No heading to anchor the summary.")
    if p.imgs_no_alt:
        score -= 10
        reasons.append(f"{p.imgs_no_alt} image(s) without alt text.")
    if p.bad_links:
        score -= 10
        reasons.append("Vague link text (e.g. 'click here').")
    if p.links == 0:
        score -= 5
        reasons.append("No clear call to action link.")
    return {"score": max(score, 0), "reasons": reasons, "has_plain_text_alt": "text/plain" in html.lower()}

if __name__ == "__main__":
    import glob
    for f in sorted(glob.glob("sample_emails/*.html")):
        r = score_email(open(f).read())
        print(f, r["score"], r["reasons"])
