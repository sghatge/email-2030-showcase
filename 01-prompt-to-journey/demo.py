"""Rule-based stand-in for 'plain-English brief to journey spec'. No LLM, synthetic only."""
import re

CHANNELS = ["email", "sms", "push", "whatsapp"]

def brief_to_spec(brief: str) -> dict:
    text = (brief or "").strip()
    spec = {"status": "ok", "audience": None, "channel": None, "trigger": None,
            "steps": [], "open_questions": []}
    if not text:
        spec["status"] = "needs_detail"
        spec["open_questions"].append("Describe the audience, channel and timing.")
        return spec
    low = text.lower()
    for c in CHANNELS:
        if c in low:
            spec["channel"] = c
            break
    m = re.search(r"after (\w+)", low)
    if m:
        spec["trigger"] = m.group(1)
    parts = [p.strip() for p in re.split(r",\s*then\s+|\bthen\b", text) if p.strip()]
    for p in parts:
        delay = re.search(r"(\d+)\s*day", p.lower())
        cond = "if not opened" in p.lower()
        label = p
        if delay:
            label += f" (wait {delay.group(1)} day(s))"
        if cond:
            label += " [condition: not opened]"
        spec["steps"].append(label)
    if spec["channel"] is None:
        spec["open_questions"].append("Which channel?")
    if "signup" not in low and "purchase" not in low and "cart" not in low:
        spec["open_questions"].append("What event starts the journey?")
    if spec["channel"] is None and not spec["steps"]:
        spec["status"] = "needs_detail"
    return spec

if __name__ == "__main__":
    import json
    print(json.dumps(brief_to_spec("Welcome email 1 day after signup, then reminder after 3 days if not opened"), indent=2))
