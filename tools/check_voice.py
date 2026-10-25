"""Prüft, ob eine neue ElevenLabs-Aufnahme dieselbe Stimme wie die Referenz hat.

Aufruf:  python3 tools/check_voice.py <audio.mp3> [Original-Dateiname]
         python3 tools/check_voice.py --set-reference <audio.mp3> <Original-Dateiname>

Geprüft werden (1) Stimmname + Einstellungen aus dem ElevenLabs-Dateinamen und
(2) akustische Merkmale: Grundtonhöhe (Median F0) und Klangfarbe (Spektralschwerpunkt).
"""
import sys, re, json, subprocess, os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
PROFILE = os.path.join(HERE, "voice_profile.json")
SR = 16000

def load(path):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.float32)

def features(x):
    frame, hop = 1024, 512
    f0s, cents = [], []
    win = np.hanning(frame)
    freqs = np.fft.rfftfreq(frame, 1 / SR)
    for i in range(0, len(x) - frame, hop):
        fr = x[i:i + frame]
        rms = np.sqrt(np.mean(fr ** 2))
        if rms < 0.02:
            continue
        spec = np.abs(np.fft.rfft(fr * win))
        cents.append(float(np.sum(freqs * spec) / (np.sum(spec) + 1e-9)))
        ac = np.correlate(fr, fr, "full")[frame - 1:]
        lo, hi = SR // 400, SR // 60          # 60–400 Hz
        lag = lo + int(np.argmax(ac[lo:hi]))
        if ac[lag] > 0.3 * ac[0]:
            f0s.append(SR / lag)
    return {"f0_median": round(float(np.median(f0s)), 1), "centroid_median": round(float(np.median(cents)), 1)}

def parse_name(name):
    m = re.search(r"ElevenLabs_[\dT_-]+_(.+?)_pvc_(.+?)(?:_\d+)?\.mp3$", name or "")
    return (m.group(1).replace("_", " "), m.group(2)) if m else (None, None)

def main():
    if sys.argv[1] == "--set-reference":
        audio, orig = sys.argv[2], sys.argv[3]
        voice, settings = parse_name(orig)
        prof = {"voice_id": "VGcePI2GWNz1BlgRb8wB", "voice_name": voice, "settings": settings,
                "reference_file": orig, **features(load(audio))}
        json.dump(prof, open(PROFILE, "w"), indent=2, ensure_ascii=False)
        print("Referenz gespeichert:", prof); return
    audio = sys.argv[1]; orig = sys.argv[2] if len(sys.argv) > 2 else os.path.basename(audio)
    ref = json.load(open(PROFILE)); f = features(load(audio))
    voice, settings = parse_name(orig)
    ok = True
    print(f"Referenz: {ref['voice_name']} [{ref['settings']}]  F0 {ref['f0_median']} Hz  Klang {ref['centroid_median']} Hz")
    print(f"Neu:      {voice} [{settings}]  F0 {f['f0_median']} Hz  Klang {f['centroid_median']} Hz")
    if voice is None:
        print("⚠️  Stimmname nicht im Dateinamen – nur akustisch geprüft.")
    elif voice != ref["voice_name"] or settings != ref["settings"]:
        print("❌ Stimmname oder Einstellungen weichen ab!"); ok = False
    df0 = abs(f["f0_median"] - ref["f0_median"]) / ref["f0_median"]
    dc = abs(f["centroid_median"] - ref["centroid_median"]) / ref["centroid_median"]
    print(f"Abweichung Tonhöhe {df0:.1%} (Grenze 8 %), Klangfarbe {dc:.1%} (Grenze 12 %)")
    if df0 > 0.08 or dc > 0.12:
        print("❌ Akustisch deutliche Abweichung – bitte Stimme in ElevenLabs prüfen."); ok = False
    print("✅ Gleiche Stimme." if ok else "➡️  Nicht freigegeben.")
    sys.exit(0 if ok else 1)

main()
