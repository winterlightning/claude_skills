from pathlib import Path
import json, re, textwrap, sys
from datetime import datetime, timezone
from icon_set.scripts import primitive_fix as f, build_gate
ROOT=Path(__file__).resolve().parent
claims=json.loads((ROOT/'claims.json').read_text())
AUTHOR='gpt-6'
HELPERS="""
def path(m,n,start,*steps,closed=False):
    names=[]; here=start
    for j,(kind,end,*args) in enumerate(steps):
        k=f'{n}-{j}'
        if kind=='L':m.add_line(k,here,end)
        elif kind=='C':m.add_bezier(k,here,(args[0],args[1],end))
        elif kind=='A':m.add_arc(k,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
        names.append(k);here=end
    m.add_contour(n,*names,closed=closed)
def circle(m,n,x,y,r):
    path(m,n,(x-r,y),('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True),closed=True)
def oval(m,n,x,y,rx,ry):
    path(m,n,(x-rx,y),('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True),closed=True)
def box(m,n,l,t,r,b,rad):
    path(m,n,(l+rad,t),('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True),closed=True)
"""
SPECS={}
def add(i,keyshape,issue,change,construction,omissions,code):
    SPECS[i]=dict(keyshape=keyshape,issue=issue,change=change,construction=construction,omissions=omissions,code=textwrap.dedent(code).strip())

def create(i):
    e=claims[i-1];s=SPECS[i];ref=e['reference'];uuid=re.search(r'[0-9a-f-]{36}$',Path(ref).stem).group();concept=Path(ref).stem[:-37]
    run=Path('icon_set/work/primitive-make-ray')/uuid/(datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')+'-batch11')
    run.mkdir(parents=True);name=e['item']['icon_id']
    metadata={'concept':concept,'source_uuid':uuid,'reference_path':ref}
    (run/(name+'.metadata.json')).write_text(json.dumps(metadata,indent=2)+'\n')
    (run/'review-before.txt').write_text(s['issue']+'\nFeedback: none recorded.\n'+s['change']+'\n')
    module=run/(name.replace('-','_')+'_'+uuid.replace('-','_')+'.py')
    code=repr(s['issue']+'\nSymbol plan: '+s['change']+'\nConstruction: '+s['construction']+'\nOmissions: '+s['omissions'])+'\n'
    code+='from icon_set.model.keyshapes import Keyshape\nfrom icon_set.model.icons.solo._base import Solo48\n'
    code+=f'SOURCE_ICON_ID = {uuid!r}\nSOURCE_PATH = {ref!r}\nAUTHOR = {AUTHOR!r}\n'+HELPERS
    code+=f"\nclass Drawing(Solo48):\n    icon_id = {name!r}\n    keyshape = Keyshape.{s['keyshape']}\n    semantic_role = 'MAIN'\n    semantic_kind = 'noun'\n    category = 'primitives-generate'\n    aliases = ()\n    keywords = {tuple(name.split('-'))!r}\n    def build(self):\n"
    code=code.replace("    def build(self):", s.get('class_extra','')+"    def build(self):")
    code+=textwrap.indent("m=self\nline=self.add_line\npoly=lambda n,pts:self.add_polyline(n,*pts)\njoin=lambda a,b:self.relate('connect',a,b)\n"+s['code'],'        ')+'\n'
    module.write_text(code)
    icon=f.load_icon(module); report=icon.validate_icon(); gate=build_gate.gate(module)
    (run/(name+'.svg')).write_text(icon.to_svg());f.render_previews(icon.to_svg(),name,48,run)
    (run/'validation.txt').write_text(report.describe()+'\n'+json.dumps(gate,indent=2)+'\n')
    result={**metadata,'icon_id':name,'author':AUTHOR,'validation_status':report.status,'errors':list(report.errors),'warnings':list(report.warnings),'build_gate':gate,'visual_review':'pending','omissions':s['omissions'],'keyshape':s['keyshape'],'module':module.name,'svg':name+'.svg','review':s['issue'],'change':s['change'],'construction':s['construction']}
    (run/'draft.json').write_text(json.dumps(result,indent=2)+'\n')
    return {'index':i,'key':e['key'],'run':str(run),'module':str(module),'status':report.status,'gate':gate['status'],'errors':list(report.errors)+gate['errors'],'warnings':list(report.warnings)+gate['warnings']}

add(1,'VRECT_L','The rejected face is tiny inside an arch, and the stress marks read as sideways chevrons.','Enlarge the circular face, taper the bob toward the shoulders and restore a lightning-shaped stress mark.','Shared human bust reference and Lucide user-round: circular jaw with broad shoulders; hair encloses the head naturally.','Reduce three stress marks to one to preserve clearance.', '''
circle(m,'face',24,27,7)
path(m,'hair',(10,35),('L',(10,26)),('A',(38,26),14,14,True),('L',(38,35)))
path(m,'shoulders',(8,44),('C',(24,38),(8,39),(17,38)),('C',(40,44),(31,38),(40,39)))
join('face','shoulders')
poly('stress',((20,4),(26,4),(22,12)))
''')
SPECS[1]['class_extra']="    human_construction = 'bust'\n"
add(2,'HRECT_L','The rejected board omits the flowing wood grain and leaves only a knot in a frame.','Restore a flowing grain split around a larger oval knot.','No useful Lucide match; shared rounded board and mirrored grain owners preserve the landscape form.','Use two short grain bands beside the knot instead of multiple crowded lines.', '''
box(m,'board',4,8,44,40,4)
oval(m,'knot',24,24,5,4)
path(m,'grain-left',(4,18),('C',(11,20),(7,18),(9,19)))
path(m,'grain-right',(37,28),('C',(44,30),(39,29),(41,30)))
join('board','grain-left');join('board','grain-right')
''')
add(3,'SQUARE','The rejected diamonds overwhelm the junction and reduce its vertical stem to a stub.','Rebalance two compact diamonds above diagonal branches and a long stem ending in a circle.','Lucide diamond and git-fork inform mirrored nodes and explicit shared attachment points.','No secondary details omitted.', '''
for side,x in [('left',12),('right',36)]:
 poly(side,((x,6),(x+6,12),(x,18),(x-6,12),(x,6)))
 line(side+'-branch',(x,18),(24,26));join(side,side+'-branch')
line('stem',(24,26),(24,32));join('left-branch','right-branch');join('left-branch','stem');join('right-branch','stem')
path(m,'terminal',(24,32),('A',(24,42),5,5,True),('A',(24,32),5,5,True),closed=True)
join('terminal','stem')
''')
add(4,'SQUARE','The rejected dinosaur has a blocky foot and loses the forward arm and curved back of Yoshi.','Round the muzzle, belly and forward foot, with a clear back hump and an open arm gesture.','No useful Lucide match; asymmetric coherent silhouette preserves the character profile.','Omit tiny facial marks and saddle inset.', '''
path(m,'body',(20,14),('L',(20,10)),('A',(28,10),4,4,True),('L',(34,10)),('A',(42,18),8,8,True),('A',(34,26),8,8,True),('L',(29,25)),('C',(27,34),(27,27),(26,31)),('C',(34,38),(31,34),(34,35)),('A',(30,42),4,4,True),('L',(18,42)),('L',(18,36)),('C',(6,24),(10,36),(6,30)),('L',(17,28)),('C',(16,20),(14,26),(13,22)),('C',(20,14),(18,20),(20,18)),closed=True)
''')
add(5,'HRECT_L','The rejected egg is a thin tube and the bird nest silhouette has a harsh angular beak.','Broaden the egg and smooth the bird body into a round nesting bowl with a small left-facing beak.','Lucide bird and egg inform a coherent bowl silhouette and asymmetric egg arc.','Omit tiny facial detail already absent in the reference.', '''
path(m,'bird',(4,25),('C',(14,26),(8,24),(10,24)),('C',(28,29),(19,29),(23,31)),('L',(28,21)),('L',(24,18)),('C',(33,14),(27,17),(30,14)),('C',(44,25),(40,14),(44,18)),('C',(24,40),(44,34),(35,40)),('C',(4,25),(12,40),(4,34)),closed=True)
path(m,'egg',(14,26),('C',(17,8),(9,18),(11,8)),('C',(23,19),(22,8),(24,13)))
join('egg','bird')
''')
add(6,'SQUARE','The rejected chip resembles a crosshair and the hands look like prongs.','Use a hollow casino-chip ring with four rim ticks above curved cupped palms and inward thumbs.','Shared human hand reference and Lucide hand: open palm curves with natural thumb branches.','Four rim divisions replace eight; omit cuff seams.', '''
circle(m,'chip',24,18,12)
circle(m,'chip-center',24,18,3)
for name,a,b in [('top',(24,6),(24,15)),('bottom',(24,21),(24,30)),('left',(12,18),(21,18)),('right',(27,18),(36,18))]:
 line(name,a,b);join(name,'chip');join(name,'chip-center')
for name,sign in [('left-hand',-1),('right-hand',1)]:
 x=lambda a:24+sign*a
 path(m,name,(x(7),42),('C',(x(18),35),(x(7),39),(x(18),40)),('L',(x(18),28)))
 line(name+'-thumb',(x(18),35),(x(12),33));join(name,name+'-thumb')
''')
add(7,'HRECT_L','The rejected flow loses one rectangular output and most of the original branching data movement.','Restore two rectangular output bars, hollow input dots and curved rightward movement.','Lucide git-fork construction informs shared flow endpoints; deliberate left-to-right asymmetry.','Reduce three input circles to two and retain one broad directional arrow.', '''
circle(m,'input-top',8,20,3);circle(m,'input-bottom',8,34,3)
poly('output-left',((24,18),(32,18),(32,29),(24,29),(24,18)))
poly('output-right',((40,18),(44,18),(44,29),(40,29),(40,18)))
path(m,'flow',(4,8),('C',(23,11),(12,8),(18,8)),('C',(44,40),(29,15),(27,40)))
poly('arrow',((36,36),(44,40),(44,32)));join('flow','arrow')
''')
add(8,'SQUARE','The rejected broom reads as a banana with no handle collar or straw structure; dust is a plain circle.','Add an explicit handle collar and a flowing straw edge beside a rounded dust puff.','Lucide broom construction: handle separated from a flaring fan, with asymmetry following the sweep.','One straw division replaces crowded bristles; dust reduced to a single puff.', '''
path(m,'broom',(6,36),('C',(30,16),(18,30),(26,22)),('L',(34,8)),('C',(39,6),(35,6),(38,6)),('C',(42,12),(42,6),(42,9)),('L',(38,23)),('C',(20,42),(35,33),(28,40)))
line('collar',(30,16),(38,23));join('collar','broom')
circle(m,'dust',11,15,5)
''')
add(9,'SQUARE','The rejected cleaver blade is a square diamond and its hanging hole is a filled central dot.','Elongate the blade, move the hollow hanging hole toward the tip and round the diagonal handle.','Lucide axe informs a broad blade and narrower handle with shared corners.','Omit tiny handle rivet.', '''
poly('blade',((29,6),(42,19),(22,39),(9,26),(29,6)))
path(m,'handle',(13,30),('L',(7,36)),('C',(7,41),(5,38),(6,40)),('C',(12,41),(8,43),(10,43)),('L',(18,35)))
join('handle','blade')
circle(m,'hole',28,20,3)
''')
add(10,'SQUARE','The rejected fist reads as a wrench because the knuckles are straight and the thumb is unclear.','Shape rounded knuckles along the diagonal fist and preserve a folded thumb above the forearm.','Shared human hand reference and Lucide hand guide knuckle lobes and a coherent thumb crease.','Reduce internal finger creases to one to keep the fist open at 48 pixels.', '''
path(m,'arm',(6,34),('L',(18,22)),('C',(18,14),(14,18),(15,17)),('L',(24,8)),('C',(30,8),(27,4),(30,6)),('C',(36,14),(34,6),(38,10)),('C',(42,20),(40,12),(42,16)),('C',(40,26),(42,22),(42,24)),('L',(30,34)),('C',(24,34),(28,36),(26,36)),('L',(16,42)))
path(m,'thumb',(30,8),('L',(26,18)),('L',(34,26)))
join('arm','thumb')
''')

extra=ROOT/'more_specs.py'
if extra.exists():exec(extra.read_text())

if __name__=='__main__':
 chosen=[int(v) for v in sys.argv[1:]] or list(SPECS)
 ledger=json.loads((ROOT/'runs.json').read_text()) if (ROOT/'runs.json').exists() else {}
 for i in chosen:
  r=create(i);ledger[str(i)]=r;(ROOT/'runs.json').write_text(json.dumps(ledger,indent=2)+'\n');print(json.dumps(r),flush=True)
