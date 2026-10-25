import os, json, subprocess
os.chdir('/home/user/Krimi/faelle/001-antwerpen/video')
BASE = """
  #root { position:absolute; inset:0; font-family:'Oswald',sans-serif; color:var(--ink); }
  .lbl { font-family:'Space Mono',monospace; letter-spacing:.08em; text-transform:uppercase; }
  .center { position:absolute; left:0; width:100%; text-align:center; }
  .y { color:var(--accent); } .r { color:var(--red); }
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
S = {}
# 1 HOOK 0-8
S['hook'] = (8, """
  #hk-num { top:430px; font-size:420px; font-weight:700; line-height:1; }
  #hk-sub { top:880px; font-size:96px; font-weight:600; letter-spacing:.02em; }
  #hk-sub2 { top:1010px; font-size:44px; }
  #hk-and { top:1140px; font-size:70px; font-weight:500; }
""", """
    <div id="hk-num" class="center clip y" data-start="0" data-duration="8">10</div>
    <div id="hk-sub" class="center clip" data-start="0" data-duration="8">SICHERHEITSSCHICHTEN</div>
    <div id="hk-sub2" class="center clip lbl" data-start="1.6" data-duration="6.4">Ein Tresor, der als unknackbar galt</div>
    <div id="hk-and" class="center clip" data-start="4.2" data-duration="3.8">…verraten von einem <span class="y">Sandwich</span> 🥪</div>
""", """
    tl.fromTo("#hk-num", {scale:1.12, opacity:1}, {scale:1, opacity:1, duration:0.35, ease:"power4.out"}, 0);
    tl.fromTo("#hk-sub", {y:20, opacity:1}, {y:0, opacity:1, duration:0.4, ease:"power3.out"}, 0.15);
    tl.fromTo("#hk-sub2", {opacity:0}, {opacity:1, duration:0.4}, 1.6);
    tl.fromTo("#hk-and", {y:30, opacity:0}, {y:0, opacity:1, duration:0.4, ease:"back.out(2)"}, 4.2);
    tl.to(["#hk-num","#hk-sub","#hk-sub2","#hk-and"], {opacity:0, duration:0.25}, 7.6);
""")
# 2 ORT 8-22 (14s)
S['ort'] = (14, """
  #or-city { top:300px; font-size:150px; font-weight:700; }
  #or-land { top:480px; font-size:36px; }
  #or-dc { top:600px; font-size:40px; color:var(--paper); opacity:.85; }
  #or-vault { position:absolute; left:290px; top:700px; width:500px; height:500px; }
  #or-vault .ring { position:absolute; inset:0; border:14px solid var(--accent); border-radius:50%; }
  #or-vault .ring2 { position:absolute; inset:70px; border:6px dashed rgba(242,194,48,.55); border-radius:50%; }
  #or-vault .hub { position:absolute; left:200px; top:200px; width:100px; height:100px; border-radius:50%; background:var(--accent); }
  #or-vault .spoke { position:absolute; left:244px; top:40px; width:12px; height:420px; background:var(--accent); border-radius:6px; }
  #or-boxes { top:1225px; font-size:64px; font-weight:600; }
  #or-list { position:absolute; left:140px; width:800px; top:330px; }
  #or-list .it { font-size:66px; font-weight:600; padding:14px 0; border-bottom:2px solid rgba(255,255,255,.12); opacity:0; }
  #or-list .it span { font-family:'Space Mono',monospace; font-size:34px; color:var(--accent); margin-right:28px; }
""", """
    <div id="or-a" class="clip" data-start="0" data-duration="8">
      <div id="or-city" class="center">ANTWERPEN</div>
      <div id="or-land" class="center lbl y">Belgien · Zentrum des Diamantenhandels</div>
      <div id="or-dc" class="center lbl">Antwerp Diamond Centre</div>
      <div id="or-vault"><div class="ring"></div><div class="ring2"></div><div class="spoke" id="or-sp1"></div><div class="spoke" id="or-sp2"></div><div class="hub"></div></div>
      <div id="or-boxes" class="center"><span class="y">160</span> Schließfächer</div>
    </div>
    <div id="or-b" class="clip" data-start="8" data-duration="6">
      <div id="or-list">
        <div class="it" id="or-i1"><span>01</span>Zahlenschloss</div>
        <div class="it" id="or-i2"><span>02</span>Wärmesensoren</div>
        <div class="it" id="or-i3"><span>03</span>Radar</div>
        <div class="it" id="or-i4"><span>04</span>Seismischer Sensor</div>
        <div class="it" id="or-i5"><span>05</span>Magnetfeld</div>
        <div class="it lbl" id="or-i6" style="font-size:40px;border:none;color:var(--paper)"><span>…</span>insgesamt 10 Schichten</div>
      </div>
    </div>
""", """
    tl.fromTo("#or-city", {y:50, opacity:0}, {y:0, opacity:1, duration:0.5, ease:"power3.out"}, 0);
    tl.fromTo("#or-land", {opacity:0}, {opacity:1, duration:0.4}, 0.5);
    tl.fromTo("#or-dc", {opacity:0}, {opacity:.85, duration:0.4}, 3.0);
    tl.fromTo("#or-vault", {scale:0.6, opacity:0}, {scale:1, opacity:1, duration:0.6, ease:"power3.out"}, 3.0);
    tl.fromTo("#or-sp1", {rotation:0}, {rotation:180, duration:5, ease:"none"}, 3.0);
    tl.fromTo("#or-sp2", {rotation:90}, {rotation:270, duration:5, ease:"none"}, 3.0);
    tl.fromTo("#or-boxes", {y:30, opacity:0}, {y:0, opacity:1, duration:0.4, ease:"power3.out"}, 5.0);
    tl.to("#or-a > *", {opacity:0, duration:0.25}, 7.7);
    ["#or-i1","#or-i2","#or-i3","#or-i4","#or-i5","#or-i6"].forEach((s,i)=>{
      tl.fromTo(s, {x:-60, opacity:0}, {x:0, opacity:1, duration:0.3, ease:"power3.out"}, 8.2 + i*0.75);
    });
    tl.to("#or-list", {opacity:0, duration:0.25}, 13.7);
""")
# 3 INSIDER 22-34 (12s)
S['insider'] = (12, """
  #in-card { position:absolute; left:110px; top:330px; width:860px; height:820px; background:var(--paper); color:#1b1b1b; border-radius:10px; padding:60px 64px; box-shadow:0 30px 80px rgba(0,0,0,.5); }
  #in-card .hd { font-family:'Space Mono',monospace; font-size:30px; letter-spacing:.12em; border-bottom:3px solid #1b1b1b; padding-bottom:18px; }
  #in-card .row { font-family:'Space Mono',monospace; font-size:30px; margin-top:34px; color:#555; }
  #in-card .val { font-family:'Oswald',sans-serif; font-size:66px; font-weight:600; color:#111; line-height:1.1; margin-top:6px; }
  #in-stamp { position:absolute; left:250px; top:1180px; font-family:'Oswald',sans-serif; font-size:64px; font-weight:700; color:var(--red); border:8px solid var(--red); padding:4px 26px; border-radius:8px; }
""", """
    <div id="in-wrap" class="clip" data-start="0" data-duration="12">
      <div id="in-card">
        <div class="hd">AKTE · MIETER · DIAMOND CENTRE</div>
        <div class="row">NAME</div><div class="val" id="in-name">Leonardo Notarbartolo</div>
        <div class="row">HERKUNFT</div><div class="val" id="in-her">Italien</div>
        <div class="row">TARNUNG</div><div class="val" id="in-tarn">„Diamantenhändler“</div>
        <div class="row">IM GEBÄUDE</div><div class="val" id="in-zeit">ca. 2 Jahre vor der Tat</div>
      </div>
      <div id="in-stamp">ZUGANG ZUM TRESOR</div>
    </div>
""", """
    tl.fromTo("#in-card", {y:120, rotation:-4, opacity:0}, {y:0, rotation:-1.5, opacity:1, duration:0.6, ease:"power3.out"}, 0);
    ["#in-zeit","#in-her","#in-name","#in-tarn"].forEach((s,i)=>{});
    tl.fromTo("#in-zeit", {opacity:0}, {opacity:1, duration:0.3}, 0.6);
    tl.fromTo("#in-her", {opacity:0}, {opacity:1, duration:0.3}, 2.2);
    tl.fromTo("#in-name", {opacity:0}, {opacity:1, duration:0.3}, 3.2);
    tl.fromTo("#in-tarn", {opacity:0}, {opacity:1, duration:0.3}, 5.2);
    tl.fromTo("#in-stamp", {scale:2.2, rotation:-14, opacity:0}, {scale:1, rotation:-9, opacity:1, duration:0.25, ease:"power4.in"}, 8.0);
    tl.fromTo("#in-card", {scale:1}, {scale:1.04, duration:10.8, ease:"none"}, 0.6);
    tl.to("#in-wrap > *", {opacity:0, duration:0.3}, 11.6);
""")
# 4 TAT 34-54 (20s)
S['tat'] = (20, """
  #ta-date { top:300px; font-size:44px; }
  #ta-date2 { top:370px; font-size:130px; font-weight:700; }
  #ta-spray { position:absolute; left:140px; width:800px; top:700px; text-align:center; }
  #ta-spray .big { font-size:96px; font-weight:700; }
  #ta-spray .note { font-family:'Space Mono',monospace; font-size:30px; color:var(--paper); opacity:.8; margin-top:20px; }
  #ta-grid { position:absolute; left:190px; top:330px; width:700px; display:grid; grid-template-columns:repeat(10, 1fr); gap:8px; }
  #ta-grid .bx { height:42px; border:3px solid rgba(237,230,214,.35); border-radius:4px; background:rgba(255,255,255,.04); }
  #ta-count { top:1130px; font-size:110px; font-weight:700; }
  #ta-count2 { top:1260px; font-size:38px; }
  #ta-loot { top:560px; font-size:200px; font-weight:700; line-height:1; }
  #ta-loot2 { top:800px; font-size:56px; font-weight:500; }
  #ta-loot3 { top:900px; font-size:32px; color:var(--paper); opacity:.75; }
""", """
    <div id="ta-a" class="clip" data-start="0" data-duration="13">
      <div id="ta-date" class="center lbl y">Wochenende</div>
      <div id="ta-date2" class="center">15./16.02.2003</div>
      <div id="ta-spray"><div class="big">Haarspray<br/><span class="y">gegen den Sensor?</span></div><div class="note">laut einem Buch über den Fall – nicht offiziell bestätigt</div></div>
    </div>
    <div id="ta-b" class="clip" data-start="13" data-duration="3.6">
      <div id="ta-grid"></div>
      <div id="ta-count" class="center"><span class="r" id="ta-n">0</span> / 160</div>
      <div id="ta-count2" class="center lbl">Schließfächer aufgebrochen</div>
    </div>
    <div id="ta-c" class="clip" data-start="16.6" data-duration="3.4">
      <div id="ta-loot" class="center y">&gt;100 Mio.</div>
      <div id="ta-loot2" class="center">US-Dollar Beute</div>
      <div id="ta-loot3" class="center lbl">Schätzung</div>
    </div>
""", """
    const grid = document.querySelector("#ta-grid");
    for (let i=0;i<160;i++){ const d=document.createElement("div"); d.className="bx"; d.id="ta-bx"+i; grid.appendChild(d); }
    const open = []; for (let i=0;i<160;i++){ if ((i*37)%160 < 123) open.push("#ta-bx"+i); }
    tl.fromTo("#ta-date", {opacity:0}, {opacity:1, duration:0.3}, 0);
    tl.fromTo("#ta-date2", {y:40, opacity:0}, {y:0, opacity:1, duration:0.45, ease:"power3.out"}, 0.1);
    tl.fromTo("#ta-spray", {y:40, opacity:0}, {y:0, opacity:1, duration:0.45, ease:"power3.out"}, 7.4);
    tl.fromTo("#ta-date2", {scale:1}, {scale:1.12, duration:12.5, ease:"none"}, 0.1);
    tl.fromTo("#ta-spray .big", {scale:0.96}, {scale:1.05, duration:5.2, ease:"none"}, 7.4);
    tl.to("#ta-a > *", {opacity:0, duration:0.25}, 12.7);
    tl.fromTo("#ta-grid", {opacity:0}, {opacity:1, duration:0.3}, 13.0);
    tl.fromTo("#ta-count, #ta-count2", {opacity:0}, {opacity:1, duration:0.3}, 13.1);
    open.forEach((s,k)=>{ tl.fromTo(s, {backgroundColor:"rgba(255,255,255,0.04)", borderColor:"rgba(237,230,214,0.35)"}, {backgroundColor:"#D2372E", borderColor:"#D2372E", duration:0.08}, 13.2 + k*(2.6/123)); });
    const cnt = {v:0};
    tl.fromTo(cnt, {v:0}, {v:123, duration:2.6, ease:"none", onUpdate:()=>{ document.querySelector("#ta-n").textContent = Math.round(cnt.v); }}, 13.2);
    tl.to("#ta-b > *", {opacity:0, duration:0.25}, 16.3);
    tl.fromTo("#ta-loot", {scale:1.3, opacity:0}, {scale:1, opacity:1, duration:0.4, ease:"power4.out"}, 16.7);
    tl.fromTo("#ta-loot2", {opacity:0}, {opacity:1, duration:0.3}, 17.0);
    tl.fromTo("#ta-loot3", {opacity:0}, {opacity:.75, duration:0.3}, 17.2);
    tl.to("#ta-c > *", {opacity:0, duration:0.25}, 19.7);
""")
# 5 MONTAG 54-58
S['montag'] = (4, """
  #mo-a { top:640px; font-size:52px; }
  #mo-b { top:720px; font-size:150px; font-weight:700; line-height:1.05; }
  #mo-c { top:1080px; font-size:60px; font-weight:500; }
""", """
    <div id="mo-a" class="center clip lbl y" data-start="0" data-duration="4">Montag, 17.02.2003</div>
    <div id="mo-b" class="center clip" data-start="0" data-duration="4">EINBRUCH<br/>ENTDECKT</div>
    <div id="mo-c" class="center clip r" data-start="1.8" data-duration="2.2">Die Täter: längst weg</div>
""", """
    tl.fromTo("#mo-a", {opacity:0}, {opacity:1, duration:0.3}, 0);
    tl.fromTo("#mo-b", {scale:1.15, opacity:0}, {scale:1, opacity:1, duration:0.35, ease:"power4.out"}, 0.1);
    tl.fromTo("#mo-c", {opacity:0, y:20}, {opacity:1, y:0, duration:0.3}, 1.8);
    tl.to(["#mo-a","#mo-b","#mo-c"], {opacity:0, duration:0.25}, 3.7);
""")
# 6 MUELL 58-76 (18s)
S['muell'] = (18, """
  #mu-road { position:absolute; left:0; top:560px; width:1080px; height:220px; background:#2a2d33; }
  #mu-line { position:absolute; left:0; top:662px; width:1080px; height:16px; background:repeating-linear-gradient(90deg, var(--paper) 0 80px, transparent 80px 160px); }
  #mu-sign { position:absolute; left:380px; top:340px; width:320px; height:150px; background:#1f7a3a; border:6px solid #fff; border-radius:14px; font-size:96px; font-weight:700; text-align:center; line-height:136px; }
  #mu-trees { position:absolute; left:0; top:820px; width:1080px; height:200px; }
  #mu-trees .t { position:absolute; bottom:0; width:0; height:0; border-left:60px solid transparent; border-right:60px solid transparent; border-bottom:180px solid #1d3b2a; }
  #mu-bag { position:absolute; left:470px; top:880px; width:140px; height:150px; background:#111; border-radius:40% 40% 30% 30%; border:4px solid #444; }
  #mu-cap1 { top:1100px; font-size:56px; font-weight:600; }
  #mu-cap2 { top:1190px; font-size:36px; color:var(--paper); }
  #mu-ev { position:absolute; left:140px; top:330px; width:800px; height:900px; }
  #mu-ev .tag { font-family:'Space Mono',monospace; font-size:34px; color:#111; background:var(--accent); display:inline-block; padding:8px 20px; letter-spacing:.1em; }
  #mu-ev .sw { font-size:260px; text-align:center; margin-top:30px; line-height:1.25; }
  #mu-ev .t1 { font-size:80px; font-weight:700; text-align:center; margin-top:50px; }
  #mu-dna { font-size:70px; font-weight:700; text-align:center; margin-top:40px; }
""", """
    <div id="mu-a" class="clip" data-start="0" data-duration="10">
      <div id="mu-road"></div><div id="mu-line"></div>
      <div id="mu-sign">E19</div>
      <div id="mu-trees"><div class="t" style="left:60px"></div><div class="t" style="left:200px;transform:scale(.8);transform-origin:bottom"></div><div class="t" style="left:720px"></div><div class="t" style="left:880px;transform:scale(.9);transform-origin:bottom"></div></div>
      <div id="mu-bag"></div>
      <div id="mu-cap1" class="center">Müll im Waldstück an der Autobahn</div>
      <div id="mu-cap2" class="center lbl">Der Grundbesitzer ruft die Polizei</div>
    </div>
    <div id="mu-b" class="clip" data-start="10" data-duration="8">
      <div id="mu-ev">
        <div style="text-align:center"><span class="tag" id="mu-tag">BEWEISSTÜCK</span></div>
        <div class="sw" id="mu-sw">🥪</div>
        <div class="t1" id="mu-t1">Halb gegessenes<br/><span class="y">Salami-Sandwich</span></div>
        <div id="mu-dna">DNA <span class="y">→</span> Notarbartolo</div>
      </div>
    </div>
""", """
    tl.fromTo("#mu-road, #mu-line", {opacity:0}, {opacity:1, duration:0.4}, 0);
    tl.fromTo("#mu-line", {x:0}, {x:-320, duration:10, ease:"none"}, 0);
    tl.fromTo("#mu-sign", {y:-40, opacity:0}, {y:0, opacity:1, duration:0.4, ease:"back.out(2)"}, 0.6);
    tl.fromTo("#mu-trees", {opacity:0}, {opacity:1, duration:0.5}, 1.2);
    tl.fromTo("#mu-bag", {y:-260, opacity:0}, {y:0, opacity:1, duration:0.5, ease:"bounce.out"}, 1.8);
    tl.fromTo("#mu-cap1", {y:30, opacity:0}, {y:0, opacity:1, duration:0.4}, 1.9);
    tl.fromTo("#mu-cap2", {opacity:0}, {opacity:1, duration:0.4}, 5.2);
    tl.to("#mu-a > *", {opacity:0, duration:0.25}, 9.7);
    tl.fromTo("#mu-tag", {opacity:0}, {opacity:1, duration:0.2}, 10.1);
    tl.fromTo("#mu-sw", {scale:0.3, rotation:-20, opacity:0}, {scale:1, rotation:0, opacity:1, duration:0.5, ease:"back.out(1.8)"}, 10.2);
    tl.fromTo("#mu-t1", {y:30, opacity:0}, {y:0, opacity:1, duration:0.4}, 10.8);
    tl.fromTo("#mu-dna", {scale:1.3, opacity:0}, {scale:1, opacity:1, duration:0.35, ease:"power4.out"}, 13.6);
    tl.to("#mu-sw", {rotation:8, scale:1.08, duration:6.8, ease:"none"}, 10.7);
    tl.to("#mu-ev", {opacity:0, duration:0.25}, 17.7);
""")
# 7 URTEIL 76-83 (7s)
S['urteil'] = (7, """
  #ur-y { top:380px; font-size:52px; }
  #ur-stamp { position:absolute; left:140px; top:500px; width:800px; text-align:center; border:14px solid var(--red); border-radius:16px; color:var(--red); padding:30px 0; }
  #ur-stamp .a { font-size:200px; font-weight:700; line-height:1; }
  #ur-stamp .b { font-size:70px; font-weight:600; }
  #ur-k { top:980px; font-size:56px; font-weight:500; }
""", """
    <div id="ur-y" class="center clip lbl" data-start="0" data-duration="7">Urteil · Belgien · 2005</div>
    <div id="ur-stamp" class="clip" data-start="0" data-duration="7"><div class="a">10 JAHRE</div><div class="b">HAFT · NOTARBARTOLO</div></div>
    <div id="ur-k" class="center clip" data-start="3.6" data-duration="3.4">3 Komplizen: je <span class="y">5 Jahre</span></div>
""", """
    tl.fromTo("#ur-y", {opacity:0}, {opacity:1, duration:0.3}, 0);
    tl.fromTo("#ur-stamp", {scale:2, rotation:-12, opacity:0}, {scale:1, rotation:-4, opacity:1, duration:0.25, ease:"power4.in"}, 1.4);
    tl.fromTo("#ur-k", {y:30, opacity:0}, {y:0, opacity:1, duration:0.35}, 3.6);
    tl.to(["#ur-y","#ur-stamp","#ur-k"], {opacity:0, duration:0.25}, 6.7);
""")
# 8 WEG 83-96 (13s)
S['weg'] = (13, """
  #wg-q { top:330px; font-size:80px; font-weight:600; }
  #wg-gem { position:absolute; left:390px; top:500px; width:300px; height:300px; }
  #wg-big { top:860px; font-size:120px; font-weight:700; line-height:1.05; }
  #wg-claim { position:absolute; left:110px; top:380px; width:860px; text-align:center; }
  #wg-claim .h { font-family:'Space Mono',monospace; font-size:34px; color:var(--accent); letter-spacing:.1em; }
  #wg-claim .c { font-size:66px; font-weight:600; margin-top:30px; line-height:1.15; }
  #wg-claim .no { font-size:84px; font-weight:700; color:var(--red); margin-top:70px; }
""", """
    <div id="wg-a" class="clip" data-start="0" data-duration="4.5">
      <div id="wg-q" class="center">Und die Diamanten?</div>
      <svg id="wg-gem" viewBox="0 0 100 100"><polygon points="20,35 35,15 65,15 80,35 50,90" fill="none" stroke="#F2C230" stroke-width="3.5"/><polyline points="20,35 80,35" fill="none" stroke="#F2C230" stroke-width="2.5"/><polyline points="35,15 42,35 50,90 58,35 65,15" fill="none" stroke="#F2C230" stroke-width="2"/></svg>
      <div id="wg-big" class="center r">BIS HEUTE<br/>VERSCHWUNDEN</div>
    </div>
    <div id="wg-b" class="clip" data-start="4.5" data-duration="8.5">
      <div id="wg-claim">
        <div class="h">NOTARBARTOLO BEHAUPTET SPÄTER</div>
        <div class="c" id="wg-c1">„Die Beute war viel kleiner …</div>
        <div class="c" id="wg-c2">… alles Versicherungsbetrug.“</div>
        <div class="no" id="wg-no">BEWEISE: KEINE</div>
      </div>
    </div>
""", """
    tl.fromTo("#wg-q", {opacity:0, y:30}, {opacity:1, y:0, duration:0.35}, 0);
    tl.fromTo("#wg-gem", {scale:0.5, opacity:0}, {scale:1, opacity:1, duration:0.5, ease:"back.out(2)"}, 0.3);
    tl.to("#wg-gem", {opacity:0.12, scale:0.9, duration:1.2, ease:"power2.in"}, 1.8);
    tl.fromTo("#wg-big", {scale:1.2, opacity:0}, {scale:1, opacity:1, duration:0.35, ease:"power4.out"}, 1.9);
    tl.to("#wg-a > *", {opacity:0, duration:0.25}, 4.2);
    tl.fromTo("#wg-claim .h", {opacity:0}, {opacity:1, duration:0.3}, 4.6);
    tl.fromTo("#wg-c1", {opacity:0, y:20}, {opacity:1, y:0, duration:0.35}, 6.0);
    tl.fromTo("#wg-c2", {opacity:0, y:20}, {opacity:1, y:0, duration:0.35}, 8.6);
    tl.fromTo("#wg-no", {scale:1.4, opacity:0}, {scale:1, opacity:1, duration:0.25, ease:"power4.in"}, 10.9);
    tl.to("#wg-claim", {opacity:0, duration:0.25}, 12.7);
""")
# 9 CTA 96-101 (5s)
S['cta'] = (5, """
  #ct-q { top:520px; font-size:120px; font-weight:700; line-height:1.05; }
  #ct-s { top:860px; font-size:56px; font-weight:500; }
  #ct-arrow { top:980px; font-size:120px; }
""", """
    <div id="ct-q" class="center clip" data-start="0" data-duration="5">Wo sind die<br/><span class="y">Diamanten?</span></div>
    <div id="ct-s" class="center clip" data-start="0.8" data-duration="4.2">Schreib deine Theorie in die Kommentare</div>
    <div id="ct-arrow" class="center clip y" data-start="1.2" data-duration="3.8">↓</div>
""", """
    tl.fromTo("#ct-q", {scale:1.15, opacity:0}, {scale:1, opacity:1, duration:0.4, ease:"power4.out"}, 0);
    tl.fromTo("#ct-s", {opacity:0, y:20}, {opacity:1, y:0, duration:0.35}, 0.8);
    tl.fromTo("#ct-arrow", {y:-20, opacity:0}, {y:20, opacity:1, duration:0.6, ease:"sine.inOut"}, 1.2);
    tl.to("#ct-arrow", {y:-10, duration:0.6, ease:"sine.inOut"}, 1.8);
    tl.to("#ct-arrow", {y:20, duration:0.6, ease:"sine.inOut"}, 2.4);
    tl.to("#ct-arrow", {y:-10, duration:0.6, ease:"sine.inOut"}, 3.0);
    tl.to("#ct-arrow", {y:20, duration:0.6, ease:"sine.inOut"}, 3.6);
""")
order = ['hook','ort','insider','tat','montag','muell','urteil','weg','cta']
t=0; hosts=[]; starts={}
for k in order:
    dur, css, body, js = S[k]
    open(f'compositions/{k}.html','w').write(scene(k,dur,css,body,js))
    starts[k]=t
    hosts.append(f'      <div id="{k}" data-composition-id="{k}" data-composition-src="compositions/{k}.html" data-start="{t}" data-duration="{dur}" data-track-index="2" data-track-kind="graphics" data-width="1080" data-height="1920" style="z-index:3"></div>')
    t+=dur
TOTAL=t
json.dump(starts, open('/tmp/claude-0/-home-user-Krimi/7a15b2cd-dc23-507b-b7db-eaab6060e39f/scratchpad/starts.json','w'))
sfx = [ # (file, time, vol)
 ('impact-bass-1',0.0,0.8),('whoosh-short',4.2,0.5),
 ('whoosh-cinematic',8.0,0.5),('click',16.2,0.4),('click',16.95,0.4),('click',17.7,0.4),('click',18.45,0.4),('click',19.2,0.4),
 ('whoosh',22.0,0.4),('typing',22.6,0.35),('impact-bass-2',30.0,0.7),
 ('whoosh-cinematic',34.0,0.5),('riser',43.0,0.4),('glitch-1',47.1,0.4),('impact-bass-1',50.7,0.8),
 ('impact-bass-2',54.1,0.7),('whoosh',58.0,0.4),('pop',69.2,0.5),('ping',71.6,0.5),
 ('impact-bass-1',77.4,0.9),('whoosh-short',83.0,0.4),('impact-bass-2',84.9,0.6),('impact-bass-1',93.9,0.8),('chime',96.8,0.4),
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
      <div id="case" class="clip" data-start="0" data-duration="{TOTAL}" data-track-index="4">FALL 001 · ANTWERPEN · 2003</div>
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
print("total", TOTAL)
