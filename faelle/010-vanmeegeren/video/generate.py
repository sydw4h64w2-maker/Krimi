# Folge 10 – Han van Meegeren · Szenen hängen an Sätzen (T), Timing kommt aus assets/words.json. Alle Zeiten global (Sekunden im Audio); L() rechnet in Szenenzeit um.
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

_W = json.load(open('assets/words.json'))
_U = _W['units']
def T(phrase, off=0.0):
    for t,u in _U:
        if u.startswith(phrase) or phrase in u: return round(t+off,2)
    raise KeyError(phrase)
END = round(_W['words'][-1]['end'] + 1.4, 2)
STAMP = "position:absolute; text-align:center; border:12px solid var(--red); border-radius:14px; color:var(--red); font-weight:700; white-space:nowrap;"
CARD = "position:absolute; background:var(--paper); color:#1b1b1b; border-radius:10px; box-shadow:0 25px 60px rgba(0,0,0,.5);"
FACE = '<svg viewBox="0 0 100 100" width="100%" height="100%"><circle cx="50" cy="38" r="20" fill="#6b7079"/><path d="M14,100 Q14,64 50,60 Q86,64 86,100 Z" fill="#6b7079"/></svg>'
def FRAME(w,h,inner=""): return f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}"><rect x="6" y="6" width="{w-12}" height="{h-12}" fill="none" stroke="#C9A04A" stroke-width="12"/><rect x="22" y="22" width="{w-44}" height="{h-44}" fill="#2a2418"/>{inner}</svg>'
PAINT = '<rect x="40" y="40" width="{w}" height="{h}" fill="#4a5a6a"/><path d="M40,{h2} Q120,{h3} 200,{h2} T{wx},{h2} L{wx},{hy} L40,{hy} Z" fill="#6b5a3a"/><circle cx="{cx}" cy="{cy}" r="40" fill="#c8a26a"/>'
S = [0, T("Mai neunzehn",-0.25), T("Am neunundzwanzigsten",-0.25), T("Doch van Meegeren sagt",-0.25), T("Also beweist",-0.25), T("Und er verrät",-0.25), T("Göring hatte",-0.25), T("Der Vorwurf der Kollaboration",-0.25), T("Antreten",-0.25), T("Genialer Held",-0.25), END]
# 1 HOOK
add('hook',S[0],S[1],"""
  #hk-a { top:370px; font-size:160px; font-weight:700; }
  #hk-b { top:620px; font-size:60px; font-weight:500; }
  #hk-c { top:720px; font-size:80px; font-weight:700; line-height:1.15; }
""", lambda L: f"""
    <div id="hk-w" class="clip" data-start="0" data-duration="{round(S[1]-S[0],2)}">
      <div id="hk-a" class="center r">TODESSTRAFE</div>
      <div id="hk-b" class="center">Seine einzige Rettung:</div>
      <div id="hk-c" class="center">Beweisen, dass er<br/><span class="y">ein Betrüger ist</span></div>
    </div>
""", lambda L: f"""
    tl.fromTo("#hk-a", {{scale:1.08, opacity:1}}, {{scale:1, opacity:1, duration:0.35, ease:"power4.out"}}, 0);
    tl.to("#hk-a", {{scale:1.06, duration:{round(S[1]-0.6,2)}, ease:"none"}}, 0.4);
""" + fin("#hk-b",L,T("Und es gab"),0.35) + fin("#hk-c",L,T("Er musste beweisen"),0.4) + f"""
    {out('"#hk-w > *"',L,S[1]-0.25).strip()}
""")
# 2 FUND
add('fund',S[1],S[2],"""
  #fd-a { top:300px; font-size:100px; font-weight:700; }
  #fd-b { top:430px; font-size:46px; }
  #fd-f { position:absolute; left:290px; top:520px; }
  #fd-q { position:absolute; left:290px; top:690px; width:500px; text-align:center; font-size:90px; font-weight:700; color:var(--accent); }
  #fd-n { top:1030px; font-size:64px; font-weight:600; }
""", lambda L: f"""
    <div id="fd-w" class="clip" data-start="0" data-duration="{round(S[2]-S[1],2)}">
      <div id="fd-a" class="center">Mai 1945</div>
      <div id="fd-b" class="center lbl y">Görings Sammlung</div>
      <div id="fd-f">{FRAME(500,440)}</div>
      <div id="fd-q" data-layout-allow-overlap>„VERMEER“?</div>
      <div id="fd-n" class="center">Spur → <span class="y">Han van Meegeren</span></div>
    </div>
""", lambda L: fin("#fd-a",L,S[1]+0.1,0.4) + fin("#fd-b",L,T("In der Sammlung"),0.3,"{opacity:0}","{opacity:1") + f"""
    tl.fromTo("#fd-f", {{y:60, opacity:0}}, {{y:0, opacity:1, duration:0.5, ease:"power3.out"}}, {L(T("In der Sammlung",0.6))});
    tl.fromTo("#fd-q", {{scale:1.3, opacity:0}}, {{scale:1, opacity:1, duration:0.35, ease:"power4.out"}}, {L(T("angeblich"))});
    tl.to("#fd-f", {{scale:1.05, duration:{round(S[2]-T("In der Sammlung")-0.5,2)}, ease:"none"}}, {L(T("In der Sammlung",1.1))});
""" + fin("#fd-n",L,T("Die Spur führt"),0.35) + f'    tl.to("#fd-a", {{scale:1.06, duration:{round(S[2]-S[1]-0.6,2)}, ease:"none"}}, {L(S[1]+0.5)});\n' + f"""
    {out('"#fd-w > *"',L,S[2]-0.25).strip()}
""")
# 3 HAFT
add('haft',S[2],S[3],f"""
  #hf-a {{ top:300px; font-size:110px; font-weight:700; }}
  #hf-b {{ top:440px; font-size:46px; }}
  #hf-c {{ top:560px; font-size:58px; font-weight:600; line-height:1.2; }}
  #hf-st {{ {STAMP} left:190px; top:780px; width:700px; font-size:110px; padding:6px 0; }}
""", lambda L: f"""
    <div id="hf-w" class="clip" data-start="0" data-duration="{round(S[3]-S[2],2)}">
      <div id="hf-a" class="center">29.05.1945</div>
      <div id="hf-b" class="center lbl y">Verhaftung</div>
      <div id="hf-c" class="center">Vorwurf: Kunstschatz<br/><span class="r">an die Nazis verkauft</span></div>
      <div id="hf-st">TODESSTRAFE</div>
    </div>
""", lambda L: fin("#hf-a",L,S[2]+0.1,0.4) + fin("#hf-b",L,S[2]+1.5,0.3,"{opacity:0}","{opacity:1") + fin("#hf-c",L,T("Er habe einen"),0.4) + f"""
    tl.fromTo("#hf-st", {{scale:2, rotation:-12, opacity:0}}, {{scale:1, rotation:-4, opacity:1, duration:0.22, ease:"power4.in"}}, {L(T("Darauf steht",1.6))});
    tl.to("#hf-a", {{scale:1.05, duration:{round(S[3]-S[2]-0.6,2)}, ease:"none"}}, {L(S[2]+0.5)});
    {out('"#hf-w > *"',L,S[3]-0.25).strip()}
""")
# 4 GESTAENDNIS
BUB="position:absolute; left:120px; width:840px; background:#EDE6D6; color:#1b1b1b; border-radius:30px; padding:30px 40px; font-size:60px; font-weight:600; text-align:center;"
add('gest',S[3],S[4],f"""
  #gs-h {{ top:300px; font-size:46px; }}
  #gs-1 {{ {BUB} top:380px; }}
  #gs-2 {{ {BUB} top:560px; }}
  #gs-n {{ top:820px; font-size:70px; font-weight:700; }}
  #gs-e {{ top:930px; font-size:56px; font-weight:500; }}
""", lambda L: f"""
    <div id="gs-w" class="clip" data-start="0" data-duration="{round(S[4]-S[3],2)}">
      <div id="gs-h" class="center lbl y">Van Meegeren sagt</div>
      <div id="gs-1">„Das ist kein Vermeer.“</div>
      <div id="gs-2">„Ich habe es <span style="color:#B3261E">selbst gemalt</span>.“</div>
      <div id="gs-n" class="center">Niemand glaubt ihm</div>
      <div id="gs-e" class="center">Experten hielten seine Bilder für <span class="y">echt</span></div>
    </div>
""", lambda L: fin("#gs-h",L,S[3]+0.1,0.3,"{opacity:0}","{opacity:1") + fin("#gs-1",L,T("Das Bild ist"),0.4,"{opacity:0, scale:0.9}","{opacity:1, scale:1",ease="back.out(1.6)") + fin("#gs-2",L,T("Ich habe es"),0.4,"{opacity:0, scale:0.9}","{opacity:1, scale:1",ease="back.out(1.6)") + f"""
    tl.to("#gs-1, #gs-2", {{opacity:0.4, duration:0.3}}, {L(T("Niemand"))});
""" + fin("#gs-n",L,T("Niemand"),0.35) + fin("#gs-e",L,T("Denn seine"),0.35) + f'    tl.to("#gs-e", {{scale:1.05, duration:{round(S[4]-T("Denn seine")-0.6,2)}, ease:"none"}}, {L(T("Denn seine",0.4))});\n' + f"""
    tl.to("#gs-2", {{scale:1.04, duration:{round(T("Niemand")-T("Ich habe es"),2)}, ease:"none"}}, {L(T("Ich habe es",0.4))});
    {out('"#gs-w > *"',L,S[4]-0.25).strip()}
""")
# 5 BEWEIS
add('beweis',S[4],S[5],"""
  #bw-h { top:300px; font-size:90px; font-weight:700; }
  #bw-svg { position:absolute; left:140px; top:430px; width:800px; height:520px; }
  #bw-t { top:990px; font-size:56px; font-weight:600; }
""", lambda L: f"""
    <div id="bw-w" class="clip" data-start="0" data-duration="{round(S[5]-S[4],2)}">
      <div id="bw-h" class="center">Der Beweis</div>
      <svg id="bw-svg" viewBox="0 0 800 520">
        <path d="M330,500 L400,90 L470,500" fill="none" stroke="#8a6a3d" stroke-width="12"/>
        <rect x="270" y="60" width="260" height="330" fill="#EDE6D6" stroke="#8a6a3d" stroke-width="8"/>
        <g id="bw-paint"><rect x="285" y="75" width="230" height="300" fill="#4a5a6a"/><path d="M285,260 Q360,220 400,250 T515,240 L515,375 L285,375 Z" fill="#6b5a3a"/><circle cx="400" cy="170" r="36" fill="#c8a26a"/><path d="M360,375 Q370,250 400,230 Q430,250 440,375 Z" fill="#2b3a5a"/></g>
        {''.join(f'<g transform="translate({x},330)"><circle cx="40" cy="40" r="30" fill="#6b7079"/><path d="M0,190 Q0,90 40,82 Q80,90 80,190 Z" fill="#6b7079"/></g>' for x in (30,130,600,700))}
      </svg>
      <div id="bw-t" class="center">„Jesus unter den <span class="y">Schriftgelehrten</span>“</div>
    </div>
""", lambda L: fin("#bw-h",L,S[4]+0.1,0.4) + f"""
    tl.fromTo("#bw-svg", {{opacity:0}}, {{opacity:1, duration:0.4}}, {L(T("Unter Aufsicht"))});
    tl.fromTo("#bw-paint", {{clipPath:"inset(100% 0 0 0)"}}, {{clipPath:"inset(0% 0 0 0)", duration:{round(T("Jesus unter")-T("Unter Aufsicht"),2)}, ease:"steps(12)"}}, {L(T("Unter Aufsicht",0.4))});
""" + fin("#bw-t",L,T("Jesus unter"),0.35) + f"""
    tl.to("#bw-svg", {{scale:1.04, duration:{round(S[5]-T("Unter Aufsicht"),2)}, ease:"none"}}, {L(T("Unter Aufsicht",0.3))});
    {out('"#bw-w > *"',L,S[5]-0.25).strip()}
""")
# 6 TRICK
add('trick',S[5],S[6],"""
  #tr-h { top:300px; font-size:56px; font-weight:600; }
  #tr-a { top:400px; font-size:66px; font-weight:600; }
  #tr-b { top:500px; font-size:160px; font-weight:700; line-height:1; }
  #tr-svg { position:absolute; left:290px; top:700px; width:500px; height:360px; }
  #tr-c { top:1090px; font-size:56px; font-weight:600; }
""", lambda L: f"""
    <div id="tr-w" class="clip" data-start="0" data-duration="{round(S[6]-S[5],2)}">
      <div id="tr-h" class="center lbl y">Sein Trick</div>
      <div id="tr-a" class="center">Kunstharz in der Farbe:</div>
      <div id="tr-b" class="center y">BAKELIT</div>
      <svg id="tr-svg" viewBox="0 0 500 360"><rect x="20" y="20" width="460" height="320" rx="20" fill="#3b3f46" stroke="#6b6f76" stroke-width="8"/><rect x="60" y="60" width="380" height="200" rx="10" fill="#1a1d22"/><g id="tr-heat">{''.join(f'<path d="M{100+i*70},240 q15,-40 0,-80 q-15,-40 0,-80" stroke="#D2372E" stroke-width="8" fill="none" opacity=".85"/>' for i in range(5))}</g><circle cx="420" cy="300" r="14" fill="#F2C230"/></svg>
      <div id="tr-c" class="center">🔥 im Ofen gehärtet – <span class="y">wie Jahrhunderte alt</span></div>
    </div>
""", lambda L: fin("#tr-h",L,S[5]+0.1,0.3,"{opacity:0}","{opacity:1") + fin("#tr-a",L,T("Er mischte"),0.35) + f"""
    tl.fromTo("#tr-b", {{scale:1.3, opacity:0}}, {{scale:1, opacity:1, duration:0.3, ease:"power4.out"}}, {L(T("Bakelit"))});
    tl.fromTo("#tr-svg", {{y:60, opacity:0}}, {{y:0, opacity:1, duration:0.45, ease:"power3.out"}}, {L(T("und härtete"))});
    tl.fromTo("#tr-heat", {{y:20, opacity:0.2}}, {{y:-10, opacity:1, duration:0.6, ease:"sine.inOut", yoyo:true, repeat:5}}, {L(T("und härtete",0.3))});
""" + fin("#tr-c",L,T("damit sie"),0.35) + f"""
    tl.to("#tr-b", {{scale:1.05, duration:{round(S[6]-T("Bakelit")-0.5,2)}, ease:"none"}}, {L(T("Bakelit",0.35))});
    {out('"#tr-w > *"',L,S[6]-0.25).strip()}
""")
# 7 GOERING
add('goering',S[6],S[7],"""
  #go-g { position:absolute; left:140px; top:300px; width:800px; display:grid; grid-template-columns:repeat(10,1fr); gap:8px; }
  #go-g .f { height:60px; border:4px solid #C9A04A; background:#2a2418; opacity:0; }
  #go-a { top:780px; font-size:60px; font-weight:600; }
  #go-b { top:880px; font-size:80px; font-weight:700; }
  #go-c { top:1030px; font-size:70px; font-weight:700; }
""", lambda L: f"""
    <div id="go-w" class="clip" data-start="0" data-duration="{round(S[7]-S[6],2)}">
      <div id="go-g">{''.join(f'<div class="f" id="go-f{i}"></div>' for i in range(60))}</div>
      <div id="go-a" class="center">Göring gab <span class="y">über 100 geraubte Gemälde</span></div>
      <div id="go-b" class="center">= 1 <span class="r">Fälschung</span></div>
      <div id="go-c" class="center"><span class="p" style="text-decoration:line-through">Verräter</span> → <span class="y">Held?</span></div>
    </div>
""", lambda L: f"""
    for (let i=0;i<60;i++) tl.fromTo("#go-f"+i, {{opacity:0}}, {{opacity:1, duration:0.1}}, {L(S[6]+0.2)}+i*0.05);
""" + fin("#go-a",L,S[6]+0.4,0.35) + f"""
    tl.fromTo("#go-b", {{scale:1.4, opacity:0}}, {{scale:1, opacity:1, duration:0.3, ease:"power4.out"}}, {L(T("Für eine Fälschung"))});
""" + fin("#go-c",L,T("Plötzlich"),0.4) + f"""
    tl.to("#go-g", {{scale:1.04, duration:{round(S[7]-S[6]-0.5,2)}, ease:"none"}}, {L(S[6]+0.3)});
    {out('"#go-w > *"',L,S[7]-0.25).strip()}
""")
# 8 URTEIL
add('urteil',S[7],S[8],f"""
  #ur-a {{ top:330px; font-size:56px; font-weight:600; }}
  #ur-b {{ top:460px; font-size:110px; font-weight:700; }}
  #ur-c {{ top:610px; font-size:52px; }}
  #ur-st {{ {STAMP} left:240px; top:730px; width:600px; font-size:120px; padding:6px 0; }}
""", lambda L: f"""
    <div id="ur-w" class="clip" data-start="0" data-duration="{round(S[8]-S[7],2)}">
      <div id="ur-a" class="center">Kollaboration: <span class="y">fallen gelassen</span></div>
      <div id="ur-b" class="center">12.11.1947</div>
      <div id="ur-c" class="center lbl">schuldig wegen Fälschung &amp; Betrug</div>
      <div id="ur-st">1 JAHR</div>
    </div>
""", lambda L: fin("#ur-a",L,S[7]+0.1,0.35) + f'    tl.to("#ur-a", {{scale:1.05, duration:{round(S[8]-S[7]-0.6,2)}, ease:"none"}}, {L(S[7]+0.5)});\n' + fin("#ur-b",L,T("Am zwölften"),0.4) + fin("#ur-c",L,T("Am zwölften",2.0),0.3,"{opacity:0}","{opacity:1") + f"""
    tl.fromTo("#ur-st", {{scale:2, rotation:-12, opacity:0}}, {{scale:1, rotation:-4, opacity:1, duration:0.22, ease:"power4.in"}}, {L(T("ein Jahr Haft"))});
    tl.to("#ur-b", {{scale:1.05, duration:{round(S[8]-T("Am zwölften")-0.5,2)}, ease:"none"}}, {L(T("Am zwölften",0.4))});
    {out('"#ur-w > *"',L,S[8]-0.25).strip()}
""")
# 9 TOD
add('tod',S[8],S[9],"""
  #td-a { top:420px; font-size:80px; font-weight:700; }
  #td-b { top:580px; font-size:110px; font-weight:700; }
  #td-c { top:730px; font-size:56px; }
""", lambda L: f"""
    <div id="td-w" class="clip" data-start="0" data-duration="{round(S[9]-S[8],2)}">
      <div id="td-a" class="center">Haft angetreten: <span class="r">nie</span></div>
      <div id="td-b" class="center p">30.12.1947</div>
      <div id="td-c" class="center lbl">Han van Meegeren stirbt · Herzversagen</div>
    </div>
""", lambda L: fin("#td-a",L,S[8]+0.1,0.4) + fin("#td-b",L,T("Am dreißigsten"),0.45) + fin("#td-c",L,T("Am dreißigsten",2.5),0.35,"{opacity:0}","{opacity:1") + f"""
    tl.to("#td-b", {{scale:1.05, duration:{round(S[9]-T("Am dreißigsten")-0.5,2)}, ease:"none"}}, {L(T("Am dreißigsten",0.45))});
    {out('"#td-w > *"',L,S[9]-0.25).strip()}
""")
# 10 CTA
add('cta',S[9],S[10],"""
  #ct-q { top:500px; font-size:130px; font-weight:700; line-height:1.05; }
  #ct-s { top:880px; font-size:56px; font-weight:500; }
  #ct-arrow { top:1000px; font-size:120px; }
""", lambda L: f"""
    <div id="ct-q" class="center clip" data-start="0" data-duration="{round(S[10]-S[9],2)}">Genialer Held<br/><span class="y">oder Betrüger?</span></div>
    <div id="ct-s" class="center clip" data-start="{L(T('Schreib'))}" data-duration="{round(S[10]-T('Schreib'),2)}">Schreib's in die Kommentare</div>
    <div id="ct-arrow" class="center clip y" data-start="{L(T('Schreib',0.3))}" data-duration="{round(S[10]-T('Schreib',0.3),2)}">↓</div>
""", lambda L: f"""
    tl.fromTo("#ct-q", {{scale:1.15, opacity:0}}, {{scale:1, opacity:1, duration:0.4, ease:"power4.out"}}, {L(S[9]+0.25)});
    tl.to("#ct-q", {{scale:1.04, duration:{round(S[10]-S[9]-0.8,2)}, ease:"none"}}, {L(S[9]+0.7)});
    tl.fromTo("#ct-s", {{opacity:0, y:20}}, {{opacity:1, y:0, duration:0.35}}, {L(T('Schreib',0.1))});
    tl.fromTo("#ct-arrow", {{y:-20, opacity:0}}, {{y:20, opacity:1, duration:0.6, ease:"sine.inOut"}}, {L(T('Schreib',0.3))});
    tl.to("#ct-arrow", {{y:-10, duration:0.6, ease:"sine.inOut"}}, {L(T('Schreib',0.9))});
""")
TOTAL=END
hosts=[]
for cid,s0,s1,css,body,js in SC:
    dur=round(s1-s0,2)
    open(f'compositions/{cid}.html','w').write(scene(cid,dur,css,body,js))
    hosts.append(f'      <div id="{cid}" data-composition-id="{cid}" data-composition-src="compositions/{cid}.html" data-start="{s0}" data-duration="{dur}" data-track-index="2" data-track-kind="graphics" data-width="1080" data-height="1920" style="z-index:3"></div>')
sfx = [ # (file, time, vol) – an Sätzen verankert
 ('impact-bass-1',0.0,0.7),('impact-bass-2',T("dass er ein Betrüger"),0.5),
 ('whoosh-cinematic',S[1],0.5),('impact-bass-2',T("angeblich"),0.5),
 ('whoosh-cinematic',S[2],0.5),('impact-bass-1',T("Darauf steht",1.6),0.8),
 ('whoosh-cinematic',S[3],0.5),('pop',T("Das Bild ist"),0.4),('pop',T("Ich habe es"),0.4),
 ('whoosh-cinematic',S[4],0.5),('typing',T("Unter Aufsicht",0.4),0.25),
 ('whoosh-cinematic',S[5],0.5),('impact-bass-2',T("Bakelit"),0.5),('riser',T("und härtete"),0.25),
 ('whoosh-cinematic',S[6],0.5),('impact-bass-1',T("Für eine Fälschung"),0.7),('chime',T("Plötzlich"),0.3),
 ('whoosh-cinematic',S[7],0.5),('impact-bass-1',T("ein Jahr Haft"),0.8),
 ('whoosh-cinematic',S[8],0.5),('whoosh',S[9],0.4),
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
      <div id="case" class="clip" data-start="0" data-duration="{TOTAL}" data-track-index="4">FALL 010 · VAN MEEGEREN · 1945</div>
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
if os.path.exists('../audio-elevenlabs.mp3'):
    normalize_voice('../audio-elevenlabs.mp3', 'assets/voice.mp3')
else:  # Vorschau ohne Aufnahme: stille Spur, Timing geschätzt
    subprocess.run(["ffmpeg","-y","-loglevel","error","-f","lavfi","-i",f"anullsrc=r=44100:cl=stereo","-t",str(TOTAL),"-b:a","64k","assets/voice.mp3"],check=True)
open('index.html','w').write(index)
print("ok", TOTAL)
