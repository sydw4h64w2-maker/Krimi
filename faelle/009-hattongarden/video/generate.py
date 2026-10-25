# Folge 9 – Hatton Garden. Alle Zeiten global (Sekunden im Audio); L() rechnet in Szenenzeit um.
import os, json, subprocess, sys
sys.path.insert(0, '/home/user/Krimi/tools')
from audio_levels import sfx_volume, normalize_voice
os.chdir(os.path.dirname(os.path.abspath(__file__)))
BASE = """
  #root { position:absolute; inset:0; font-family:'Oswald',sans-serif; color:var(--ink); }
  .lbl { font-family:'Space Mono',monospace; letter-spacing:.08em; text-transform:uppercase; }
  .center { position:absolute; left:0; width:100%; text-align:center; }
  .y { color:var(--accent); } .r { color:var(--red); } .p { color:var(--paper); }
"""
def scene(cid, dur, css, body, js):
    return f"""<template>
  <style>{BASE}{css}</style>
  <div id="root" data-composition-id="{cid}" data-width="1080" data-height="1920">
{body}
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
{js}
    window.__timelines["{cid}"] = tl;
  </script>
</template>
"""
SC=[]  # (id, start, end, css, body, js)
def add(cid, s0, s1, css, body, js):
    L=lambda g: round(g-s0,2)
    SC.append((cid,s0,s1,css,body(L),js(L)))
def fin(sel, L, g, d=0.3, frm="{opacity:0, y:30}", to="{opacity:1, y:0", ease="power3.out"):
    return f'    tl.fromTo("{sel}", {frm}, {to}, duration:{d}, ease:"{ease}"}}, {L(g)});\n'
def out(sel, L, g): return f'    tl.to({sel}, {{opacity:0, duration:0.25}}, {L(g)});\n'

STAMP = "position:absolute; text-align:center; border:12px solid var(--red); border-radius:14px; color:var(--red); font-weight:700; white-space:nowrap;"
CARD = "position:absolute; background:var(--paper); color:#1b1b1b; border-radius:10px; box-shadow:0 25px 60px rgba(0,0,0,.5);"
FACE = '<svg viewBox="0 0 100 100" width="100%" height="100%"><circle cx="50" cy="38" r="20" fill="#6b7079"/><path d="M14,100 Q14,64 50,60 Q86,64 86,100 Z" fill="#6b7079"/></svg>'
# 1 HOOK 0-10.1
add('hook',0,10.1,"""
  #hk-a { top:330px; font-size:56px; font-weight:600; }
  #hk-n { top:410px; font-size:250px; font-weight:700; line-height:1; }
  #hk-b { top:700px; font-size:66px; font-weight:600; }
  #hk-c { top:860px; font-size:62px; font-weight:700; line-height:1.15; }
""", lambda L: f"""
    <div id="hk-w" class="clip" data-start="0" data-duration="10.1">
      <div id="hk-a" class="center">Durchschnittsalter</div>
      <div id="hk-n" class="center y">60+</div>
      <div id="hk-b" class="center">👴 der Älteste: <span class="y">76</span></div>
      <div id="hk-c" class="center">Größter Einbruch der<br/><span class="r">englischen Rechtsgeschichte</span></div>
    </div>
""", lambda L: f"""
    tl.fromTo("#hk-n", {{scale:1.08, opacity:1}}, {{scale:1, opacity:1, duration:0.35, ease:"power4.out"}}, 0);
    tl.to("#hk-n", {{scale:1.06, duration:9.3, ease:"none"}}, 0.4);
    tl.fromTo("#hk-a", {{y:20, opacity:1}}, {{y:0, opacity:1, duration:0.4}}, 0.1);
""" + fin("#hk-b",L,2.7,0.35) + fin("#hk-c",L,5.8,0.4) + f"""
    {out('"#hk-w > *"',L,9.85).strip()}
""")
# 2 ORT 10.1-18.9
add('ort',10.1,18.9,"""
  #or-a { top:300px; font-size:120px; font-weight:700; }
  #or-b { top:450px; font-size:40px; white-space:nowrap; }
  #or-svg { position:absolute; left:190px; top:560px; width:700px; height:620px; }
""", lambda L: f"""
    <div id="or-w" class="clip" data-start="0" data-duration="{L(18.9)}">
      <div id="or-a" class="center">HATTON GARDEN</div>
      <div id="or-b" class="center lbl y">London · Diamantenviertel 💎</div>
      <svg id="or-svg" viewBox="0 0 700 620">
        <rect x="120" y="0" width="460" height="300" fill="#4a4c52"/>{''.join(f'<rect x="{150+c*110}" y="{30+r*90}" width="70" height="56" fill="#F2C230" opacity=".35"/>' for r in range(3) for c in range(4))}
        <rect x="0" y="300" width="700" height="8" fill="#9EA3AC"/><rect x="0" y="308" width="700" height="312" fill="#2a241c"/>
        <g id="or-vault"><rect x="160" y="360" width="380" height="220" fill="#1a1d22" stroke="#C9A04A" stroke-width="6"/>{''.join(f'<rect x="{180+c*45}" y="{380+r*45}" width="38" height="38" fill="#3b3f46" stroke="#6b6f76" stroke-width="2"/>' for r in range(4) for c in range(8))}</g>
        <text x="350" y="610" text-anchor="middle" fill="#C9A04A" font-family="Oswald" font-size="32">TRESORRAUM</text>
      </svg>
    </div>
""", lambda L: fin("#or-a",L,10.3,0.4) + fin("#or-b",L,12.4,0.3,"{opacity:0}","{opacity:1") + f"""
    tl.fromTo("#or-svg", {{opacity:0, y:40}}, {{opacity:1, y:0, duration:0.5}}, {L(12.8)});
    tl.fromTo("#or-vault", {{opacity:0.2}}, {{opacity:1, duration:0.6}}, {L(14.8)});
    tl.to("#or-svg", {{scale:1.05, duration:6, ease:"none"}}, {L(13.3)});
    {out('"#or-w > *"',L,18.65).strip()}
""")
# 3 EINSTIEG 18.9-31.6
add('einstieg',18.9,31.6,"""
  #es-a { top:300px; font-size:90px; font-weight:700; }
  #es-b { top:420px; font-size:46px; }
  #es-svg { position:absolute; left:140px; top:500px; width:800px; height:520px; }
  #es-c { top:1060px; font-size:80px; font-weight:700; }
""", lambda L: f"""
    <div id="es-w" class="clip" data-start="0" data-duration="{L(31.6)}">
      <div id="es-a" class="center">Osterwochenende</div>
      <div id="es-b" class="center lbl y">April 2015</div>
      <svg id="es-svg" viewBox="0 0 800 520">
        <rect x="60" y="0" width="120" height="520" fill="#1a1d22" stroke="#6b6f76" stroke-width="4"/><text x="120" y="40" text-anchor="middle" fill="#EDE6D6" font-family="Oswald" font-size="28">AUFZUG</text>
        <path id="es-path" d="M120,60 L120,400 L330,400" fill="none" stroke="#F2C230" stroke-width="8" stroke-dasharray="560" stroke-dashoffset="560"/>
        <rect x="330" y="250" width="110" height="270" fill="#8f9399"/>{''.join(f'<circle id="es-h{i}" cx="385" cy="{330+i*48}" r="22" fill="#0b0b0b" opacity="0"/>' for i in range(4))}
        <rect x="440" y="250" width="360" height="270" fill="#1a1d22"/>{''.join(f'<rect x="{460+c*55}" y="{270+r*55}" width="45" height="45" fill="#3b3f46" stroke="#6b6f76" stroke-width="2"/>' for r in range(4) for c in range(6))}
        <g id="es-drill"><rect x="200" y="380" width="110" height="40" rx="8" fill="#D2372E"/><rect x="300" y="392" width="40" height="16" fill="#9EA3AC"/></g>
      </svg>
      <div id="es-c" class="center">50 cm <span class="y">Beton</span></div>
    </div>
""", lambda L: fin("#es-a",L,19.0,0.4) + fin("#es-b",L,20.2,0.3,"{opacity:0}","{opacity:1") + f"""
    tl.fromTo("#es-svg", {{opacity:0}}, {{opacity:1, duration:0.4}}, {L(22.3)});
    tl.fromTo("#es-path", {{strokeDashoffset:560}}, {{strokeDashoffset:0, duration:2.6, ease:"power1.inOut"}}, {L(22.5)});
    tl.fromTo("#es-drill", {{x:-40, opacity:0}}, {{x:0, opacity:1, duration:0.4}}, {L(25.8)});
    tl.to("#es-drill", {{x:6, duration:0.08, yoyo:true, repeat:30, ease:"none"}}, {L(26.3)});
    for (let i=0;i<4;i++) tl.fromTo("#es-h"+i, {{opacity:0, scale:0.3, svgOrigin:"385 "+(330+i*48)}}, {{opacity:1, scale:1, duration:0.4}}, {L(26.6)}+i*0.6);
""" + f"""
    tl.fromTo("#es-c", {{scale:1.3, opacity:0}}, {{scale:1, opacity:1, duration:0.3, ease:"power4.out"}}, {L(29.5)});
    tl.to("#es-svg", {{scale:1.04, duration:9, ease:"none"}}, {L(22.7)});
    {out('"#es-w > *"',L,31.35).strip()}
""")
# 4 ALARM 31.6-35.4
add('alarm',31.6,35.4,"""
  #al-flash { position:absolute; inset:0; background:#D2372E; opacity:0; }
  #al-a { top:520px; font-size:200px; font-weight:700; line-height:1; }
  #al-b { top:800px; font-size:66px; font-weight:600; }
""", lambda L: f"""
    <div id="al-w" class="clip" data-start="0" data-duration="{L(35.4)}">
      <div id="al-flash" data-layout-ignore></div>
      <div id="al-a" class="center r">🚨 ALARM</div>
      <div id="al-b" class="center">Polizei: <span class="p">niemand kommt</span></div>
    </div>
""", lambda L: f"""
    tl.fromTo("#al-a", {{scale:1.3, opacity:0}}, {{scale:1, opacity:1, duration:0.25, ease:"power4.out"}}, {L(31.7)});
    for (let i=0;i<4;i++) {{ tl.fromTo("#al-flash", {{opacity:0}}, {{opacity:0.28, duration:0.15}}, {L(31.7)}+i*0.5); tl.to("#al-flash", {{opacity:0, duration:0.3}}, {L(31.85)}+i*0.5); }}
""" + fin("#al-b",L,33.2,0.35) + f"""
    {out('"#al-w > *:not(#al-flash)"',L,35.15).strip()}
""")
# 5 BOXES 35.4-48.1
add('boxes',35.4,48.1,"""
  #bx-g { position:absolute; left:140px; top:300px; width:800px; display:grid; grid-template-columns:repeat(8,1fr); gap:10px; }
  #bx-g .b { height:80px; background:#3b3f46; border:3px solid #6b6f76; }
  #bx-i { top:700px; font-size:58px; font-weight:600; white-space:nowrap; }
  #bx-l { top:830px; font-size:38px; white-space:nowrap; }
  #bx-m { top:920px; font-size:160px; font-weight:700; line-height:1; }
""", lambda L: f"""
    <div id="bx-w" class="clip" data-start="0" data-duration="{L(48.1)}">
      <div id="bx-g">{''.join(f'<div class="b" id="bx-b{i}"></div>' for i in range(32))}</div>
      <div id="bx-i" class="center">💵 Bargeld · 🪙 Gold · 💍 Schmuck</div>
      <div id="bx-l" class="center lbl">Beute laut offiziellen Angaben</div>
      <div id="bx-m" class="center y">bis £14 Mio.</div>
    </div>
""", lambda L: f"""
    tl.fromTo("#bx-g", {{opacity:0}}, {{opacity:1, duration:0.3}}, {L(35.5)});
    const ob=[]; for (let i=0;i<32;i++) if ((i*13)%32<26) ob.push("#bx-b"+i);
    ob.forEach((s,k)=>tl.fromTo(s, {{backgroundColor:"#3b3f46", borderColor:"#6b6f76"}}, {{backgroundColor:"#C9A04A", borderColor:"#F2C230", duration:0.08}}, {L(36.0)}+k*(3.2/ob.length)));
""" + fin("#bx-i",L,39.9,0.35) + fin("#bx-l",L,42.4,0.3,"{opacity:0}","{opacity:1") + f"""
    tl.fromTo("#bx-m", {{scale:1.3, opacity:0}}, {{scale:1, opacity:1, duration:0.35, ease:"power4.out"}}, {L(45.65)});
    tl.to("#bx-g", {{scale:1.04, duration:12, ease:"none"}}, {L(35.9)});
    {out('"#bx-w > *"',L,47.85).strip()}
""")
# 6 SQUAD 48.1-62.9
add('squad',48.1,62.9,"""
  #sq-a { top:300px; font-size:58px; font-weight:600; }
  #sq-b { top:390px; font-size:140px; font-weight:700; }
  #sq-c { top:590px; font-size:46px; font-weight:600; white-space:nowrap; }
  #sq-d { top:740px; font-size:96px; font-weight:700; }
  #sq-e { top:880px; font-size:50px; }
""", lambda L: f"""
    <div id="sq-w" class="clip" data-start="0" data-duration="{L(62.9)}">
      <div id="sq-a" class="center">Nach Ostern: <span class="r">Einbruch entdeckt</span></div>
      <div id="sq-b" class="center">FLYING SQUAD</div>
      <div id="sq-c" class="center">🔍 Die Ermittler kommen der Bande auf die Spur</div>
      <div id="sq-d" class="center y">„Diamond Wheezers“</div>
      <div id="sq-e" class="center lbl p">die keuchenden Diamantendiebe</div>
    </div>
""", lambda L: fin("#sq-a",L,48.3,0.35) + f"""
    tl.fromTo("#sq-b", {{scale:1.25, opacity:0}}, {{scale:1, opacity:1, duration:0.35, ease:"power4.out"}}, {L(51.1)});
    tl.to("#sq-b", {{scale:1.05, duration:11, ease:"none"}}, {L(51.5)});
""" + fin("#sq-c",L,53.9,0.35) + f"""
    tl.fromTo("#sq-d", {{scale:1.3, opacity:0, rotation:-4}}, {{scale:1, opacity:1, rotation:-2, duration:0.35, ease:"back.out(1.8)"}}, {L(58.6)});
""" + fin("#sq-e",L,60.6,0.3,"{opacity:0}","{opacity:1") + f"""
    {out('"#sq-w > *"',L,62.65).strip()}
""")
# 7 URTEIL 62.9-68.8
add('urteil',62.9,68.8,f"""
  #ut-a {{ top:420px; font-size:60px; }}
  #ut-st {{ {STAMP} left:160px; top:540px; width:760px; padding:16px 0; }}
  #ut-st .a {{ font-size:130px; line-height:1; }} #ut-st .b {{ font-size:56px; }}
""", lambda L: f"""
    <div id="ut-w" class="clip" data-start="0" data-duration="{L(68.8)}">
      <div id="ut-a" class="center lbl y">März 2016 · Haupttäter</div>
      <div id="ut-st"><div class="a">BIS 7 JAHRE</div><div class="b">HAFT</div></div>
    </div>
""", lambda L: fin("#ut-a",L,63.1,0.3,"{opacity:0}","{opacity:1") + f"""
    tl.fromTo("#ut-st", {{scale:2, rotation:-12, opacity:0}}, {{scale:1, rotation:-4, opacity:1, duration:0.22, ease:"power4.in"}}, {L(65.5)});
    tl.to("#ut-st", {{scale:1.05, duration:2.8, ease:"none"}}, {L(65.75)});
    {out('"#ut-w > *"',L,68.55).strip()}
""")
# 8 BASIL 68.8-82.6
add('basil',68.8,82.6,f"""
  #bs-h {{ top:300px; font-size:66px; font-weight:600; }}
  #bs-c {{ {CARD} left:340px; top:410px; width:400px; padding:20px 16px; text-align:center; }}
  #bs-c .ph {{ height:300px; background:#d9d2c0; border:4px solid #1b1b1b; position:relative; }}
  #bs-q {{ position:absolute; inset:0; display:flex; align-items:center; justify-content:center; font-size:200px; font-weight:700; color:#1b1b1b; }}
  #bs-c .nm {{ font-size:60px; font-weight:700; margin-top:10px; }}
  #bs-r {{ top:900px; font-size:58px; font-weight:600; }}
  #bs-u {{ top:1000px; font-size:60px; font-weight:700; }}
""", lambda L: f"""
    <div id="bs-w" class="clip" data-start="0" data-duration="{L(82.6)}">
      <div id="bs-h" class="center">Einer fehlt noch …</div>
      <div id="bs-c"><div class="ph"><div id="bs-face" style="position:absolute; inset:0">{FACE}</div><div id="bs-q">?</div></div><div class="nm">„Basil“</div></div>
      <div id="bs-r" class="center">= <span class="y">Michael Seed</span> · Alarm-Experte</div>
      <div id="bs-u" class="center r">2019 · 10 Jahre</div>
    </div>
""", lambda L: fin("#bs-h",L,69.0,0.35) + f"""
    tl.fromTo("#bs-c", {{y:100, rotation:-6, opacity:0}}, {{y:0, rotation:-2, opacity:1, duration:0.5, ease:"power3.out"}}, {L(70.9)});
    tl.fromTo("#bs-face", {{opacity:0}}, {{opacity:0, duration:0.1}}, {L(70.9)});
    tl.to("#bs-q", {{opacity:0, duration:0.3}}, {L(76.3)});
    tl.to("#bs-face", {{opacity:1, duration:0.3}}, {L(76.3)});
""" + fin("#bs-r",L,76.5,0.35) + fin("#bs-u",L,79.8,0.35) + f"""
    tl.to("#bs-c", {{scale:1.04, duration:11, ease:"none"}}, {L(71.5)});
    {out('"#bs-w > *"',L,82.35).strip()}
""")
# 9 BEUTE 82.6-89.2
add('beute',82.6,89.2,"""
  #bt-h { top:330px; font-size:80px; font-weight:700; }
  #bt-bar { position:absolute; left:140px; top:520px; width:800px; height:90px; border:6px solid #EDE6D6; border-radius:12px; }
  #bt-fill { position:absolute; left:0; top:0; height:100%; width:31%; background:#3FBF5F; border-radius:6px 0 0 6px; transform-origin:left center; }
  #bt-l1 { position:absolute; left:140px; top:640px; width:400px; font-size:48px; font-weight:600; color:#3FBF5F; }
  #bt-l2 { top:780px; font-size:80px; font-weight:700; }
""", lambda L: f"""
    <div id="bt-w" class="clip" data-start="0" data-duration="{L(89.2)}">
      <div id="bt-h" class="center">Und die Beute?</div>
      <div id="bt-bar"><div id="bt-fill"></div></div>
      <div id="bt-l1">gefunden: ~£4,3 Mio.</div>
      <div id="bt-l2" class="center r">Rest: verschwunden</div>
    </div>
""", lambda L: fin("#bt-h",L,82.75,0.35) + f"""
    tl.fromTo("#bt-bar", {{opacity:0}}, {{opacity:1, duration:0.3}}, {L(83.6)});
    tl.fromTo("#bt-fill", {{scaleX:0}}, {{scaleX:1, duration:1.4, ease:"power2.out"}}, {L(83.8)});
""" + fin("#bt-l1",L,84.6,0.3,"{opacity:0}","{opacity:1") + f"""
    tl.fromTo("#bt-l2", {{scale:1.3, opacity:0}}, {{scale:1, opacity:1, duration:0.3, ease:"power4.out"}}, {L(87.3)});
    {out('"#bt-w > *"',L,88.95).strip()}
""")
# 10 CTA 89.2-95.5
add('cta',89.2,95.5,"""
  #ct-q { top:500px; font-size:130px; font-weight:700; line-height:1.05; }
  #ct-s { top:880px; font-size:56px; font-weight:500; }
  #ct-arrow { top:1000px; font-size:120px; }
""", lambda L: f"""
    <div id="ct-q" class="center clip" data-start="0" data-duration="{L(95.5)}">Geniale Profis<br/><span class="y">oder nur Glück?</span></div>
    <div id="ct-s" class="center clip" data-start="{L(92.6)}" data-duration="{round(L(95.5)-L(92.6),2)}">Schreib's in die Kommentare</div>
    <div id="ct-arrow" class="center clip y" data-start="{L(92.9)}" data-duration="{round(L(95.5)-L(92.9),2)}">↓</div>
""", lambda L: f"""
    tl.fromTo("#ct-q", {{scale:1.15, opacity:0}}, {{scale:1, opacity:1, duration:0.4, ease:"power4.out"}}, {L(89.45)});
    tl.to("#ct-q", {{scale:1.04, duration:5.8, ease:"none"}}, {L(89.9)});
    tl.fromTo("#ct-s", {{opacity:0, y:20}}, {{opacity:1, y:0, duration:0.35}}, {L(92.7)});
    tl.fromTo("#ct-arrow", {{y:-20, opacity:0}}, {{y:20, opacity:1, duration:0.6, ease:"sine.inOut"}}, {L(92.9)});
    tl.to("#ct-arrow", {{y:-10, duration:0.6, ease:"sine.inOut"}}, {L(93.5)});
    tl.to("#ct-arrow", {{y:20, duration:0.6, ease:"sine.inOut"}}, {L(94.1)});
""")
TOTAL=95.5
hosts=[]
for cid,s0,s1,css,body,js in SC:
    dur=round(s1-s0,2)
    open(f'compositions/{cid}.html','w').write(scene(cid,dur,css,body,js))
    hosts.append(f'      <div id="{cid}" data-composition-id="{cid}" data-composition-src="compositions/{cid}.html" data-start="{s0}" data-duration="{dur}" data-track-index="2" data-track-kind="graphics" data-width="1080" data-height="1920" style="z-index:3"></div>')
sfx = [ # (file, time, vol)
 ('impact-bass-1',0.0,0.7),('pop',2.7,0.4),('impact-bass-2',5.8,0.5),
 ('whoosh-cinematic',10.1,0.5),('whoosh-short',12.8,0.4),
 ('whoosh-cinematic',18.9,0.5),('whoosh',22.5,0.4),('glitch-3',26.3,0.25),('impact-bass-2',29.5,0.6),
 ('error',31.7,0.35),('error',32.2,0.35),('error',32.7,0.35),
 ('whoosh-cinematic',35.4,0.5),('click',36.0,0.4),('click',37.5,0.4),('impact-bass-1',45.65,0.7),
 ('whoosh-cinematic',48.1,0.5),('impact-bass-2',51.1,0.5),('pop',58.6,0.4),
 ('whoosh-cinematic',62.9,0.5),('impact-bass-1',65.5,0.8),
 ('whoosh-cinematic',68.8,0.5),('ping',76.3,0.4),
 ('whoosh-cinematic',82.6,0.5),('impact-bass-2',87.3,0.5),('whoosh',89.2,0.4),
]
aud=[]
for i,(f,tt,v) in enumerate(sfx):
    d=float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f"assets/sfx/{f}.mp3"],capture_output=True,text=True).stdout.strip())
    d=round(min(d, TOTAL-tt),2)
    aud.append(f'      <audio id="sfx{i}" class="clip" src="assets/sfx/{f}.mp3" data-start="{tt}" data-duration="{d}" data-track-index="{10+i}" data-volume="{sfx_volume(f, min(1.0, v/0.6))}"></audio>')
index=f"""<!doctype html>
<html lang="de" data-resolution="portrait">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <script src="assets/vendor/gsap.min.js"></script>
    <style>
      :root {{ --ground:#0c0e12; --ink:#ffffff; --accent:#F2C230; --red:#D2372E; --paper:#EDE6D6; }}
      * {{ margin:0; padding:0; box-sizing:border-box; }}
      html, body {{ margin:0; width:1080px; height:1920px; overflow:hidden; background:var(--ground); }}
      #root {{ width:100%; height:100%; position:relative; }}
      #bg {{ position:absolute; inset:0; z-index:0;
        background:
          radial-gradient(ellipse at 50% 40%, rgba(242,194,48,.07), transparent 60%),
          repeating-linear-gradient(0deg, rgba(255,255,255,.025) 0 2px, transparent 2px 80px),
          repeating-linear-gradient(90deg, rgba(255,255,255,.025) 0 2px, transparent 2px 80px),
          var(--ground); }}
      #vig {{ position:absolute; inset:0; z-index:1; background:radial-gradient(ellipse at 50% 45%, transparent 45%, rgba(0,0,0,.75) 100%); }}
      #tape {{ position:absolute; left:-40px; top:190px; width:1160px; height:64px; z-index:4; background:repeating-linear-gradient(-45deg, #F2C230 0 40px, #111 40px 80px); transform:rotate(-2deg); opacity:.9; }}
      #case {{ position:absolute; left:0; top:1380px; width:100%; z-index:4; text-align:center; font-family:'Space Mono',monospace; font-size:28px; letter-spacing:.2em; color:rgba(237,230,214,.45); }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL}" data-width="1080" data-height="1920">
      <div id="bg" class="clip" data-start="0" data-duration="{TOTAL}" data-track-index="0"></div>
      <div id="vig" class="clip" data-start="0" data-duration="{TOTAL}" data-track-index="1"></div>
{chr(10).join(hosts)}
      <div id="tape" class="clip" data-start="0" data-duration="{TOTAL}" data-track-index="3"></div>
      <div id="case" class="clip" data-start="0" data-duration="{TOTAL}" data-track-index="4">FALL 009 · HATTON GARDEN · 2015</div>
      <audio id="music" class="clip" src="assets/music.mp3" data-start="0" data-duration="{TOTAL}" data-track-index="8" data-volume="0.35" data-fade-out="2"></audio>
      <audio id="voice" class="clip" src="assets/voice.mp3" data-start="0" data-track-index="9" data-volume="1"></audio>
{chr(10).join(aud)}
    </div>
    <script>
      const tl = gsap.timeline({{ paused: true }});
      window.__timelines["main"] = tl;
      tl.seek(0);
    </script>
  </body>
</html>
"""
normalize_voice('../audio-elevenlabs.mp3', 'assets/voice.mp3')
open('index.html','w').write(index)
print("ok", TOTAL)
