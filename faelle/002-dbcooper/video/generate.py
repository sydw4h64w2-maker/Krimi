# Folge 2 – D. B. Cooper. Alle Zeiten global (Sekunden im Audio); L() rechnet in Szenenzeit um.
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

# 1 HOOK 0-9.8
add('hook',0,9.8,"""
  #hk-a { top:400px; font-size:250px; font-weight:700; line-height:1; }
  #hk-b { top:690px; font-size:64px; font-weight:600; }
  #hk-chute { position:absolute; left:390px; top:820px; width:300px; height:300px; }
  #hk-c { top:600px; font-size:120px; font-weight:700; line-height:1.05; }
""", lambda L: f"""
    <div id="hk-1" class="clip" data-start="0" data-duration="{L(6.7)}">
      <div id="hk-a" class="center y">$200.000</div>
      <div id="hk-b" class="center">Lösegeld · 1 Fallschirmsprung</div>
      <svg id="hk-chute" viewBox="0 0 100 100"><path d="M10,40 Q50,-5 90,40 Z" fill="#F2C230"/><path d="M10,40 Q30,30 50,40 Q70,30 90,40" fill="none" stroke="#0c0e12" stroke-width="2"/><line x1="12" y1="40" x2="50" y2="78" stroke="#EDE6D6" stroke-width="1.5"/><line x1="88" y1="40" x2="50" y2="78" stroke="#EDE6D6" stroke-width="1.5"/><line x1="50" y1="40" x2="50" y2="78" stroke="#EDE6D6" stroke-width="1.5"/><circle cx="50" cy="82" r="5" fill="#EDE6D6"/><rect x="46" y="86" width="8" height="10" rx="2" fill="#EDE6D6"/></svg>
    </div>
    <div id="hk-2" class="clip" data-start="{L(6.7)}" data-duration="{L(9.8)-L(6.7)}">
      <div id="hk-c" class="center">BIS HEUTE<br/><span class="r">UNBEKANNT</span></div>
    </div>
""", lambda L: f"""
    tl.fromTo("#hk-a", {{scale:1.1, opacity:1}}, {{scale:1, opacity:1, duration:0.35, ease:"power4.out"}}, 0);
    tl.to("#hk-a", {{scale:1.06, duration:6.0, ease:"none"}}, 0.4);
    tl.fromTo("#hk-b", {{y:20, opacity:1}}, {{y:0, opacity:1, duration:0.4}}, 0.1);
    tl.fromTo("#hk-chute", {{y:-200, opacity:0}}, {{y:60, opacity:1, duration:2.2, ease:"power1.out"}}, {L(4.15)});
    tl.to("#hk-chute", {{y:120, rotation:6, duration:0.4, ease:"none"}}, {L(6.35)});
    {out('"#hk-1 > *"',L,6.45).strip()}
    tl.fromTo("#hk-c", {{scale:1.2, opacity:0}}, {{scale:1, opacity:1, duration:0.35, ease:"power4.out"}}, {L(6.9)});
    tl.to("#hk-c", {{scale:1.05, duration:2.4, ease:"none"}}, {L(7.25)});
    {out('"#hk-c"',L,9.5).strip()}
""")
# 2 TICKET 9.8-23.1
add('ticket',9.8,23.1,"""
  #tk-date { top:320px; font-size:110px; font-weight:700; }
  #tk-place { top:470px; font-size:44px; }
  #tk-card { position:absolute; left:100px; top:620px; width:880px; height:470px; background:var(--paper); color:#111; border-radius:18px; box-shadow:0 30px 80px rgba(0,0,0,.5); overflow:hidden; }
  #tk-card .band { position:absolute; left:0; top:0; width:100%; height:90px; background:#B3261E; color:#fff; font-family:'Space Mono',monospace; font-size:30px; letter-spacing:.15em; line-height:90px; padding-left:44px; }
  #tk-card .route { position:absolute; left:44px; top:130px; font-size:120px; font-weight:700; letter-spacing:.02em; }
  #tk-card .f { position:absolute; left:44px; top:290px; font-family:'Space Mono',monospace; font-size:30px; color:#444; }
  #tk-card .v { position:absolute; left:44px; top:330px; font-size:64px; font-weight:600; }
  #tk-card .pay { position:absolute; right:44px; top:300px; width:230px; text-align:center; font-family:'Space Mono',monospace; font-size:28px; color:#B3261E; border:5px solid #B3261E; border-radius:10px; padding:10px 0; transform:rotate(-8deg); }
""", lambda L: f"""
    <div id="tk-w" class="clip" data-start="0" data-duration="{L(23.1)}">
      <div id="tk-date" class="center">24.11.1971</div>
      <div id="tk-place" class="center lbl y">Portland · USA</div>
      <div id="tk-card">
        <div class="band">BORDKARTE · FLUG 305</div>
        <div class="route">PDX → SEA</div>
        <div class="pay" id="tk-pay">BAR<br/>BEZAHLT</div>
        <div class="f">PASSAGIER</div>
        <div class="v" id="tk-name">DAN COOPER</div>
      </div>
    </div>
""", lambda L: fin("#tk-date",L,9.97,0.45) + fin("#tk-place",L,13.56,0.3,"{opacity:0}","{opacity:1") + f"""
    tl.fromTo("#tk-card", {{y:160, rotation:4, opacity:0}}, {{y:0, rotation:-1.5, opacity:1, duration:0.55, ease:"power3.out"}}, {L(15.6)});
    tl.fromTo("#tk-pay", {{scale:2, opacity:0}}, {{scale:1, opacity:1, duration:0.22, ease:"power4.in"}}, {L(17.6)});
    tl.fromTo("#tk-name", {{opacity:0, x:-30}}, {{opacity:1, x:0, duration:0.35}}, {L(20.95)});
    tl.to("#tk-card", {{scale:1.04, duration:6.8, ease:"none"}}, {L(16.2)});
    {out('"#tk-w > *"',L,22.8).strip()}
""")
# 3 ZETTEL 23.1-37.2
add('zettel',23.1,37.2,"""
  #zt-note { position:absolute; left:200px; top:380px; width:680px; height:520px; background:#F4EFD8; box-shadow:0 25px 60px rgba(0,0,0,.55); padding:60px; color:#222; }
  #zt-note .lines { position:absolute; inset:0; background:repeating-linear-gradient(0deg, transparent 0 58px, rgba(60,90,160,.25) 58px 60px); }
  #zt-q { position:absolute; left:40px; top:70px; width:600px; text-align:center; font-size:58px; white-space:nowrap; font-weight:500; color:#555; }
  #zt-bomb { position:absolute; left:60px; top:260px; width:560px; text-align:center; font-size:130px; font-weight:700; color:var(--red); }
  #zt-cap { top:960px; font-size:46px; }
  #zt-dem { top:400px; font-size:56px; }
  #zt-m { top:500px; font-size:220px; font-weight:700; line-height:1; }
  #zt-p { top:780px; font-size:96px; font-weight:600; }
""", lambda L: f"""
    <div id="zt-a" class="clip" data-start="0" data-duration="{L(32.6)}">
      <div id="zt-note"><div class="lines"></div>
        <div id="zt-q">☎ Telefonnummer?</div>
        <div id="zt-bomb">BOMBE</div>
      </div>
      <div id="zt-cap" class="center lbl p">Ein Zettel für die Flugbegleiterin</div>
    </div>
    <div id="zt-b" class="clip" data-start="{L(32.6)}" data-duration="{round(L(37.2)-L(32.6),2)}">
      <div id="zt-dem" class="center lbl y">Die Forderung</div>
      <div id="zt-m" class="center">$200.000</div>
      <div id="zt-p" class="center">+ <span class="y">4</span> Fallschirme</div>
    </div>
""", lambda L: f"""
    tl.fromTo("#zt-note", {{x:-500, rotation:-12, opacity:0}}, {{x:0, rotation:-3, opacity:1, duration:0.6, ease:"power3.out"}}, {L(23.3)});
    tl.fromTo("#zt-cap", {{opacity:0}}, {{opacity:1, duration:0.3}}, {L(24.2)});
    tl.fromTo("#zt-q", {{opacity:0}}, {{opacity:1, duration:0.3}}, {L(27.4)});
    tl.to("#zt-q", {{opacity:0.25, duration:0.3}}, {L(29.9)});
    tl.fromTo("#zt-bomb", {{scale:2.2, opacity:0}}, {{scale:1, opacity:1, duration:0.22, ease:"power4.in"}}, {L(31.4)});
    tl.to("#zt-note", {{scale:1.05, duration:8.4, ease:"none"}}, {L(23.9)});
    {out('"#zt-a > *"',L,32.35).strip()}
    tl.fromTo("#zt-dem", {{opacity:0}}, {{opacity:1, duration:0.25}}, {L(32.7)});
    tl.fromTo("#zt-m", {{scale:1.25, opacity:0}}, {{scale:1, opacity:1, duration:0.35, ease:"power4.out"}}, {L(33.95)});
    tl.fromTo("#zt-p", {{y:30, opacity:0}}, {{y:0, opacity:1, duration:0.3}}, {L(35.6)});
    {out('"#zt-b > *"',L,36.95).strip()}
""")
# 4 GELD 37.2-49.4
add('geld',37.2,49.4,"""
  #gd-city { top:300px; font-size:110px; font-weight:700; }
  #gd-stack { position:absolute; left:290px; top:470px; width:500px; height:360px; }
  #gd-stack .bill { position:absolute; left:0; width:500px; height:210px; background:#3E6B47; border:6px solid #9CC3A2; border-radius:10px; }
  #gd-stack .bill span { position:absolute; left:30px; top:40px; font-size:110px; font-weight:700; color:#D9EBDC; }
  #gd-n { top:880px; font-size:96px; font-weight:700; }
  #gd-ser { position:absolute; left:120px; top:1020px; width:840px; text-align:center; font-family:'Space Mono',monospace; font-size:34px; color:var(--paper); }
  #gd-ser b { color:var(--accent); font-weight:400; }
  #gd-pax { top:1130px; font-size:60px; font-weight:600; }
""", lambda L: f"""
    <div id="gd-w" class="clip" data-start="0" data-duration="{L(49.4)}">
      <div id="gd-city" class="center">SEATTLE</div>
      <div id="gd-stack" data-layout-allow-overlap><div class="bill" id="gd-b1" style="top:150px"><span>$20</span></div><div class="bill" id="gd-b2" style="top:90px"><span>$20</span></div><div class="bill" id="gd-b3" style="top:30px"><span>$20</span></div></div>
      <div id="gd-n" class="center">10.000 <span class="y">×</span> $20</div>
      <div id="gd-ser">📷 jede Seriennummer <b>fotografiert</b></div>
      <div id="gd-pax" class="center">36 Passagiere <span class="y">frei</span></div>
    </div>
""", lambda L: fin("#gd-city",L,37.3,0.45) + f"""
    ["#gd-b1","#gd-b2","#gd-b3"].forEach((s,i)=>{{ tl.fromTo(s, {{y:-400, opacity:0, rotation:-6+i*5}}, {{y:0, opacity:1, rotation:-3+i*3, duration:0.4, ease:"power3.out"}}, {L(39.45)}+i*0.25); }});
""" + fin("#gd-n",L,40.3,0.35) + fin("#gd-ser",L,42.0,0.3) + fin("#gd-pax",L,46.5,0.35) + f"""
    tl.to("#gd-stack", {{scale:1.05, duration:8.5, ease:"none"}}, {L(40.6)});
    {out('"#gd-w > *"',L,49.1).strip()}
""")
# 5 FLUG 49.4-59.3  (route map, stylised)
add('flug',49.4,59.3,"""
  #fl-h { top:300px; font-size:52px; }
  #fl-map { position:absolute; left:140px; top:390px; width:800px; height:640px; }
  #fl-d1 { top:1060px; font-size:62px; font-weight:600; }
  #fl-d2 { top:1150px; font-size:62px; font-weight:600; }
""", lambda L: f"""
    <div id="fl-w" class="clip" data-start="0" data-duration="{L(59.3)}">
      <div id="fl-h" class="center lbl y">Neuer Kurs</div>
      <svg id="fl-map" viewBox="0 0 800 640">
        <path id="fl-route" d="M180,60 C200,200 230,260 260,300 S420,470 560,580" fill="none" stroke="#F2C230" stroke-width="8" stroke-dasharray="900" stroke-dashoffset="900" stroke-linecap="round"/>
        <circle cx="180" cy="60" r="16" fill="#EDE6D6"/><text x="210" y="72" fill="#EDE6D6" font-family="Oswald" font-size="44">Seattle</text>
        <g id="fl-reno"><circle cx="260" cy="300" r="16" fill="#F2C230"/><text x="292" y="312" fill="#F2C230" font-family="Oswald" font-size="44">Reno (Tankstopp)</text></g>
        <g id="fl-mex"><circle cx="560" cy="580" r="16" fill="#EDE6D6"/><text x="400" y="545" fill="#EDE6D6" font-family="Oswald" font-size="44">Mexiko-Stadt?</text></g>
      </svg>
      <div id="fl-d1" class="center">✈ niedrig fliegen</div>
      <div id="fl-d2" class="center">⚙ Fahrwerk <span class="y">ausgefahren</span></div>
    </div>
""", lambda L: f"""
    tl.fromTo("#fl-h", {{opacity:0}}, {{opacity:1, duration:0.3}}, {L(49.5)});
    tl.fromTo("#fl-map", {{opacity:0}}, {{opacity:1, duration:0.4}}, {L(49.6)});
    tl.fromTo("#fl-route", {{strokeDashoffset:900}}, {{strokeDashoffset:0, duration:3.6, ease:"power1.inOut"}}, {L(51.5)});
    tl.fromTo("#fl-mex", {{opacity:0}}, {{opacity:1, duration:0.3}}, {L(52.2)});
    tl.fromTo("#fl-reno", {{opacity:0, scale:0.6, transformOrigin:"260px 300px"}}, {{opacity:1, scale:1, duration:0.35, ease:"back.out(2)"}}, {L(53.5)});
""" + fin("#fl-d1",L,56.55,0.3) + fin("#fl-d2",L,57.65,0.3) + f"""
    {out('"#fl-w > *"',L,59.0).strip()}
""")
# 6 SPRUNG 59.3-72.1
add('sprung',59.3,72.1,"""
  #sp-sky { position:absolute; inset:0; background:radial-gradient(ellipse at 50% 30%, rgba(80,100,160,.25), transparent 70%); }
  #sp-plane { position:absolute; left:90px; top:380px; width:900px; height:300px; }
  #sp-man { position:absolute; left:250px; top:600px; width:60px; height:90px; }
  #sp-t1 { top:960px; font-size:58px; font-weight:600; }
  #sp-t2 { top:1060px; font-size:46px; }
  #sp-t3 { top:1150px; font-size:70px; font-weight:700; }
""", lambda L: f"""
    <div id="sp-w" class="clip" data-start="0" data-duration="{L(72.1)}">
      <div id="sp-sky"></div>
      <svg id="sp-plane" viewBox="0 0 900 300">
        <path d="M60,150 L760,140 Q850,140 870,160 Q850,180 760,180 L60,170 Z" fill="#B8BCC4"/>
        <path d="M120,145 L40,60 L95,60 L210,145 Z" fill="#9EA3AC"/>
        <path d="M500,160 L380,250 L450,250 L620,165 Z" fill="#9EA3AC"/>
        <rect x="70" y="120" width="120" height="22" rx="6" fill="#9EA3AC"/>
        <g id="sp-stair"><rect x="150" y="165" width="120" height="14" fill="#F2C230"/></g>
      </svg>
      <svg id="sp-man" viewBox="0 0 60 90"><circle cx="30" cy="14" r="11" fill="#EDE6D6"/><rect x="18" y="28" width="24" height="34" rx="8" fill="#EDE6D6"/><rect x="10" y="30" width="10" height="26" rx="5" fill="#EDE6D6"/><rect x="40" y="30" width="10" height="26" rx="5" fill="#EDE6D6"/><rect x="20" y="60" width="9" height="28" rx="4" fill="#EDE6D6"/><rect x="31" y="60" width="9" height="28" rx="4" fill="#EDE6D6"/></svg>
      <div id="sp-t1" class="center">Hintere Tür auf · Treppe runter</div>
      <div id="sp-t2" class="center lbl y">Südwest-Washington · nachts</div>
      <div id="sp-t3" class="center r">MIT DEM GELD</div>
    </div>
""", lambda L: f"""
    tl.fromTo("#sp-plane", {{x:300, opacity:0}}, {{x:0, opacity:1, duration:0.8, ease:"power2.out"}}, {L(59.4)});
    tl.fromTo("#sp-plane", {{y:0}}, {{y:-20, duration:12, ease:"sine.inOut"}}, {L(60.2)});
""" + fin("#sp-t1",L,60.5,0.35) + f"""
    tl.fromTo("#sp-stair", {{rotation:0, transformOrigin:"270px 172px"}}, {{rotation:-28, duration:0.8, ease:"power2.inOut"}}, {L(63.5)});
    tl.fromTo("#sp-man", {{x:0, y:0, opacity:0}}, {{x:0, y:0, opacity:1, duration:0.15}}, {L(65.0)});
    tl.to("#sp-man", {{x:-120, y:520, rotation:-200, duration:2.2, ease:"power2.in"}}, {L(65.15)});
    tl.to("#sp-man", {{opacity:0, duration:0.3}}, {L(67.1)});
""" + fin("#sp-t2",L,66.4,0.3,"{opacity:0}","{opacity:1") + f"""
    tl.fromTo("#sp-t3", {{scale:1.3, opacity:0}}, {{scale:1, opacity:1, duration:0.3, ease:"power4.out"}}, {L(70.3)});
    {out('"#sp-w > *"',L,71.85).strip()}
""")
# 7 RENO 72.1-76.6
add('reno',72.1,76.6,"""
  #rn-a { top:420px; font-size:56px; }
  #rn-b { top:500px; font-size:160px; font-weight:700; }
  #rn-st { position:absolute; left:170px; top:780px; width:740px; text-align:center; border:12px solid var(--red); border-radius:14px; color:var(--red); font-size:76px; font-weight:700; padding:16px 0; white-space:nowrap; }
""", lambda L: f"""
    <div id="rn-a" class="center clip lbl y" data-start="0" data-duration="{L(76.6)}">Landung</div>
    <div id="rn-b" class="center clip" data-start="0" data-duration="{L(76.6)}">RENO</div>
    <div id="rn-st" class="clip" data-start="0" data-duration="{L(76.6)}">COOPER: KEINE SPUR</div>
""", lambda L: f"""
    tl.fromTo("#rn-a", {{opacity:0}}, {{opacity:1, duration:0.3}}, {L(72.2)});
    tl.fromTo("#rn-b", {{scale:1.2, opacity:0}}, {{scale:1, opacity:1, duration:0.35, ease:"power4.out"}}, {L(72.3)});
    tl.to("#rn-b", {{scale:1.06, duration:3.8, ease:"none"}}, {L(72.65)});
    tl.fromTo("#rn-st", {{scale:2, rotation:-12, opacity:0}}, {{scale:1, rotation:-5, opacity:1, duration:0.22, ease:"power4.in"}}, {L(74.45)});
    tl.to(["#rn-a","#rn-b","#rn-st"], {{opacity:0, duration:0.25}}, {L(76.35)});
""")
# 8 NAME 76.6-83.7
add('name',76.6,83.7,"""
  #nm-h { top:380px; font-size:46px; }
  #nm-a { top:470px; font-size:130px; font-weight:700; color:var(--paper); }
  #nm-x { position:absolute; left:250px; top:545px; width:580px; height:14px; background:var(--red); transform-origin:left center; }
  #nm-b { top:690px; font-size:170px; font-weight:700; }
  #nm-c { top:930px; font-size:56px; font-weight:500; }
""", lambda L: f"""
    <div id="nm-w" class="clip" data-start="0" data-duration="{L(83.7)}">
      <div id="nm-h" class="center lbl">Ein Reporter hört falsch</div>
      <div id="nm-a" class="center">Dan Cooper</div>
      <div id="nm-x"></div>
      <div id="nm-b" class="center y">D. B. COOPER</div>
      <div id="nm-c" class="center">So kennt ihn die ganze Welt</div>
    </div>
""", lambda L: fin("#nm-h",L,76.7,0.3,"{opacity:0}","{opacity:1") + fin("#nm-a",L,77.0,0.35) + f"""
    tl.fromTo("#nm-x", {{scaleX:0}}, {{scaleX:1, duration:0.35, ease:"power2.out"}}, {L(78.6)});
    tl.fromTo("#nm-b", {{scale:1.3, opacity:0}}, {{scale:1, opacity:1, duration:0.35, ease:"power4.out"}}, {L(79.4)});
    tl.to("#nm-b", {{scale:1.05, duration:3.8, ease:"none"}}, {L(79.75)});
""" + fin("#nm-c",L,80.95,0.35) + f"""
    {out('"#nm-w > *"',L,83.45).strip()}
""")
# 9 FUND 83.7-100.2
add('fund',83.7,100.2,"""
  #fd-y { top:300px; font-size:150px; font-weight:700; }
  #fd-river { position:absolute; left:0; top:520px; width:1080px; height:200px; background:repeating-linear-gradient(90deg, #1d3550 0 60px, #24425f 60px 120px); }
  #fd-riv { top:545px; font-size:46px; color:#cfe0f0; }
  #fd-sand { position:absolute; left:0; top:720px; width:1080px; height:300px; background:#5b4a33; }
  #fd-bills { position:absolute; left:300px; top:780px; width:480px; height:180px; }
  #fd-bills .b { position:absolute; width:200px; height:90px; background:#56704f; border:4px solid #8aa585; border-radius:6px; opacity:.85; }
  #fd-amt { top:1050px; font-size:110px; font-weight:700; }
  #fd-ok { top:1180px; font-size:50px; font-weight:600; }
  #fd-rest { top:480px; font-size:96px; font-weight:700; line-height:1.1; }
  #fd-rest2 { top:720px; font-size:52px; }
""", lambda L: f"""
    <div id="fd-a" class="clip" data-start="0" data-duration="{L(97.2)}">
      <div id="fd-y" class="center">1980</div>
      <div id="fd-river"></div><div id="fd-riv" class="center lbl">Columbia River</div>
      <div id="fd-sand"></div>
      <div id="fd-bills"><div class="b" style="left:0;top:40px;transform:rotate(-12deg)"></div><div class="b" style="left:140px;top:10px;transform:rotate(8deg)"></div><div class="b" style="left:270px;top:60px;transform:rotate(-4deg)"></div></div>
      <div id="fd-amt" class="center y">≈ $5.800</div>
      <div id="fd-ok" class="center">Seriennummern: <span class="y">✔ passen</span></div>
    </div>
    <div id="fd-b" class="clip" data-start="{L(97.2)}" data-duration="{round(L(100.2)-L(97.2),2)}">
      <div id="fd-rest" class="center">Der Rest<br/><span class="r">NIE GEFUNDEN</span></div>
    </div>
""", lambda L: fin("#fd-y",L,83.9,0.4) + f"""
    tl.fromTo("#fd-river, #fd-riv", {{opacity:0}}, {{opacity:1, duration:0.5}}, {L(85.7)});
    tl.fromTo("#fd-river", {{x:0}}, {{x:-240, duration:11.5, ease:"none"}}, {L(85.7)});
    tl.fromTo("#fd-sand", {{opacity:0}}, {{opacity:1, duration:0.5}}, {L(86.2)});
    tl.fromTo("#fd-bills", {{opacity:0, y:30}}, {{opacity:1, y:0, duration:0.5}}, {L(90.3)});
""" + fin("#fd-amt",L,92.8,0.35) + fin("#fd-ok",L,95.4,0.3) + f"""
    {out('"#fd-a > *"',L,96.95).strip()}
    tl.fromTo("#fd-rest", {{scale:1.2, opacity:0}}, {{scale:1, opacity:1, duration:0.35, ease:"power4.out"}}, {L(97.35)});
    tl.to("#fd-rest", {{scale:1.05, duration:2.4, ease:"none"}}, {L(97.7)});
    {out('"#fd-rest"',L,99.95).strip()}
""")
# 10 FBI 100.2-107.2
add('fbi',100.2,107.2,"""
  #fb-n { top:380px; font-size:260px; font-weight:700; line-height:1; }
  #fb-l { top:660px; font-size:60px; font-weight:600; }
  #fb-st { position:absolute; left:120px; top:830px; width:840px; text-align:center; border:12px solid var(--red); border-radius:14px; color:var(--red); padding:18px 0; }
  #fb-st .a { font-size:110px; font-weight:700; line-height:1; } #fb-st .b { font-size:52px; font-weight:600; }
""", lambda L: f"""
    <div id="fb-w" class="clip" data-start="0" data-duration="{L(107.2)}">
      <div id="fb-n" class="center y"><span id="fb-c">1971</span></div>
      <div id="fb-l" class="center">45 Jahre Ermittlungen</div>
      <div id="fb-st"><div class="a">EINGESTELLT</div><div class="b">FBI · AKTIVE SUCHE</div></div>
    </div>
""", lambda L: f"""
    tl.fromTo("#fb-n", {{opacity:0}}, {{opacity:1, duration:0.3}}, {L(100.4)});
    const yr = {{v:1971}};
    tl.fromTo(yr, {{v:1971}}, {{v:2016, duration:2.6, ease:"power1.inOut", onUpdate:()=>{{ document.querySelector("#fb-c").textContent = Math.round(yr.v); }}}}, {L(100.5)});
""" + fin("#fb-l",L,101.2,0.35) + f"""
    tl.fromTo("#fb-st", {{scale:2, rotation:-12, opacity:0}}, {{scale:1, rotation:-4, opacity:1, duration:0.22, ease:"power4.in"}}, {L(103.75)});
    tl.to("#fb-n", {{scale:1.05, duration:3.4, ease:"none"}}, {L(103.4)});
    {out('"#fb-w > *"',L,106.95).strip()}
""")
# 11 VANE 107.2-117.3
add('vane',107.2,117.3,"""
  #vn-h { top:320px; font-size:52px; }
  #vn-t { top:400px; font-size:140px; font-weight:700; }
  #vn-svg { position:absolute; left:140px; top:600px; width:800px; height:420px; }
  #vn-c { top:1080px; font-size:54px; font-weight:600; }
""", lambda L: f"""
    <div id="vn-w" class="clip" data-start="0" data-duration="{L(117.3)}">
      <div id="vn-h" class="center lbl y">Cooper verändert die Luftfahrt</div>
      <div id="vn-t" class="center">COOPER VANE</div>
      <svg id="vn-svg" viewBox="0 0 800 420">
        <path d="M0,120 L720,120 Q790,120 800,150 L800,190 L0,190 Z" fill="#B8BCC4"/>
        <rect id="vn-stair" x="360" y="190" width="260" height="22" fill="#F2C230"/>
        <g id="vn-flap"><rect x="610" y="190" width="18" height="90" fill="#D2372E"/><path d="M628,200 L700,230 L628,262 Z" fill="#D2372E"/></g>
        <text x="250" y="350" fill="#EDE6D6" font-family="Space Mono" font-size="30">Klappe sperrt die Treppe</text>
        <path d="M660,320 L640,285" stroke="#EDE6D6" stroke-width="3"/>
      </svg>
      <div id="vn-c" class="center">Hecktreppe im Flug: <span class="r">gesperrt</span></div>
    </div>
""", lambda L: fin("#vn-h",L,107.4,0.3,"{opacity:0}","{opacity:1") + f"""
    tl.fromTo("#vn-t", {{scale:1.2, opacity:0}}, {{scale:1, opacity:1, duration:0.35, ease:"power4.out"}}, {L(110.5)});
    tl.fromTo("#vn-svg", {{opacity:0, y:30}}, {{opacity:1, y:0, duration:0.4}}, {L(108.0)});
    tl.fromTo("#vn-flap", {{rotation:-90, transformOrigin:"619px 190px", opacity:0}}, {{rotation:0, opacity:1, duration:0.6, ease:"back.out(2)"}}, {L(111.0)});
    tl.fromTo("#vn-stair", {{rotation:-14, transformOrigin:"360px 200px"}}, {{rotation:0, duration:0.5, ease:"power2.out"}}, {L(114.0)});
""" + fin("#vn-c",L,114.0,0.35) + f"""
    tl.to("#vn-t", {{scale:1.05, duration:6.2, ease:"none"}}, {L(110.85)});
    {out('"#vn-w > *"',L,117.05).strip()}
""")
# 12 CTA 117.3-122
add('cta',117.3,122.0,"""
  #ct-q { top:500px; font-size:130px; font-weight:700; line-height:1.05; }
  #ct-s { top:860px; font-size:56px; font-weight:500; }
  #ct-arrow { top:980px; font-size:120px; }
""", lambda L: f"""
    <div id="ct-q" class="center clip" data-start="0" data-duration="{L(122)}">Hat er den Sprung<br/><span class="y">überlebt?</span></div>
    <div id="ct-s" class="center clip" data-start="{L(119.2)}" data-duration="{round(L(122)-L(119.2),2)}">Schreib's in die Kommentare</div>
    <div id="ct-arrow" class="center clip y" data-start="{L(119.5)}" data-duration="{round(L(122)-L(119.5),2)}">↓</div>
""", lambda L: f"""
    tl.fromTo("#ct-q", {{scale:1.15, opacity:0}}, {{scale:1, opacity:1, duration:0.4, ease:"power4.out"}}, {L(117.45)});
    tl.fromTo("#ct-s", {{opacity:0, y:20}}, {{opacity:1, y:0, duration:0.35}}, {L(119.3)});
    tl.fromTo("#ct-arrow", {{y:-20, opacity:0}}, {{y:20, opacity:1, duration:0.6, ease:"sine.inOut"}}, {L(119.5)});
    tl.to("#ct-arrow", {{y:-10, duration:0.6, ease:"sine.inOut"}}, {L(120.1)});
    tl.to("#ct-arrow", {{y:20, duration:0.6, ease:"sine.inOut"}}, {L(120.7)});
    tl.to("#ct-arrow", {{y:-10, duration:0.6, ease:"sine.inOut"}}, {L(121.3)});
""")

TOTAL=122.0
hosts=[]
for cid,s0,s1,css,body,js in SC:
    dur=round(s1-s0,2)
    open(f'compositions/{cid}.html','w').write(scene(cid,dur,css,body,js))
    hosts.append(f'      <div id="{cid}" data-composition-id="{cid}" data-composition-src="compositions/{cid}.html" data-start="{s0}" data-duration="{dur}" data-track-index="2" data-track-kind="graphics" data-width="1080" data-height="1920" style="z-index:3"></div>')
sfx = [ # (file, time, vol)
 ('impact-bass-1',0.0,0.8),('whoosh',4.1,0.4),('impact-bass-2',6.9,0.7),
 ('whoosh-cinematic',9.8,0.5),('impact-bass-2',17.6,0.5),('typing',20.9,0.3),
 ('whoosh-short',23.3,0.5),('glitch-1',31.4,0.5),('impact-bass-1',33.95,0.8),
 ('whoosh',37.2,0.4),('pop',39.45,0.4),('pop',39.7,0.4),('pop',39.95,0.4),('click',42.0,0.4),
 ('whoosh-cinematic',49.4,0.5),('ping',53.5,0.4),
 ('whoosh-cinematic',59.4,0.5),('riser',63.5,0.35),('whoosh',65.1,0.6),('impact-bass-2',70.3,0.7),
 ('impact-bass-1',74.45,0.8),('glitch-2',78.6,0.4),('impact-bass-2',79.4,0.6),
 ('whoosh-short',83.7,0.4),('sparkle',90.3,0.35),('ping',95.4,0.4),('impact-bass-2',97.35,0.6),
 ('typing',100.5,0.3),('impact-bass-1',103.75,0.8),('whoosh-cinematic',107.3,0.5),('click',111.0,0.5),('chime',117.5,0.4),
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
      <div id="case" class="clip" data-start="0" data-duration="{TOTAL}" data-track-index="4">FALL 002 · D. B. COOPER · 1971</div>
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
