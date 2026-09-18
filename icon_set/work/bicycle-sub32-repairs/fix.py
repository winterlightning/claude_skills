import json,hashlib,shutil,io,xml.etree.ElementTree as ET
from pathlib import Path
from svgpathtools import Document
D=Path('icon_set/work/bicycle-sub32-repairs');mf=Path('icon_set/data/combination-sub32.json');manifest=json.loads(mf.read_text());rp=Path('icon_set/data/sub-icon-repairs.json');repairs=json.loads(rp.read_text()) if rp.exists() else {};updated={}
for icon in ['bicycle-reference-165-solo','bicycle-reference-184-solo','bicycle-reference-25-solo','bicycle-angled-handlebar']:
 rec=manifest[icon];key='solo/'+icon;old=Path(rec['svg']);backup=D/'before'/old.name
 if not backup.exists():shutil.copy2(old,backup)
 angled=icon=='bicycle-angled-handlebar';radius=5;cy=22 if angled else 25;centers=[7,25]
 root=ET.Element('svg',xmlns='http://www.w3.org/2000/svg',width='32',height='32',viewBox='0 0 32 32',fill='none',stroke='currentColor',**{'stroke-width':'4','stroke-linecap':'round','stroke-linejoin':'round'})
 ET.SubElement(root,'title').text=icon
 for name,cx in zip(['rear-wheel','front-wheel'],centers):ET.SubElement(root,'circle',id=name,cx=str(cx),cy=str(cy),r=str(radius))
 paths= {'frame':'M7 17L13 10L20 10L25 17','seat':'M5 5H10L13 10','bar':'M20 10V7L24 5'} if angled else {'frame':'M11 8H21L16 18Z','rear-fork':'M11 8L7 20','front-fork':'M21 8L25 20','seat-post':'M11 2V8','seat':'M8 2H14','handlebar':'M21 8L20 2H25'}
 for name,d in paths.items():ET.SubElement(root,'path',id=name,d=d)
 doc=ET.tostring(root,encoding='unicode');file=Path('icon_set/assets/sub32-repairs')/(icon+'.svg');file.write_text(doc+'\n');doc=file.read_text()
 boxes=[p.bbox() for p in Document(io.StringIO(doc)).paths()];l=min(b[0] for b in boxes);r=max(b[1] for b in boxes);t=min(b[2] for b in boxes);b=max(b[3] for b in boxes)
 metrics=dict(ink_bounds=[l-2,t-2,r+2,b+2],ink_width=r-l+4,ink_height=b-t+4,stroke=4,canvas=32,canvas_width=32,bounds=[l,t,r,b],grid=1)
 repair=dict(repair_svg=str(file),ink32=metrics,symbol=True,text='',source_sha256=rec['source_sha256'],reason='Shared integer circle centers and radii; fork endpoints on wheel tops.')
 repairs[key]=repair;rec.update(ink32=metrics,repair_svg=str(file),sizing_kind='symbol');old.write_text(doc);Path('icon_set/dist/gallery',rec['export_url']).write_text(doc);updated[key]=(rec,doc)
 # Exact geometry constraints, beyond an integer-coordinate check.
 assert l>=2 and r<=30 and t>=2 and b<=30 and max(r-l,b-t)==28
 for cx in centers:
  assert cx-radius>=2 and cx+radius<=30
 assert paths['frame'] if angled else all(f'L{cx} {cy-radius}' in paths[fork] for cx,fork in zip(centers,['rear-fork','front-fork']))
rp.write_text(json.dumps(repairs,indent=2)+'\n');mf.write_text(json.dumps(manifest,indent=2)+'\n')
p=Path('icon_set/data/combination-pairs.json');data=json.loads(p.read_text())
for row in data['rows']:
 for item in row['subs']:
  key=item['family']+'/'+item['icon']
  if key in updated:
   rec,doc=updated[key];item.update(rec,document=doc,sha256=hashlib.sha256(doc.encode()).hexdigest(),bounds=rec['ink32']['bounds'],canvas=32,export_size=32)
p.write_text(json.dumps(data));Path('icon_set/dist/gallery/experiment-combination.json').write_text(json.dumps(data))
p=Path('icon_set/dist/gallery/combinations.json');data=json.loads(p.read_text())
for row in data['rows']:
 for i,rec in enumerate(row.get('sub_exports',[])):
  if 'solo/'+rec['icon'] in updated:row['sub_exports'][i]=updated['solo/'+rec['icon']][0]
p.write_text(json.dumps(data,separators=(',',':'))+'\n')
print('Repaired four bicycle exports; source SOLO48 artwork preserved.')
