# Folge 6 – Gardner-Kunstraub. Alle Zeiten global (Sekunden im Audio); L() rechnet in Szenenzeit um.
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

def FRAME(id_, w, h, inner=""):
    return f'''<svg id="{id_}" viewBox="0 0 {w} {h}" width="{w}" height="{h}"><rect x="6" y="6" width="{w-12}" height="{h-12}" fill="none" stroke="#C9A04A" stroke-width="12"/><rect x="22" y="22" width="{w-44}" height="{h-44}" fill="none" stroke="#8A6A2A" stroke-width="5"/><rect x="34" y="34" width="{w-68}" height="{h-68}" fill="#14161a"/>{inner}</svg>'''
STAMP = "position:absolute; text-align:center; border:12px solid var(--red); border-radius:14px; color:var(--red); font-weight:700; white-space:nowrap;"
# 1 HOOK 0-10.1
add('hook',0,10.1,f"""
  #hk-f {{ position:absolute; left:240px; top:330px; }}
  #hk-st {{ {STAMP} left:270px; top:560px; width:540px; font-size:84px; padding:4px 0; }}
  #hk-v {{ top:990px; font-size:140px; font-weight:700; }}
  #hk-l {{ top:1200px; font-size:44px; }}
""", lambda L: f"""
    <div id="hk-w" class="clip" data-start="0" data-duration="10.1">
      <div id="hk-f">{FRAME('hk-fr',600,620)}</div>
      <div id="hk-st" data-layout-allow-overlap>GESTOHLEN</div>
      <div id="hk-v" class="center y">&gt;$500 Mio.</div>
      <div id="hk-l" class="center lbl p">Boston · leere Rahmen</div>
    </div>
""", lambda L: f"""
    tl.fromTo("#hk-f", {{scale:1.06, opacity:1}}, {{scale:1, opacity:1, duration:0.4, ease:"power3.out"}}, 0);
    tl.to("#hk-f", {{scale:1.05, duration:9.3, ease:"none"}}, 0.5);
    tl.fromTo("#hk-l", {{opacity:1}}, {{opacity:1, duration:0.1}}, 0);
    tl.fromTo("#hk-st", {{scale:2.2, rotation:-14, opacity:0}}, {{scale:1, rotation:-8, opacity:1, duration:0.22, ease:"power4.in"}}, {L(5.7)});
    tl.fromTo("#hk-v", {{scale:1.3, opacity:0}}, {{scale:1, opacity:1, duration:0.35, ease:"power4.out"}}, {L(7.6)});
    {out('"#hk-w > *"',L,9.85).strip()}
""")
# 2 NACHT 10.1-22.5
COP = lambda x: f'<g transform="translate({x},0)"><rect x="18" y="0" width="64" height="18" rx="4" fill="#1f2a44"/><rect x="10" y="16" width="80" height="8" fill="#1f2a44"/><circle cx="50" cy="48" r="24" fill="#EDE6D6"/><path d="M8,180 Q8,90 50,82 Q92,90 92,180 Z" fill="#1f2a44"/><circle cx="50" cy="110" r="6" fill="#F2C230"/></g>'
add('nacht',10.1,22.5,"""
  #nc-d { top:300px; font-size:110px; font-weight:700; }
  #nc-o { top:440px; font-size:46px; }
  #nc-svg { position:absolute; left:190px; top:540px; width:700px; height:420px; }
  #nc-b { position:absolute; left:140px; top:990px; width:800px; background:#EDE6D6; color:#1b1b1b; border-radius:30px; padding:24px 30px; text-align:center; font-size:50px; font-weight:600; }
""", lambda L: f"""
    <div id="nc-w" class="clip" data-start="0" data-duration="{L(22.5)}">
      <div id="nc-d" class="center">18.03.1990</div>
      <div id="nc-o" class="center lbl y">Boston · mitten in der Nacht</div>
      <svg id="nc-svg" viewBox="0 0 700 420"><rect x="380" y="20" width="300" height="400" fill="#3b2f25"/><rect x="410" y="60" width="240" height="360" fill="#5a4636"/><circle cx="620" cy="250" r="10" fill="#C9A04A"/><text x="530" y="45" text-anchor="middle" fill="#C9A04A" font-family="Oswald" font-size="30">MUSEUM</text><g id="nc-cops" transform="translate(40,230)">{COP(0)}{COP(130)}</g></svg>
      <div id="nc-b">„Wir sind wegen einer Störung hier.“</div>
    </div>
""", lambda L: fin("#nc-d",L,10.4,0.45) + fin("#nc-o",L,12.9,0.3,"{opacity:0}","{opacity:1") + f"""
    tl.fromTo("#nc-svg", {{opacity:0}}, {{opacity:1, duration:0.4}}, {L(14.3)});
    tl.fromTo("#nc-cops", {{x:-260}}, {{x:40, duration:1.6, ease:"power2.out"}}, {L(14.4)});
""" + fin("#nc-b",L,19.4,0.4,"{opacity:0, scale:0.9}","{opacity:1, scale:1",ease="back.out(1.6)") + f"""
    tl.to("#nc-d", {{scale:1.05, duration:11.5, ease:"none"}}, {L(10.9)});
    {out('"#nc-w > *"',L,22.25).strip()}
""")
# 3 REIN 22.5-32.0
add('rein',22.5,32.0,f"""
  #rn-a {{ top:330px; font-size:80px; font-weight:700; }}
  #rn-b {{ top:460px; font-size:50px; }}
  #rn-st {{ {STAMP} left:270px; top:580px; width:540px; font-size:110px; padding:4px 0; }}
  #rn-c {{ top:820px; font-size:62px; font-weight:600; line-height:1.2; }}
""", lambda L: f"""
    <div id="rn-w" class="clip" data-start="0" data-duration="{L(32.0)}">
      <div id="rn-a" class="center">Der Wachmann öffnet</div>
      <div id="rn-b" class="center lbl y">entgegen der Vorschrift</div>
      <div id="rn-st">FEHLER</div>
      <div id="rn-c" class="center">2 Wachleute<br/><span class="r">gefesselt im Keller</span></div>
    </div>
""", lambda L: fin("#rn-a",L,22.8,0.4) + fin("#rn-b",L,24.7,0.3,"{opacity:0}","{opacity:1") + f"""
    tl.fromTo("#rn-st", {{scale:2.2, rotation:-14, opacity:0}}, {{scale:1, rotation:-5, opacity:1, duration:0.22, ease:"power4.in"}}, {L(26.6)});
""" + fin("#rn-c",L,28.2,0.4) + f"""
    tl.to("#rn-a", {{scale:1.05, duration:9, ease:"none"}}, {L(23.2)});
    {out('"#rn-w > *"',L,31.75).strip()}
""")
# 4 MINUTEN 32.0-36.5
add('minuten',32.0,36.5,"""
  #mn-a { top:340px; font-size:52px; }
  #mn-t { top:440px; font-size:260px; font-weight:700; line-height:1; font-family:'Space Mono',monospace; }
  #mn-b { top:760px; font-size:96px; font-weight:700; }
""", lambda L: f"""
    <div id="mn-w" class="clip" data-start="0" data-duration="{L(36.5)}">
      <div id="mn-a" class="center lbl">Das Museum gehört ihnen</div>
      <div id="mn-t" class="center y"><span id="mn-n">00</span>:00</div>
      <div id="mn-b" class="center">81 MINUTEN</div>
    </div>
""", lambda L: fin("#mn-a",L,32.1,0.3,"{opacity:0}","{opacity:1") + f"""
    tl.fromTo("#mn-t", {{opacity:0}}, {{opacity:1, duration:0.2}}, {L(32.2)});
    const m = {{v:0}};
    tl.fromTo(m, {{v:0}}, {{v:81, duration:2.6, ease:"power1.in", onUpdate:()=>{{ document.querySelector("#mn-n").textContent = String(Math.round(m.v)).padStart(2,"0"); }}}}, {L(32.4)});
    tl.fromTo("#mn-b", {{scale:1.3, opacity:0}}, {{scale:1, opacity:1, duration:0.3, ease:"power4.out"}}, {L(34.6)});
    {out('"#mn-w > *"',L,36.25).strip()}
""")
# 5 WERKE 36.5-53.1
add('werke',36.5,53.1,"""
  #wk-h { top:300px; font-size:90px; font-weight:700; }
  #wk-g { position:absolute; left:140px; top:440px; width:800px; display:grid; grid-template-columns:repeat(5,1fr); gap:14px; }
  #wk-g .f { height:130px; border:7px solid #C9A04A; background:#14161a; opacity:0; }
  #wk-l { position:absolute; left:140px; top:900px; width:800px; }
  #wk-l .r1 { font-size:52px; font-weight:600; margin-top:10px; opacity:0; }
  #wk-l .r1 span { color:var(--accent); }
""", lambda L: f"""
    <div id="wk-w" class="clip" data-start="0" data-duration="{L(53.1)}">
      <div id="wk-h" class="center">13 KUNSTWERKE</div>
      <div id="wk-g">{''.join(f'<div class="f" id="wk-f{i}"></div>' for i in range(13))}</div>
      <div id="wk-l">
        <div class="r1" id="wk-r1"><span>2 ×</span> Rembrandt</div>
        <div class="r1" id="wk-r2" style="font-size:42px">„Der Sturm auf dem See Genezareth“</div>
        <div class="r1" id="wk-r3"><span>1 ×</span> Vermeer – „Das Konzert“</div>
        <div class="r1" id="wk-r4"><span>1 ×</span> Manet · <span>5 ×</span> Degas</div>
      </div>
    </div>
""", lambda L: f"""
    tl.fromTo("#wk-h", {{scale:1.2, opacity:0}}, {{scale:1, opacity:1, duration:0.35, ease:"power4.out"}}, {L(36.7)});
    for (let i=0;i<13;i++) tl.fromTo("#wk-f"+i, {{opacity:0, scale:0.7}}, {{opacity:1, scale:1, duration:0.18}}, {L(37.0)}+i*0.12);
    tl.fromTo("#wk-r1", {{opacity:0, x:-40}}, {{opacity:1, x:0, duration:0.3}}, {L(39.6)});
    tl.fromTo("#wk-r2", {{opacity:0, x:-40}}, {{opacity:1, x:0, duration:0.3}}, {L(44.4)});
    tl.fromTo("#wk-r3", {{opacity:0, x:-40}}, {{opacity:1, x:0, duration:0.3}}, {L(47.4)});
    tl.fromTo("#wk-r4", {{opacity:0, x:-40}}, {{opacity:1, x:0, duration:0.3}}, {L(49.8)});
    tl.to("#wk-g", {{scale:1.04, duration:14, ease:"none"}}, {L(38.6)});
    {out('"#wk-w > *"',L,52.85).strip()}
""")
# 6 REKORD 53.1-56.8
add('rekord',53.1,56.8,"""
  #rk-t { top:560px; font-size:120px; font-weight:700; line-height:1.05; }
""", lambda L: f"""
    <div id="rk-t" class="center clip" data-start="0" data-duration="{L(56.8)}">GRÖSSTER<br/><span class="y">KUNSTRAUB</span><br/>DER GESCHICHTE</div>
""", lambda L: f"""
    tl.fromTo("#rk-t", {{scale:1.25, opacity:0}}, {{scale:1, opacity:1, duration:0.35, ease:"power4.out"}}, {L(53.3)});
    tl.to("#rk-t", {{scale:1.06, duration:3.0, ease:"none"}}, {L(53.65)});
    {out('"#rk-t"',L,56.55).strip()}
""")
# 7 FBI 56.8-72.3
add('fbi',56.8,72.3,"""
  #fb-a { top:320px; font-size:140px; font-weight:700; }
  #fb-b { top:500px; font-size:52px; }
  #fb-c { top:620px; font-size:58px; font-weight:600; }
  #fb-d { top:720px; font-size:58px; font-weight:600; }
  #fb-e { top:880px; font-size:80px; font-weight:700; line-height:1.1; }
""", lambda L: f"""
    <div id="fb-w" class="clip" data-start="0" data-duration="{L(72.3)}">
      <div id="fb-a" class="center">FBI</div>
      <div id="fb-b" class="center lbl y">seit über 30 Jahren</div>
      <div id="fb-c" class="center">2013: <span class="y">Täter identifiziert?</span></div>
      <div id="fb-d" class="center">später: <span class="p">beide tot</span></div>
      <div id="fb-e" class="center">Die Bilder:<br/><span class="r">nie aufgetaucht</span></div>
    </div>
""", lambda L: f"""
    tl.fromTo("#fb-a", {{scale:1.25, opacity:0}}, {{scale:1, opacity:1, duration:0.35, ease:"power4.out"}}, {L(57.0)});
    tl.to("#fb-a", {{scale:1.05, duration:14.5, ease:"none"}}, {L(57.4)});
""" + fin("#fb-b",L,58.0,0.3,"{opacity:0}","{opacity:1") + fin("#fb-c",L,60.6,0.35) + fin("#fb-d",L,67.0,0.35) + f"""
    tl.fromTo("#fb-e", {{scale:1.25, opacity:0}}, {{scale:1, opacity:1, duration:0.3, ease:"power4.out"}}, {L(70.4)});
    {out('"#fb-w > *"',L,72.05).strip()}
""")
# 8 RAHMEN 72.3-84.1
add('rahmen',72.3,84.1,"""
  #rh-a { top:320px; font-size:52px; }
  #rh-m { top:390px; font-size:150px; font-weight:700; line-height:1; }
  #rh-f { position:absolute; left:290px; top:620px; }
  #rh-c { top:1050px; font-size:40px; }
  #rh-s { top:1130px; font-size:80px; font-weight:700; }
""", lambda L: f"""
    <div id="rh-w" class="clip" data-start="0" data-duration="{L(84.1)}">
      <div id="rh-a" class="center lbl">Belohnung bis zu</div>
      <div id="rh-m" class="center y">$<span id="rh-n">0</span></div>
      <div id="rh-f">{FRAME('rh-fr',500,400)}</div>
      <div id="rh-c" class="center lbl p">Testament: die Rahmen bleiben</div>
      <div id="rh-s" class="center">Sie warten.</div>
    </div>
""", lambda L: fin("#rh-a",L,72.5,0.3,"{opacity:0}","{opacity:1") + f"""
    tl.fromTo("#rh-m", {{opacity:0}}, {{opacity:1, duration:0.2}}, {L(72.6)});
    const r = {{v:0}};
    tl.fromTo(r, {{v:0}}, {{v:10000000, duration:2.4, ease:"power2.out", onUpdate:()=>{{ document.querySelector("#rh-n").textContent = Math.round(r.v).toLocaleString("de-DE"); }}}}, {L(72.7)});
    tl.fromTo("#rh-f", {{y:60, opacity:0}}, {{y:0, opacity:1, duration:0.6, ease:"power3.out"}}, {L(76.4)});
    tl.to("#rh-f", {{scale:1.06, duration:7, ease:"none"}}, {L(77.0)});
""" + fin("#rh-c",L,78.5,0.3,"{opacity:0}","{opacity:1") + fin("#rh-s",L,83.1,0.3) + f"""
    {out('"#rh-w > *"',L,83.85).strip()}
""")
# 9 CTA 84.1-90
add('cta',84.1,90.0,"""
  #ct-q { top:520px; font-size:140px; font-weight:700; line-height:1.05; }
  #ct-s { top:880px; font-size:56px; font-weight:500; }
  #ct-arrow { top:1000px; font-size:120px; }
""", lambda L: f"""
    <div id="ct-q" class="center clip" data-start="0" data-duration="{L(90)}">Wo sind<br/><span class="y">die Bilder?</span></div>
    <div id="ct-s" class="center clip" data-start="{L(85.9)}" data-duration="{round(L(90)-L(85.9),2)}">Schreib deine Theorie in die Kommentare</div>
    <div id="ct-arrow" class="center clip y" data-start="{L(86.2)}" data-duration="{round(L(90)-L(86.2),2)}">↓</div>
""", lambda L: f"""
    tl.fromTo("#ct-q", {{scale:1.15, opacity:0}}, {{scale:1, opacity:1, duration:0.4, ease:"power4.out"}}, {L(84.35)});
    tl.to("#ct-q", {{scale:1.04, duration:5.2, ease:"none"}}, {L(84.8)});
    tl.fromTo("#ct-s", {{opacity:0, y:20}}, {{opacity:1, y:0, duration:0.35}}, {L(86.0)});
    tl.fromTo("#ct-arrow", {{y:-20, opacity:0}}, {{y:20, opacity:1, duration:0.6, ease:"sine.inOut"}}, {L(86.2)});
    tl.to("#ct-arrow", {{y:-10, duration:0.6, ease:"sine.inOut"}}, {L(86.8)});
    tl.to("#ct-arrow", {{y:20, duration:0.6, ease:"sine.inOut"}}, {L(87.4)});
    tl.to("#ct-arrow", {{y:-10, duration:0.6, ease:"sine.inOut"}}, {L(88.0)});
""")
TOTAL=90.0
hosts=[]
for cid,s0,s1,css,body,js in SC:
    dur=round(s1-s0,2)
    open(f'compositions/{cid}.html','w').write(scene(cid,dur,css,body,js))
    hosts.append(f'      <div id="{cid}" data-composition-id="{cid}" data-composition-src="compositions/{cid}.html" data-start="{s0}" data-duration="{dur}" data-track-index="2" data-track-kind="graphics" data-width="1080" data-height="1920" style="z-index:3"></div>')
sfx = [ # (file, time, vol)
 ('impact-bass-1',0.0,0.7),('impact-bass-2',5.7,0.7),('impact-bass-1',7.6,0.6),
 ('whoosh-cinematic',10.1,0.5),('whoosh-short',14.4,0.4),('pop',19.4,0.4),
 ('whoosh-cinematic',22.5,0.5),('impact-bass-2',26.6,0.7),
 ('whoosh',32.0,0.4),('typing',32.4,0.35),('impact-bass-1',34.6,0.7),
 ('whoosh-cinematic',36.5,0.5),('click',39.6,0.4),('click',44.4,0.4),('click',47.4,0.4),('click',49.8,0.4),
 ('impact-bass-1',53.3,0.8),('whoosh-cinematic',56.8,0.5),('impact-bass-2',70.4,0.6),
 ('whoosh-cinematic',72.3,0.5),('whoosh',84.1,0.4),
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
      <div id="case" class="clip" data-start="0" data-duration="{TOTAL}" data-track-index="4">FALL 006 · GARDNER-KUNSTRAUB · 1990</div>
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
