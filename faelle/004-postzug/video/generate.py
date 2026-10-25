# Folge 4 – Great Train Robbery. Alle Zeiten global (Sekunden im Audio); L() rechnet in Szenenzeit um.
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

# 1 HOOK 0-8.5
add('hook',0,8.5,"""
  #hk-a { top:410px; font-size:180px; font-weight:700; line-height:1; }
  #hk-b { top:660px; font-size:60px; font-weight:600; }
  #hk-card { position:absolute; left:270px; top:800px; width:540px; height:360px; background:#EDE6D6; border:8px solid #1b1b1b; border-radius:10px; color:#1b1b1b; text-align:center; }
  #hk-card .bar { height:80px; background:#D2372E; }
  #hk-card .t { font-size:66px; font-weight:700; margin-top:44px; white-space:nowrap; letter-spacing:.04em; }
  #hk-card .s { font-family:'Space Mono',monospace; font-size:30px; margin-top:6px; }
""", lambda L: f"""
    <div id="hk-w" class="clip" data-start="0" data-duration="8.5">
      <div id="hk-a" class="center y">£2.600.000</div>
      <div id="hk-b" class="center">aus einem Postzug</div>
      <div id="hk-card"><div class="bar"></div><div class="t">🎲 MONOPOLY</div><div class="s">verrät die Täter</div></div>
    </div>
""", lambda L: f"""
    tl.fromTo("#hk-a", {{scale:1.08, opacity:1}}, {{scale:1, opacity:1, duration:0.35, ease:"power4.out"}}, 0);
    tl.to("#hk-a", {{scale:1.06, duration:7.6, ease:"none"}}, 0.4);
    tl.fromTo("#hk-b", {{y:20, opacity:1}}, {{y:0, opacity:1, duration:0.4}}, 0.1);
    tl.fromTo("#hk-card", {{y:200, rotation:10, opacity:0}}, {{y:0, rotation:-4, opacity:1, duration:0.5, ease:"back.out(1.6)"}}, {L(6.7)});
    {out('"#hk-w > *"',L,8.2).strip()}
""")
# 2 ZUG 8.5-20.2
add('zug',8.5,20.2,"""
  #zg-d { top:300px; font-size:120px; font-weight:700; }
  #zg-e { top:450px; font-size:48px; }
  #zg-svg { position:absolute; left:0; top:600px; width:1080px; height:300px; }
  #zg-r { top:920px; font-size:62px; font-weight:600; }
  #zg-s { top:1040px; font-size:56px; font-weight:500; }
""", lambda L: f"""
    <div id="zg-w" class="clip" data-start="0" data-duration="{L(20.2)}">
      <div id="zg-d" class="center">08.08.1963</div>
      <div id="zg-e" class="center lbl y">England · nachts</div>
      <svg id="zg-svg" viewBox="0 0 1080 300">
        <rect x="0" y="250" width="1080" height="8" fill="#9EA3AC"/>
        <g id="zg-train">
          <rect x="0" y="130" width="260" height="110" rx="10" fill="#1f5c3a"/><rect x="200" y="100" width="60" height="40" fill="#1f5c3a"/><rect x="20" y="150" width="60" height="40" fill="#F2C230" opacity=".8"/>
          <rect x="270" y="140" width="240" height="100" rx="6" fill="#7a1f1f"/><text x="390" y="205" text-anchor="middle" fill="#EDE6D6" font-family="Oswald" font-size="34">ROYAL MAIL</text>
          <rect x="520" y="140" width="240" height="100" rx="6" fill="#7a1f1f"/><text x="640" y="205" text-anchor="middle" fill="#EDE6D6" font-family="Oswald" font-size="34">ROYAL MAIL</text>
          <circle cx="60" cy="245" r="14" fill="#333"/><circle cx="200" cy="245" r="14" fill="#333"/><circle cx="320" cy="245" r="14" fill="#333"/><circle cx="460" cy="245" r="14" fill="#333"/><circle cx="570" cy="245" r="14" fill="#333"/><circle cx="710" cy="245" r="14" fill="#333"/>
        </g>
      </svg>
      <div id="zg-r" class="center">Glasgow <span class="y">→</span> London</div>
      <div id="zg-s" class="center">💰 Säcke voller <span class="y">gebrauchter Scheine</span></div>
    </div>
""", lambda L: fin("#zg-d",L,8.65,0.45) + fin("#zg-e",L,11.6,0.3,"{opacity:0}","{opacity:1") + f"""
    tl.fromTo("#zg-svg", {{opacity:0}}, {{opacity:1, duration:0.4}}, {L(12.7)});
    tl.fromTo("#zg-train", {{x:1100}}, {{x:-800, duration:7.2, ease:"none"}}, {L(12.7)});
""" + fin("#zg-r",L,13.4,0.35) + fin("#zg-s",L,17.6,0.35) + f"""
    tl.to("#zg-d", {{scale:1.05, duration:11, ease:"none"}}, {L(9.1)});
    {out('"#zg-w > *"',L,19.95).strip()}
""")
# 3 SIGNAL 20.2-32.3
add('signal',20.2,32.3,"""
  #sg-h { top:300px; font-size:56px; font-weight:600; }
  #sg-svg { position:absolute; left:340px; top:390px; width:400px; height:700px; }
  #sg-m { top:1100px; font-size:80px; font-weight:700; }
  #sg-l1 { position:absolute; left:640px; top:520px; width:400px; font-size:46px; font-weight:600; }
  #sg-l2 { position:absolute; left:640px; top:740px; width:400px; font-size:46px; font-weight:600; }
""", lambda L: f"""
    <div id="sg-w" class="clip" data-start="0" data-duration="{L(32.3)}">
      <div id="sg-h" class="center">Das Signal zeigt <span class="r">Rot</span></div>
      <svg id="sg-svg" viewBox="0 0 400 700">
        <rect x="185" y="380" width="30" height="320" fill="#555"/>
        <rect x="100" y="40" width="200" height="380" rx="24" fill="#1a1a1a" stroke="#444" stroke-width="6"/>
        <circle cx="200" cy="130" r="56" fill="#2a3a2a"/><circle id="sg-green" cx="200" cy="130" r="50" fill="#3FBF5F" opacity=".25"/>
        <circle cx="200" cy="300" r="56" fill="#3a2a2a"/><circle id="sg-red" cx="200" cy="300" r="50" fill="#FF3B30" opacity=".15"/>
        <g id="sg-glove"><path d="M150,70 Q150,50 170,50 L170,100 L180,45 Q190,35 200,45 L200,100 L210,42 Q222,34 230,46 L228,104 L244,70 Q258,62 262,80 L250,170 Q240,200 200,200 Q150,198 145,160 Z" fill="#111" stroke="#666" stroke-width="3"/></g>
        <g id="sg-bat"><rect x="290" y="440" width="90" height="140" rx="8" fill="#F2C230"/><rect x="315" y="425" width="40" height="18" fill="#F2C230"/><text x="335" y="525" text-anchor="middle" fill="#111" font-family="Oswald" font-size="40" font-weight="700">6V</text><path d="M335,425 C335,360 300,320 250,305" stroke="#F2C230" stroke-width="5" fill="none"/></g>
      </svg>
      <div id="sg-m" class="center r">MANIPULIERT</div>
      <div id="sg-l1" class="lbl p" style="font-family:'Oswald';font-size:44px;letter-spacing:0;text-transform:none">← Handschuh</div>
      <div id="sg-l2" class="lbl p" style="font-family:'Oswald';font-size:44px;letter-spacing:0;text-transform:none">← Batterie</div>
    </div>
""", lambda L: fin("#sg-h",L,20.3,0.3) + f"""
    tl.fromTo("#sg-svg", {{opacity:0}}, {{opacity:1, duration:0.4}}, {L(20.4)});
    tl.fromTo("#sg-green", {{opacity:0.9}}, {{opacity:0.9, duration:0.1}}, {L(20.5)});
    tl.to("#sg-green", {{opacity:0.15, duration:0.2}}, {L(22.3)});
    tl.to("#sg-red", {{opacity:1, duration:0.2}}, {L(22.3)});
    tl.fromTo("#sg-m", {{scale:1.4, opacity:0}}, {{scale:1, opacity:1, duration:0.25, ease:"power4.out"}}, {L(24.6)});
    tl.fromTo("#sg-glove", {{y:-300, opacity:0}}, {{y:0, opacity:1, duration:0.5, ease:"power3.out"}}, {L(27.6)});
""" + fin("#sg-l1",L,27.9,0.3,"{opacity:0}","{opacity:1") + f"""
    tl.fromTo("#sg-bat", {{x:80, opacity:0}}, {{x:0, opacity:1, duration:0.4, ease:"power3.out"}}, {L(30.4)});
""" + fin("#sg-l2",L,30.6,0.3,"{opacity:0}","{opacity:1") + f"""
    tl.to("#sg-svg", {{scale:1.04, duration:11, ease:"none"}}, {L(20.8)});
    {out('"#sg-w > *"',L,32.05).strip()}
""")
# 4 MILLS 32.3-43.8
add('mills',32.3,43.8,"""
  #ml-h { top:300px; font-size:46px; }
  #ml-n { top:370px; font-size:130px; font-weight:700; }
  #ml-gang { position:absolute; left:140px; top:600px; width:800px; height:260px; display:grid; grid-template-columns:repeat(8, 1fr); gap:10px; }
  #ml-gang .g { height:120px; background:radial-gradient(circle at 50% 22%, #EDE6D6 0 17%, transparent 18%), radial-gradient(ellipse at 50% 100%, #EDE6D6 0 46%, transparent 47%); opacity:0; }
  #ml-c { top:900px; font-size:60px; font-weight:600; }
  #ml-hit { position:absolute; inset:0; background:#D2372E; opacity:0; }
  #ml-x { top:1010px; font-size:64px; font-weight:700; }
  #ml-y { top:1110px; font-size:46px; }
""", lambda L: f"""
    <div id="ml-w" class="clip" data-start="0" data-duration="{L(43.8)}">
      <div id="ml-h" class="center lbl y">Lokführer</div>
      <div id="ml-n" class="center">JACK MILLS</div>
      <div id="ml-gang">{''.join(f'<div class="g" id="ml-g{i}"></div>' for i in range(15))}</div>
      <div id="ml-c" class="center">≈ 15 Männer stürmen den Zug</div>
      <div id="ml-x" class="center r">Schlag auf den Kopf</div>
      <div id="ml-y" class="center lbl p">erholt sich nie ganz</div>
      <div id="ml-hit" data-layout-ignore></div>
    </div>
""", lambda L: fin("#ml-h",L,32.45,0.3,"{opacity:0}","{opacity:1") + fin("#ml-n",L,32.6,0.4) + f"""
    for (let i=0;i<15;i++) tl.fromTo("#ml-g"+i, {{opacity:0, y:30}}, {{opacity:0.9, y:0, duration:0.2}}, {L(35.1)}+i*0.09);
""" + fin("#ml-c",L,35.6,0.35) + f"""
    tl.fromTo("#ml-hit", {{opacity:0}}, {{opacity:0.55, duration:0.05}}, {L(39.9)});
    tl.to("#ml-hit", {{opacity:0, duration:0.5}}, {L(39.95)});
    tl.fromTo("#ml-x", {{scale:1.4, opacity:0}}, {{scale:1, opacity:1, duration:0.25, ease:"power4.out"}}, {L(39.9)});
""" + fin("#ml-y",L,41.0,0.3,"{opacity:0}","{opacity:1") + f"""
    tl.to("#ml-n", {{scale:1.05, duration:10.5, ease:"none"}}, {L(33.0)});
    {out('"#ml-w > *:not(#ml-hit)"',L,43.55).strip()}
""")
# 5 BRUECKE 43.8-55.2
add('bruecke',43.8,55.2,"""
  #br-h { top:300px; font-size:52px; }
  #br-svg { position:absolute; left:90px; top:390px; width:900px; height:380px; }
  #br-b { top:800px; font-size:56px; }
  #br-m { top:880px; font-size:160px; font-weight:700; }
  #br-t { top:1080px; font-size:56px; font-weight:500; }
""", lambda L: f"""
    <div id="br-w" class="clip" data-start="0" data-duration="{L(55.2)}">
      <div id="br-h" class="center lbl y">Bridego Bridge</div>
      <svg id="br-svg" viewBox="0 0 900 380">
        <rect x="0" y="110" width="900" height="40" fill="#6d6f75"/><rect x="0" y="100" width="900" height="10" fill="#9EA3AC"/>
        <path d="M320,150 L320,380 L580,380 L580,150 Q450,240 320,150 Z" fill="#4a4c52"/>
        <rect x="350" y="300" width="200" height="70" rx="6" fill="#2b3a4a"/><text x="450" y="345" text-anchor="middle" fill="#cfe0f0" font-family="Oswald" font-size="30">FAHRZEUG</text>
        {''.join(f'<g id="br-s{i}"><ellipse cx="{380+i*45}" cy="85" rx="20" ry="24" fill="#c9b28a"/><rect x="{372+i*45}" y="58" width="16" height="10" fill="#8a6a3d"/></g>' for i in range(4))}
      </svg>
      <div id="br-b" class="center lbl">Beute</div>
      <div id="br-m" class="center y">£2,6 Mio.</div>
      <div id="br-t" class="center">heute ≈ <span class="y">£50 Mio.</span></div>
    </div>
""", lambda L: fin("#br-h",L,44.0,0.3,"{opacity:0}","{opacity:1") + f"""
    tl.fromTo("#br-svg", {{opacity:0}}, {{opacity:1, duration:0.4}}, {L(44.1)});
    for (let i=0;i<4;i++) tl.fromTo("#br-s"+i, {{y:0, opacity:1}}, {{y:250, opacity:0.0, duration:0.7, ease:"power2.in"}}, {L(45.0)}+i*0.6);
""" + fin("#br-b",L,48.5,0.25,"{opacity:0}","{opacity:1") + f"""
    tl.fromTo("#br-m", {{scale:1.3, opacity:0}}, {{scale:1, opacity:1, duration:0.35, ease:"power4.out"}}, {L(49.3)});
""" + fin("#br-t",L,52.1,0.35) + f"""
    tl.to("#br-m", {{scale:1.05, duration:5.5, ease:"none"}}, {L(49.7)});
    {out('"#br-w > *"',L,54.95).strip()}
""")
# 6 FARM 55.2-64.0
add('farm',55.2,64.0,"""
  #fm-svg { position:absolute; left:240px; top:330px; width:600px; height:440px; }
  #fm-n { top:800px; font-size:110px; font-weight:700; }
  #fm-c { top:960px; font-size:56px; font-weight:500; }
""", lambda L: f"""
    <div id="fm-w" class="clip" data-start="0" data-duration="{L(64.0)}">
      <svg id="fm-svg" viewBox="0 0 600 440">
        <rect x="0" y="380" width="600" height="60" fill="#2c3b24"/>
        <rect x="120" y="200" width="360" height="190" fill="#6b5a45"/><path d="M90,210 L300,70 L510,210 Z" fill="#3b2f25"/>
        <rect x="270" y="290" width="60" height="100" fill="#2a2018"/><rect id="fm-win" x="170" y="250" width="60" height="50" fill="#F2C230" opacity=".2"/><rect x="370" y="250" width="60" height="50" fill="#F2C230" opacity=".2"/>
      </svg>
      <div id="fm-n" class="center">LEATHERSLADE FARM</div>
      <div id="fm-c" class="center">Ein Nachbar wird misstrauisch – <span class="r">📞 Polizei</span></div>
    </div>
""", lambda L: f"""
    tl.fromTo("#fm-svg", {{y:40, opacity:0}}, {{y:0, opacity:1, duration:0.5, ease:"power3.out"}}, {L(55.4)});
    tl.to("#fm-win", {{opacity:0.9, duration:0.3}}, {L(57.0)});
    tl.fromTo("#fm-n", {{scale:1.25, opacity:0}}, {{scale:1, opacity:1, duration:0.35, ease:"power4.out"}}, {L(58.7)});
""" + fin("#fm-c",L,60.3,0.35) + f"""
    tl.to("#fm-svg", {{scale:1.05, duration:8, ease:"none"}}, {L(55.9)});
    {out('"#fm-w > *"',L,63.75).strip()}
""")
# 7 SPUREN 64.0-76.2
add('spuren',64.0,76.2,"""
  #sp-d { top:330px; font-size:140px; font-weight:700; }
  #sp-w2 { top:520px; font-size:60px; font-weight:600; }
  #sp-board { position:absolute; left:240px; top:420px; width:600px; height:600px; background:#CFE3CF; border:10px solid #1b1b1b; }
  #sp-board .in { position:absolute; inset:90px; background:#BFD8C0; border:4px solid #1b1b1b; display:flex; align-items:center; justify-content:center; }
  #sp-board .in span { font-size:72px; font-weight:700; color:#B3261E; transform:rotate(-30deg); letter-spacing:.05em; }
  #sp-fp { position:absolute; left:560px; top:620px; width:240px; height:300px; }
  #sp-t { top:1070px; font-size:66px; font-weight:700; }
""", lambda L: f"""
    <div id="sp-a" class="clip" data-start="0" data-duration="{L(69.7)}">
      <div id="sp-d" class="center y">+5 TAGE</div>
      <div id="sp-w2" class="center">Polizei auf dem Hof · <span class="r">Täter weg</span></div>
    </div>
    <div id="sp-b" class="clip" data-start="{L(69.7)}" data-duration="{round(L(76.2)-L(69.7),2)}">
      <div id="sp-board" data-layout-allow-overlap><div class="in"><span>MONOPOLY</span></div></div>
      <svg id="sp-fp" viewBox="0 0 240 300" data-layout-allow-overlap>{''.join(f'<ellipse cx="120" cy="160" rx="{30+i*14}" ry="{40+i*17}" fill="none" stroke="#1b1b1b" stroke-width="5" stroke-dasharray="{60+i*9} 14" opacity=".85"/>' for i in range(6))}</svg>
      <div id="sp-t" class="center">FINGERABDRÜCKE</div>
    </div>
""", lambda L: f"""
    tl.fromTo("#sp-d", {{scale:1.25, opacity:0}}, {{scale:1, opacity:1, duration:0.35, ease:"power4.out"}}, {L(64.3)});
    tl.to("#sp-d", {{scale:1.06, duration:5, ease:"none"}}, {L(64.7)});
""" + fin("#sp-w2",L,66.0,0.35) + f"""
    {out('"#sp-a > *"',L,69.45).strip()}
    tl.fromTo("#sp-board", {{rotation:-8, scale:0.9, opacity:0}}, {{rotation:-3, scale:1, opacity:1, duration:0.5, ease:"power3.out"}}, {L(69.85)});
    tl.fromTo("#sp-t", {{scale:1.3, opacity:0}}, {{scale:1, opacity:1, duration:0.3, ease:"power4.out"}}, {L(72.05)});
    tl.fromTo("#sp-fp", {{scale:0.4, opacity:0}}, {{scale:1, opacity:1, duration:0.4, ease:"back.out(1.6)"}}, {L(73.4)});
    tl.to("#sp-board", {{scale:1.05, duration:5.6, ease:"none"}}, {L(70.4)});
    {out('"#sp-b > *"',L,75.95).strip()}
""")
# 8 URTEIL 76.2-87.5
add('urteil',76.2,87.5,"""
  #ur-g { position:absolute; left:190px; top:320px; width:700px; display:grid; grid-template-columns:repeat(4,1fr); gap:14px; }
  #ur-g .m { height:150px; background:#20242b; border:4px solid #4a4f58; position:relative; opacity:0; }
  #ur-g .m::after { content:""; position:absolute; left:30%; top:18%; width:40%; height:40%; border-radius:50%; background:#6b7079; }
  #ur-d { top:700px; font-size:52px; }
  #ur-st { position:absolute; left:160px; top:780px; width:760px; text-align:center; border:14px solid var(--red); border-radius:16px; color:var(--red); padding:14px 0; }
  #ur-st .a { font-size:150px; font-weight:700; line-height:1; } #ur-st .b { font-size:52px; font-weight:600; }
  #ur-n { top:1110px; font-size:52px; font-weight:500; }
""", lambda L: f"""
    <div id="ur-w" class="clip" data-start="0" data-duration="{L(87.5)}">
      <div id="ur-g">{''.join(f'<div class="m" id="ur-m{i}"></div>' for i in range(8))}</div>
      <div id="ur-d" class="center lbl y">April 1964</div>
      <div id="ur-st"><div class="a">7 × 30</div><div class="b">JAHRE HAFT</div></div>
      <div id="ur-n" class="center">Großteil des Geldes: <span class="r">nie gefunden</span></div>
    </div>
""", lambda L: f"""
    for (let i=0;i<8;i++) tl.fromTo("#ur-m"+i, {{opacity:0, scale:0.8}}, {{opacity:1, scale:1, duration:0.2}}, {L(76.4)}+i*0.25);
""" + fin("#ur-d",L,78.9,0.3,"{opacity:0}","{opacity:1") + f"""
    tl.fromTo("#ur-st", {{scale:2, rotation:-12, opacity:0}}, {{scale:1, rotation:-4, opacity:1, duration:0.22, ease:"power4.in"}}, {L(81.6)});
""" + fin("#ur-n",L,84.6,0.35) + f"""
    tl.to("#ur-g", {{scale:1.04, duration:10, ease:"none"}}, {L(77.0)});
    {out('"#ur-w > *"',L,87.25).strip()}
""")
# 9 FLUCHT 87.5-97.6
add('flucht',87.5,97.6,"""
  #fl-a { top:300px; font-size:130px; font-weight:700; }
  #fl-n { top:470px; font-size:64px; font-weight:600; }
  #fl-svg { position:absolute; left:190px; top:580px; width:700px; height:500px; }
  #fl-d { top:1110px; font-size:54px; font-weight:600; }
""", lambda L: f"""
    <div id="fl-w" class="clip" data-start="0" data-duration="{L(97.6)}">
      <div id="fl-a" class="center y">FILMREIF</div>
      <div id="fl-n" class="center">Ronnie Biggs · 30 Jahre Haft</div>
      <svg id="fl-svg" viewBox="0 0 700 500">
        <rect x="260" y="60" width="180" height="440" fill="#5d5f66"/>{''.join(f'<rect x="260" y="{60+i*55}" width="180" height="3" fill="#44464c"/>' for i in range(8))}
        <g id="fl-lad"><rect x="190" y="40" width="10" height="460" fill="#c9a46a"/><rect x="250" y="40" width="10" height="460" fill="#c9a46a"/>{''.join(f'<rect x="190" y="{70+i*50}" width="70" height="8" fill="#c9a46a"/>' for i in range(9))}</g>
        <g id="fl-man"><circle cx="225" cy="410" r="16" fill="#EDE6D6"/><rect x="210" y="428" width="30" height="48" rx="10" fill="#EDE6D6"/></g>
      </svg>
      <div id="fl-d" class="center">08.07.1965 · <span class="y">über die Mauer</span></div>
    </div>
""", lambda L: f"""
    tl.fromTo("#fl-a", {{scale:1.3, opacity:0}}, {{scale:1, opacity:1, duration:0.35, ease:"power4.out"}}, {L(87.75)});
""" + fin("#fl-n",L,90.2,0.35) + f"""
    tl.fromTo("#fl-svg", {{opacity:0}}, {{opacity:1, duration:0.4}}, {L(91.0)});
    tl.fromTo("#fl-lad", {{y:-500}}, {{y:0, duration:0.5, ease:"bounce.out"}}, {L(91.3)});
    tl.fromTo("#fl-man", {{x:0, y:0}}, {{x:120, y:-400, duration:3.2, ease:"power1.inOut"}}, {L(93.2)});
    tl.to("#fl-man", {{x:300, y:-330, opacity:0, duration:0.8, ease:"power2.in"}}, {L(96.4)});
""" + fin("#fl-d",L,92.3,0.35) + f"""
    tl.to("#fl-a", {{scale:1.05, duration:9.5, ease:"none"}}, {L(88.1)});
    {out('"#fl-w > *"',L,97.35).strip()}
""")
# 10 WELT 97.6-112.2
add('welt',97.6,112.2,"""
  #wl-svg { position:absolute; left:40px; top:330px; width:1000px; height:560px; }
  #wl-y { top:920px; font-size:110px; font-weight:700; }
  #wl-t { top:1060px; font-size:52px; font-weight:500; }
  #wl-st { position:absolute; left:190px; top:1150px; width:700px; text-align:center; border:10px solid var(--red); border-radius:12px; color:var(--red); font-size:56px; font-weight:700; padding:4px 0; white-space:nowrap; }
""", lambda L: f"""
    <div id="wl-w" class="clip" data-start="0" data-duration="{L(112.2)}">
      <svg id="wl-svg" viewBox="0 0 1000 560">
        <path id="wl-p1" d="M420,140 C420,150 440,160 450,170" fill="none" stroke="#F2C230" stroke-width="6" stroke-dasharray="80" stroke-dashoffset="80"/>
        <path id="wl-p2" d="M450,170 C650,200 820,320 880,430" fill="none" stroke="#F2C230" stroke-width="6" stroke-dasharray="620" stroke-dashoffset="620"/>
        <path id="wl-p3" d="M880,430 C700,520 450,520 330,400" fill="none" stroke="#F2C230" stroke-width="6" stroke-dasharray="680" stroke-dashoffset="680"/>
        <path id="wl-p4" d="M330,400 C330,300 380,180 420,140" fill="none" stroke="#EDE6D6" stroke-width="6" stroke-dasharray="320" stroke-dashoffset="320"/>
        <g><circle cx="420" cy="140" r="12" fill="#EDE6D6"/><text x="380" y="118" fill="#EDE6D6" font-family="Oswald" font-size="38">London</text></g>
        <g id="wl-c1"><circle cx="450" cy="170" r="12" fill="#F2C230"/><text x="470" y="200" fill="#F2C230" font-family="Oswald" font-size="38">Paris · neues Gesicht</text></g>
        <g id="wl-c2"><circle cx="880" cy="430" r="12" fill="#F2C230"/><text x="740" y="480" fill="#F2C230" font-family="Oswald" font-size="38">Australien</text></g>
        <g id="wl-c3"><circle cx="330" cy="400" r="12" fill="#F2C230"/><text x="120" y="440" fill="#F2C230" font-family="Oswald" font-size="38">Brasilien</text></g>
      </svg>
      <div id="wl-y" class="center y"><span id="wl-yr">1965</span></div>
      <div id="wl-t" class="center">über 30 Jahre auf der Flucht</div>
      <div id="wl-st">ZURÜCK · FESTGENOMMEN</div>
    </div>
""", lambda L: f"""
    tl.fromTo("#wl-svg", {{opacity:0}}, {{opacity:1, duration:0.4}}, {L(97.7)});
    tl.fromTo("#wl-p1", {{strokeDashoffset:80}}, {{strokeDashoffset:0, duration:0.6}}, {L(97.8)});
    tl.fromTo("#wl-c1", {{opacity:0}}, {{opacity:1, duration:0.3}}, {L(98.2)});
    tl.fromTo("#wl-p2", {{strokeDashoffset:620}}, {{strokeDashoffset:0, duration:1.0, ease:"power1.inOut"}}, {L(100.3)});
    tl.fromTo("#wl-c2", {{opacity:0}}, {{opacity:1, duration:0.3}}, {L(100.9)});
    tl.fromTo("#wl-p3", {{strokeDashoffset:680}}, {{strokeDashoffset:0, duration:1.0, ease:"power1.inOut"}}, {L(101.8)});
    tl.fromTo("#wl-c3", {{opacity:0}}, {{opacity:1, duration:0.3}}, {L(102.5)});
    tl.fromTo("#wl-y", {{opacity:0}}, {{opacity:1, duration:0.3}}, {L(104.0)});
    const yr = {{v:1965}};
    tl.fromTo(yr, {{v:1965}}, {{v:2001, duration:2.4, ease:"power1.inOut", onUpdate:()=>{{ document.querySelector("#wl-yr").textContent = Math.round(yr.v); }}}}, {L(104.1)});
""" + fin("#wl-t",L,104.3,0.35) + f"""
    tl.fromTo("#wl-p4", {{strokeDashoffset:320}}, {{strokeDashoffset:0, duration:1.2, ease:"power1.inOut"}}, {L(106.8)});
    tl.fromTo("#wl-st", {{scale:2, rotation:-12, opacity:0}}, {{scale:1, rotation:-4, opacity:1, duration:0.22, ease:"power4.in"}}, {L(110.3)});
    tl.to("#wl-svg", {{scale:1.04, duration:14, ease:"none"}}, {L(98.1)});
    {out('"#wl-w > *"',L,111.95).strip()}
""")
# 11 CTA 112.2-118
add('cta',112.2,118.0,"""
  #ct-q { top:480px; font-size:120px; font-weight:700; line-height:1.05; }
  #ct-s { top:960px; font-size:56px; font-weight:500; }
  #ct-arrow { top:1060px; font-size:120px; }
""", lambda L: f"""
    <div id="ct-q" class="center clip" data-start="0" data-duration="{L(118)}">Genialer Coup<br/><span class="r">oder brutaler Überfall?</span></div>
    <div id="ct-s" class="center clip" data-start="{L(115.4)}" data-duration="{round(L(118)-L(115.4),2)}">Schreib's in die Kommentare</div>
    <div id="ct-arrow" class="center clip y" data-start="{L(115.7)}" data-duration="{round(L(118)-L(115.7),2)}">↓</div>
""", lambda L: f"""
    tl.fromTo("#ct-q", {{scale:1.15, opacity:0}}, {{scale:1, opacity:1, duration:0.4, ease:"power4.out"}}, {L(112.45)});
    tl.to("#ct-q", {{scale:1.04, duration:5.2, ease:"none"}}, {L(112.9)});
    tl.fromTo("#ct-s", {{opacity:0, y:20}}, {{opacity:1, y:0, duration:0.35}}, {L(115.5)});
    tl.fromTo("#ct-arrow", {{y:-20, opacity:0}}, {{y:20, opacity:1, duration:0.6, ease:"sine.inOut"}}, {L(115.7)});
    tl.to("#ct-arrow", {{y:-10, duration:0.6, ease:"sine.inOut"}}, {L(116.3)});
    tl.to("#ct-arrow", {{y:20, duration:0.6, ease:"sine.inOut"}}, {L(116.9)});
""")
TOTAL=118.0
hosts=[]
for cid,s0,s1,css,body,js in SC:
    dur=round(s1-s0,2)
    open(f'compositions/{cid}.html','w').write(scene(cid,dur,css,body,js))
    hosts.append(f'      <div id="{cid}" data-composition-id="{cid}" data-composition-src="compositions/{cid}.html" data-start="{s0}" data-duration="{dur}" data-track-index="2" data-track-kind="graphics" data-width="1080" data-height="1920" style="z-index:3"></div>')
sfx = [ # (file, time, vol)
 ('impact-bass-1',0.0,0.8),('whoosh',6.7,0.4),
 ('whoosh-cinematic',8.5,0.5),('whoosh-short',12.7,0.4),
 ('whoosh-cinematic',20.2,0.5),('click',22.3,0.5),('impact-bass-2',24.6,0.6),('whoosh-short',27.6,0.4),('click',30.4,0.5),
 ('whoosh-cinematic',32.3,0.5),('impact-bass-1',39.9,0.8),
 ('whoosh-cinematic',43.8,0.5),('impact-bass-2',49.3,0.6),
 ('whoosh-cinematic',55.2,0.5),('impact-bass-2',58.7,0.6),
 ('whoosh',64.0,0.4),('impact-bass-1',64.3,0.6),('whoosh-short',69.85,0.4),('impact-bass-2',72.05,0.6),
 ('whoosh-cinematic',76.2,0.5),('impact-bass-1',81.6,0.8),
 ('whoosh-cinematic',87.5,0.5),('riser',93.2,0.3),
 ('whoosh-cinematic',97.6,0.5),('impact-bass-1',110.3,0.8),('whoosh',112.2,0.4),
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
      <div id="case" class="clip" data-start="0" data-duration="{TOTAL}" data-track-index="4">FALL 004 · POSTZUGRAUB · 1963</div>
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
