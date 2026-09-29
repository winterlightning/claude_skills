"""Fresh primitive-make-ray runs for the twenty explicitly claimed references.
Each generated module records its own SOURCE_ICON_ID, SOURCE_PATH and AUTHOR.
"""
from pathlib import Path
import json, sys, textwrap, io
from datetime import datetime, timezone
import cairosvg
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[2]
sys.path.insert(0, str(REPO))
from icon_set.scripts.primitive_fix import load_icon, render_previews
from icon_set.scripts.build_gate import gate

HELPERS = '''
    def path(self, name, start, steps, closed=False):
        members = []
        here = start
        for i, step in enumerate(steps):
            member = f"{name}-{i}"
            if step[0] == "L":
                self.add_line(member, here, step[1])
            else:
                self.add_arc(member, here, step[1], radius_x=step[2], radius_y=step[3], sweep=step[4])
            here = step[1]
            members.append(member)
        self.add_contour(name, *members, closed=closed)

    def circle(self, name, x, y, r):
        self.path(name, (x-r,y), [("A",(x+r,y),r,r,True),("A",(x-r,y),r,r,True)], True)

    def oval(self, name, x, y, rx, ry):
        self.path(name, (x-rx,y), [("A",(x+rx,y),rx,ry,True),("A",(x-rx,y),rx,ry,True)], True)

    def poly(self, name, *points, closed=False):
        self.add_polyline(name, *points, closed=closed)

    def line(self, name, a, b):
        self.add_line(name, a, b)
'''


from specs import SPECS, EXTRA_HELPERS
HELPERS += EXTRA_HELPERS

def run(indices):
    claims=json.loads((ROOT/'claims.json').read_text())
    previous=json.loads((ROOT/'runs.json').read_text()) if (ROOT/'runs.json').exists() else {}
    stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    for i in indices:
        c=claims[i]; key,wrong,change,body=SPECS[i]
        ref=Path(c['reference']); uuid=ref.stem[-36:]; concept=ref.stem[:-37]
        out=REPO/'icon_set/work/primitive-make-ray'/uuid/(stamp+f'-meaning-{i:02d}')
        out.mkdir(parents=True)
        metadata=dict(concept=concept,source_uuid=uuid,reference_path=str(ref),icon_id=c['icon_id'],feedback=c['feedback'],before_findings=wrong,revision_plan=change,keyshape=key,author='gpt-6')
        (out/(c['icon_id']+'.metadata.json')).write_text(json.dumps(metadata,indent=2))
        module=out/(c['icon_id'].replace('-','_')+'_'+uuid.replace('-','_')+'.py')
        source=f'''from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = {uuid!r}
SOURCE_PATH = {str(ref)!r}
AUTHOR = "gpt-6"

class Revision(Solo48):
    icon_id = {c['icon_id']!r}
    keyshape = Keyshape.{key}
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()
    # Plan: {change}
    # Original/current comparison: {wrong}
    # References: claimed original; Lucide smartphone/lock-open/headset/memory-stick/drone
    # original and atomic-debug where applicable; human_ref/user.svg and full_body_ref.png.
    # Paired anatomical parts share parameters; directional profiles stay asymmetric.
{HELPERS}
    def build(self):
{textwrap.indent(textwrap.dedent(body).strip(), '        ')}
'''
        module.write_text(source)
        try:
            icon=load_icon(module); report=icon.validate_icon(); svg=icon.to_svg()
            (out/(c['icon_id']+'.svg')).write_text(svg)
            (out/'validation.txt').write_text(report.describe())
            render_previews(svg,c['icon_id'],48,out)
            cairosvg.svg2png(url=str(REPO/ref),write_to=str(out/'reference.png'),output_width=384,output_height=384)
            result=gate(module); (out/'gate.json').write_text(json.dumps(result,indent=2))
            print(i,c['icon_id'],report.status,result['status'],len(result['errors']),len(result['warnings']),flush=True)
        except Exception as e:
            print(i,type(e).__name__,str(e),flush=True)
            raise
        previous[str(i)]=str(out.relative_to(REPO))
        (ROOT/'runs.json').write_text(json.dumps(previous,indent=2))

def sheets():
    runs=json.loads((ROOT/'runs.json').read_text());claims=json.loads((ROOT/'claims.json').read_text())
    for page in range(4):
        im=Image.new('RGB',(1000,1000),'#eee');d=ImageDraw.Draw(im)
        for row in range(5):
            i=page*5+row
            if str(i) not in runs:continue
            out=REPO/runs[str(i)];y=row*200
            d.text((8,y+5),f'{i}: '+claims[i]['icon_id'],fill='black')
            for x,theme in ((10,'light'),(510,'dark')):
                pic=Image.open(out/f'preview-{theme}-384.png').resize((168,168))
                im.paste(pic,(x,y+25))
                native=Image.open(out/f'preview-{theme}-48.png');im.paste(native,(x+195,y+65))
        im.save(ROOT/f'after-{page}.png')

if __name__=='__main__':
    if len(sys.argv)>1 and sys.argv[1]=='sheets':sheets()
    else:run([int(x) for x in sys.argv[1:]] if len(sys.argv)>1 else range(20));sheets()
