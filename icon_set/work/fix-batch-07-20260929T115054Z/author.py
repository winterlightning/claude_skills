from pathlib import Path
import json,re,sys,datetime,importlib.util,shutil
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.scripts import build_gate,primitive_fix
OUT=Path(__file__).parent
ROWS=json.loads((OUT/'claims.json').read_text())
AUTHOR='gpt-6';SOURCE_ICON_ID=[re.search(r'[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}',r['reference']).group() for r in ROWS];SOURCE_PATH=[r['reference'] for r in ROWS]
HELPERS='''
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*ps,closed=False): self.add_polyline(n,*ps,closed=closed)
        def bez(n,a,*ss): self.add_bezier(n,a,*ss)
        def arc(n,a,b,rx,ry=None,s=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry,sweep=s)
        def circle(n,x,y,r):
            arc(n+'a',(x-r,y),(x+r,y),r);arc(n+'b',(x+r,y),(x-r,y),r)
            self.add_contour(n,n+'a',n+'b',closed=True)
        def path(n,a,commands,closed=False):
            members=[]
            for j,c in enumerate(commands):
                k,b,*args=c; name=n+str(j)
                if k=='L': line(name,a,b)
                elif k=='A': arc(name,a,b,*args)
                elif k=='C': bez(name,a,(args[0],args[1],b))
                members.append(name);a=b
            self.add_contour(n,*members,closed=closed)
        def rect(n,x,y,w,h,r=0):
            if not r: poly(n,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True);return
            path(n,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r),('L',(x+r,y+h)),('A',(x,y+h-r),r),('L',(x,y+r)),('A',(x+r,y),r)],True)
        def join(*ns): self.relate('connect',*ns)
'''
SPECS={}
def spec(i,key,note,code,refs='No useful exact Lucide match; reference composition and geometric construction.',extra=''):
 SPECS[i]=dict(key=key,note=note,code=code,refs=refs,extra=extra)

def make(i):
 s=SPECS[i];r=ROWS[i];uid=SOURCE_ICON_ID[i]
 stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')+'-batch07'
 run=ROOT/'icon_set/work/primitive-make-ray'/uid/stamp;run.mkdir(parents=True)
 meta=dict(concept=Path(r['reference']).stem[:-37],source_uuid=uid,reference_path=r['reference'],icon_id=r['id'],author=AUTHOR)
 (run/(r['id']+'.metadata.json')).write_text(json.dumps(meta,indent=2))
 (run/'review-before.txt').write_text(s['note']+'\n'+s['refs'])
 module=run/(r['id'].replace('-','_')+'_'+uid.replace('-','_')+'.py')
 body='\n'.join('        '+l if l else '' for l in s['code'].strip().splitlines())
 code=f'''"""{s['note']}\nConstruction: {s['refs']}\nPlan: {s['key']} SOLO48; shared shape parameters and scoped real joins.\n"""\nfrom icon_set.model.keyshapes import Keyshape\nfrom icon_set.model.icons.solo._base import Solo48\nSOURCE_ICON_ID = {uid!r}\nSOURCE_PATH = {r['reference']!r}\nAUTHOR = {AUTHOR!r}\nclass Drawing(Solo48):\n    icon_id = {r['id']!r}\n    keyshape = Keyshape.{s['key']}\n    semantic_role = 'MAIN'\n    semantic_kind = 'noun'\n    category = 'primitives-generate'\n    aliases = ()\n    keywords = {tuple(r['id'].split('-'))!r}\n    {s['extra']}\n    def build(self):\n{HELPERS}\n{body}\n'''
 module.write_text(code)
 try:
  icon=primitive_fix.load_icon(module);report=icon.validate_icon();svg=icon.to_svg();(run/(r['id']+'.svg')).write_text(svg)
  (run/'validation.txt').write_text(report.describe());primitive_fix.render_previews(svg,r['id'],48,run)
  gate=build_gate.gate(module);(run/'gate.json').write_text(json.dumps(gate,indent=2));print(i,r['id'],report.status,gate,flush=True)
  meta.update(module=module.name,svg=r['id']+'.svg',validation_status=report.status,gate=gate,review=s['note'],references=s['refs'],visual_review='pending',result_dir=str(run.relative_to(ROOT)))
  (run/'candidate.json').write_text(json.dumps(meta,indent=2));(OUT/f'latest-{i}.txt').write_text(str(run.relative_to(ROOT)))
 except Exception as e:print(i,type(e).__name__,str(e),flush=True);raise
if __name__=='__main__':
 for i in map(int,sys.argv[1:]):make(i)
