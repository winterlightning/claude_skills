import json,subprocess,datetime,uuid,importlib.util,shutil
from pathlib import Path
import cairosvg
from PIL import Image,ImageDraw
SOURCE_ICON_ID = "c577e0e4-e7f4-48be-941f-09df216731ed"
SOURCE_PATH = "pictographic-primitives/container/concentrics circle 1_c577e0e4-e7f4-48be-941f-09df216731ed.svg"
AUTHOR = "gpt-6"
def retrieve():
 p=subprocess.run(['python3','icon_set/scripts/next_side_main.py','--offset','40'],capture_output=True,text=True)
 print(p.stdout,p.stderr)
 if p.returncode: raise RuntimeError(p.stderr)
 a={}
 for l in p.stdout.splitlines():
  if ': ' in l and not l.startswith('- '):
   k,v=l.split(': ',1);a[k]=v
 m={k:a.get(v) for k,v in [('concept','concept'),('source_uuid','source UUID'),('reference_path','reference'),('category','category'),('aliases','aliases'),('uses','uses')]}
 m.update(combination_context=[l for l in p.stdout.splitlines() if l.startswith('- ')],retrieval_stdout=p.stdout,retrieval_stderr=p.stderr)
 d=Path('icon_set/work/side-main-make-thuan')/m['source_uuid']/(datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid.uuid4().hex[:6]);d.mkdir(parents=True)
 (d/'retrieval.metadata.json').write_text(json.dumps(m,indent=2))
 shutil.copyfile(m['reference_path'],d/'reference.svg')
 cairosvg.svg2png(url=m['reference_path'],write_to=str(d/'reference.png'),output_width=384,output_height=384,background_color='white')
 print('RESULT_DIR',d)
 return d

def author(d,name,keyshape,body,description):
 d=Path(d);m=json.loads((d/'retrieval.metadata.json').read_text())
 fn=name.replace('-','_')+'_'+m['source_uuid'].replace('-','_')+'.py'
 code='from icon_set.model.keyshapes import Keyshape\nfrom icon_set.model.icons.solo._base import Solo48\n'
 code+=f'SOURCE_ICON_ID = {m["source_uuid"]!r}\nSOURCE_PATH = {m["reference_path"]!r}\nAUTHOR = "gpt-6"\n\n'
 code+=f'class Drawing(Solo48):\n    """{description}"""\n    icon_id = {name!r}\n    keyshape = Keyshape.{keyshape}\n    semantic_role = "MAIN"\n    semantic_kind = "noun"\n    category = "objects/general"\n    aliases = ()\n    keywords = {tuple(m['concept'].lower().split())!r}\n\n    def build(self):\n'
 code+='\n'.join('        '+l for l in body.splitlines())+'\n'
 (d/fn).write_text(code)
 (d/(name+'.metadata.json')).write_text(json.dumps(m,indent=2))
 shutil.copyfile(m['reference_path'],d/'reference.svg')
 return export(d,fn)

def export(d,fn):
 d=Path(d);spec=importlib.util.spec_from_file_location('candidate',d/fn);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);i=mod.Drawing();r=i.validate_icon()
 (d/'validation.txt').write_text(r.describe());print(r.describe())
 svg=i.to_svg();(d/(i.icon_id+'.svg')).write_text(svg)
 sheet=Image.new('RGB',(768,460),'#dddddd');draw=ImageDraw.Draw(sheet)
 for j,(theme,bg,neg) in enumerate([('light','white',False),('dark','#151515',True)]):
  for size in [48,320]:
   f=d/f'{theme}-{size}.png';cairosvg.svg2png(bytestring=svg.encode(),write_to=str(f),output_width=size,output_height=size,background_color=bg,negate_colors=neg)
   sheet.paste(Image.open(f).convert('RGB'),(j*384+(384-size)//2,35 if size==320 else 390))
  draw.text((j*384+12,12),theme,fill='black')
 sheet.save(d/'review.png')
 return r.status

def finish(d,findings,omissions,refs,reason):
 d=Path(d);m=json.loads((d/'retrieval.metadata.json').read_text());fn=next(p for p in d.glob('*.py') if p.name!='batch_tools.py')
 spec=importlib.util.spec_from_file_location('candidate',fn);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);i=mod.Drawing();r=i.validate_icon()
 result=dict(source_uuid=m['source_uuid'],source_path=m['reference_path'],icon_id=i.icon_id,author=mod.AUTHOR,keyshape=i.keyshape.name,keyshape_reason=reason,validation_status=r.status,validation_findings=r.describe(),visual_review=findings,omissions=omissions,references=refs,artifacts=[p.name for p in d.iterdir() if p.is_file()])
 (d/'result.json').write_text(json.dumps(result,indent=2))
 print('SAVED',d,i.icon_id,r.status)
