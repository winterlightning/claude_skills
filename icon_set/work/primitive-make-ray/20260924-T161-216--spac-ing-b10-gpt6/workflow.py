"""Private batch authoring/evidence helper. Each module retains its own source ID."""
import json, sys, subprocess, importlib.util, io
from pathlib import Path
import cairosvg
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))
BATCH = Path(__file__).resolve().parent
ITEMS = json.loads((BATCH/'manifest.json').read_text())
AUTHOR = 'gpt-6'
SOURCE_ICON_ID = None
SOURCE_PATH = None

HELPERS = '''
    def circle(self,n,x,y,r):
        pts=[(x-r,y),(x,y-r),(x+r,y),(x,y+r),(x-r,y)]
        for i,(a,b) in enumerate(zip(pts,pts[1:])):
            self.add_arc(n+str(i),a,b,radius_x=r)
        self.add_contour(n,*(n+str(i) for i in range(4)),closed=True)

    def box(self,n,l,t,r,b,rad=3,breaks=None):
        pts=[(l+rad,t),(r-rad,t),(r,t+rad),(r,b-rad),(r-rad,b),(l+rad,b),(l,b-rad),(l,t+rad)]
        members=[]
        for i,a in enumerate(pts):
            z=pts[(i+1)%8]
            if i%2:
                p=f'{n}-{i}';self.add_arc(p,a,z,radius_x=rad);members.append(p)
            else:
                nodes=[a]+(breaks or {}).get(i,[])+[z]
                for j,(u,v) in enumerate(zip(nodes,nodes[1:])):
                    if u==v:continue
                    p=f'{n}-{i}-{j}';self.add_line(p,u,v);members.append(p)
        self.add_contour(n,*members,closed=True)

    def monitor(self,l=6,t=6,r=42,b=34,foot=42):
        self.box('screen',l,t,r,b,3,{4:[(24,b)]})
        self.add_line('stand',(24,b),(24,foot))
        self.add_polyline('foot',(16,foot),(24,foot),(32,foot))
        self.relate('connect','screen','stand')
        self.relate('connect','stand','foot')

    def bust(self,n,x,y,r,w,h):
        # human_ref/user.svg: circular head, smooth open shoulders, exact 4 ink gap.
        self.circle(n+'-head',x,y,r)
        top=y+r+8
        self.add_arc(n+'-shoulder-l',(x-w,top+h),(x,top),radius_x=w,radius_y=h)
        self.add_arc(n+'-shoulder-r',(x,top),(x+w,top+h),radius_x=w,radius_y=h)
        self.add_contour(n+'-shoulders',n+'-shoulder-l',n+'-shoulder-r')
'''

def author(index,body,key='SQUARE',note='',omissions=''):
    it=ITEMS[index-1];out=ROOT/it['out']; name=it['icon_id'].replace('-','_')+'_'+it['source_uuid'].replace('-','_')+'.py'
    module=out/name
    rounds=list(out.glob('attempt-*.py'));roundno=len(rounds)+1
    src=f'''"""{it['concept']}. {note}
Symbol plan: enclosure and content use shared parameters and genuine attachment nodes.
Construction: Lucide smartphone/monitor/megaphone geometric enclosures and joins;
human_ref/user.svg supplies circular heads and open shoulder proportions where applicable.
Omissions: {omissions}
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = {it['source_uuid']!r}
SOURCE_PATH = {it['reference_path']!r}
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = {it['icon_id']!r}
    keyshape = Keyshape.{key}
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ({it['concept']!r},)
    ink_extremes = keyshape.bounds_for(Profile.SOLO48)
{HELPERS}
    def build(self):
'''+''.join('        '+line+'\n' for line in body.strip().splitlines())
    module.write_text(src);(out/f'attempt-{roundno:02d}.py').write_text(src)
    (out/'design.json').write_text(json.dumps(dict(keyshape=key,note=note,omissions=omissions,round=roundno,module=name),indent=2))
    return check(index)

def check(index):
    it=ITEMS[index-1];out=ROOT/it['out'];design=json.loads((out/'design.json').read_text());module=out/design['module'];n=design['round']
    spec=importlib.util.spec_from_file_location('_drawing',module);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);icon=m.Drawing();report=icon.validate_icon()
    desc=report.describe();(out/'validation.txt').write_text(desc);(out/f'validation-{n:02d}.txt').write_text(desc)
    svg=icon.to_svg();(out/(it['icon_id']+'.svg')).write_text(svg)
    proc=subprocess.run([sys.executable,'icon_set/scripts/build_gate.py',str(module),'--debug',str(out/'gate')],cwd=ROOT,text=True,capture_output=True)
    gate=proc.stdout+proc.stderr;(out/'build-gate.txt').write_text(gate);(out/f'build-gate-{n:02d}.txt').write_text(gate)
    for theme,fg,bg in [('light','#171717','#ffffff'),('dark','#eeeeee','#171717')]:
        themed=svg.replace('currentColor',fg).replace('#000000',fg).replace('stroke="black"',f'stroke="{fg}"')
        for size in [48,288]:
            cairosvg.svg2png(bytestring=themed.encode(),write_to=str(out/f'{theme}-{size}.png'),output_width=size,output_height=size,background_color=bg)
    ok=report.status=='valid' and not report.warnings and proc.returncode==0
    (out/'check.json').write_text(json.dumps(dict(valid=report.status,warnings=len(report.warnings),build_gate='pass' if proc.returncode==0 else 'fail',ok=ok),indent=2))
    print(f'[{index}] round {n}: {it["concept"]}\n{desc}\n{gate}',flush=True)
    return ok

def preview(index):
    it=ITEMS[index-1];out=ROOT/it['out'];s=Image.new('RGB',(800,360),'#dddddd')
    ref=Image.open(out/'reference.png');s.paste(ref,(5,55),ref)
    for j,theme in enumerate(['light','dark']):
        s.paste(Image.open(out/f'{theme}-288.png'),(180+j*310,10))
        s.paste(Image.open(out/f'{theme}-48.png'),(300+j*310,305))
    s.save(out/'review.png');print(out/'review.png')

def finish(index,review,blocker=None):
    it=ITEMS[index-1];out=ROOT/it['out'];design=json.loads((out/'design.json').read_text());checkdata=json.loads((out/'check.json').read_text())
    result={**it,**design,**checkdata,'visual_review':review,'blocker':blocker,'status':'pass' if checkdata['ok'] and not blocker else 'blocked','artifacts':sorted(p.name for p in out.iterdir() if p.is_file())}
    (out/'result.json').write_text(json.dumps(result,indent=2))

if __name__=='__main__':
    preview(int(sys.argv[1]))
