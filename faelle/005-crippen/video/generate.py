# Folge 5 – Dr. Crippen. Alle Zeiten global (Sekunden im Audio); L() rechnet in Szenenzeit um.
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

SHIP = lambda id_, fill="#B8BCC4": f'<g id="{id_}"><path d="M0,60 L260,60 L230,100 L30,100 Z" fill="#3b3f46"/><rect x="60" y="30" width="150" height="30" fill="{fill}"/><rect x="95" y="0" width="22" height="32" fill="#D2372E"/><rect x="145" y="0" width="22" height="32" fill="#D2372E"/></g>'
WAVES = lambda id_, cx, cy: f'<g id="{id_}">' + ''.join(f'<path d="M{cx-40-i*30},{cy-20-i*24} Q{cx},{cy-60-i*40} {cx+40+i*30},{cy-20-i*24}" fill="none" stroke="#F2C230" stroke-width="6" opacity="{1-i*0.25}"/>' for i in range(3)) + '</g>'
# 1 HOOK 0-10.6
add('hook',0,10.6,"""
  #hk-y { top:330px; font-size:220px; font-weight:700; line-height:1; }
  #hk-s { position:absolute; left:0; top:640px; width:1080px; height:300px; }
  #hk-f { top:960px; font-size:120px; font-weight:700; }
  #hk-t { top:1190px; font-size:46px; }
""", lambda L: f"""
    <div id="hk-w" class="clip" data-start="0" data-duration="10.6">
      <div id="hk-y" class="center y">1910</div>
      <svg id="hk-s" viewBox="0 0 1080 300"><rect x="0" y="210" width="1080" height="90" fill="#16324a"/><g transform="translate(0,110)">{SHIP('hk-ship')}</g>{WAVES('hk-wv',640,120)}</svg>
      <div id="hk-f" class="center">📡 FUNK</div>
      <div id="hk-t" class="center lbl p">Flucht über den Atlantik</div>
    </div>
""", lambda L: f"""
    tl.fromTo("#hk-y", {{scale:1.08, opacity:1}}, {{scale:1, opacity:1, duration:0.35, ease:"power4.out"}}, 0);
    tl.to("#hk-y", {{scale:1.06, duration:9.8, ease:"none"}}, 0.4);
    tl.fromTo("#hk-t", {{opacity:1}}, {{opacity:1, duration:0.1}}, 0);
    tl.fromTo("#hk-ship", {{x:-300}}, {{x:900, duration:9.5, ease:"none"}}, {L(1.0)});
    tl.fromTo("#hk-wv", {{opacity:0, scale:0.6, transformOrigin:"640px 120px"}}, {{opacity:1, scale:1, duration:0.5, ease:"back.out(2)"}}, {L(9.4)});
    tl.fromTo("#hk-f", {{scale:1.3, opacity:0}}, {{scale:1, opacity:1, duration:0.3, ease:"power4.out"}}, {L(9.45)});
    {out('"#hk-w > *"',L,10.35).strip()}
""")
# 2 PAAR 10.6-23.5
CARD="""position:absolute; width:420px; height:560px; background:var(--paper); color:#1b1b1b; border-radius:10px; box-shadow:0 25px 60px rgba(0,0,0,.5); text-align:center; padding-top:30px;"""
add('paar',10.6,23.5,f"""
  #pa-h {{ top:300px; font-size:56px; }}
  #pa-a {{ {CARD} left:80px; top:400px; }}
  #pa-b {{ {CARD} left:580px; top:400px; }}
  .sil {{ width:200px; height:240px; margin:0 auto; background:radial-gradient(circle at 50% 30%, #6b6f78 0 22%, transparent 23%), radial-gradient(ellipse at 50% 100%, #6b6f78 0 48%, transparent 49%); background-color:#d9d2c0; border:4px solid #1b1b1b; }}
  .nm {{ font-size:44px; font-weight:700; margin-top:22px; line-height:1.05; }}
  .ds {{ font-family:'Space Mono',monospace; font-size:28px; color:#444; margin-top:10px; line-height:1.3; }}
  #pa-st {{ position:absolute; left:560px; top:900px; width:460px; text-align:center; border:9px solid var(--red); border-radius:10px; color:var(--red); font-size:54px; font-weight:700; padding:2px 0; }}
  #pa-d {{ top:1030px; font-size:60px; font-weight:600; }}
""", lambda L: f"""
    <div id="pa-w" class="clip" data-start="0" data-duration="{L(23.5)}">
      <div id="pa-h" class="center lbl y">London</div>
      <div id="pa-a"><div class="sil"></div><div class="nm">Hawley Harvey<br/>Crippen</div><div class="ds">Arzt · Amerikaner</div></div>
      <div id="pa-b"><div class="sil"></div><div class="nm">Cora<br/>Crippen</div><div class="ds">Sängerin<br/>„Belle Elmore“</div></div>
      <div id="pa-st" data-layout-allow-overlap>VERSCHWUNDEN</div>
      <div id="pa-d" class="center">Anfang Februar 1910</div>
    </div>
""", lambda L: fin("#pa-h",L,10.9,0.3,"{opacity:0}","{opacity:1") + f"""
    tl.fromTo("#pa-a", {{x:-120, rotation:-6, opacity:0}}, {{x:0, rotation:-2, opacity:1, duration:0.5, ease:"power3.out"}}, {L(11.9)});
    tl.fromTo("#pa-b", {{x:120, rotation:6, opacity:0}}, {{x:0, rotation:2, opacity:1, duration:0.5, ease:"power3.out"}}, {L(14.6)});
""" + fin("#pa-d",L,19.4,0.35) + f"""
    tl.to("#pa-b", {{opacity:0.45, duration:0.8}}, {L(21.4)});
    tl.fromTo("#pa-st", {{scale:2, rotation:-14, opacity:0}}, {{scale:1, rotation:-8, opacity:1, duration:0.22, ease:"power4.in"}}, {L(22.0)});
    tl.to("#pa-a", {{scale:1.04, duration:11, ease:"none"}}, {L(12.4)});
    {out('"#pa-w > *"',L,23.25).strip()}
""")
# 3 LUEGEN 23.5-37.8
BUB="position:absolute; left:120px; width:840px; background:#EDE6D6; color:#1b1b1b; border-radius:30px; padding:30px 40px; font-size:56px; font-weight:600; text-align:center;"
add('luegen',23.5,37.8,f"""
  #lg-h {{ top:300px; font-size:46px; }}
  #lg-b1 {{ {BUB} top:380px; }}
  #lg-b2 {{ {BUB} top:560px; }}
  #lg-e {{ top:820px; font-size:72px; font-weight:700; }}
  #lg-j {{ top:940px; font-size:56px; font-weight:500; }}
""", lambda L: f"""
    <div id="lg-w" class="clip" data-start="0" data-duration="{L(37.8)}">
      <div id="lg-h" class="center lbl">Crippen erzählt</div>
      <div id="lg-b1">„Sie ist zurück in Amerika.“</div>
      <div id="lg-b2">„Sie ist dort gestorben.“</div>
      <div id="lg-e" class="center y">Ethel Le Neve zieht ein</div>
      <div id="lg-j" class="center">💍 trägt <span class="r">Coras Kleider &amp; Schmuck</span></div>
    </div>
""", lambda L: fin("#lg-h",L,23.7,0.3,"{opacity:0}","{opacity:1") + fin("#lg-b1",L,24.6,0.4,"{opacity:0, scale:0.9}","{opacity:1, scale:1",ease="back.out(1.6)") + fin("#lg-b2",L,28.9,0.4,"{opacity:0, scale:0.9}","{opacity:1, scale:1",ease="back.out(1.6)") + f"""
    tl.to("#lg-b1", {{scale:1.04, duration:4.2, ease:"none"}}, {L(25.0)});
    tl.to("#lg-b1, #lg-b2", {{opacity:0.35, duration:0.4}}, {L(30.8)});
""" + fin("#lg-e",L,31.4,0.35) + fin("#lg-j",L,34.7,0.35) + f"""
    tl.to("#lg-e", {{scale:1.05, duration:6, ease:"none"}}, {L(31.8)});
    {out('"#lg-w > *"',L,37.55).strip()}
""")
# 4 YARD 37.8-50.8
add('yard',37.8,50.8,"""
  #yd-a { top:340px; font-size:130px; font-weight:700; }
  #yd-b { top:540px; font-size:46px; }
  #yd-c { top:610px; font-size:96px; font-weight:700; }
  #yd-d { top:800px; font-size:56px; font-weight:500; }
  #yd-st { position:absolute; left:170px; top:920px; width:740px; text-align:center; border:12px solid var(--red); border-radius:14px; color:var(--red); font-size:70px; font-weight:700; padding:8px 0; white-space:nowrap; }
""", lambda L: f"""
    <div id="yd-w" class="clip" data-start="0" data-duration="{L(50.8)}">
      <div id="yd-a" class="center">SCOTLAND YARD</div>
      <div id="yd-b" class="center lbl y">Chief Inspector</div>
      <div id="yd-c" class="center">Walter Dew</div>
      <div id="yd-d" class="center">1. Durchsuchung: <span class="p">nichts</span></div>
      <div id="yd-st">CRIPPEN &amp; LE NEVE: WEG</div>
    </div>
""", lambda L: f"""
    tl.fromTo("#yd-a", {{scale:1.2, opacity:0}}, {{scale:1, opacity:1, duration:0.35, ease:"power4.out"}}, {L(38.2)});
    tl.to("#yd-a", {{scale:1.05, duration:12, ease:"none"}}, {L(38.6)});
""" + fin("#yd-b",L,42.2,0.3,"{opacity:0}","{opacity:1") + fin("#yd-c",L,42.5,0.35) + fin("#yd-d",L,45.5,0.35) + f"""
    tl.fromTo("#yd-st", {{scale:2, rotation:-12, opacity:0}}, {{scale:1, rotation:-4, opacity:1, duration:0.22, ease:"power4.in"}}, {L(49.0)});
    {out('"#yd-w > *"',L,50.55).strip()}
""")
# 5 KELLER 50.8-64.5
add('keller',50.8,64.5,"""
  #kl-h { top:300px; font-size:40px; }
  #kl-floor { position:absolute; left:140px; top:390px; width:800px; height:420px; display:grid; grid-template-columns:repeat(8,1fr); gap:6px; background:#1a1410; padding:6px; }
  #kl-floor .b { background:#6b3f2a; border-radius:3px; }
  #kl-c { top:850px; font-size:56px; font-weight:600; }
  #kl-r { top:950px; font-size:70px; font-weight:700; }
  #kl-g { top:1070px; font-size:52px; font-weight:500; }
""", lambda L: f"""
    <div id="kl-w" class="clip" data-start="0" data-duration="{L(64.5)}">
      <div id="kl-h" class="center lbl y">2. Durchsuchung · Kohlenkeller</div>
      <div id="kl-floor">{''.join(f'<div class="b" id="kl-b{i}"></div>' for i in range(48))}</div>
      <div id="kl-c" class="center">ein <span class="y">loser Ziegelstein</span></div>
      <div id="kl-r" class="center r">Menschliche Überreste</div>
      <div id="kl-g" class="center">☠ Spuren von Gift – <span class="y">vorher gekauft</span></div>
    </div>
""", lambda L: fin("#kl-h",L,51.0,0.3,"{opacity:0}","{opacity:1") + f"""
    tl.fromTo("#kl-floor", {{opacity:0}}, {{opacity:1, duration:0.4}}, {L(51.2)});
    tl.fromTo("#kl-b27", {{backgroundColor:"#6b3f2a"}}, {{backgroundColor:"#F2C230", duration:0.3}}, {L(54.6)});
    tl.to("#kl-b27", {{y:-40, rotation:12, duration:0.5, ease:"power2.out"}}, {L(55.0)});
""" + fin("#kl-c",L,54.7,0.35) + f"""
    tl.to("#kl-floor", {{opacity:0.35, duration:0.5}}, {L(57.4)});
""" + fin("#kl-r",L,57.6,0.35) + fin("#kl-g",L,59.5,0.35) + f"""
    tl.to("#kl-floor", {{scale:1.04, duration:13, ease:"none"}}, {L(51.4)});
    {out('"#kl-w > *"',L,64.25).strip()}
""")
# 6 SCHIFF 64.5-83.3
add('schiff',64.5,83.3,"""
  #sc-h { top:300px; font-size:80px; font-weight:700; }
  #sc-svg { position:absolute; left:0; top:420px; width:1080px; height:280px; }
  #sc-n { top:720px; font-size:60px; font-weight:600; }
  #sc-v { top:810px; font-size:52px; }
  #sc-tg { position:absolute; left:110px; top:350px; width:860px; height:620px; background:#F3E9C8; color:#1b1b1b; box-shadow:0 25px 60px rgba(0,0,0,.55); padding:50px 56px; font-family:'Space Mono',monospace; }
  #sc-tg .hd { font-size:30px; letter-spacing:.2em; border-bottom:3px solid #1b1b1b; padding-bottom:14px; }
  #sc-tg .ln { font-size:36px; line-height:1.4; margin-top:30px; text-transform:uppercase; }
  #sc-k { top:1020px; font-size:52px; font-weight:600; }
""", lambda L: f"""
    <div id="sc-a" class="clip" data-start="0" data-duration="{L(76.2)}">
      <div id="sc-h" class="center">FAHNDUNG</div>
      <svg id="sc-svg" viewBox="0 0 1080 280"><rect x="0" y="190" width="1080" height="90" fill="#16324a"/><g transform="translate(400,90)">{SHIP('sc-ship')}</g><text x="530" y="80" text-anchor="middle" fill="#EDE6D6" font-family="Oswald" font-size="40">SS MONTROSE → Kanada</text></svg>
      <div id="sc-n" class="center">👦 Le Neve <span class="y">als Junge verkleidet</span></div>
      <div id="sc-v" class="center">Kapitän Henry Kendall <span class="r">erkennt sie</span></div>
    </div>
    <div id="sc-b" class="clip" data-start="{L(76.2)}" data-duration="{round(L(83.3)-L(76.2),2)}">
      <div id="sc-tg"><div class="hd">FUNKTELEGRAMM · SS MONTROSE</div>
        <div class="ln" id="sc-l1">Komplizin als Junge verkleidet.</div>
        <div class="ln" id="sc-l2">Statur eindeutig ein Mädchen.</div>
      </div>
      <div id="sc-k" class="center lbl y">📡 an Scotland Yard</div>
    </div>
""", lambda L: f"""
    tl.fromTo("#sc-h", {{scale:1.2, opacity:0}}, {{scale:1, opacity:1, duration:0.35, ease:"power4.out"}}, {L(64.8)});
    tl.fromTo("#sc-svg", {{opacity:0}}, {{opacity:1, duration:0.4}}, {L(66.3)});
    tl.fromTo("#sc-ship", {{x:-60}}, {{x:60, duration:9.6, ease:"none"}}, {L(66.3)});
""" + fin("#sc-n",L,71.0,0.35) + fin("#sc-v",L,73.5,0.35) + f"""
    {out('"#sc-a > *"',L,75.95).strip()}
    tl.fromTo("#sc-tg", {{y:150, rotation:3, opacity:0}}, {{y:0, rotation:-1.5, opacity:1, duration:0.5, ease:"power3.out"}}, {L(76.4)});
""" + fin("#sc-k",L,77.2,0.3,"{opacity:0}","{opacity:1") + f"""
    tl.fromTo("#sc-l1", {{clipPath:"inset(0 100% 0 0)"}}, {{clipPath:"inset(0 0% 0 0)", duration:1.6, ease:"steps(30)"}}, {L(79.05)});
    tl.fromTo("#sc-l2", {{clipPath:"inset(0 100% 0 0)"}}, {{clipPath:"inset(0 0% 0 0)", duration:1.6, ease:"steps(28)"}}, {L(81.1)});
    tl.to("#sc-tg", {{scale:1.04, duration:6.5, ease:"none"}}, {L(76.9)});
    {out('"#sc-b > *"',L,83.05).strip()}
""")
# 7 JAGD 83.3-97.7
add('jagd',83.3,97.7,"""
  #jg-svg { position:absolute; left:0; top:330px; width:1080px; height:520px; }
  #jg-d { top:880px; font-size:96px; font-weight:700; }
  #jg-o { top:1000px; font-size:36px; white-space:nowrap; }
  #jg-st { position:absolute; left:220px; top:1100px; width:640px; text-align:center; border:12px solid var(--red); border-radius:14px; color:var(--red); font-size:76px; font-weight:700; padding:4px 0; }
""", lambda L: f"""
    <div id="jg-w" class="clip" data-start="0" data-duration="{L(97.7)}">
      <svg id="jg-svg" viewBox="0 0 1080 520">
        <rect x="0" y="0" width="1080" height="520" fill="#0f2233" rx="20"/>
        <path d="M1080,40 L960,40 L940,140 L1080,200 Z" fill="#2c3b24"/><text x="1000" y="110" fill="#EDE6D6" font-family="Oswald" font-size="30">Europa</text>
        <path d="M0,280 L120,300 L160,420 L0,520 Z" fill="#2c3b24"/><text x="20" y="380" fill="#EDE6D6" font-family="Oswald" font-size="30">Kanada</text>
        <g id="jg-m"><circle r="16" fill="#B8BCC4"/><text x="0" y="-26" text-anchor="middle" fill="#B8BCC4" font-family="Oswald" font-size="30">Montrose</text></g>
        <g id="jg-l"><circle r="16" fill="#F2C230"/><text x="0" y="46" text-anchor="middle" fill="#F2C230" font-family="Oswald" font-size="30">Dew</text></g>
      </svg>
      <div id="jg-d" class="center">31.07.1910</div>
      <div id="jg-o" class="center lbl y">Sankt-Lorenz-Strom · Dew als Lotse</div>
      <div id="jg-st">FESTGENOMMEN</div>
    </div>
""", lambda L: f"""
    tl.fromTo("#jg-svg", {{opacity:0}}, {{opacity:1, duration:0.4}}, {L(83.5)});
    tl.fromTo("#jg-m", {{x:700, y:200}}, {{x:220, y:330, duration:5.5, ease:"none"}}, {L(83.6)});
    tl.fromTo("#jg-l", {{x:950, y:160}}, {{x:190, y:360, duration:4.6, ease:"power1.inOut"}}, {L(84.2)});
""" + fin("#jg-d",L,89.0,0.4) + fin("#jg-o",L,91.5,0.3,"{opacity:0}","{opacity:1") + f"""
    tl.fromTo("#jg-st", {{scale:2, rotation:-12, opacity:0}}, {{scale:1, rotation:-4, opacity:1, duration:0.22, ease:"power4.in"}}, {L(96.1)});
    tl.to("#jg-svg", {{scale:1.03, duration:13, ease:"none"}}, {L(84.0)});
    {out('"#jg-w > *"',L,97.45).strip()}
""")
# 8 FUNK 97.7-102.7
add('funk',97.7,102.7,"""
  #fk-svg { position:absolute; left:340px; top:330px; width:400px; height:400px; }
  #fk-t { top:780px; font-size:70px; font-weight:700; line-height:1.15; }
""", lambda L: f"""
    <div id="fk-w" class="clip" data-start="0" data-duration="{L(102.7)}">
      <svg id="fk-svg" viewBox="0 0 400 400"><path d="M200,380 L160,200 L240,200 Z" fill="#9EA3AC"/><rect x="190" y="150" width="20" height="60" fill="#9EA3AC"/>{WAVES('fk-wv',200,180)}</svg>
      <div id="fk-t" class="center">Einer der ersten Verbrecher,<br/><span class="y">gefasst per Funk</span></div>
    </div>
""", lambda L: f"""
    tl.fromTo("#fk-svg", {{opacity:0, y:30}}, {{opacity:1, y:0, duration:0.4}}, {L(97.9)});
    tl.fromTo("#fk-wv", {{opacity:0.2, scale:0.7, transformOrigin:"200px 180px"}}, {{opacity:1, scale:1.1, duration:1.2, ease:"sine.inOut", yoyo:true, repeat:3}}, {L(98.2)});
""" + fin("#fk-t",L,98.4,0.4) + f"""
    {out('"#fk-w > *"',L,102.45).strip()}
""")
# 9 URTEIL 102.7-113.5
add('urteil',102.7,113.5,"""
  #ut-a { top:330px; font-size:56px; }
  #ut-b { top:410px; font-size:130px; font-weight:700; }
  #ut-c { top:640px; font-size:64px; font-weight:600; }
  #ut-d { top:780px; font-size:64px; font-weight:600; }
""", lambda L: f"""
    <div id="ut-w" class="clip" data-start="0" data-duration="{L(113.5)}">
      <div id="ut-a" class="center lbl y">Oktober 1910 · London</div>
      <div id="ut-b" class="center r">SCHULDIG</div>
      <div id="ut-c" class="center">23.11.1910 · <span class="p">hingerichtet</span></div>
      <div id="ut-d" class="center">Ethel Le Neve: <span class="y">freigesprochen</span></div>
    </div>
""", lambda L: fin("#ut-a",L,103.0,0.3,"{opacity:0}","{opacity:1") + f"""
    tl.fromTo("#ut-b", {{scale:1.4, opacity:0}}, {{scale:1, opacity:1, duration:0.3, ease:"power4.out"}}, {L(105.6)});
    tl.to("#ut-b", {{scale:1.05, duration:7.5, ease:"none"}}, {L(105.9)});
""" + fin("#ut-c",L,107.7,0.35) + fin("#ut-d",L,111.0,0.35) + f"""
    {out('"#ut-w > *"',L,113.25).strip()}
""")
# 10 DNA 113.5-125.7
add('dna',113.5,125.7,"""
  #dn-a { top:320px; font-size:38px; white-space:nowrap; }
  #dn-svg { position:absolute; left:390px; top:410px; width:300px; height:420px; }
  #dn-b { top:860px; font-size:62px; font-weight:600; }
  #dn-c { top:960px; font-size:50px; font-weight:500; }
  #dn-st { position:absolute; left:230px; top:1060px; width:620px; text-align:center; border:12px solid var(--accent); border-radius:14px; color:var(--accent); font-size:80px; font-weight:700; padding:4px 0; }
""", lambda L: f"""
    <div id="dn-w" class="clip" data-start="0" data-duration="{L(125.7)}">
      <div id="dn-a" class="center lbl y">Fast 100 Jahre später · DNA-Analyse</div>
      <svg id="dn-svg" viewBox="0 0 300 420"><g id="dn-h">{''.join(f'<line x1="{150-90*__import__("math").sin(i/2)}" y1="{20+i*20}" x2="{150+90*__import__("math").sin(i/2)}" y2="{20+i*20}" stroke="{"#F2C230" if i%2 else "#EDE6D6"}" stroke-width="6"/>' for i in range(20))}</g></svg>
      <div id="dn-b" class="center">Überreste <span class="r">nicht von Cora?</span></div>
      <div id="dn-c" class="center">Andere Fachleute: nicht überzeugend</div>
      <div id="dn-st">UMSTRITTEN</div>
    </div>
""", lambda L: fin("#dn-a",L,113.8,0.3,"{opacity:0}","{opacity:1") + f"""
    tl.fromTo("#dn-svg", {{opacity:0, scale:0.8}}, {{opacity:1, scale:1, duration:0.5, ease:"power3.out"}}, {L(116.0)});
    tl.fromTo("#dn-h", {{scaleX:1, transformOrigin:"150px 210px"}}, {{scaleX:-1, duration:2.4, ease:"sine.inOut", yoyo:true, repeat:3}}, {L(116.4)});
""" + fin("#dn-b",L,118.9,0.35) + fin("#dn-c",L,122.4,0.35) + f"""
    tl.fromTo("#dn-st", {{scale:2, rotation:-12, opacity:0}}, {{scale:1, rotation:-4, opacity:1, duration:0.22, ease:"power4.in"}}, {L(124.2)});
    {out('"#dn-w > *"',L,125.45).strip()}
""")
# 11 CTA 125.7-131
add('cta',125.7,131.0,"""
  #ct-q { top:500px; font-size:130px; font-weight:700; line-height:1.05; }
  #ct-s { top:880px; font-size:56px; font-weight:500; }
  #ct-arrow { top:1000px; font-size:120px; }
""", lambda L: f"""
    <div id="ct-q" class="center clip" data-start="0" data-duration="{L(131)}">Schuldig oder<br/><span class="y">Justizirrtum?</span></div>
    <div id="ct-s" class="center clip" data-start="{L(128.3)}" data-duration="{round(L(131)-L(128.3),2)}">Schreib's in die Kommentare</div>
    <div id="ct-arrow" class="center clip y" data-start="{L(128.6)}" data-duration="{round(L(131)-L(128.6),2)}">↓</div>
""", lambda L: f"""
    tl.fromTo("#ct-q", {{scale:1.15, opacity:0}}, {{scale:1, opacity:1, duration:0.4, ease:"power4.out"}}, {L(126.0)});
    tl.to("#ct-q", {{scale:1.04, duration:4.8, ease:"none"}}, {L(126.4)});
    tl.fromTo("#ct-s", {{opacity:0, y:20}}, {{opacity:1, y:0, duration:0.35}}, {L(128.4)});
    tl.fromTo("#ct-arrow", {{y:-20, opacity:0}}, {{y:20, opacity:1, duration:0.6, ease:"sine.inOut"}}, {L(128.6)});
    tl.to("#ct-arrow", {{y:-10, duration:0.6, ease:"sine.inOut"}}, {L(129.2)});
    tl.to("#ct-arrow", {{y:20, duration:0.6, ease:"sine.inOut"}}, {L(129.8)});
""")
TOTAL=131.0
hosts=[]
for cid,s0,s1,css,body,js in SC:
    dur=round(s1-s0,2)
    open(f'compositions/{cid}.html','w').write(scene(cid,dur,css,body,js))
    hosts.append(f'      <div id="{cid}" data-composition-id="{cid}" data-composition-src="compositions/{cid}.html" data-start="{s0}" data-duration="{dur}" data-track-index="2" data-track-kind="graphics" data-width="1080" data-height="1920" style="z-index:3"></div>')
sfx = [ # (file, time, vol)
 ('impact-bass-1',0.0,0.8),('ping',9.45,0.4),
 ('whoosh-cinematic',10.6,0.5),('whoosh-short',11.9,0.4),('whoosh-short',14.6,0.4),('impact-bass-2',22.0,0.6),
 ('whoosh-cinematic',23.5,0.5),('pop',24.6,0.4),('pop',28.9,0.4),
 ('whoosh-cinematic',37.8,0.5),('impact-bass-2',38.2,0.5),('impact-bass-1',49.0,0.7),
 ('whoosh-cinematic',50.8,0.5),('click',54.6,0.5),('impact-bass-2',57.6,0.6),
 ('whoosh-cinematic',64.5,0.5),('whoosh',76.2,0.4),('typing',79.05,0.35),('typing',81.1,0.35),
 ('whoosh-cinematic',83.3,0.5),('riser',92.0,0.3),('impact-bass-1',96.1,0.8),
 ('notification',98.2,0.3),('whoosh-cinematic',102.7,0.5),('impact-bass-1',105.6,0.8),
 ('whoosh-cinematic',113.5,0.5),('impact-bass-2',124.2,0.6),('whoosh',125.7,0.4),
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
      <div id="case" class="clip" data-start="0" data-duration="{TOTAL}" data-track-index="4">FALL 005 · DR. CRIPPEN · 1910</div>
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
