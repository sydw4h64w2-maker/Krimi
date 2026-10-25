"""Erzeugt ein geschätztes Timing (gleiches Format wie align.py), solange noch keine Aufnahme da ist.
Aufruf: python3 tools/predict_timing.py <elevenlabs.txt> <out.json>"""
import re, json, sys
text = re.sub(r'<break[^>]*/>', ' ', open(sys.argv[1]).read())
parts = re.split(r'(?<=[.?!:,–])\s+|\s+(?=\.\.\.)|(?<=\.\.\.)\s+', ' '.join(text.split()))
units = [p.strip() for p in parts if p.strip() and p.strip() != '...']
syl = lambda w: max(1, len(re.findall(r'[aeiouäöüy]+', w.lower())))
RATE, PAUSE = 0.215, 0.42          # Mittelwerte aus den bisherigen Hans-Aufnahmen
t, words, ut = 0.0, [], []
for u in units:
    ut.append((round(t, 3), u))
    for w in u.split():
        d = syl(w) * RATE
        words.append({"text": w, "start": round(t, 3), "end": round(t + d, 3)}); t += d
    t += PAUSE
json.dump({"words": words, "units": ut, "estimated": True}, open(sys.argv[2], 'w'), ensure_ascii=False, indent=0)
print(f"geschätzte Länge: {t:.1f} s, {len(units)} Abschnitte")
