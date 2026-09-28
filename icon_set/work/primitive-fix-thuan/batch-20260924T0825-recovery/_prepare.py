from pathlib import Path
import json,re,sys,cairosvg
from PIL import Image,ImageDraw
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts.primitive_fix import reference_name
ROOT=Path(__file__).parent
claims=sorted(json.loads((ROOT/'claim-receipts.json').read_text()),key=lambda c:c['work']['claimed_at'])
rows=[]
for i,c in enumerate(claims):
 item=c['item'];key=item['key'];ident=item['icon_id'];fix=Path('icon_set/work/primitive-fix-thuan')/key.replace('/','__')/'20260924T083118Z-thuan-mac'
 ref=fix/'reference'/reference_name(item);uid=re.search(r'[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}$',ref.stem).group();concept=ref.stem[:-37]
 out=Path('icon_set/work/primitive-make-ray')/uid/'20260924T0832-thuan-mac-stroke'
 row={'key':key,'icon_id':ident,'fix':str(fix),'ref':str(ref),'before':str(fix/'before'/(ident+'.svg')),'concept':concept,'source_uuid':uid,'reference_path':str(ref),'run':str(out),'author':'gpt-6','feedback':item.get('feedback'),'module':str(out/(re.sub(r'[^a-z0-9_]+','_',concept.lower())+'_'+uid.replace('-','_')+'.py'))}
 rows.append(row)
 if not ref.exists():continue
 out.mkdir(parents=True,exist_ok=True)
 (out/(ident+'.metadata.json')).write_text(json.dumps({k:row[k] for k in ('concept','source_uuid','reference_path','icon_id','author')},indent=2))
 for kind,src in [('ref',ref),('before',Path(row['before']))]:
  if src.exists():cairosvg.svg2png(url=str(src),write_to=str(ROOT/f'{i}-{kind}.png'),output_width=144,output_height=144,background_color='white')
(ROOT/'inputs.json').write_text(json.dumps(rows,indent=2))
for batch in range(4):
 im=Image.new('RGB',(760,950),'#eee');d=ImageDraw.Draw(im)
 for k,row in enumerate(rows[batch*5:batch*5+5]):
  i=batch*5+k;d.text((5,k*190+3),str(i)+': '+row['key'],fill='black')
  for j,kind in enumerate(('ref','before')):
   path=ROOT/f'{i}-{kind}.png'
   if path.exists():im.paste(Image.open(path),(25+j*260,k*190+30))
 im.save(ROOT/f'sheet-{batch}.png')
print('Rendered',sum(Path(r['ref']).exists() for r in rows),'of',len(rows))
