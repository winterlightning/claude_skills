"""Read-only inventory of sub references and actual linked/exported SVGs."""
import json,re,base64,hashlib,xml.etree.ElementTree as ET
from pathlib import Path
from collections import Counter,defaultdict
ROOT=Path(__file__).resolve().parents[3];G=ROOT/'icon_set/dist/gallery';OUT=Path(__file__).parent
catalog=json.loads((G/'combinations.json').read_text());refs=catalog['references'];exports=json.loads((ROOT/'icon_set/data/combination-sub32.json').read_text());usage=defaultdict(Counter)
for r in catalog['rows']:usage[r['sub_id']][r['kind']]+=1
pairs=json.loads((ROOT/'icon_set/data/combination-pairs.json').read_text())['rows'];selected=Counter(s['family']+'/'+s['icon'] for row in pairs for s in row.get('subs',[]))
# Include state-study assets chosen by the pair builder, even when absent from gallery links.
for pair in pairs:
 uid=pair['sub_id']
 if uid not in refs:continue
 for sub in pair.get('subs',[]):
  key=sub['family']+'/'+sub['icon']
  if not any(g['key']==key for g in refs[uid]['generated']):
   import os
   refs[uid]['generated'].append({'key':key,'icon_id':sub['icon'],'preview_url':os.path.relpath(ROOT/sub.get('source_svg',sub['svg']),G),'pair_only':True})
meta={r['key']:r for r in json.loads((G/'icons.json').read_text())['icons']};assets={};rows=[]
def metric(path,family,stale=False):
 doc=path.read_text();root=ET.fromstring(doc);vb=list(map(float,root.get('viewBox','0 0 32 32').replace(',',' ').split()));num=lambda s:float(re.search(r'[\d.]+',s).group())
 w=num(root.get('width',str(vb[2])));h=num(root.get('height',str(vb[3])));scale=min(w/vb[2],h/vb[3]);strokes=set()
 def walk(el,sw=None,ss=1):
  sw=el.get('stroke-width',sw);t=el.get('transform','');m=re.search(r'scale\(([^)]+)\)',t)
  if m:ss*=float(m.group(1).replace(',',' ').split()[0])
  if el.tag.split('}')[-1] in ('path','line','circle','ellipse','polyline','polygon','rect') and sw is not None:
   try:strokes.add(round(float(sw)*ss*scale,3))
   except ValueError:pass
  for child in el:walk(child,sw,ss)
 walk(root)
 status='text' if family=='text' else 'native' if family=='sub' and w==32 and h==32 and strokes=={4.0} else 'thin' if w==32 and h==32 and strokes and min(strokes)<3.99 else 'resized' if w==32 and h==32 else 'unconverted'
 if stale:status='stale'
 ink=None
 if True:
  import io
  from svgpathtools import Document
  boxes=[p.bbox() for p in Document(io.StringIO(doc)).paths() if len(p)]
  if boxes:
   ink=[(max(b[1] for b in boxes)-min(b[0] for b in boxes))*scale+(max(strokes) if strokes else 0),(max(b[3] for b in boxes)-min(b[2] for b in boxes))*scale+(max(strokes) if strokes else 0)]
   if family!='text' and w==32 and h==32 and strokes=={4.0} and abs(max(ink)-32)<1e-6 and not stale:status='ink32'
 # Render at actual size; never squeeze artwork into the guide.
 return dict(width=w,height=h,viewbox=vb,stroke=sorted(strokes),ink=ink,status=status,uri='data:image/svg+xml;base64,'+base64.b64encode(doc.encode()).decode(),path=str(path.relative_to(ROOT)))
for uid,count in usage.items():
 ref=refs[uid];choices=[]
 for g in ref['generated']:
  key=g['key'];a=assets.get(key)
  if a is None:
   path=(G/g['preview_url']).resolve();exp=exports.get(g['icon_id']);family=key.split('/')[0];sourcepath=path;kind='Selected state artwork' if g.get('pair_only') else 'Original linked artwork';stale=False
   if exp and (ROOT/exp['svg']).exists():
    path=ROOT/exp['svg'];kind='32-unit ink reuse export';sp=ROOT/exp['source_svg'];stale=sp.exists() and hashlib.sha256(sp.read_bytes()).hexdigest()!=exp.get('source_sha256')
   try:a=metric(path,family,stale)
   except (OSError,ValueError,ET.ParseError) as e:a={'status':'missing_file','error':str(e),'width':0,'height':0,'stroke':[],'viewbox':[],'uri':''}
   try:
    source=metric(sourcepath,family)
   except (OSError,ValueError,ET.ParseError):source=None
   a['generated']=source
   a['sizing_kind']=exp.get('sizing_kind',family) if exp else family
   a['grid']=exp.get('ink32',{}).get('grid') if exp else None
   a.update(key=key,name=meta.get(key,{}).get('name') or g['icon_id'],family=family,kind=kind,selected=selected[key],source_path=str(sourcepath.relative_to(ROOT)),uses={'side':0,'container':0})
   assets[key]=a
  choices.append(key)
  for k,v in count.items():a['uses'][k]+=v
 rows.append(dict(id=uid,name=ref['concept'],uses=dict(count),assets=choices,original='data:image/svg+xml;base64,'+base64.b64encode((G/ref['reference_url']).read_bytes()).decode() if ref.get('reference_url') and (G/ref['reference_url']).exists() else ''))
rows.sort(key=lambda r:r['name'].lower());data={'rows':rows,'assets':assets,'stats':dict(Counter(a['status'] for a in assets.values()))}
(OUT/'inventory.json').write_text(json.dumps(data,separators=(',',':')))
template=(OUT/'template.html').read_text();page=template.replace('__DATA__',json.dumps(data,separators=(',',':')).replace('</','<\\/'))
(OUT/'index.html').write_text(page);(G/'sub-icon-review.html').write_text(page)
print(json.dumps({'references':len(rows),'side_references':sum(bool(r['uses'].get('side')) for r in rows),'artworks':len(assets),'status':data['stats']},indent=2))
