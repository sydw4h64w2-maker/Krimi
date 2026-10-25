# Folge 8 – Mona Lisa. Alle Zeiten global (Sekunden im Audio); L() rechnet in Szenenzeit um.
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
def PORTRAIT(id_, w=360, h=480):
    return f'''<svg id="{id_}" viewBox="0 0 360 480" width="{w}" height="{h}"><rect x="0" y="0" width="360" height="480" fill="#C9A04A"/><rect x="18" y="18" width="324" height="444" fill="#8A6A2A"/><rect x="30" y="30" width="300" height="420" fill="#4b5a3c"/><path d="M30,300 Q120,260 180,280 Q250,250 330,290 L330,450 L30,450 Z" fill="#3b4a30"/><ellipse cx="180" cy="190" rx="62" ry="80" fill="#c8a26a"/><path d="M110,170 Q120,90 180,92 Q240,90 250,170 L262,300 Q230,260 222,200 Q200,130 180,130 Q160,130 138,200 Q130,260 98,300 Z" fill="#2b2016"/><path d="M90,450 Q100,320 180,300 Q260,320 270,450 Z" fill="#2b2016"/><path d="M162,222 Q180,232 198,222" stroke="#6b4a2a" stroke-width="4" fill="none"/></svg>'''
CARD = "position:absolute; background:var(--paper); color:#1b1b1b; border-radius:10px; box-shadow:0 25px 60px rgba(0,0,0,.5);"
# 1 HOOK 0-7.2
add('hook',0,7.2,"""
  #hk-p { position:absolute; left:360px; top:300px; }
  #hk-t { top:820px; font-size:130px; font-weight:700; }
  #hk-s { top:990px; font-size:56px; font-weight:500; }
""", lambda L: f"""
    <div id="hk-w" class="clip" data-start="0" data-duration="7.2">
      <div id="hk-p">{PORTRAIT('hk-pt')}</div>
      <div id="hk-t" class="center y">MONA LISA</div>
      <div id="hk-s" class="center">gestohlen – <span class="r">unter einem Kittel</span></div>
    </div>
""", lambda L: f"""
    tl.fromTo("#hk-p", {{scale:1.06, opacity:1}}, {{scale:1, opacity:1, duration:0.4, ease:"power3.out"}}, 0);
    tl.to("#hk-p", {{scale:1.05, duration:6.4, ease:"none"}}, 0.5);
    tl.fromTo("#hk-t", {{y:20, opacity:1}}, {{y:0, opacity:1, duration:0.35}}, 0.05);
    tl.fromTo("#hk-s", {{opacity:0, y:20}}, {{opacity:1, y:0, duration:0.3}}, {L(5.15)});
    {out('"#hk-w > *"',L,6.95).strip()}
""")
# 2 LOUVRE 7.2-27.6
add('louvre',7.2,27.6,f"""
  #lv-d {{ top:300px; font-size:110px; font-weight:700; }}
  #lv-o {{ top:440px; font-size:46px; }}
  #lv-sign {{ position:absolute; left:300px; top:540px; width:480px; text-align:center; background:#1f2a44; color:#fff; border:6px solid #EDE6D6; border-radius:10px; font-size:60px; font-weight:700; padding:10px 0; }}
  #lv-sign span {{ display:block; font-family:'Space Mono',monospace; font-size:28px; font-weight:400; }}
  #lv-card {{ {CARD} left:140px; top:720px; width:800px; padding:32px 44px; }}
  #lv-card .hd {{ font-family:'Space Mono',monospace; font-size:28px; letter-spacing:.12em; border-bottom:3px solid #1b1b1b; padding-bottom:12px; }}
  #lv-card .v {{ font-size:56px; font-weight:700; margin-top:14px; }}
  #lv-card .r2 {{ font-size:40px; font-weight:500; margin-top:8px; }}
""", lambda L: f"""
    <div id="lv-w" class="clip" data-start="0" data-duration="{L(27.6)}">
      <div id="lv-d" class="center">21.08.1911</div>
      <div id="lv-o" class="center lbl y">Paris · Louvre</div>
      <div id="lv-sign">MONTAG<span>FERMÉ · geschlossen</span></div>
      <div id="lv-card"><div class="hd">AKTE · IN DER ABSTELLKAMMER</div>
        <div class="v" id="lv-n">Vincenzo Peruggia</div>
        <div class="r2" id="lv-a">Italiener · früher im Louvre beschäftigt</div>
        <div class="r2" id="lv-b">baute <b>Schutzgläser</b> für die Gemälde ein</div>
      </div>
    </div>
""", lambda L: fin("#lv-d",L,7.4,0.45) + fin("#lv-o",L,10.2,0.3,"{opacity:0}","{opacity:1") + f"""
    tl.fromTo("#lv-sign", {{rotation:-8, y:-40, opacity:0}}, {{rotation:-2, y:0, opacity:1, duration:0.45, ease:"back.out(1.8)"}}, {L(11.4)});
    tl.fromTo("#lv-card", {{y:120, opacity:0}}, {{y:0, opacity:1, duration:0.5, ease:"power3.out"}}, {L(15.4)});
    tl.fromTo("#lv-n", {{opacity:0}}, {{opacity:1, duration:0.3}}, {L(18.4)});
    tl.fromTo("#lv-a", {{opacity:0}}, {{opacity:1, duration:0.3}}, {L(20.5)});
    tl.fromTo("#lv-b", {{opacity:0}}, {{opacity:1, duration:0.3}}, {L(24.0)});
    tl.to("#lv-d", {{scale:1.05, duration:19.5, ease:"none"}}, {L(7.9)});
    {out('"#lv-w > *"',L,27.35).strip()}
""")
# 3 RAUB 27.6-43.1
add('raub',27.6,43.1,"""
  #rb-wall { position:absolute; left:0; top:300px; width:1080px; height:640px; background:#5b2a2a; }
  #rb-p { position:absolute; left:405px; top:360px; }
  #rb-hooks { position:absolute; left:405px; top:360px; width:270px; height:360px; }
  #rb-t1 { top:980px; font-size:62px; font-weight:600; }
  #rb-t2 { top:1080px; font-size:52px; }
""", lambda L: f"""
    <div id="rb-w" class="clip" data-start="0" data-duration="{L(43.1)}">
      <div id="rb-wall"></div>
      <svg id="rb-hooks" viewBox="0 0 270 360">{''.join(f'<path d="M{x},{y} l0,18 q0,10 10,10" stroke="#9EA3AC" stroke-width="8" fill="none" stroke-linecap="round"/>' for x,y in [(20,20),(240,20),(20,320),(240,320)])}</svg>
      <div id="rb-p">{PORTRAIT('rb-pt',270,360)}</div>
      <div id="rb-t1" class="center">Unter dem Kittel – <span class="y">hinaus</span></div>
      <div id="rb-t2" class="center lbl p">am nächsten Tag: nur 4 Eisenhaken</div>
    </div>
""", lambda L: f"""
    tl.fromTo("#rb-wall, #rb-p", {{opacity:0}}, {{opacity:1, duration:0.4}}, {L(27.7)});
    tl.fromTo("#rb-hooks", {{opacity:0}}, {{opacity:1, duration:0.1}}, {L(28.5)});
    tl.to("#rb-p", {{y:40, rotation:-6, duration:0.6, ease:"power2.inOut"}}, {L(28.0)});
    tl.to("#rb-p", {{x:-700, rotation:-12, duration:1.6, ease:"power2.in"}}, {L(30.2)});
""" + fin("#rb-t1",L,30.4,0.35) + f"""
    tl.to("#rb-t1", {{opacity:0, duration:0.3}}, {L(35.5)});
    tl.to("#rb-wall", {{opacity:0.75, duration:4, ease:"none"}}, {L(33.6)});
""" + fin("#rb-t2",L,41.0,0.35,"{opacity:0}","{opacity:1") + f"""
    tl.fromTo("#rb-hooks", {{scale:1}}, {{scale:1.15, duration:6, ease:"none"}}, {L(36.0)});
    {out('"#rb-w > *"',L,42.85).strip()}
""")
# 4 VERDACHT 43.1-54.4
add('verdacht',43.1,54.4,f"""
  #vd-h {{ top:300px; font-size:80px; font-weight:700; }}
  .vc {{ {CARD} width:420px; padding:24px; text-align:center; }}
  .vc .n {{ font-size:50px; font-weight:700; line-height:1.05; }}
  .vc .r2 {{ font-family:'Space Mono',monospace; font-size:28px; margin-top:10px; color:#444; }}
  #vd-a {{ left:80px; top:460px; }}
  #vd-b {{ left:580px; top:460px; }}
  #vd-st {{ {STAMP} left:260px; top:720px; width:560px; font-size:90px; padding:4px 0; border-color:#3FBF5F; color:#3FBF5F; }}
""", lambda L: f"""
    <div id="vd-w" class="clip" data-start="0" data-duration="{L(54.4)}">
      <div id="vd-h" class="center">Die Polizei sucht</div>
      <div id="vd-a" class="vc"><div class="n">Guillaume<br/>Apollinaire</div><div class="r2">Dichter · verhaftet</div></div>
      <div id="vd-b" class="vc"><div class="n">Pablo<br/>Picasso</div><div class="r2">Maler · verhört</div></div>
      <div id="vd-st" data-layout-allow-overlap>ENTLASTET</div>
    </div>
""", lambda L: fin("#vd-h",L,43.3,0.4) + f"""
    tl.fromTo("#vd-a", {{x:-120, rotation:-6, opacity:0}}, {{x:0, rotation:-2, opacity:1, duration:0.45, ease:"power3.out"}}, {L(46.5)});
    tl.fromTo("#vd-b", {{x:120, rotation:6, opacity:0}}, {{x:0, rotation:2, opacity:1, duration:0.45, ease:"power3.out"}}, {L(50.0)});
    tl.fromTo("#vd-st", {{scale:2, rotation:-12, opacity:0}}, {{scale:1, rotation:-5, opacity:1, duration:0.22, ease:"power4.in"}}, {L(52.7)});
    tl.to("#vd-h", {{scale:1.05, duration:10.5, ease:"none"}}, {L(43.7)});
    {out('"#vd-w > *"',L,54.15).strip()}
""")
# 5 KOFFER 54.4-64.4
add('koffer',54.4,64.4,"""
  #kf-a { top:300px; font-size:60px; font-weight:600; }
  #kf-b { top:390px; font-size:52px; }
  #kf-n { top:500px; font-size:170px; font-weight:700; line-height:1; }
  #kf-svg { position:absolute; left:340px; top:760px; width:400px; height:300px; }
""", lambda L: f"""
    <div id="kf-w" class="clip" data-start="0" data-duration="{L(64.4)}">
      <div id="kf-a" class="center">Peruggia: befragt</div>
      <div id="kf-b" class="center lbl y">nie ernsthaft verdächtigt</div>
      <div id="kf-n" class="center"><span id="kf-c">0</span> JAHRE</div>
      <svg id="kf-svg" viewBox="0 0 400 300"><rect x="20" y="80" width="360" height="200" rx="16" fill="#6b4f2a" stroke="#c9a46a" stroke-width="8"/><rect x="150" y="40" width="100" height="50" rx="10" fill="none" stroke="#c9a46a" stroke-width="10"/><rect x="20" y="160" width="360" height="12" fill="#c9a46a"/><rect id="kf-gold" x="120" y="110" width="160" height="140" fill="#C9A04A" opacity="0"/></svg>
    </div>
""", lambda L: fin("#kf-a",L,54.6,0.35) + fin("#kf-b",L,57.0,0.3,"{opacity:0}","{opacity:1") + f"""
    tl.fromTo("#kf-n", {{opacity:0}}, {{opacity:1, duration:0.3}}, {L(59.4)});
    const k = {{v:0}};
    tl.fromTo(k, {{v:0}}, {{v:2, duration:1.6, ease:"steps(2)", onUpdate:()=>{{ document.querySelector("#kf-c").textContent = Math.round(k.v); }}}}, {L(59.5)});
    tl.fromTo("#kf-svg", {{y:60, opacity:0}}, {{y:0, opacity:1, duration:0.45, ease:"power3.out"}}, {L(61.5)});
    tl.to("#kf-gold", {{opacity:0.35, duration:0.3, yoyo:true, repeat:3}}, {L(63.1)});
    tl.to("#kf-n", {{scale:1.05, duration:4.5, ease:"none"}}, {L(59.8)});
    {out('"#kf-w > *"',L,64.15).strip()}
""")
# 6 FLORENZ 64.4-81.3
add('florenz',64.4,81.3,f"""
  #fz-d {{ top:300px; font-size:90px; font-weight:700; }}
  #fz-l {{ {CARD} left:150px; top:440px; width:780px; height:380px; padding:44px 50px; background:#F3E9C8; font-family:'EB Garamond',serif; }}
  #fz-l .t {{ font-size:58px; font-style:italic; line-height:1.2; }}
  #fz-l .s {{ font-size:46px; text-align:right; margin-top:40px; }}
  #fz-u {{ top:880px; font-size:54px; font-weight:600; }}
  #fz-st {{ {STAMP} left:330px; top:990px; width:420px; font-size:96px; padding:2px 0; border-color:#3FBF5F; color:#3FBF5F; }}
  #fz-p {{ top:1160px; font-size:54px; font-weight:600; }}
""", lambda L: f"""
    <div id="fz-w" class="clip" data-start="0" data-duration="{L(81.3)}">
      <div id="fz-d" class="center">Nov. 1913 · Florenz</div>
      <div id="fz-l"><div class="t">„Ich habe die Mona Lisa.“</div><div class="s">– „Leonardo Vincenzo“</div></div>
      <div id="fz-u" class="center">Kunsthändler + <span class="y">Uffizien-Direktor</span> prüfen</div>
      <div id="fz-st">ECHT</div>
      <div id="fz-p" class="center r">📞 Polizei</div>
    </div>
""", lambda L: fin("#fz-d",L,64.6,0.4) + f"""
    tl.fromTo("#fz-l", {{y:120, rotation:4, opacity:0}}, {{y:0, rotation:-1.5, opacity:1, duration:0.5, ease:"power3.out"}}, {L(66.9)});
    tl.fromTo("#fz-l .t", {{clipPath:"inset(0 100% 0 0)"}}, {{clipPath:"inset(0 0% 0 0)", duration:1.4, ease:"steps(24)"}}, {L(70.5)});
""" + fin("#fz-u",L,72.5,0.35) + f"""
    tl.fromTo("#fz-st", {{scale:2, rotation:-12, opacity:0}}, {{scale:1, rotation:-5, opacity:1, duration:0.22, ease:"power4.in"}}, {L(77.7)});
""" + fin("#fz-p",L,79.3,0.3) + f"""
    tl.to("#fz-l", {{scale:1.04, duration:14, ease:"none"}}, {L(67.5)});
    {out('"#fz-w > *"',L,81.05).strip()}
""")
# 7 MOTIV 81.3-90.6
add('motiv',81.3,90.6,"""
  #mt-h { top:300px; font-size:52px; }
  #mt-svg { position:absolute; left:140px; top:390px; width:800px; height:480px; }
  #mt-a { position:absolute; left:120px; top:900px; width:400px; text-align:center; font-size:58px; font-weight:700; }
  #mt-b { position:absolute; left:560px; top:900px; width:400px; text-align:center; font-size:58px; font-weight:700; }
""", lambda L: f"""
    <div id="mt-w" class="clip" data-start="0" data-duration="{L(90.6)}">
      <div id="mt-h" class="center lbl">Das Motiv?</div>
      <svg id="mt-svg" viewBox="0 0 800 480"><rect x="390" y="80" width="20" height="380" fill="#9EA3AC"/><rect x="300" y="450" width="200" height="20" fill="#9EA3AC"/>
        <g id="mt-beam"><rect x="100" y="70" width="600" height="16" fill="#C9A04A"/><g id="mt-l"><line x1="140" y1="86" x2="140" y2="220" stroke="#EDE6D6" stroke-width="4"/><path d="M60,220 L220,220 Q140,280 60,220 Z" fill="#EDE6D6"/><text x="140" y="210" text-anchor="middle" font-size="60">🇮🇹</text></g><g id="mt-r"><line x1="660" y1="86" x2="660" y2="220" stroke="#EDE6D6" stroke-width="4"/><path d="M580,220 L740,220 Q660,280 580,220 Z" fill="#EDE6D6"/><text x="660" y="210" text-anchor="middle" font-size="60">💰</text></g></g>
      </svg>
      <div id="mt-a">Patriotismus?</div>
      <div id="mt-b" class="y">Geld?</div>
    </div>
""", lambda L: fin("#mt-h",L,81.5,0.3,"{opacity:0}","{opacity:1") + f"""
    tl.fromTo("#mt-svg", {{opacity:0}}, {{opacity:1, duration:0.4}}, {L(81.6)});
    tl.fromTo("#mt-beam", {{rotation:0, svgOrigin:"400 78"}}, {{rotation:3, duration:1.6, ease:"sine.inOut"}}, {L(82.0)});
    tl.to("#mt-beam", {{rotation:-2, duration:1.6, ease:"sine.inOut"}}, {L(83.6)});
    tl.to("#mt-beam", {{rotation:-8, duration:0.8, ease:"power2.inOut"}}, {L(85.3)});
    tl.to("#mt-beam", {{rotation:8, duration:1.0, ease:"power2.inOut"}}, {L(89.2)});
""" + fin("#mt-a",L,85.3,0.35) + fin("#mt-b",L,89.2,0.35) + f"""
    {out('"#mt-w > *"',L,90.35).strip()}
""")
# 8 ENDE 90.6-105.8
add('ende',90.6,105.8,f"""
  #en-a {{ top:300px; font-size:52px; }}
  #en-b {{ top:370px; font-size:120px; font-weight:700; }}
  #en-p {{ position:absolute; left:405px; top:560px; }}
  #en-c {{ top:960px; font-size:58px; font-weight:600; }}
  #en-d {{ top:1070px; font-size:80px; font-weight:700; }}
""", lambda L: f"""
    <div id="en-w" class="clip" data-start="0" data-duration="{L(105.8)}">
      <div id="en-a" class="center lbl">Strafe</div>
      <div id="en-b" class="center y">≈ 7 Monate</div>
      <div id="en-p">{PORTRAIT('en-pt',270,360)}</div>
      <div id="en-c" class="center">Jan. 1914 · <span class="y">zurück in Paris</span></div>
      <div id="en-d" class="center">✨ WELTBERÜHMT ✨</div>
    </div>
""", lambda L: fin("#en-a",L,90.8,0.3,"{opacity:0}","{opacity:1") + f"""
    tl.fromTo("#en-b", {{scale:1.3, opacity:0}}, {{scale:1, opacity:1, duration:0.35, ease:"power4.out"}}, {L(93.0)});
    tl.fromTo("#en-p", {{x:700, rotation:12, opacity:0}}, {{x:0, rotation:0, opacity:1, duration:1.0, ease:"power3.out"}}, {L(95.4)});
""" + fin("#en-c",L,96.4,0.35) + f"""
    tl.fromTo("#en-d", {{scale:1.4, opacity:0}}, {{scale:1, opacity:1, duration:0.35, ease:"power4.out"}}, {L(102.4)});
    tl.to("#en-p", {{scale:1.08, duration:9, ease:"none"}}, {L(96.5)});
    {out('"#en-w > *"',L,105.55).strip()}
""")
# 9 CTA 105.8-111.5
add('cta',105.8,111.5,"""
  #ct-q { top:500px; font-size:130px; font-weight:700; line-height:1.05; }
  #ct-s { top:880px; font-size:56px; font-weight:500; }
  #ct-arrow { top:1000px; font-size:120px; }
""", lambda L: f"""
    <div id="ct-q" class="center clip" data-start="0" data-duration="{L(111.5)}">Patriot oder<br/><span class="y">einfach ein Dieb?</span></div>
    <div id="ct-s" class="center clip" data-start="{L(108.5)}" data-duration="{round(L(111.5)-L(108.5),2)}">Schreib's in die Kommentare</div>
    <div id="ct-arrow" class="center clip y" data-start="{L(108.8)}" data-duration="{round(L(111.5)-L(108.8),2)}">↓</div>
""", lambda L: f"""
    tl.fromTo("#ct-q", {{scale:1.15, opacity:0}}, {{scale:1, opacity:1, duration:0.4, ease:"power4.out"}}, {L(106.0)});
    tl.to("#ct-q", {{scale:1.04, duration:5.2, ease:"none"}}, {L(106.4)});
    tl.fromTo("#ct-s", {{opacity:0, y:20}}, {{opacity:1, y:0, duration:0.35}}, {L(108.6)});
    tl.fromTo("#ct-arrow", {{y:-20, opacity:0}}, {{y:20, opacity:1, duration:0.6, ease:"sine.inOut"}}, {L(108.8)});
    tl.to("#ct-arrow", {{y:-10, duration:0.6, ease:"sine.inOut"}}, {L(109.4)});
    tl.to("#ct-arrow", {{y:20, duration:0.6, ease:"sine.inOut"}}, {L(110.0)});
""")
TOTAL=111.5
hosts=[]
for cid,s0,s1,css,body,js in SC:
    dur=round(s1-s0,2)
    open(f'compositions/{cid}.html','w').write(scene(cid,dur,css,body,js))
    hosts.append(f'      <div id="{cid}" data-composition-id="{cid}" data-composition-src="compositions/{cid}.html" data-start="{s0}" data-duration="{dur}" data-track-index="2" data-track-kind="graphics" data-width="1080" data-height="1920" style="z-index:3"></div>')
sfx = [ # (file, time, vol)
 ('impact-bass-1',0.0,0.7),('whoosh-short',5.15,0.4),
 ('whoosh-cinematic',7.2,0.5),('impact-bass-2',11.4,0.5),('whoosh-short',15.4,0.4),('typing',18.4,0.3),
 ('whoosh-cinematic',27.6,0.5),('whoosh',30.2,0.5),('impact-bass-2',41.0,0.5),
 ('whoosh-cinematic',43.1,0.5),('whoosh-short',46.5,0.4),('whoosh-short',50.0,0.4),('impact-bass-2',52.7,0.6),
 ('whoosh-cinematic',54.4,0.5),('click',59.5,0.4),('click',60.3,0.4),
 ('whoosh-cinematic',64.4,0.5),('typing',70.5,0.3),('impact-bass-1',77.7,0.7),
 ('whoosh-cinematic',81.3,0.5),('whoosh-cinematic',90.6,0.5),('impact-bass-2',93.0,0.5),('whoosh',95.4,0.4),('chime',102.4,0.35),
 ('whoosh',105.8,0.4),
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
      <div id="case" class="clip" data-start="0" data-duration="{TOTAL}" data-track-index="4">FALL 008 · MONA LISA · 1911</div>
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
