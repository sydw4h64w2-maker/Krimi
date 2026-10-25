# Folge 7 – Flucht aus Alcatraz. Alle Zeiten global (Sekunden im Audio); L() rechnet in Szenenzeit um.
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
ISLAND = '<path d="M140,240 Q200,170 300,180 L330,120 L470,110 L520,170 Q640,170 700,240 Z" fill="#3a3f36"/><rect x="340" y="70" width="140" height="60" fill="#8f9399"/><rect x="390" y="30" width="22" height="50" fill="#8f9399"/>'
FACE = '<svg viewBox="0 0 100 100" width="100%" height="100%"><circle cx="50" cy="38" r="20" fill="#6b7079"/><path d="M14,100 Q14,64 50,60 Q86,64 86,100 Z" fill="#6b7079"/></svg>'
BED = lambda x, hid: f'<g transform="translate({x},0)"><rect x="0" y="60" width="220" height="70" rx="8" fill="#5b5f66"/><rect x="0" y="40" width="220" height="30" rx="8" fill="#7d8188"/><g id="{hid}"><ellipse cx="45" cy="44" rx="28" ry="24" fill="#d8b89a"/><path d="M18,40 Q45,8 72,40 Z" fill="#3a2a1a"/></g><rect x="70" y="36" width="150" height="34" rx="8" fill="#9EA3AC"/></g>'
# 1 HOOK 0-9.6
add('hook',0,9.6,"""
  #hk-a { top:310px; font-size:62px; font-weight:600; }
  #hk-svg { position:absolute; left:120px; top:420px; width:840px; height:320px; }
  #hk-n { top:760px; font-size:170px; font-weight:700; }
  #hk-m { position:absolute; left:290px; top:990px; width:500px; height:170px; display:flex; justify-content:space-between; }
  #hk-m .p { width:140px; height:170px; }
""", lambda L: f"""
    <div id="hk-w" class="clip" data-start="0" data-duration="9.6">
      <div id="hk-a" class="center">Das sicherste Gefängnis der USA</div>
      <svg id="hk-svg" viewBox="0 0 840 320"><rect x="0" y="220" width="840" height="100" fill="#16324a"/>{ISLAND}</svg>
      <div id="hk-n" class="center y">ALCATRAZ</div>
      <div id="hk-m"><div class="p" id="hk-p1">{FACE}</div><div class="p" id="hk-p2">{FACE}</div><div class="p" id="hk-p3">{FACE}</div></div>
    </div>
""", lambda L: f"""
    tl.fromTo("#hk-n", {{scale:1.08, opacity:1}}, {{scale:1, opacity:1, duration:0.35, ease:"power4.out"}}, 0);
    tl.to("#hk-n", {{scale:1.05, duration:8.8, ease:"none"}}, 0.4);
    tl.fromTo("#hk-a", {{y:20, opacity:1}}, {{y:0, opacity:1, duration:0.4}}, 0.1);
    tl.fromTo("#hk-svg", {{opacity:1, y:10}}, {{opacity:1, y:0, duration:0.6}}, 0);
    ["#hk-p1","#hk-p2","#hk-p3"].forEach((s,i)=>tl.fromTo(s, {{opacity:0, y:30}}, {{opacity:1, y:0, duration:0.25}}, {L(6.4)}+i*0.15));
    ["#hk-p1","#hk-p2","#hk-p3"].forEach((s,i)=>tl.to(s, {{opacity:0, duration:0.9}}, {L(7.9)}+i*0.2));
    {out('"#hk-w > *"',L,9.35).strip()}
""")
# 2 HAEFTLINGE 9.6-20.2
add('haeftl',9.6,20.2,"""
  #hf-y { top:300px; font-size:120px; font-weight:700; }
  #hf-g { position:absolute; left:80px; top:470px; width:920px; display:flex; justify-content:space-between; }
  #hf-g .c { width:285px; background:var(--paper); color:#1b1b1b; border-radius:8px; padding:20px 16px; text-align:center; opacity:0; }
  #hf-g .c .ph { height:230px; background:#d9d2c0; border:4px solid #1b1b1b; }
  #hf-g .c .nm { font-size:44px; font-weight:700; margin-top:14px; line-height:1.05; }
  #hf-p { top:950px; font-size:60px; font-weight:600; }
""", lambda L: f"""
    <div id="hf-w" class="clip" data-start="0" data-duration="{L(20.2)}">
      <div id="hf-y" class="center">1962</div>
      <div id="hf-g">
        <div class="c" id="hf-c1"><div class="ph">{FACE}</div><div class="nm">Frank<br/>Morris</div></div>
        <div class="c" id="hf-c2"><div class="ph">{FACE}</div><div class="nm">John<br/>Anglin</div></div>
        <div class="c" id="hf-c3"><div class="ph">{FACE}</div><div class="nm">Clarence<br/>Anglin</div></div>
      </div>
      <div id="hf-p" class="center">Plan: <span class="y">monatelang</span></div>
    </div>
""", lambda L: fin("#hf-y",L,9.9,0.4) + f"""
    tl.fromTo("#hf-c1", {{y:80, rotation:-5, opacity:0}}, {{y:0, rotation:-2, opacity:1, duration:0.45, ease:"power3.out"}}, {L(14.0)});
    tl.fromTo("#hf-c2", {{y:80, rotation:4, opacity:0}}, {{y:0, rotation:1, opacity:1, duration:0.45, ease:"power3.out"}}, {L(16.2)});
    tl.fromTo("#hf-c3", {{y:80, rotation:-3, opacity:0}}, {{y:0, rotation:2, opacity:1, duration:0.45, ease:"power3.out"}}, {L(16.9)});
""" + fin("#hf-p",L,19.0,0.35) + f"""
    tl.to("#hf-y", {{scale:1.06, duration:10, ease:"none"}}, {L(10.3)});
    {out('"#hf-w > *"',L,19.95).strip()}
""")
# 3 WERKZEUG 20.2-29.1
add('werkzeug',20.2,29.1,"""
  #wz-h { top:300px; font-size:58px; font-weight:600; }
  #wz-svg { position:absolute; left:290px; top:400px; width:500px; height:500px; }
  #wz-c { top:940px; font-size:60px; font-weight:600; }
""", lambda L: f"""
    <div id="wz-w" class="clip" data-start="0" data-duration="{L(29.1)}">
      <div id="wz-h" class="center">🥄 Werkzeug – <span class="y">u. a. aus Löffeln</span></div>
      <svg id="wz-svg" viewBox="0 0 500 500">
        <rect x="0" y="0" width="500" height="500" fill="#7d8188"/>{''.join(f'<rect x="0" y="{i*50}" width="500" height="2" fill="#6b6f76"/>' for i in range(10))}
        <rect id="wz-hole" x="150" y="150" width="200" height="200" fill="#0b0b0b"/>
        <g id="wz-grill">{''.join(f'<rect x="{150+i*28}" y="150" width="8" height="200" fill="#3b3f46"/>' for i in range(8))}<rect x="150" y="150" width="200" height="8" fill="#3b3f46"/><rect x="150" y="342" width="200" height="8" fill="#3b3f46"/></g>
        <g id="wz-fake">{''.join(f'<rect x="{110+i*40}" y="110" width="10" height="280" fill="#c9a46a"/>' for i in range(8))}<rect x="110" y="110" width="290" height="10" fill="#c9a46a"/><rect x="110" y="380" width="290" height="10" fill="#c9a46a"/></g>
      </svg>
      <div id="wz-c" class="center">Loch hinter <span class="y">falschem Gitter</span></div>
    </div>
""", lambda L: fin("#wz-h",L,20.5,0.35) + f"""
    tl.fromTo("#wz-svg", {{opacity:0}}, {{opacity:1, duration:0.4}}, {L(20.6)});
    tl.fromTo("#wz-grill", {{opacity:1}}, {{opacity:0, duration:1.5}}, {L(23.0)});
    tl.fromTo("#wz-hole", {{scale:1, svgOrigin:"250 250"}}, {{scale:1.45, duration:2.5, ease:"power1.inOut"}}, {L(23.0)});
    tl.fromTo("#wz-fake", {{y:-500, opacity:0}}, {{y:0, opacity:1, duration:0.5, ease:"power3.out"}}, {L(26.3)});
""" + fin("#wz-c",L,26.6,0.35) + f"""
    tl.to("#wz-svg", {{scale:1.04, duration:8, ease:"none"}}, {L(21.0)});
    {out('"#wz-w > *"',L,28.85).strip()}
""")
# 4 NACHT 29.1-41.4
add('nacht',29.1,41.4,"""
  #nt-d { top:300px; font-size:120px; font-weight:700; }
  #nt-svg { position:absolute; left:80px; top:500px; width:920px; height:200px; }
  #nt-c { top:760px; font-size:60px; font-weight:600; }
  #nt-z { top:880px; font-size:56px; font-weight:500; }
""", lambda L: f"""
    <div id="nt-w" class="clip" data-start="0" data-duration="{L(41.4)}">
      <div id="nt-d" class="center">11.06.1962</div>
      <svg id="nt-svg" viewBox="0 0 920 200">{BED(30,'nt-h1')}{BED(350,'nt-h2')}{BED(670,'nt-h3')}</svg>
      <div id="nt-c" class="center">Nachgebaute Köpfe – <span class="y">echtes Haar</span></div>
      <div id="nt-z" class="center p">💤 „Sie schlafen.“</div>
    </div>
""", lambda L: fin("#nt-d",L,29.4,0.4) + f"""
    tl.fromTo("#nt-svg", {{opacity:0}}, {{opacity:1, duration:0.5}}, {L(33.7)});
""" + fin("#nt-c",L,37.1,0.35) + fin("#nt-z",L,39.1,0.35) + f"""
    tl.to("#nt-d", {{scale:1.05, duration:11.5, ease:"none"}}, {L(29.8)});
    {out('"#nt-w > *"',L,41.15).strip()}
""")
# 5 FLUCHT 41.4-53.9
add('flucht',41.4,53.9,"""
  #fl-svg { position:absolute; left:90px; top:300px; width:900px; height:640px; }
  #fl-c { top:980px; font-size:60px; font-weight:600; }
  #fl-d { top:1080px; font-size:52px; font-weight:500; }
""", lambda L: f"""
    <div id="fl-w" class="clip" data-start="0" data-duration="{L(53.9)}">
      <svg id="fl-svg" viewBox="0 0 900 640">
        <rect x="80" y="80" width="360" height="380" fill="#5d5f66"/><rect x="80" y="70" width="360" height="14" fill="#8f9399"/>
        <rect x="0" y="470" width="900" height="170" fill="#16324a"/><path d="M0,460 L500,460 L540,480 L0,480 Z" fill="#3a3f36"/>
        <path id="fl-path" d="M250,420 L250,90 L470,90 L520,460" fill="none" stroke="#F2C230" stroke-width="8" stroke-dasharray="1200" stroke-dashoffset="1200" stroke-linecap="round"/>
        <text x="265" y="300" fill="#EDE6D6" font-family="Oswald" font-size="32">Schacht</text><text x="300" y="60" fill="#EDE6D6" font-family="Oswald" font-size="32">Dach</text>
        <g id="fl-raft"><rect x="500" y="490" width="170" height="40" rx="18" fill="#c9a04a"/><rect x="500" y="500" width="170" height="8" fill="#8a6a2a"/></g>
      </svg>
      <div id="fl-c" class="center">Floß aus <span class="y">Regenmänteln</span></div>
      <div id="fl-d" class="center">hinaus in die <span class="p">eiskalte Bucht</span></div>
    </div>
""", lambda L: f"""
    tl.fromTo("#fl-svg", {{opacity:0}}, {{opacity:1, duration:0.4}}, {L(41.6)});
    tl.fromTo("#fl-path", {{strokeDashoffset:1200}}, {{strokeDashoffset:0, duration:3.8, ease:"power1.inOut"}}, {L(41.7)});
    tl.to("#fl-svg", {{scale:1.05, duration:12, ease:"none"}}, {L(41.8)});
    tl.fromTo("#fl-raft", {{opacity:0, scale:0.6, transformOrigin:"585px 510px"}}, {{opacity:1, scale:1, duration:0.4, ease:"back.out(2)"}}, {L(46.1)});
""" + fin("#fl-c",L,48.3,0.35) + f"""
    tl.to("#fl-raft", {{x:220, y:60, duration:3.2, ease:"sine.inOut"}}, {L(50.5)});
""" + fin("#fl-d",L,50.6,0.35) + f"""
    {out('"#fl-w > *"',L,53.65).strip()}
""")
# 6 WEST 53.9-63.7
add('west',53.9,63.7,f"""
  #ws-h {{ top:300px; font-size:52px; }}
  #ws-c {{ position:absolute; left:340px; top:390px; width:400px; background:var(--paper); color:#1b1b1b; border-radius:8px; padding:20px 16px; text-align:center; }}
  #ws-c .ph {{ height:300px; background:#d9d2c0; border:4px solid #1b1b1b; }}
  #ws-c .nm {{ font-size:56px; font-weight:700; margin-top:12px; }}
  #ws-st {{ {STAMP} left:200px; top:830px; width:680px; font-size:72px; padding:4px 0; }}
  #ws-f {{ top:1010px; font-size:58px; font-weight:600; }}
""", lambda L: f"""
    <div id="ws-w" class="clip" data-start="0" data-duration="{L(63.7)}">
      <div id="ws-h" class="center lbl y">Der vierte Mann</div>
      <div id="ws-c"><div class="ph">{FACE}</div><div class="nm">Allen West</div></div>
      <div id="ws-st" data-layout-allow-overlap>NICHT RECHTZEITIG</div>
      <div id="ws-f" class="center">verrät dem FBI <span class="y">den ganzen Plan</span></div>
    </div>
""", lambda L: fin("#ws-h",L,54.1,0.3,"{opacity:0}","{opacity:1") + f"""
    tl.fromTo("#ws-c", {{y:100, rotation:-6, opacity:0}}, {{y:0, rotation:-2, opacity:1, duration:0.5, ease:"power3.out"}}, {L(55.0)});
    tl.fromTo("#ws-st", {{scale:2, rotation:-14, opacity:0}}, {{scale:1, rotation:-6, opacity:1, duration:0.22, ease:"power4.in"}}, {L(58.0)});
""" + fin("#ws-f",L,60.6,0.35) + f"""
    tl.to("#ws-c", {{scale:1.04, duration:8, ease:"none"}}, {L(55.6)});
    {out('"#ws-w > *"',L,63.45).strip()}
""")
# 7 MORGEN 63.7-73.4
add('morgen',63.7,73.4,f"""
  #mg-h {{ top:300px; font-size:60px; font-weight:600; }}
  #mg-svg {{ position:absolute; left:80px; top:420px; width:920px; height:200px; }}
  #mg-l {{ top:660px; font-size:120px; font-weight:700; }}
  #mg-f {{ top:830px; font-size:56px; }}
  #mg-st {{ {STAMP} left:200px; top:930px; width:680px; font-size:78px; padding:4px 0; }}
""", lambda L: f"""
    <div id="mg-w" class="clip" data-start="0" data-duration="{L(73.4)}">
      <div id="mg-h" class="center">Am nächsten Morgen</div>
      <svg id="mg-svg" viewBox="0 0 920 200">{BED(30,'mg-h1')}{BED(350,'mg-h2')}{BED(670,'mg-h3')}</svg>
      <div id="mg-l" class="center r">LEER</div>
      <div id="mg-f" class="center lbl y">Die Fahndung beginnt</div>
      <div id="mg-st">NIE GEFUNDEN</div>
    </div>
""", lambda L: fin("#mg-h",L,64.0,0.35) + f"""
    tl.fromTo("#mg-svg", {{opacity:0}}, {{opacity:1, duration:0.4}}, {L(64.2)});
    tl.to(["#mg-h1","#mg-h2","#mg-h3"], {{y:-40, opacity:0, duration:0.4, stagger:0.15}}, {L(66.0)});
    tl.fromTo("#mg-l", {{scale:1.4, opacity:0}}, {{scale:1, opacity:1, duration:0.3, ease:"power4.out"}}, {L(67.3)});
""" + fin("#mg-f",L,69.1,0.3,"{opacity:0}","{opacity:1") + f"""
    tl.fromTo("#mg-st", {{scale:2, rotation:-12, opacity:0}}, {{scale:1, rotation:-4, opacity:1, duration:0.22, ease:"power4.in"}}, {L(71.6)});
    tl.to("#mg-svg", {{scale:1.04, duration:9, ease:"none"}}, {L(64.6)});
    {out('"#mg-w > *"',L,73.15).strip()}
""")
# 8 AKTE 73.4-87.4
add('akte',73.4,87.4,"""
  #ak-1 { top:330px; font-size:110px; font-weight:700; }
  #ak-1b { top:480px; font-size:56px; font-weight:500; }
  #ak-2 { top:640px; font-size:60px; font-weight:600; }
  #ak-2b { top:730px; font-size:56px; font-weight:500; }
  #ak-3 { top:900px; font-size:60px; font-weight:600; }
  #ak-svg { position:absolute; left:390px; top:1000px; width:300px; height:120px; }
""", lambda L: f"""
    <div id="ak-w" class="clip" data-start="0" data-duration="{L(87.4)}">
      <div id="ak-1" class="center">1979 · FBI</div>
      <div id="ak-1b" class="center">„vermutlich <span class="y">ertrunken</span>“</div>
      <div id="ak-2" class="center">U.S. Marshals</div>
      <div id="ak-2b" class="center">Akte <span class="r">offen gehalten</span></div>
      <div id="ak-3" class="center">1963 · Alcatraz <span class="p">geschlossen</span></div>
      <svg id="ak-svg" viewBox="0 0 300 120"><rect x="60" y="20" width="180" height="90" rx="10" fill="none" stroke="#F2C230" stroke-width="10"/><path d="M95,20 L95,0 Q150,-30 205,0 L205,20" fill="none" stroke="#F2C230" stroke-width="10"/></svg>
    </div>
""", lambda L: f"""
    tl.fromTo("#ak-1", {{scale:1.2, opacity:0}}, {{scale:1, opacity:1, duration:0.35, ease:"power4.out"}}, {L(73.7)});
    tl.to("#ak-1", {{scale:1.05, duration:13.5, ease:"none"}}, {L(74.1)});
""" + fin("#ak-1b",L,77.1,0.35) + fin("#ak-2",L,79.6,0.35) + fin("#ak-2b",L,81.0,0.35) + fin("#ak-3",L,84.9,0.35) + f"""
    tl.fromTo("#ak-svg", {{opacity:0, y:-20}}, {{opacity:1, y:0, duration:0.35, ease:"bounce.out"}}, {L(85.6)});
    {out('"#ak-w > *"',L,87.15).strip()}
""")
# 9 CTA 87.4-92.5
add('cta',87.4,92.5,"""
  #ct-q { top:520px; font-size:140px; font-weight:700; line-height:1.05; }
  #ct-s { top:880px; font-size:56px; font-weight:500; }
  #ct-arrow { top:1000px; font-size:120px; }
""", lambda L: f"""
    <div id="ct-q" class="center clip" data-start="0" data-duration="{L(92.5)}">Ertrunken oder<br/><span class="y">entkommen?</span></div>
    <div id="ct-s" class="center clip" data-start="{L(89.6)}" data-duration="{round(L(92.5)-L(89.6),2)}">Schreib's in die Kommentare</div>
    <div id="ct-arrow" class="center clip y" data-start="{L(89.9)}" data-duration="{round(L(92.5)-L(89.9),2)}">↓</div>
""", lambda L: f"""
    tl.fromTo("#ct-q", {{scale:1.15, opacity:0}}, {{scale:1, opacity:1, duration:0.4, ease:"power4.out"}}, {L(87.65)});
    tl.to("#ct-q", {{scale:1.04, duration:4.6, ease:"none"}}, {L(88.1)});
    tl.fromTo("#ct-s", {{opacity:0, y:20}}, {{opacity:1, y:0, duration:0.35}}, {L(89.7)});
    tl.fromTo("#ct-arrow", {{y:-20, opacity:0}}, {{y:20, opacity:1, duration:0.6, ease:"sine.inOut"}}, {L(89.9)});
    tl.to("#ct-arrow", {{y:-10, duration:0.6, ease:"sine.inOut"}}, {L(90.5)});
    tl.to("#ct-arrow", {{y:20, duration:0.6, ease:"sine.inOut"}}, {L(91.1)});
""")
TOTAL=92.5
hosts=[]
for cid,s0,s1,css,body,js in SC:
    dur=round(s1-s0,2)
    open(f'compositions/{cid}.html','w').write(scene(cid,dur,css,body,js))
    hosts.append(f'      <div id="{cid}" data-composition-id="{cid}" data-composition-src="compositions/{cid}.html" data-start="{s0}" data-duration="{dur}" data-track-index="2" data-track-kind="graphics" data-width="1080" data-height="1920" style="z-index:3"></div>')
sfx = [ # (file, time, vol)
 ('impact-bass-1',0.0,0.7),('whoosh-short',6.4,0.4),
 ('whoosh-cinematic',9.6,0.5),('whoosh-short',14.0,0.4),('whoosh-short',16.2,0.4),('whoosh-short',16.9,0.4),
 ('whoosh-cinematic',20.2,0.5),('impact-bass-2',26.3,0.5),
 ('whoosh-cinematic',29.1,0.5),
 ('whoosh-cinematic',41.4,0.5),('pop',46.1,0.4),
 ('whoosh-cinematic',53.9,0.5),('impact-bass-2',58.0,0.6),
 ('whoosh-cinematic',63.7,0.5),('impact-bass-1',67.3,0.7),('impact-bass-1',71.6,0.7),
 ('whoosh-cinematic',73.4,0.5),('impact-bass-2',85.6,0.5),('whoosh',87.4,0.4),
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
      <div id="case" class="clip" data-start="0" data-duration="{TOTAL}" data-track-index="4">FALL 007 · ALCATRAZ · 1962</div>
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
