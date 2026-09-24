from pathlib import Path
import json, importlib.util, textwrap
from PIL import Image, ImageDraw
from icon_set.renderers.png import render_png
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID = "600bc5a2-131a-4e43-b134-f5e672684c21"
SOURCE_PATH = "pictographic-primitives/other/mobile phone bug_600bc5a2-131a-4e43-b134-f5e672684c21.svg"
AUTHOR = "gpt-6"
ROOT = Path(__file__).parent
ROWS = json.loads((ROOT/'batch-inputs.json').read_text())
COMMON = '''
    def circle(self, name, cx, cy, r):
        self.add_arc(name+"-top", (cx-r,cy), (cx+r,cy), radius_x=r)
        self.add_arc(name+"-bottom", (cx+r,cy), (cx-r,cy), radius_x=r)
        self.add_contour(name, name+"-top", name+"-bottom", closed=True)

    def box(self, name, left, top, right, bottom, r=3):
        points = [(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),
                  (right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
        members=[]
        for i,a in enumerate(points):
            b=points[(i+1)%8]; part=f"{name}-{i}"
            if i%2: self.add_arc(part,a,b,radius_x=r)
            else: self.add_line(part,a,b)
            members.append(part)
        self.add_contour(name,*members,closed=True)
'''
def author(n, key, body, description, plan, refs, omissions=()):
    row=ROWS[n-1]; out=Path(row['result_dir']); iconid=row['icon_id']
    if (out/'result.json').exists(): raise RuntimeError('Finalized run must not be overwritten')
    filename=iconid.replace('-','_')+'_'+row['source_uuid'].replace('-','_')+'.py'
    pre=f'''"""{description}
Symbol plan: {plan}
Keyshape visible bounds: {getattr(Keyshape,key).bounds_for(Profile.SOLO48)}.
Construction references: {refs}.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = {row['source_uuid']!r}
SOURCE_PATH = {row['reference_path']!r}
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = {iconid!r}
    keyshape = Keyshape.{key}
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = {tuple(row['concept'].split())!r}
    def build(self):
'''
    (out/filename).write_text(pre+textwrap.indent(textwrap.dedent(body).strip(),'        ')+'\n'+COMMON)
    record={**row,'python_module':filename,'keyshape':key,'description':description,'symbol_plan':plan,'construction_references':refs,'omissions':list(omissions)}
    (out/'draft.json').write_text(json.dumps(record,indent=2)+'\n')
    return check(n)
def check(n):
    out=Path(ROWS[n-1]['result_dir']);record=json.loads((out/'draft.json').read_text());spec=importlib.util.spec_from_file_location('drawing_'+str(n),out/record['python_module']);module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);icon=module.Drawing();report=icon.validate_icon()
    (out/'validation.txt').write_text(report.describe()+'\n');(out/(icon.icon_id+'.svg')).write_text(icon.to_svg())
    record['validation_status']=report.status;record['warnings_count']=len(report.warnings);record['errors_count']=len(report.errors)
    for theme,ink,bg in [('light','#111111','#ffffff'),('dark','#f4f4f5','#18181b')]:
        for scale in [1,5]:
            import io
            im=Image.open(io.BytesIO(render_png(icon,ink=ink,scale=scale))).convert('RGBA');base=Image.new('RGBA',im.size,bg);base.alpha_composite(im);base.convert('RGB').save(out/f'{theme}-{48*scale}.png')
    sheet=Image.new('RGB',(650,330),'#cccccc');draw=ImageDraw.Draw(sheet)
    for x,theme in [(0,'light'),(325,'dark')]:
        sheet.paste(Image.open(out/f'{theme}-240.png'),(x,25));sheet.paste(Image.open(out/f'{theme}-48.png'),(x+250,25));draw.text((x+5,5),f'{n}. {icon.icon_id} / {theme}',fill='black')
    sheet.save(out/'review.png');(out/'draft.json').write_text(json.dumps(record,indent=2)+'\n')
    print(n, report.describe());print('PREVIEW',out/'review.png')
    return record
def finish(n, findings, approved=True):
    out=Path(ROWS[n-1]['result_dir']);r=json.loads((out/'draft.json').read_text());r['visual_review']={'reviewed_native_light_and_dark':True,'approved':approved,'findings':findings};r['artifacts']=sorted(p.name for p in out.iterdir() if p.is_file() and p.name!='result.json');(out/'result.json').write_text(json.dumps(r,indent=2)+'\n');print('FINAL',n,r['validation_status'])
