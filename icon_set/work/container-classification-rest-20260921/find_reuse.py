"""Shortlist existing artwork; semantic candidates are not approved matches."""
import collections, json, math, re
from pathlib import Path
P=Path(__file__).resolve().parent
ROOT=P.parents[2]
rows=json.loads((P/'scope.json').read_text())
dec=json.loads((P/'visual-decisions.json').read_text())
catalog=ROOT/'icon_set/.local/combined-dist/gallery/icons.json'
icons=json.loads(catalog.read_text())['icons']
stop=set('a an the with and of in inside icon symbol simple empty blank shape device geometric standalone solo container frame batch'.split())
def tokens(s):
    return {w for w in re.findall('[a-z]+',s.lower()) if w not in stop and len(w)>1}
index=[];df=collections.Counter()
for x in icons:
    if x['family'] not in ('solo','container'):continue
    ts=tokens(x['name']+' '+x['icon_id']+' '+' '.join(x.get('aliases',[])))
    uuids=set(re.findall(r'[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}',json.dumps(x.get('original_sources',[]))+' '+json.dumps(x.get('python_source',{}))+' '+x['icon_id']))
    index.append((x,ts,uuids));df.update(ts)
idf={t:math.log((len(index)+1)/(v+1)) for t,v in df.items()}
result=[]
for n,r in enumerate(rows,1):
    route='container' if r['decision'].get('sub_brief') else 'solo'
    for k in ['solo','container','side','text']:
        if str(n) in dec[k+'_overrides']:route=k
    if route!='solo':continue
    q=tokens(r['concept']); ranked=[]
    for x,ts,uuids in index:
        direct=r['uuid'] in uuids or x['icon_id'] in r.get('models',[])
        overlap=sum(idf.get(t,1) for t in q&ts)
        if not direct and not overlap:continue
        score=2*overlap/(sum(idf.get(t,1) for t in q)+sum(idf.get(t,1) for t in ts))
        score+=0.06 if x['family']=='solo' else 0
        score+=10 if direct else 0
        path=(catalog.parent/x['preview_url']).resolve()
        if not path.is_file():continue
        ranked.append((score,{'icon_id':x['icon_id'],'name':x['name'],'family':x['family'],'svg_path':str(path),'source_linked':direct,'validation':x.get('validation',{}).get('status'),'score':round(score,3),'match_status':'candidate_only'}))
    ranked.sort(key=lambda v:-v[0])
    result.append({'number':n,'uuid':r['uuid'],'name':r['concept'],'candidates':[v[1] for v in ranked[:3]],'new_generation_allowed':False})
(P/'reuse-shortlist.json').write_text(json.dumps(result,indent=2))
print('Solo sources',len(result),'source-linked',sum(any(c['source_linked'] for c in x['candidates']) for x in result),'shortlists',sum(bool(x['candidates']) for x in result))
for x in result:
    c=x['candidates'][0] if x['candidates'] else {}
    print(x['number'],x['name'],'=>',c.get('icon_id'),c.get('family'),'SOURCE' if c.get('source_linked') else '')
