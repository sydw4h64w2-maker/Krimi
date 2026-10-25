# Ablauf: Wer macht was?

| Schritt | Wer | Ergebnis |
|---|---|---|
| 1. Fall auswählen & recherchieren | Claude | Faktenblatt mit Quellen |
| 2. Sprechertext schreiben | Claude | `skript.md` (ca. 60–75 s) |
| 3. Faktencheck & Freigabe | **Du** | kurzes OK oder Änderungswunsch |
| 4. Audio aufnehmen | **Du** | `audio.m4a` / `.mp3` / `.wav` hochladen |
| 5. Video bauen (Untertitel, Grafiken, Musik, 9:16) | Claude | fertige `video.mp4` |
| 6. Posten (TikTok, Reels, Shorts) + Caption & Hashtags | **Du** (Caption liefert Claude) | Video online |

## Ausrichtung

- **Fälle aus der ganzen Welt**, gesprochen auf Deutsch.
- Bevorzugt abgeschlossene Fälle (Urteil) oder historische Fälle; dazu berühmte ungelöste Fälle.

## Video-Vorgaben

- **Keine Untertitel** (Wunsch ab Folge 2). Der Text auf dem Bildschirm kommt nur aus den Grafik-Einblendungen.
- **Lautstärke:** Stimme wird auf −16 LUFS normalisiert; jeder Soundeffekt wird einzeln eingemessen und liegt 13–15 dB unter der Stimme (`tools/audio_levels.py`). Musik nur als leiser Teppich. Kein Effekt darf lauter als die Stimme sein.
- Hochformat 1080×1920, Akten-Look (dunkel, Absperrband gelb/schwarz, rote Stempel).

## Recherche-Regeln

- Jede Aussage im Skript steht in der Faktencheck-Tabelle mit mindestens einer seriösen Quelle
  (Zeitung, Gericht, Biografie). Widersprechen sich Quellen, wird das im Text gesagt oder die Aussage gestrichen.
- Was nicht sicher belegt ist, kommt nicht ins Video – auch wenn es spannend wäre.
- Keine erfundenen Dialoge, Gedanken oder Szenen. Nur was dokumentiert ist.
- Daten, Orte, Summen und Urteile werden einzeln geprüft.
- Internationale Fälle: englische Primärquellen (Gericht, große Medien) vor Blogs; Blogs nur ergänzend.

## Ordnerstruktur

```
faelle/
  001-antwerpen/   (Folge 1)
  002-dbcooper/    (Folge 2)
  003-dagobert/    (Folge 3)
  004-postzug/     (Folge 4)
  <nr>-<fall>/
    skript.md     # Sprechertext + Caption + Quellen
    audio.*       # deine Aufnahme
    video.mp4     # fertiges Video
```

## Stimme (ElevenLabs)

- **Voice-ID:** `VGcePI2GWNz1BlgRb8wB`
- Modell: Eleven Multilingual v2 (versteht `<break time="…" />`-Pausen)
- Startwerte: Stability 45–55 %, Similarity ~75 %, Style 0–15 %
- Pro Folge liegt der fertige Text in `faelle/<nr>/elevenlabs.txt`.
- Referenzstimme: **Hans – Clear and Soft**, Einstellungen `sp100_s50_sb75_v4` (aus dem ElevenLabs-Dateinamen).
- **Bei jeder neuen Aufnahme zuerst prüfen:** `python3 tools/check_voice.py <audio.mp3> "<Original-Dateiname>"`
  vergleicht Stimmname, Einstellungen, Tonhöhe und Klangfarbe mit Folge 1. Erst bei ✅ wird das Video gebaut.

| Folge | Original-Datei | Prüfung |
|---|---|---|
| 001 | ElevenLabs_2026-10-25T14_11_47_Hans_-_Clear_and_Soft_pvc_sp100_s50_sb75_v4_2.mp3 | Referenz |
| 002 | ElevenLabs_2026-10-25T14_46_19_Hans_-_Clear_and_Soft_pvc_sp100_s50_sb75_v4.mp3 | ✅ Tonhöhe 1,9 %, Klang 1,6 % |
| 003 | ElevenLabs_2026-10-25T16_02_45_Hans_-_Clear_and_Soft_pvc_sp100_s50_sb75_v4.mp3 | ✅ Tonhöhe 0,0 %, Klang 0,8 % |

## Tipps für die Aufnahme

- Ruhiger Raum, Handy ca. 20 cm vom Mund, gern unter einer Decke oder im Kleiderschrank (dämpft Hall).
- Langsam und mit Pausen sprechen, vor allem nach dem Hook.
- Versprecher nicht neu starten, einfach den Satz wiederholen – ich schneide das raus.

## Grenzen (ehrlich)

- Ich kann nicht selbst posten, Accounts bedienen oder Kommentare beantworten.
- Fotos echter Personen / Tatorte verwende ich nicht (Bildrechte, Persönlichkeitsrecht).
  Visuals sind Grafiken, Karten, Texteinblendungen, Akten-Optik.
- Ich recherchiere sorgfältig und nenne Quellen, aber **du** veröffentlichst und trägst
  damit die Verantwortung – deshalb Schritt 3 nicht überspringen.
