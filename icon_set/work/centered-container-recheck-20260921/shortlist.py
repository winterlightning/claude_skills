import collections,io,json,math,re,textwrap
from pathlib import Path
import cairosvg
from PIL import Image,ImageDraw
P=Path(__file__).resolve().parent;ROOT=P.parents[2]
previous=P.parent/'container-classification-rest-20260921'
rows=json.loads((previous/'review.json').read_text())['rows']
sources={n+1:r for n,r in enumerate(json.loads((previous/'scope.json').read_text()))}
dec=json.loads((P/'decisions.json').read_text())
selected=[r for r in rows if r['route']=='solo' or str(r['number']) in dec['solo']]
catalog=ROOT/'icon_set/.local/combined-dist/gallery/icons.json';icons=json.loads(catalog.read_text())['icons']
stop=set('a an the with and of in inside icon symbol simple empty blank shape geometric standalone solo container frame batch device'.split())
syn={'notepad':'notebook','notepads':'notebook','files':'document','file':'document','documents':'document','paper':'document','watch':'smartwatch','smart':'','television':'tv','monitor':'screen','display':'screen','chat':'speech','bubbles':'bubble','frames':'frame','card':'card','cards':'card','panels':'panel','columns':'column','squares':'square','rows':'row','three':'3','two':'2','four':'4','nine':'9','six':'6','handheld':'handheld','mobile':'phone','smartphone':'phone','cellphone':'phone','windscreen':'windshield'}
def tokens(s):
    return {syn.get(w,w) for w in re.findall('[a-z]+',s.lower()) if w not in stop and len(w)>1 and syn.get(w,w)}
index=[];df=collections.Counter()
for x in icons:
    if x['family'] not in ('solo','container'):continue
    ts=tokens(x['name']+' '+x['icon_id']+' '+' '.join(x.get('aliases',[])))
    raw=json.dumps(x.get('original_sources',[]))+' '+json.dumps(x.get('python_source',{}))+' '+x['icon_id']
    uuids=set(re.findall(r'[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}',raw))
    old=set()
    for ref in x.get('original_sources',[]):
        old|=tokens(re.sub(r'_[0-9a-f]{8}.*','',Path(ref.get('source_path','')).stem))
    path=(catalog.parent/x['preview_url']).resolve()
    if not path.is_file():continue
    index.append((x,ts,old,uuids,path));df.update(ts)
idf={t:math.log((len(index)+1)/(v+1)) for t,v in df.items()}
def sim(q,ts):
    return 2*sum(idf.get(t,5) for t in q&ts)/(sum(idf.get(t,5) for t in q)+sum(idf.get(t,5) for t in ts) or 1)
out=[]
for r in selected:
    n=r['number'];s=sources[n];q=tokens(r['name']);qo=tokens(s['old_concept']);rank=[]
    for x,ts,old,uuids,path in index:
        direct=s['uuid'] in uuids or x['icon_id'] in s.get('models',[])
        score=max(sim(q,ts),sim(qo,old)*.94 if old else 0,sim(qo,ts)*.90)
        score+=.035 if x['family']=='solo' else 0
        if direct:score+=10
        rank.append((score,x,path,direct))
    rank.sort(key=lambda v:-v[0]);candidates=[];seen=set()
    for score,x,path,direct in rank:
        # Avoid filling the shortlist with versions of the same drawing.
        fingerprint=x.get('svg_sha256') or x['icon_id']
        if fingerprint in seen:continue
        seen.add(fingerprint)
        candidates.append(dict(icon_id=x['icon_id'],name=x['name'],family=x['family'],path=str(path),validation=x.get('validation',{}).get('status'),score=round(score,3),source_linked=direct))
        if len(candidates)==5:break
    out.append(dict(number=n,name=r['name'],uuid=r['uuid'],reference_path=r['reference_path'],old_concept=s['old_concept'],previous_route=r['route'],candidates=candidates))
(P/'shortlist.json').write_text(json.dumps(out,indent=2))
cache=P/'candidate-previews';cache.mkdir(exist_ok=True)
sheets=P/'match-sheets';sheets.mkdir(exist_ok=True)
for start in range(0,len(out),10):
    subset=out[start:start+10];sheet=Image.new('RGB',(1200,5*255),'white');draw=ImageDraw.Draw(sheet)
    for i,r in enumerate(subset):
        ox=(i%2)*600;oy=(i//2)*255
        ims=[Image.open(previous/f"previews/{r['number']:03}.png").convert('RGBA').resize((170,170))]
        for c in r['candidates'][:2]:
            cp=cache/(c['icon_id']+'.png')
            if not cp.exists():cairosvg.svg2png(url=c['path'],write_to=str(cp),output_width=170,output_height=170,background_color='white')
            ims.append(Image.open(cp).convert('RGBA'))
        for j,im in enumerate(ims):sheet.paste(im,(ox+j*195,oy+28),im)
        draw.text((ox+6,oy+5),str(r['number'])+' '+r['name'][:63],fill='black')
        draw.text((ox+6,oy+203),'ORIGINAL',fill='black')
        for j,c in enumerate(r['candidates'][:2],1):draw.multiline_text((ox+j*195,oy+203),str(j)+' '+ '\n'.join(textwrap.wrap(c['icon_id'],27)[:3]),fill='black')
    sheet.save(sheets/f'{start//10+1:02}.png')
    print('sheet',start//10+1,flush=True)
print('Solo sources',len(out),'source-linked',sum(any(c['source_linked'] for c in r['candidates']) for r in out))
