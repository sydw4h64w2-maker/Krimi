# Folge 3 – Dagobert. Alle Zeiten global (Sekunden im Audio); L() rechnet in Szenenzeit um.
import os, json, subprocess
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

# 1 HOOK 0-8.3
add('hook',0,8.3,"""
  #hk-t { top:340px; font-size:58px; font-weight:600; }
  #hk-n { top:420px; font-size:200px; font-weight:700; line-height:1; }
  .chip { position:absolute; left:240px; width:600px; text-align:center; font-size:76px; font-weight:700; border:6px solid var(--accent); border-radius:14px; padding:6px 0; color:var(--accent); }
""", lambda L: f"""
    <div id="hk-w" class="clip" data-start="0" data-duration="8.3">
      <div id="hk-t" class="center">Der Kaufhaus-Erpresser</div>
      <div id="hk-n" class="center">KaDeWe<br/><span class="y">Karstadt</span></div>
      <div id="hk-c1" class="chip" style="top:880px">💣 BOMBEN</div>
      <div id="hk-c2" class="chip" style="top:1010px">🛤 LORE</div>
      <div id="hk-c3" class="chip" style="top:1140px">🕳 SANDKISTE</div>
    </div>
""", lambda L: f"""
    tl.fromTo("#hk-n", {{scale:1.08, opacity:1}}, {{scale:1, opacity:1, duration:0.35, ease:"power4.out"}}, 0);
    tl.to("#hk-n", {{scale:1.06, duration:7.5, ease:"none"}}, 0.4);
    tl.fromTo("#hk-t", {{y:20, opacity:1}}, {{y:0, opacity:1, duration:0.4}}, 0.1);
    tl.fromTo("#hk-c1", {{x:-80, opacity:0}}, {{x:0, opacity:1, duration:0.3, ease:"back.out(2)"}}, {L(3.35)});
    tl.fromTo("#hk-c2", {{x:80, opacity:0}}, {{x:0, opacity:1, duration:0.3, ease:"back.out(2)"}}, {L(4.4)});
    tl.fromTo("#hk-c3", {{x:-80, opacity:0}}, {{x:0, opacity:1, duration:0.3, ease:"back.out(2)"}}, {L(6.2)});
    {out('"#hk-w > *"',L,8.0).strip()}
""")
# 2 KADEWE 8.3-24.8
add('kadewe',8.3,24.8,"""
  #kd-d { top:300px; font-size:52px; }
  #kd-n { top:380px; font-size:170px; font-weight:700; }
  #kd-f { top:610px; font-size:56px; font-weight:500; }
  #kd-m { top:690px; font-size:130px; font-weight:700; }
  #kd-flash { position:absolute; inset:0; background:#fff3c4; opacity:0; }
  #kd-b { top:900px; font-size:64px; font-weight:700; }
  #kd-z { top:1010px; font-size:64px; font-weight:600; }
  #kd-st { position:absolute; left:220px; top:1120px; width:640px; text-align:center; border:10px solid var(--red); border-radius:12px; color:var(--red); font-size:72px; font-weight:700; padding:6px 0; }
""", lambda L: f"""
    <div id="kd-w" class="clip" data-start="0" data-duration="{L(24.8)}">
      <div id="kd-d" class="center lbl y">Mai 1988 · Berlin</div>
      <div id="kd-n" class="center">KaDeWe</div>
      <div id="kd-f" class="center">Forderung</div>
      <div id="kd-m" class="center y">500.000 DM</div>
      <div id="kd-b" class="center r">💥 Bombe · Nacht zum 25.05.</div>
      <div id="kd-z" class="center">Das KaDeWe <span class="y">zahlt</span></div>
      <div id="kd-st">TÄTER: UNERKANNT</div>
      <div id="kd-flash" data-layout-ignore></div>
    </div>
""", lambda L: fin("#kd-d",L,8.5,0.3,"{opacity:0}","{opacity:1") + fin("#kd-n",L,8.6,0.4) + fin("#kd-f",L,11.0,0.3,"{opacity:0}","{opacity:1") + f"""
    tl.fromTo("#kd-m", {{scale:1.3, opacity:0}}, {{scale:1, opacity:1, duration:0.35, ease:"power4.out"}}, {L(13.4)});
    tl.fromTo("#kd-flash", {{opacity:0}}, {{opacity:0.85, duration:0.06}}, {L(18.6)});
    tl.to("#kd-flash", {{opacity:0, duration:0.6}}, {L(18.66)});
    tl.fromTo("#kd-b", {{scale:1.4, opacity:0}}, {{scale:1, opacity:1, duration:0.25, ease:"power4.out"}}, {L(18.6)});
    tl.to("#kd-n", {{scale:1.08, duration:15.5, ease:"none"}}, {L(9.0)});
""" + fin("#kd-z",L,20.0,0.3) + f"""
    tl.fromTo("#kd-st", {{scale:2, rotation:-12, opacity:0}}, {{scale:1, rotation:-4, opacity:1, duration:0.22, ease:"power4.in"}}, {L(23.4)});
    {out('"#kd-w > *:not(#kd-flash)"',L,24.55).strip()}
""")
# 3 KARSTADT 24.8-45.8
add('karstadt',24.8,45.8,"""
  #ks-a { top:300px; font-size:52px; }
  #ks-d { top:380px; font-size:120px; font-weight:700; }
  #ks-r { top:540px; font-size:64px; font-weight:600; }
  #ks-m { top:660px; font-size:150px; font-weight:700; }
  #ks-paper { position:absolute; left:120px; top:340px; width:840px; height:640px; background:#ECE6D3; color:#1a1a1a; box-shadow:0 30px 70px rgba(0,0,0,.55); padding:40px 50px; }
  #ks-paper .mast { font-family:'EB Garamond',serif; font-size:72px; font-weight:700; text-align:center; border-bottom:4px double #1a1a1a; padding-bottom:10px; }
  #ks-paper .col { margin-top:26px; height:16px; background:repeating-linear-gradient(90deg,#b9b29f 0 60%, transparent 60% 64%); opacity:.7; }
  #ks-ad { position:absolute; left:120px; top:300px; width:600px; border:5px solid #1a1a1a; padding:26px; text-align:center; font-family:'EB Garamond',serif; font-size:56px; font-style:italic; line-height:1.15; background:#F7F2E2; }
  #ks-ad .k { font-family:'Space Mono',monospace; font-style:normal; font-size:28px; letter-spacing:.15em; }
  #ks-code { top:1080px; font-size:56px; }
  #ks-name { top:1150px; font-size:120px; font-weight:700; }
""", lambda L: f"""
    <div id="ks-a1" class="clip" data-start="0" data-duration="{L(35.0)}">
      <div id="ks-a" class="center lbl y">Vier Jahre später</div>
      <div id="ks-d" class="center">Juni 1992 · Hamburg</div>
      <div id="ks-r" class="center r">💣 Rohrbombe bei Karstadt</div>
      <div id="ks-m" class="center y">1,4 Mio. DM</div>
    </div>
    <div id="ks-b1" class="clip" data-start="{L(35.0)}" data-duration="{round(L(45.8)-L(35.0),2)}">
      <div id="ks-paper"><div class="mast">ANZEIGEN</div><div class="col"></div><div class="col"></div><div class="col"></div><div class="col"></div><div class="col"></div><div class="col"></div><div class="col"></div><div class="col"></div><div class="col"></div><div class="col"></div><div class="col"></div><div class="col"></div>
        <div id="ks-ad"><div class="k">KENNWORT</div>Onkel Dagobert grüßt seine Neffen</div>
      </div>
      <div id="ks-code" class="center lbl y">Codename</div>
      <div id="ks-name" class="center">DAGOBERT</div>
    </div>
""", lambda L: fin("#ks-a",L,25.0,0.3,"{opacity:0}","{opacity:1") + fin("#ks-d",L,26.45,0.4) + f"""
    tl.fromTo("#ks-r", {{scale:1.3, opacity:0}}, {{scale:1, opacity:1, duration:0.25, ease:"power4.out"}}, {L(28.9)});
    tl.fromTo("#ks-m", {{scale:1.3, opacity:0}}, {{scale:1, opacity:1, duration:0.35, ease:"power4.out"}}, {L(32.9)});
    tl.to("#ks-d", {{scale:1.05, duration:8, ease:"none"}}, {L(26.9)});
    {out('"#ks-a1 > *"',L,34.75).strip()}
    tl.fromTo("#ks-paper", {{y:200, rotation:3, opacity:0}}, {{y:0, rotation:-1, opacity:1, duration:0.6, ease:"power3.out"}}, {L(35.1)});
    tl.fromTo("#ks-ad", {{opacity:0, scale:0.9}}, {{opacity:1, scale:1, duration:0.4, ease:"back.out(1.8)"}}, {L(39.5)});
    tl.to("#ks-paper", {{scale:1.05, duration:9.5, ease:"none"}}, {L(35.8)});
""" + fin("#ks-code",L,42.3,0.3,"{opacity:0}","{opacity:1") + f"""
    tl.fromTo("#ks-name", {{scale:1.4, opacity:0}}, {{scale:1, opacity:1, duration:0.3, ease:"power4.out"}}, {L(44.8)});
    {out('"#ks-b1 > *"',L,45.55).strip()}
""")
# 4 KATZ 45.8-49.1
add('katz',45.8,49.1,"""
  #kz-t { top:600px; font-size:150px; font-weight:700; line-height:1.05; }
""", lambda L: f"""
    <div id="kz-t" class="center clip" data-start="0" data-duration="{L(49.1)}">KATZ <span class="y">&amp;</span><br/>MAUS</div>
""", lambda L: f"""
    tl.fromTo("#kz-t", {{scale:1.25, opacity:0}}, {{scale:1, opacity:1, duration:0.35, ease:"power4.out"}}, {L(45.95)});
    tl.to("#kz-t", {{scale:1.07, duration:2.5, ease:"none"}}, {L(46.3)});
    {out('"#kz-t"',L,48.85).strip()}
""")
# 5 SANDKISTE 49.1-67.8
add('sand',49.1,67.8,"""
  #sd-d { top:300px; font-size:52px; }
  #sd-svg { position:absolute; left:140px; top:390px; width:800px; height:760px; }
  #sd-c1 { top:1170px; font-size:58px; font-weight:600; }
  #sd-c2 { top:1250px; font-size:46px; }
""", lambda L: f"""
    <div id="sd-w" class="clip" data-start="0" data-duration="{L(67.8)}">
      <div id="sd-d" class="center lbl y">April 1993 · Berlin-Steglitz</div>
      <svg id="sd-svg" viewBox="0 0 800 760">
        <rect x="0" y="300" width="800" height="460" fill="#2a241c"/>
        <rect x="0" y="292" width="800" height="12" fill="#5b4a33"/>
        <g id="sd-shaft"><rect x="330" y="304" width="140" height="300" fill="#0b0b0b"/><rect x="0" y="604" width="800" height="120" fill="#141a20"/><text x="400" y="680" text-anchor="middle" fill="#7d93a8" font-family="Space Mono" font-size="30">KANALISATION</text></g>
        <g id="sd-box"><rect x="260" y="180" width="280" height="112" fill="#8a6a3d" stroke="#c9a46a" stroke-width="6"/><rect x="275" y="195" width="250" height="40" fill="#d8c08a"/><text x="400" y="160" text-anchor="middle" fill="#EDE6D6" font-family="Oswald" font-size="40">Sandkiste</text></g>
        <g id="sd-pkg"><rect x="365" y="240" width="70" height="46" fill="#F2C230"/></g>
        <path id="sd-arrow" d="M400,620 L700,650" stroke="#F2C230" stroke-width="8" fill="none" stroke-dasharray="320" stroke-dashoffset="320" marker-end="url(#sd-ah)"/>
        <defs><marker id="sd-ah" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#F2C230"/></marker></defs>
      </svg>
      <div id="sd-c1" class="center">Präparierter <span class="y">Gullydeckel</span></div>
      <div id="sd-c2" class="center lbl r">Im Paket: kein echtes Geld</div>
    </div>
""", lambda L: fin("#sd-d",L,49.3,0.3,"{opacity:0}","{opacity:1") + f"""
    tl.fromTo("#sd-svg", {{opacity:0}}, {{opacity:1, duration:0.4}}, {L(49.6)});
    tl.fromTo("#sd-box", {{y:-60, opacity:0}}, {{y:0, opacity:1, duration:0.4, ease:"power3.out"}}, {L(53.1)});
    tl.fromTo("#sd-pkg", {{opacity:0}}, {{opacity:1, duration:0.3}}, {L(54.0)});
    tl.fromTo("#sd-shaft", {{opacity:0}}, {{opacity:1, duration:0.6}}, {L(57.2)});
""" + fin("#sd-c1",L,57.8,0.3) + f"""
    tl.to("#sd-pkg", {{y:330, duration:0.9, ease:"power2.in"}}, {L(60.4)});
    tl.fromTo("#sd-arrow", {{strokeDashoffset:320}}, {{strokeDashoffset:0, duration:1.0, ease:"power2.out"}}, {L(62.7)});
    tl.to("#sd-pkg", {{x:260, y:360, duration:1.0, ease:"power2.out"}}, {L(62.7)});
""" + fin("#sd-c2",L,65.0,0.3) + f"""
    tl.to("#sd-svg", {{scale:1.04, duration:17, ease:"none"}}, {L(50.0)});
    {out('"#sd-w > *"',L,67.55).strip()}
""")
# 6 LORE 67.8-88.9
add('lore',67.8,88.9,"""
  #lr-d { top:300px; font-size:52px; }
  #lr-svg { position:absolute; left:0; top:420px; width:1080px; height:420px; }
  #lr-m { top:880px; font-size:64px; font-weight:600; }
  #lr-q { top:880px; font-size:76px; font-weight:700; }
  #lr-q2 { top:990px; font-size:46px; }
  #lr-f { top:1090px; font-size:64px; font-weight:700; }
""", lambda L: f"""
    <div id="lr-w" class="clip" data-start="0" data-duration="{L(88.9)}">
      <div id="lr-d" class="center lbl y">Januar 1994</div>
      <svg id="lr-svg" viewBox="0 0 1080 420">
        <g id="lr-track"><rect x="0" y="300" width="1080" height="10" fill="#9EA3AC"/><rect x="0" y="330" width="1080" height="10" fill="#9EA3AC"/>
        <rect x="0" y="292" width="1080" height="56" fill="url(#lr-sl)"/></g>
        <defs><pattern id="lr-sl" width="60" height="56" patternUnits="userSpaceOnUse"><rect x="0" y="0" width="22" height="56" fill="#5b4a33" opacity=".7"/></pattern></defs>
        <g id="lr-cart"><rect x="0" y="210" width="220" height="80" fill="#6b4f2a" stroke="#c9a46a" stroke-width="5"/><rect x="55" y="170" width="110" height="44" fill="#F2C230"/><circle cx="45" cy="300" r="22" fill="#333" stroke="#bbb" stroke-width="4"/><circle cx="175" cy="300" r="22" fill="#333" stroke="#bbb" stroke-width="4"/></g>
      </svg>
      <div id="lr-m" class="center">Polizei legt <span class="y">1,4 Mio. DM</span> hinein</div>
      <div id="lr-q" class="center r">PECH – ODER POLIZEI?</div>
      <div id="lr-q2" class="center lbl">bis heute umstritten</div>
      <div id="lr-f" class="center">Dagobert flieht <span class="r">ohne Geld</span></div>
    </div>
""", lambda L: fin("#lr-d",L,68.0,0.3,"{opacity:0}","{opacity:1") + f"""
    tl.fromTo("#lr-svg", {{opacity:0}}, {{opacity:1, duration:0.4}}, {L(70.4)});
    tl.fromTo("#lr-cart", {{x:-240}}, {{x:560, duration:8.2, ease:"none"}}, {L(70.5)});
""" + fin("#lr-m",L,74.2,0.35) + f"""
    tl.to("#lr-cart", {{x:660, y:70, rotation:28, transformOrigin:"110px 300px", duration:0.6, ease:"power2.in"}}, {L(78.7)});
    tl.to("#lr-m", {{opacity:0, duration:0.25}}, {L(80.8)});
    tl.fromTo("#lr-q", {{scale:1.3, opacity:0}}, {{scale:1, opacity:1, duration:0.3, ease:"power4.out"}}, {L(81.1)});
""" + fin("#lr-q2",L,84.2,0.3,"{opacity:0}","{opacity:1") + fin("#lr-f",L,86.6,0.35) + f"""
    tl.to("#lr-track", {{opacity:0.6, duration:8, ease:"none"}}, {L(79.5)});
    {out('"#lr-w > *"',L,88.65).strip()}
""")
# 7 FESTNAHME 88.9-101.2
add('fest',88.9,101.2,"""
  #fs-d { top:300px; font-size:130px; font-weight:700; }
  #fs-booth { position:absolute; left:390px; top:470px; width:300px; height:500px; }
  #fs-o { top:990px; font-size:46px; }
  #fs-st { position:absolute; left:150px; top:1090px; width:780px; text-align:center; border:10px solid var(--red); border-radius:12px; color:var(--red); font-size:70px; font-weight:700; padding:6px 0; white-space:nowrap; }
""", lambda L: f"""
    <div id="fs-w" class="clip" data-start="0" data-duration="{L(101.2)}">
      <div id="fs-d" class="center">22.04.1994</div>
      <svg id="fs-booth" viewBox="0 0 300 500"><rect x="20" y="20" width="260" height="470" rx="10" fill="#C8B400" opacity=".9"/><rect x="45" y="90" width="210" height="370" fill="#1b2430"/><rect x="20" y="20" width="260" height="60" rx="10" fill="#e8d400"/><text x="150" y="62" text-anchor="middle" fill="#111" font-family="Oswald" font-size="38" font-weight="700">TELEFON</text><rect x="110" y="170" width="80" height="120" rx="8" fill="#888"/><rect id="fs-hs" x="90" y="150" width="24" height="90" rx="10" fill="#333"/></svg>
      <div id="fs-o" class="center lbl y">Berlin-Johannisthal</div>
      <div id="fs-st">POLIZEI IST SCHON DA</div>
    </div>
""", lambda L: fin("#fs-d",L,89.2,0.4) + f"""
    tl.fromTo("#fs-booth", {{y:60, opacity:0}}, {{y:0, opacity:1, duration:0.5, ease:"power3.out"}}, {L(93.4)});
    tl.fromTo("#fs-hs", {{rotation:0, transformOrigin:"102px 195px"}}, {{rotation:-10, duration:0.3, yoyo:true, repeat:5, ease:"sine.inOut"}}, {L(95.0)});
""" + fin("#fs-o",L,94.0,0.3,"{opacity:0}","{opacity:1") + f"""
    tl.fromTo("#fs-st", {{scale:2, rotation:-12, opacity:0}}, {{scale:1, rotation:-4, opacity:1, duration:0.22, ease:"power4.in"}}, {L(99.05)});
    tl.to("#fs-d", {{scale:1.06, duration:11, ease:"none"}}, {L(89.6)});
    {out('"#fs-w > *"',L,100.95).strip()}
""")
# 8 FUNKE 101.2-117.3
add('funke',101.2,117.3,"""
  #fk-card { position:absolute; left:110px; top:320px; width:860px; height:780px; background:var(--paper); color:#1b1b1b; border-radius:10px; padding:50px 60px; box-shadow:0 30px 80px rgba(0,0,0,.5); }
  #fk-card .hd { font-family:'Space Mono',monospace; font-size:28px; letter-spacing:.12em; border-bottom:3px solid #1b1b1b; padding-bottom:16px; }
  #fk-card .row { font-family:'Space Mono',monospace; font-size:28px; margin-top:18px; color:#555; }
  #fk-card .val { font-family:'Oswald',sans-serif; font-size:54px; font-weight:600; color:#111; line-height:1.1; margin-top:4px; }
""", lambda L: f"""
    <div id="fk-w" class="clip" data-start="0" data-duration="{L(117.3)}">
      <div id="fk-card">
        <div class="hd">AKTE · „DAGOBERT“</div>
        <div class="row">NAME</div><div class="val" id="fk-1">Arno Funke</div>
        <div class="row">BERUF</div><div class="val" id="fk-2">Schildermaler &amp; Autolackierer</div>
        <div class="row">URTEIL 1996</div><div class="val" id="fk-3">9 Jahre Haft</div>
        <div class="row">ENTLASSUNG</div><div class="val" id="fk-4">2000 · vorzeitig</div>
        <div class="row">HEUTE</div><div class="val" id="fk-5">Autor &amp; Cartoonist</div>
      </div>
    </div>
""", lambda L: f"""
    tl.fromTo("#fk-card", {{y:140, rotation:-4, opacity:0}}, {{y:0, rotation:-1.5, opacity:1, duration:0.6, ease:"power3.out"}}, {L(101.3)});
    tl.to("#fk-card", {{scale:1.04, duration:15, ease:"none"}}, {L(101.9)});
""" + ''.join(f'    tl.fromTo("#fk-{i}", {{opacity:0}}, {{opacity:1, duration:0.3}}, {L(t)});\n' for i,t in [(1,102.6),(2,104.0),(3,108.6),(4,111.1),(5,114.6)]) + f"""
    {out('"#fk-w > *"',L,117.05).strip()}
""")
# 9 HELD 117.3-128.9
add('held',117.3,128.9,"""
  #hd-a { top:420px; font-size:150px; font-weight:700; }
  #hd-b { top:680px; font-size:70px; font-weight:700; line-height:1.1; }
  #hd-c { top:900px; font-size:54px; font-weight:500; line-height:1.2; }
""", lambda L: f"""
    <div id="hd-w" class="clip" data-start="0" data-duration="{L(128.9)}">
      <div id="hd-a" class="center y">VOLKSHELD?</div>
      <div id="hd-b" class="center r">2 Menschen<br/>leicht verletzt</div>
      <div id="hd-c" class="center">Seine Bomben hätten jederzeit<br/>noch mehr Menschen treffen können</div>
    </div>
""", lambda L: f"""
    tl.fromTo("#hd-a", {{scale:1.25, opacity:0}}, {{scale:1, opacity:1, duration:0.35, ease:"power4.out"}}, {L(117.6)});
    tl.to("#hd-a", {{scale:1.05, duration:11, ease:"none"}}, {L(118.0)});
    tl.fromTo("#hd-b", {{y:30, opacity:0}}, {{y:0, opacity:1, duration:0.35}}, {L(121.1)});
""" + fin("#hd-c",L,125.1,0.35) + f"""
    {out('"#hd-w > *"',L,128.65).strip()}
""")
# 10 CTA 128.9-134.5
add('cta',128.9,134.5,"""
  #ct-q { top:480px; font-size:120px; font-weight:700; line-height:1.05; }
  #ct-s { top:880px; font-size:56px; font-weight:500; }
  #ct-arrow { top:1000px; font-size:120px; }
""", lambda L: f"""
    <div id="ct-q" class="center clip" data-start="0" data-duration="{L(134.5)}">Genialer Tüftler<br/><span class="y">oder nur Glück?</span></div>
    <div id="ct-s" class="center clip" data-start="{L(131.9)}" data-duration="{round(L(134.5)-L(131.9),2)}">Schreib's in die Kommentare</div>
    <div id="ct-arrow" class="center clip y" data-start="{L(132.2)}" data-duration="{round(L(134.5)-L(132.2),2)}">↓</div>
""", lambda L: f"""
    tl.fromTo("#ct-q", {{scale:1.15, opacity:0}}, {{scale:1, opacity:1, duration:0.4, ease:"power4.out"}}, {L(129.15)});
    tl.to("#ct-q", {{scale:1.04, duration:4.8, ease:"none"}}, {L(129.6)});
    tl.fromTo("#ct-s", {{opacity:0, y:20}}, {{opacity:1, y:0, duration:0.35}}, {L(132.0)});
    tl.fromTo("#ct-arrow", {{y:-20, opacity:0}}, {{y:20, opacity:1, duration:0.6, ease:"sine.inOut"}}, {L(132.2)});
    tl.to("#ct-arrow", {{y:-10, duration:0.6, ease:"sine.inOut"}}, {L(132.8)});
    tl.to("#ct-arrow", {{y:20, duration:0.6, ease:"sine.inOut"}}, {L(133.4)});
""")
TOTAL=134.5
hosts=[]
for cid,s0,s1,css,body,js in SC:
    dur=round(s1-s0,2)
    open(f'compositions/{cid}.html','w').write(scene(cid,dur,css,body,js))
    hosts.append(f'      <div id="{cid}" data-composition-id="{cid}" data-composition-src="compositions/{cid}.html" data-start="{s0}" data-duration="{dur}" data-track-index="2" data-track-kind="graphics" data-width="1080" data-height="1920" style="z-index:3"></div>')
sfx = [ # (file, time, vol)
 ('impact-bass-1',0.0,0.8),('pop',3.35,0.5),('pop',4.4,0.5),('pop',6.2,0.5),
 ('whoosh-cinematic',8.3,0.5),('impact-bass-2',13.4,0.6),('impact-bass-1',18.6,0.9),('click',20.0,0.4),('impact-bass-2',23.4,0.6),
 ('whoosh-cinematic',24.8,0.5),('impact-bass-1',28.9,0.8),('impact-bass-2',32.9,0.6),('whoosh',35.1,0.4),('typing',39.5,0.3),('impact-bass-1',44.8,0.8),
 ('glitch-1',45.95,0.4),('whoosh-cinematic',49.1,0.5),('click',57.2,0.4),('whoosh-short',60.4,0.5),('whoosh',62.7,0.4),('error',65.0,0.3),
 ('whoosh-cinematic',67.8,0.5),('riser',75.5,0.3),('impact-bass-1',78.7,0.9),('glitch-2',81.1,0.4),
 ('whoosh-cinematic',88.9,0.5),('notification',95.0,0.3),('impact-bass-1',99.05,0.8),
 ('whoosh',101.3,0.4),('typing',102.6,0.3),('impact-bass-2',117.6,0.6),('impact-bass-2',121.1,0.5),('chime',129.15,0.4),
]
aud=[]
for i,(f,tt,v) in enumerate(sfx):
    d=float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f"assets/sfx/{f}.mp3"],capture_output=True,text=True).stdout.strip())
    d=round(min(d, TOTAL-tt),2)
    aud.append(f'      <audio id="sfx{i}" class="clip" src="assets/sfx/{f}.mp3" data-start="{tt}" data-duration="{d}" data-track-index="{10+i}" data-volume="{v}"></audio>')
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
      <div id="case" class="clip" data-start="0" data-duration="{TOTAL}" data-track-index="4">FALL 003 · DAGOBERT · 1988–1994</div>
      <audio id="music" class="clip" src="assets/music.mp3" data-start="0" data-duration="{TOTAL}" data-track-index="8" data-volume="0.55" data-fade-out="2"></audio>
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
open('index.html','w').write(index)
print("ok", TOTAL)
