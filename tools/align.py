import re, json, subprocess, sys
audio=sys.argv[1]; text=open(sys.argv[2]).read()
text=re.sub(r'<break[^>]*/>',' ',text)
out=subprocess.run(["ffmpeg","-i",audio,"-af","silencedetect=noise=-35dB:d=0.25","-f","null","-"],capture_output=True,text=True).stderr
dur=float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",audio],capture_output=True,text=True).stdout)
ss=[float(x) for x in re.findall(r'silence_start: ([\d.]+)',out)]; se=[float(x) for x in re.findall(r'silence_end: ([\d.]+)',out)]
sil=[]
if se and (not ss or se[0]<ss[0]): sil.append((0.0,se[0])); se=se[1:]
for a,b in zip(ss,se+[dur]): sil.append((a,b))
segs=[]; prev=0.0
for a,b in sil:
    if a-prev>0.05: segs.append((prev,a))
    prev=b
if dur-prev>0.05: segs.append((prev,dur))
# units: split at sentence/clause punctuation followed by space
parts=re.split(r'(?<=[.?!:,–])\s+|\s+(?=\.\.\.)|(?<=\.\.\.)\s+',' '.join(text.split()))
units=[p.strip() for p in parts if p.strip() and p.strip()!='...']
def syl(w): return max(1,len(re.findall(r'[aeiouäöüy]+',w.lower())))
U=[sum(syl(w) for w in u.split()) for u in units]
total_speech=sum(b-a for a,b in segs); rate=total_speech/sum(U)
# DP: assign units to segments in order; each segment holds >=1 unit, or a unit spans several segments.
# Simplify: boundaries of segments must coincide with unit boundaries (pauses happen at punctuation) -> group consecutive units per segment, but allow a segment to hold zero-boundary? use DP over (i units, j segs)
import math
n,m=len(U),len(segs); INF=1e18
dp=[[INF]*(m+1) for _ in range(n+1)]; bk=[[None]*(m+1) for _ in range(n+1)]
dp[0][0]=0
for i in range(n+1):
    for j in range(m+1):
        if dp[i][j]>=INF: continue
        # group units i..k-1 into segments j..l-1 (one of k-i or l-j must be 1)
        for k in range(i+1,min(n,i+6)+1):
            for l in range(j+1,min(m,j+4)+1):
                if k-i>1 and l-j>1: continue
                pred=sum(U[i:k])*rate; act=sum(b-a for a,b in segs[j:l])
                c=dp[i][j]+(pred-act)**2/ max(act,0.5) + (0.3 if l-j>1 else 0)
                if c<dp[k][l]: dp[k][l]=c; bk[k][l]=(i,j)
i,j=n,m; groups=[]
while (i,j)!=(0,0):
    pi,pj=bk[i][j]; groups.append((pi,i,pj,j)); i,j=pi,pj
groups.reverse()
words=[]; unit_times=[]
for (a,b,c,d) in groups:
    t0=segs[c][0]; t1=segs[d-1][1]
    ws=[]; 
    for u in units[a:b]: ws+= [(w,u) for w in u.split()]
    # time inside merged segments: map syllable cursor over speech time of segs c..d-1
    spans=segs[c:d]; sp=sum(y-x for x,y in spans)
    tot=sum(syl(w) for w,_ in ws); cur=0
    def at(frac):
        tt=frac*sp
        for x,y in spans:
            if tt<=y-x+1e-9: return x+tt
            tt-=y-x
        return spans[-1][1]
    ustart={}
    for w,u in ws:
        s=at(cur/tot); cur+=syl(w); e=at(cur/tot)
        words.append({"text":w,"start":round(s,3),"end":round(e,3)})
        ustart.setdefault(u,round(s,3))
    for u in units[a:b]: unit_times.append((ustart[u],u))
    print(f"{t0:6.2f}-{t1:6.2f} | pred {sum(U[a:b])*rate:5.2f} act {sum(y-x for x,y in spans):5.2f} | {' / '.join(units[a:b])}")
json.dump({"words":words,"units":unit_times},open(sys.argv[3],'w'),ensure_ascii=False,indent=0)
