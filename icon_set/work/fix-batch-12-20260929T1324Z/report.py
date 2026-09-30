from pathlib import Path
import json,hashlib
from PIL import Image,ImageDraw
ROOT=Path(__file__).parent
AUTHOR='gpt-6'
SOURCE_ICON_ID=None
SOURCE_PATH=None
rs=json.loads((ROOT/'runs.json').read_text())
assert len(rs)==20 and len({r['icon_id'] for r in rs})==20
lines=['# Once-disapproved solo fix batch 12','', '20 of 20 completed, uploaded and reported done; returned to Ready. Worker: thuan-mac. Author: gpt-6. Offset: 0; max-disapprovals: 1.','', 'Claims used the production disapproval-history filter. The final six candidates also have a saved eligibility audit in remaining-eligibility.json. Icons with unreadable histories were not claimed. No written reviewer feedback was attached to these claims.','', 'Every original and rejected drawing was inspected before authoring. For the three uploads with no separate original, the rejected drawing supplied the reference. All final modules are valid, with zero model or build-gate warnings, and were inspected at 48 px and enlarged in both themes.','']
summary=[]
def link(label,p):return f'[{label}]({Path(p).resolve()})'
for n,r in enumerate(rs,1):
 p=Path(r['run']);fix=Path(r['claim']);result=json.loads((p/'result.json').read_text());f=json.loads((fix/'result.json').read_text())
 assert f['outcome']=='done' and f['review_status']=='ready' and f['reported']['state']=='done'
 assert f['author']=='gpt-6' and f['validation_status']=='valid' and not f['validation_errors'] and not f['validation_warnings']
 assert f['build_gate']['status']=='pass' and not f['build_gate']['errors'] and not f['build_gate']['warnings']
 svg=p/(r['icon_id']+'.svg');after=fix/'after'/svg.name
 assert svg.read_bytes()==after.read_bytes()
 assert (p/result['module']).read_bytes()==(fix/'after'/result['module']).read_bytes()
 summary.append({'icon':'solo/'+r['icon_id'],'outcome':'done','review_status':'ready','author':f['author'],'validation':'valid','warnings':0,'build_gate':'pass','run':str(p),'fix':str(fix),'svg_sha256':hashlib.sha256(svg.read_bytes()).hexdigest()})
 lines += [f'## {n}. solo/{r["icon_id"]}','',r['comparison'],'', '**Changed:** '+r['change'],'', '**Construction and omissions:** '+result['omissions_and_references'],'', '**Result:** AUTHOR gpt-6; model valid; build gate pass; zero warnings; production done / Ready.','',link('RESULT_DIR',p)+' · '+link('SVG',svg)+' · '+link('Validation',p/'validation.txt')+' · '+link('Production receipt',fix/'result.json'),'']
(ROOT/'report.md').write_text('\n'.join(lines));(ROOT/'summary.json').write_text(json.dumps(summary,indent=2))
sheet=Image.new('RGB',(1000,800),'white');d=ImageDraw.Draw(sheet)
for i,r in enumerate(rs):
 x=(i%5)*200;y=(i//5)*200;p=Path(r['run'])
 sheet.paste(Image.open(p/'preview-light-384.png').resize((112,112)),(x+44,y+8));sheet.paste(Image.open(p/'preview-dark-48.png'),(x+76,y+126))
 label=r['icon_id'];parts=[]
 while len(label)>26:parts.append(label[:26]);label=label[26:]
 parts.append(label);d.text((x+4,y+176),'\n'.join(parts[:2]),fill='black')
sheet.save(ROOT/'completed-previews.png');print('Verified all20 done/Ready, byte-identical SVGs and modules; report:',ROOT/'report.md')
