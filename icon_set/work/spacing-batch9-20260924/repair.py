from pathlib import Path
import json,sys,importlib.util,subprocess,datetime,shutil
import cairosvg
ROOT=Path(__file__).resolve().parent
SOURCE_PATH=json.loads((ROOT/'inputs.json').read_text())
SOURCE_ICON_ID=[Path(p).stem[-36:] for p in SOURCE_PATH]
AUTHOR='gpt-6'
HELPERS="""
    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def rect(self,n,l,t,r,b,rad=2):
        pts=[(l+rad,t),(r-rad,t),(r,t+rad),(r,b-rad),(r-rad,b),(l+rad,b),(l,b-rad),(l,t+rad)]
        for i,a in enumerate(pts):
            z=pts[(i+1)%8]
            if i%2:self.add_arc(n+str(i),a,z,radius_x=rad)
            else:self.add_line(n+str(i),a,z)
        self.add_contour(n,*(n+str(i) for i in range(8)),closed=True)
    def house(self):
        self.add_polyline('house',(6,42),(6,18),(24,6),(42,18),(42,42),closed=True)
    def page(self):
        self.add_polyline('page',(8,44),(8,4),(28,4),(40,16),(40,44),closed=True)
"""
def setup(i):
    src=Path(SOURCE_PATH[i]);uid=SOURCE_ICON_ID[i];concept=src.stem[:-37];slug=concept.replace(' ','-')
    index=ROOT/'runs.json';runs=json.loads(index.read_text()) if index.exists() else {}
    if str(i) not in runs:
        d=Path('icon_set/work/primitive-make-ray')/uid/(datetime.datetime.now().strftime('%Y%m%dT%H%M%S')+'-spacing-batch9-gpt-6')
        d.mkdir(parents=True);runs[str(i)]=str(d);index.write_text(json.dumps(runs,indent=2))
        meta=dict(concept=concept,source_uuid=uid,reference_path=str(src),author=AUTHOR)
        (d/(slug+'.metadata.json')).write_text(json.dumps(meta,indent=2))
        shutil.copy(src,d/'reference.svg');cairosvg.svg2png(url=str(src),write_to=str(d/'reference.png'),output_width=384,output_height=384)
    return Path(runs[str(i)]),slug

def run(i,body,key='SQUARE',note=''):
    d,slug=setup(i);uid=SOURCE_ICON_ID[i]
    attempts=list(d.glob('attempt-*.txt'));num=len(attempts)+1
    code=f'''"""{slug}: {note}
Symbol plan: shared shape helpers and mirrored coordinates. Keyshape {key}; exact bounds from contract.
Local Lucide originals and atomic-debug: bluetooth, skull, file-user, shield-plus, heart, house, paw-print, search, bug, smartphone, eye, fingerprint-pattern. Coherent outlines and shared junctions inform construction.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID={uid!r}
SOURCE_PATH={SOURCE_PATH[i]!r}
AUTHOR={AUTHOR!r}
class Drawing(Solo48):
    icon_id={slug!r}
    keyshape=Keyshape.{key}
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=({slug!r},)
    def build(self):
'''+''.join('        '+line+'\n' for line in body.splitlines())+HELPERS
    mod=d/(slug.replace('-','_')+'_'+uid.replace('-','_')+'.py');mod.write_text(code)
    spec=importlib.util.spec_from_file_location('candidate'+str(i)+str(num),mod);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);icon=m.Drawing();report=icon.validate_icon();val=report.describe();(d/'validation.txt').write_text(val)
    svg=icon.to_svg();(d/(slug+'.svg')).write_text(svg)
    for theme,bg,fg in [('light','#ffffff','#000000'),('dark','#171717','#ffffff')]:
        for size in [48,384]:
            cairosvg.svg2png(bytestring=svg.replace('currentColor',fg).replace('#000000',fg).encode(),write_to=str(d/f'{theme}-{size}.png'),output_width=size,output_height=size,background_color=bg)
    proc=subprocess.run([sys.executable,'icon_set/scripts/build_gate.py',str(mod),'--debug',str(d/'gate')],capture_output=True,text=True)
    out=proc.stdout+proc.stderr;(d/'build-gate.txt').write_text(out);(d/f'attempt-{num:02}.txt').write_text(note+'\n'+val+'\n'+out);shutil.copy(mod,d/f'attempt-{num:02}.py')
    print(f'#{i+1} {slug} round {num}\n{val}\n{out}',flush=True)
    return proc.returncode==0,d
