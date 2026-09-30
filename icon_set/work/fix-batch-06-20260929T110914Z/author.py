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
spec(0,'SQUARE','The rejected sweets form narrow pinched loops and the kite is squat. No written feedback. Rebuilt two round sweet lobes above a shallow bowl and a taller kite; omitted the third sweet and kite spars to preserve openings.', '''
poly('kite',(33,6),(42,14),(34,26),(25,14),closed=True)
bez('tail',(34,26),((34,33),(42,35),(42,42)));join('kite','tail')
arc('sweet-left',(6,32),(16,32),5)
arc('sweet-right',(16,32),(26,32),5)
self.add_contour('sweets','sweet-left','sweet-right')
line('rim',(6,32),(26,32))
path('bowl',(26,32),[('C',(20,42),(25,38),(24,42)),('L',(12,42)),('C',(6,32),(8,42),(7,38))]);join('rim','bowl','sweets')
''')
spec(1,'SQUARE','The rejected bowl has only one undifferentiated semicircle and an overlarge diamond. No written feedback. Restored distinct sweet lobes, a shallow bowl and tapered kite; omitted the third sweet and spars for spacing.',SPECS[0]['code'])
spec(2,'SQUARE','The current kite is a parallelogram with a flattened tail, and the cloud is cramped. No written feedback. Rebuilt a pointed kite and curling tail beside an open, larger cloud; omitted internal spars.', '''
path('cloud',(17,18),[('L',(11,18)),('A',(11,8),5),('C',(21,11),(11,4),(20,5))])
poly('kite',(33,17),(42,26),(31,36),(23,26),closed=True)
bez('tail',(31,36),((29,42),(37,42),(42,42)));join('tail','kite')
''','Lucide cloud: broad rounded lobe and coherent open contour.')
spec(3,'SQUARE','The rejected knives are bare rods and the block reads as a quarter circle. No written feedback. Restored two outlined handles with diagonal placement and a broad sloping block; omitted wood grain.', '''
poly('block',(6,24),(22,28),(42,36),(42,42),(6,42),closed=True)
path('left-handle',(10,25),[('L',(22,7)),('C',(29,12),(26,3),(33,7)),('L',(19,27))]);join('block','left-handle')
path('right-handle',(29,31),[('L',(35,21)),('C',(42,26),(38,16),(46,21)),('L',(36,34))]);join('block','right-handle')
''')
spec(4,'HRECT_L','The rejected palm is a Y and the person is only a detached shoulder arc. No written feedback. Added a third drooping frond, a curved trunk, and a clearer seated upper body beside a tilted laptop; omitted the screen logo and waves.', '''
circle('head',34,13,5)
bez('torso',(34,26),((40,26),(44,33),(44,40)))
self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
poly('laptop',(4,30),(23,30),(27,40),(8,40),closed=True)
bez('frond-left',(4,8),((8,8),(11,9),(13,13)))
bez('frond-right',(13,13),((16,8),(19,8),(21,8)))
bez('frond-down',(13,13),((18,13),(21,17),(21,20)))
bez('trunk',(13,13),((10,17),(10,20),(10,22)))
join('frond-left','frond-right','frond-down','trunk')
''','Human full_body_ref.png: round head and 4-unit detached gap. Lucide laptop: simple panel.')
spec(5,'SQUARE','The current wreath has only two bulky loops per branch, losing the laurel leaf rhythm. No written feedback. Rebuilt paired curved branches with three tapered leaves each and crossed stems; reduced the source leaf count for native readability.', '''
for side in (-1,1):
 def p(x,y):return (24+side*(x-24),y)
 # Each branch owns three consistently pointed leaf contours.
 bez(f'branch{side}',p(14,6),(p(7,17),p(9,31),p(27,42)))
 for j,(a,c1,c2,b) in enumerate([((14,6),(6,6),(6,15),(10,18)),((10,18),(6,20),(6,29),(14,30)),((14,30),(13,38),(19,38),(23,39))]):
  n=f'leaf{side}-{j}'
  bez(n,p(*a),(p(*c1),p(*c2),p(*b)))
  join(n,f'branch{side}')
join('branch-1','branch1')
''','Lucide sprout: pointed leaves and curved stems; mirrored branches.')
spec(6,'HRECT_L','The current top is sharply trapezoidal and the bottom layer is an open dash. No written feedback. Rounded the pasta top, retained a wavy filling and restored a closed lower layer.', '''
path('top',(4,17),[('L',(8,10)),('C',(12,8),(9,8),(10,8)),('L',(36,8)),('C',(40,10),(38,8),(39,8)),('L',(44,17)),('L',(4,17))],True)
bez('filling',(4,27),((11,22),(17,32),(24,27)),((31,22),(37,32),(44,27)))
path('bottom',(4,35),[('L',(44,35)),('C',(38,40),(44,40),(42,40)),('L',(10,40)),('C',(4,35),(6,40),(4,40))],True)
''')

def make(i):
 s=SPECS[i];r=ROWS[i];uid=SOURCE_ICON_ID[i]
 stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')+'-batch06'
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
