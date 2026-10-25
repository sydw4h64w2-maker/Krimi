"""Einheitliche Lautstärke: Stimme -16 LUFS, Effekte deutlich darunter.

sfx_volume(name, rel) liefert den data-volume-Wert für einen Effekt, gemessen an
seiner eigenen Lautheit, damit kein Effekt lauter als die Stimme wird.
"""
import subprocess, re, functools, os

VOICE_LUFS = -16.0
SFX_TARGET = {"impact": -29.0, "default": -31.0}   # 13–15 dB unter der Stimme
SFX_DIR = os.path.join(os.path.dirname(__file__), "..", "faelle", "001-antwerpen", "video", "assets", "sfx")

@functools.lru_cache(None)
def lufs(path):
    out = subprocess.run(["ffmpeg", "-i", path, "-af", "ebur128", "-f", "null", "-"], capture_output=True, text=True).stderr
    m = re.findall(r"I:\s+(-?[\d.]+) LUFS", out)
    return float(m[-1])

def sfx_volume(name, rel=1.0):
    i = lufs(os.path.join(SFX_DIR, name + ".mp3"))
    if i < -60:            # praktisch stumm (Klicks) – nicht hochziehen
        return round(0.5 * rel, 3)
    target = SFX_TARGET["impact"] if name.startswith("impact") else SFX_TARGET["default"]
    return round(min(3.0, rel * 10 ** ((target - i) / 20)), 3)

def normalize_voice(src, dst):
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", src, "-af",
                    f"loudnorm=I={VOICE_LUFS}:TP=-1.5:LRA=11", "-ar", "44100", "-ac", "2", "-b:a", "192k", dst], check=True)
