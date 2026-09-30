from pathlib import Path
import json,sys,cairosvg
sys.path.insert(0,str(Path(__file__).resolve().parents[3]))
from icon_set.scripts.primitive_fix import load_icon,run_module,render_previews
from icon_set.scripts.build_gate import gate
ROOT=Path(__file__).parent
AUTHOR='gpt-6'
SOURCE_ICON_ID=None
SOURCE_PATH=None
cmd=sys.argv[1];args=sys.argv[2:]
if cmd=='author':
 from designs import D
 rs=json.loads((ROOT/'runs.json').read_text()) if (ROOT/'runs.json').exists() else []
 for p in map(Path,json.loads((ROOT/'claims.json').read_text())):
  item=json.loads((p/'claim.json').read_text())['item'];ident=item['icon_id']
  if ident not in D or any(r['icon_id']==ident for r in rs):continue
  ref=next((p/'reference').glob('*.svg'));uid=ref.stem[-36:];concept=ref.stem[:-37];run=Path('icon_set/work/primitive-make-ray')/uid/'20260929-batch12b-attempt01';run.mkdir(parents=True,exist_ok=False)
  key,comparison,body=D[ident]
  r={'concept':concept,'source_uuid':uid,'reference_path':str(ref),'icon_id':ident,'feedback':item.get('feedback'),'comparison':comparison+' No written reviewer feedback.','run':str(run),'claim':str(p),'change':comparison.split('. ',1)[1]}
  (run/(ident+'.metadata.json')).write_text(json.dumps(r,indent=2));(run/'comparison.txt').write_text(r['comparison']+'\n')
  text=f'''"""{comparison}
Plan: {key}; coherent source-specific contours with shared physical joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID={uid!r}
SOURCE_PATH={str(ref)!r}
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id={ident!r}
    keyshape=Keyshape.{key}
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords={tuple(concept.split())!r}
'''
  if ident=='female-user-profile-icon-upload-ba893b6ce54bc48b':text+="    human_construction='bust'\n"
  text+='    def build(self):\n'+(ROOT/'helpers.txt').read_text()+body
  (run/(ident.replace('-','_')+'_'+uid.replace('-','_')+'.py')).write_text(text);rs.append(r)
 (ROOT/'runs.json').write_text(json.dumps(rs,indent=2));print('Authored',len(rs))
elif cmd=='check':
 rs=json.loads((ROOT/'runs.json').read_text())
 for r in rs:
  if args and r['icon_id'] not in args:continue
  p=Path(r['run']);m=run_module(p);icon=load_icon(m);v=icon.validate_icon();g=gate(m)
  (p/'validation.txt').write_text(v.describe()+'\n'+json.dumps(g,indent=2));(p/'gate.json').write_text(json.dumps(g,indent=2))
  svg=icon.to_svg();(p/(r['icon_id']+'.svg')).write_text(svg);render_previews(svg,r['icon_id'],48,p)
  print(r['icon_id'],v.status,g['status'],v.errors,v.warnings,g['errors'],g['warnings'],flush=True)
elif cmd=='sheets':
 from PIL import Image,ImageDraw
 rs=json.loads((ROOT/'runs.json').read_text())
 for batch in range((len(rs)+4)//5):
  sheet=Image.new('RGB',(740,1000),'#ddd');d=ImageDraw.Draw(sheet)
  for i,r in enumerate(rs[batch*5:batch*5+5]):
   p=Path(r['run']);d.text((8,i*200+5),r['icon_id'],fill='black')
   for j,t in enumerate(['light','dark']):
    if (p/f'preview-{t}-384.png').exists():
     sheet.paste(Image.open(p/f'preview-{t}-384.png').resize((156,156)),(j*370+10,i*200+28));sheet.paste(Image.open(p/f'preview-{t}-48.png'),(j*370+205,i*200+80))
  sheet.save(ROOT/f'candidates-{batch}.png')
