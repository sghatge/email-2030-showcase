"""Tiny experiment loop: pick a winner only when the data supports it. Synthetic data."""
import math

def pick_winner(variants: dict, min_sample: int = 500) -> dict:
    names = list(variants)
    if len(names) < 2:
        return {"status": "not_enough_data", "winner": None, "explanation": "Need at least two variants."}
    for n in names:
        sends, conv = variants[n]
        if sends < min_sample:
            return {"status": "not_enough_data", "winner": None,
                    "explanation": f"{n} has {sends} sends; minimum is {min_sample}."}
    if sum(c for _, c in variants.values()) == 0:
        return {"status": "not_enough_data", "winner": None, "explanation": "No conversions yet."}
    ranked = sorted(names, key=lambda n: variants[n][1] / variants[n][0], reverse=True)
    a, b = ranked[0], ranked[1]
    (na, ca), (nb, cb) = variants[a], variants[b]
    pa, pb = ca / na, cb / nb
    pool = (ca + cb) / (na + nb)
    se = math.sqrt(pool * (1 - pool) * (1 / na + 1 / nb))
    if se == 0:
        return {"status": "not_enough_data", "winner": None, "explanation": "No variation to compare."}
    z = (pa - pb) / se
    p = math.erfc(abs(z) / math.sqrt(2))
    if p < 0.05:
        return {"status": "winner", "winner": a,
                "explanation": f"{a} converts {pa:.2%} vs {b} {pb:.2%} (p={p:.4f})."}
    return {"status": "not_enough_data", "winner": None,
            "explanation": f"Difference not significant (p={p:.3f}). Keep testing."}

if __name__ == "__main__":
    print(pick_winner({"A": (2000, 40), "B": (2000, 90)}))
