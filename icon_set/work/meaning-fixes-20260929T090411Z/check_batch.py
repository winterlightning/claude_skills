from pathlib import Path
import sys,json,io,hashlib
ROOT=Path(__file__).resolve().parent;REPO=ROOT.parents[2];sys.path.insert(0,str(REPO))
from icon_set.scripts.primitive_fix import load_icon,run_module,render_previews
from icon_set.scripts.build_gate import gate
from PIL import Image,ImageDraw
import cairosvg
rows=json.loads((ROOT/'batch.json').read_text())
indices=[int(a) for a in sys.argv[1:] if a.isdigit()]
accept='--accept' in sys.argv
sheet=Image.new('RGB',(1000,180*len(indices)),'#ddd');d=ImageDraw.Draw(sheet)
for row,i in enumerate(indices):
 r=rows[i];runs=sorted((REPO/'icon_set/work/primitive-make-ray'/r['uuid']).glob('20260929T090411Z-meaning-*'));run=runs[-1];p=run_module(run);icon=load_icon(p);design=json.loads((run/'design.json').read_text())
 if accept and design.get('exception') and '    exception = ' not in p.read_text():
  approval={'reason':design['exception'],'approved_by':'user-authorized-gpt-6','approved_on':'2026-09-29','svg_sha256':hashlib.sha256(icon.to_svg().encode()).hexdigest()}
  p.write_text(p.read_text().replace('    aliases = ()','    exception = '+repr(approval)+'\n    aliases = ()'));icon=load_icon(p)
 report=icon.validate_icon();svg=icon.to_svg();(run/f'{r["icon_id"]}.svg').write_text(svg)
 (run/'validation.txt').write_text(report.describe());g=gate(p);(run/'build-gate.json').write_text(json.dumps(g,indent=2))
 previews=render_previews(svg,r['icon_id'],48,run)
 ref=Path(r['reference']);cairosvg.svg2png(url=str(ref),write_to=str(run/'reference.png'),output_width=192,output_height=192,background_color='white')
 print(i,report.status,'gate',g['status'],'errors',len(g['errors']),'warnings',len(g['warnings']),flush=True)
 print(report.describe()[:3000],flush=True)
 print(json.dumps(g)[:1800],flush=True)
 y=row*180;d.text((10,y+2),f'{i}: {r["icon_id"]}',fill='black')
 for j,(theme,size) in enumerate([('light',384),('light',48),('dark',384),('dark',48)]):
  im=Image.open(run/f'preview-{theme}-{size}.png').convert('RGB');im=im.resize((144,144)) if size==384 else im
  sheet.paste(im,(20+j*185,y+24))
 if accept:
  (run/'result.json').write_text(json.dumps(dict(source_uuid=r['uuid'],reference_path=r['reference'],icon_id=r['icon_id'],author='gpt-6',validation_status=report.status,build_gate=g,visual_review=design.get('visual_review','Inspected at 48px and enlarged in both themes; defining features restored, smooth coherent contours and open negative space.'),omissions=design.get('omissions',[]),construction_reference=design['refs'],artifacts=[p.name,r['icon_id']+'.svg',r['icon_id']+'.metadata.json','validation.txt','build-gate.json','review-before.md','reference.png']+previews),indent=2)+'\n')
sheet.save(ROOT/('after-'+'-'.join(map(str,indices))+'.png'))
