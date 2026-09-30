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
    path(m,n,(x-r,y),('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),closed=True)
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
    run=Path('icon_set/work/primitive-make-ray')/uuid/(datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')+'-batch08')
    run.mkdir(parents=True);name=e['item']['icon_id']
    metadata={'concept':concept,'source_uuid':uuid,'reference_path':ref}
    (run/(name+'.metadata.json')).write_text(json.dumps(metadata,indent=2)+'\n')
    (run/'review-before.txt').write_text(s['issue']+'\nFeedback: none recorded.\n'+s['change']+'\n')
    module=run/(name.replace('-','_')+'_'+uuid.replace('-','_')+'.py')
    code=repr(s['issue']+'\nSymbol plan: '+s['change']+'\nConstruction: '+s['construction']+'\nOmissions: '+s['omissions'])+'\n'
    code+='from icon_set.model.keyshapes import Keyshape\nfrom icon_set.model.icons.solo._base import Solo48\n'
    code+=f'SOURCE_ICON_ID = {uuid!r}\nSOURCE_PATH = {ref!r}\nAUTHOR = {AUTHOR!r}\n'+HELPERS
    code+=f"\nclass Drawing(Solo48):\n    icon_id = {name!r}\n    keyshape = Keyshape.{s['keyshape']}\n    semantic_role = 'MAIN'\n    semantic_kind = 'noun'\n    category = 'primitives-generate'\n    aliases = ()\n    keywords = {tuple(name.split('-'))!r}\n    def build(self):\n"
    code+=textwrap.indent("m=self\nline=self.add_line\npoly=self.add_polyline\njoin=lambda a,b:self.relate('connect',a,b)\n"+s['code'],'        ')+'\n'
    module.write_text(code)
    icon=f.load_icon(module); report=icon.validate_icon(); gate=build_gate.gate(module)
    (run/(name+'.svg')).write_text(icon.to_svg());f.render_previews(icon.to_svg(),name,48,run)
    (run/'validation.txt').write_text(report.describe()+'\n'+json.dumps(gate,indent=2)+'\n')
    result={**metadata,'icon_id':name,'author':AUTHOR,'validation_status':report.status,'errors':list(report.errors),'warnings':list(report.warnings),'build_gate':gate,'visual_review':'pending','omissions':s['omissions'],'keyshape':s['keyshape'],'module':module.name,'svg':name+'.svg','review':s['issue'],'change':s['change'],'construction':s['construction']}
    (run/'draft.json').write_text(json.dumps(result,indent=2)+'\n')
    return {'index':i,'key':e['key'],'run':str(run),'module':str(module),'status':report.status,'gate':gate['status'],'errors':list(report.errors)+gate['errors'],'warnings':list(report.warnings)+gate['warnings']}

add(1,'HRECT_L','The rejected border walker has a stiff symmetrical stride and a vertical upper boundary dash.','Bend the forward knee, reach the front arm and align both boundary marks diagonally.','human_ref/full_body_ref.png: circular head and coherent limbs, head bottom16 to torso24 =8 centerline units. Lucide flag: joined pole and flag.','Outline body reduced to strokes; two border dashes retained.',"""
circle(m,'head',16,12,4)
line('torso',(16,24),(16,30))
poly('arms',(6,28),(10,24),(16,24),(22,26))
poly('legs',(8,40),(16,30),(24,34),(26,40))
poly('flag',(32,28),(32,8),(44,14),(32,20))
line('boundary-a',(4,8),(6,10));line('boundary-b',(36,34),(44,40))
join('torso','arms');join('torso','legs')
m.mark_human_figure('walker',head='head',torso='torso',torso_junction='start')
""")
add(2,'HRECT_M','The rejected visor is too tall and has a deep narrow nose notch.','Flatten the wide upper visor and make a broad shallow mirrored nose notch.','Lucide glasses original and atomic-debug: mirrored eye-area balance; supplied reference owns the blank visor.','None.',"""
path(m,'visor',(24,10),('C',(4,24),(8,10),(4,12)),('C',(14,38),(4,32),(8,38)),('C',(24,30),(18,38),(20,30)),('C',(34,38),(28,30),(30,38)),('C',(44,24),(40,38),(44,32)),('C',(24,10),(44,12),(40,10)),closed=True)
""")
add(3,'CIRCLE','The rejected coin replaces the reference central ring with a solid dot.','Restore a small hollow central ring and six evenly paired satellite dots inside the coin.','No useful exact Lucide match; concentric circular construction from the supplied reference.','Satellite count reduced to six to preserve a clear central ring.',"""
circle(m,'coin',24,24,20);circle(m,'center-ring',24,24,3)
for j,p in enumerate(((24,12),(34,18),(34,30),(24,36),(14,30),(14,18))):m.add_dot('satellite-'+str(j),p)
""")
add(4,'SQUARE','The rejected narwhal has a square tail block and omits the projecting flipper.','Round the tail into two lobes, recover a projecting lower flipper and lengthen the tusk.','No useful local Lucide narwhal match. Supplied reference owns the asymmetrical swimming silhouette.','Fine tusk outline reduced to a single stroke; eye retained.',"""
path(m,'animal',(32,16),('C',(13,31),(22,8),(20,21)),('C',(6,28),(12,27),(8,26)),('C',(10,35),(6,32),(7,34)),('C',(6,42),(7,37),(6,39)),('C',(17,36),(12,42),(15,40)),('C',(25,38),(19,37),(22,38)),('C',(29,34),(25,41),(28,39)),('C',(40,24),(36,34),(40,30)),('C',(32,16),(40,19),(36,16)),closed=True)
line('tusk',(32,16),(42,6));join('animal','tusk');m.add_dot('eye',(30,26))
""")
add(5,'CIRCLE','The rejected stick is a broad pill with almost no straight shaft.','Restore a slender upright capsule with long parallel sides and equal round ends, touching the radial envelope at top and bottom.','No useful exact Lucide stick match; equal semicircle ends and parallel sides.','None.',"""
path(m,'stick',(20,8),('A',(28,8),4,4,True),('L',(28,40)),('A',(20,40),4,4,True),('L',(20,8)),closed=True)
""")
add(6,'CIRCLE','The rejected oar has a broad squat blade and a short shaft.','Restore a narrow rounded blade and long centered shaft with a smooth blade-to-shaft taper.','No useful exact Lucide oar match; supplied reference owns the upright proportions.','None.',"""
path(m,'blade',(17,11),('A',(31,11),7,7,True),('L',(31,17)),('C',(24,26),(31,21),(28,24)),('C',(17,17),(20,24),(17,21)),('L',(17,11)),closed=True)
line('shaft',(24,26),(24,44));join('shaft','blade')
""")
add(7,'HRECT_L','The rejected palm ends in a broad curved bowl and an arbitrary gap instead of a wrist.','Restore two upright wrist sides below the palm, preserving four unequal rounded fingers and the outward thumb.','Lucide hand original and atomic-debug: four rounded fingertips and shared finger creases. Human reference supplies simple anatomy.','Palm crease omitted to preserve finger-to-palm clearance.',"""
heights=(14,12,14,20);members=[]
for i,y in enumerate(heights):
 x=12+i*8
 if i==0:line('rise',(12,28),(12,y));members.append('rise')
 else:line('rise'+str(i),(x,heights[i-1]),(x,y));members.append('rise'+str(i))
 m.add_arc('tip'+str(i),(x,y),(x+8,y),radius_x=4);members.append('tip'+str(i))
line('side',(44,20),(44,28));m.add_bezier('right-palm',(44,28),((44,34),(36,34),(36,40)))
m.add_contour('fingers',*members,'side','right-palm')
path(m,'left-palm',(20,40),('C',(12,32),(20,36),(16,35)),('L',(4,26)),('C',(12,28),(4,20),(8,22)))
join('left-palm','fingers')
for i,end in enumerate((24,24,26)):
 x=20+i*8;line('crease'+str(i),(x,max(heights[i],heights[i+1])),(x,end));join('crease'+str(i),'fingers')
""")
add(8,'VRECT_M','The rejected eyedropper has a short bulb, a stubby nozzle and an oversized drop.','Lengthen the tube below a high collar, round the bulb and reduce the detached falling drop.','Lucide pipette original and atomic-debug: collar attached to a longer tube. Supplied reference owns vertical orientation.','Inner reservoir omitted; detached droplet simplified to a small circular drop.',"""
path(m,'tube',(18,10),('A',(30,10),6,6,True),('L',(30,14)),('L',(30,24)),('C',(24,32),(30,28),(24,28)),('C',(18,24),(24,28),(18,28)),('L',(18,14)),('L',(18,10)),closed=True)
line('collar-left',(10,14),(18,14));line('collar-right',(30,14),(38,14));join('tube','collar-left');join('tube','collar-right')
circle(m,'drop',24,42,2)
""")
add(9,'VRECT_L','The rejected femur has a long curved outer shaft and a small head, reading like a bent tube.','Enlarge the rounded femoral head, restore the short inward neck and narrow the straight lower shaft.','No useful exact Lucide anatomy match; supplied femur reference owns the asymmetrical head and projection.','None.',"""
path(m,'bone',(16,44),('C',(8,26),(16,32),(8,33)),('C',(18,21),(8,17),(14,17)),('C',(22,17),(22,24),(24,21)),('C',(30,4),(18,10),(23,4)),('C',(40,14),(36,4),(40,8)),('C',(31,24),(40,21),(36,24)),('C',(28,34),(27,24),(28,30)),('L',(28,44)))
""")
add(10,'VRECT_L','The rejected gopher has pointed flared feet and no forepaws, unlike the rounded plump reference.','Round the lower body and feet and restore paired tucked forepaw marks below a small face.','Lucide mouse original and atomic-debug informs smooth rounded enclosure; reference owns ears, muzzle and paws.','Tiny toe and mouth details omitted.',"""
path(m,'body',(8,10),('A',(18,10),5,6,True),('C',(30,10),(21,8),(27,8)),('A',(40,10),5,6,True),('C',(40,32),(38,19),(40,24)),('C',(34,44),(40,38),(40,44)),('L',(28,44)),('C',(20,44),(26,41),(22,41)),('L',(14,44)),('C',(8,32),(8,44),(8,38)),('C',(8,10),(8,24),(10,19)),closed=True)
m.add_dot('eye-left',(18,19));m.add_dot('eye-right',(30,19));line('muzzle',(24,27),(24,29))
path(m,'paw-left',(16,33),('C',(18,35),(16,35),(17,35)))
path(m,'paw-right',(32,33),('C',(30,35),(32,35),(31,35)))
""")
add(11,'SQUARE','The rejected wedding scene has solid-dot heads, tiny fork bodies and a flattened heart ornament.','Use visible circular heads and a taller pointed heart, and separate the groom torso and bride gown under the arch.','human_ref/full_body_ref.png: circular heads and detached bodies. Head bottom26 to body34 =8 centerline units /4 ink.','Arms and gown hem simplified at this scale.',"""
path(m,'heart',(24,10),('C',(16,10),(20,2),(16,6)),('C',(24,15),(16,12),(21,14)),('C',(32,10),(27,14),(32,12)),('C',(24,10),(32,6),(28,2)),closed=True)
for side in (-1,1):
 def p(x,y):return (24+side*x,y)
 path(m,'arch'+str(side),p(18,42),('L',p(18,22)),('C',p(8,10),p(18,14),p(14,10)))
 join('arch'+str(side),'heart')
for name,x in [('groom',17),('bride',31)]:circle(m,name+'-head',x,23,3)
line('groom-torso',(17,34),(17,38));poly('groom-legs',(14,42),(17,38),(20,42));join('groom-torso','groom-legs')
poly('groom-arms',(13,34),(17,34),(21,34));join('groom-arms','groom-torso')
poly('bride-gown',(28,42),(31,34),(34,42))
m.mark_human_figure('groom',head='groom-head',torso='groom-torso',torso_junction='start')
""")
add(12,'CIRCLE','The rejected weary face uses straight eye dashes and a cramped tiny frown.','Curve both closed eyelids, soften the worried brows and widen the frown.','No useful exact Lucide expression match; supplied face reference owns the expression and symmetry.','None.',"""
circle(m,'face',24,24,20)
path(m,'brow-left',(17,15),('C',(20,14),(18,15),(19,15)))
path(m,'brow-right',(31,15),('C',(28,14),(30,15),(29,15)))
path(m,'eye-left',(14,23),('C',(19,23),(15,25),(18,25)))
path(m,'eye-right',(29,23),('C',(34,23),(30,25),(33,25)))
m.add_arc('frown',(18,33),(30,33),radius_x=6,radius_y=2,sweep=True)
""")
add(13,'VRECT_L','The rejected wheat grains form stacked semicircular bowls instead of pointed kernels.','Use a pointed terminal kernel and a mirrored pair of slanted pointed side kernels on a long stem.','Lucide wheat original and atomic-debug: pointed repeated grain loops attached to a shared stem.','Three pairs reduced to one broad pair to preserve open grain interiors.',"""
path(m,'terminal',(24,4),('C',(30,12),(27,7),(30,8)),('C',(24,20),(30,16),(27,18)),('C',(18,12),(21,18),(18,16)),('C',(24,4),(18,8),(21,7)),closed=True)
line('stem',(24,20),(24,44));join('stem','terminal')
for side in (-1,1):
 def p(x,y):return (24+side*x,y)
 path(m,'grain'+str(side),p(0,36),('C',p(16,24),p(0,28),p(10,24)),('C',p(0,36),p(16,34),p(10,36)),closed=True)
 join('grain'+str(side),'stem')
join('grain-1','grain1')
""")
add(14,'SQUARE','The rejected fencer has a flattened wheel and a short upward stub for the blade.','Restore a round rear wheel arc and a longer fencing blade with a compact upright guard.','human_ref/full_body_ref.png: head bottom14 to torso22 gives exact4-unit ink gap. Lucide accessibility and sword original/atomic-debug: open round wheel and visible blade.','Lower sword guard and wheel spokes omitted.',"""
circle(m,'head',16,10,4);line('torso',(16,22),(16,30));m.mark_human_figure('fencer',head='head',torso='torso',torso_junction='start')
poly('leg',(16,30),(28,30),(32,42));join('torso','leg')
line('arm',(16,22),(28,22));line('guard',(28,18),(28,22));line('sword',(28,22),(42,14));join('arm','torso');join('arm','guard');join('arm','sword');join('guard','sword')
path(m,'wheel',(16,22),('A',(6,32),10,10,False),('A',(16,42),10,10,False),('A',(22,40),10,10,False));join('wheel','torso');join('wheel','arm')
""")
add(15,'SQUARE','The rejected wheelchair omits the armrest, footrest and rear-wheel hub, and its front caster looks detached.','Restore the armrest and projecting footrest with a smaller outlined caster below them and a visible rear-wheel hub.','Lucide accessibility original/atomic-debug: circular rear wheel and simple frame. Source owns the empty chair.','Extra parallel seat rail omitted.',"""
circle(m,'wheel',16,32,10);m.add_dot('hub',(16,32))
poly('back',(8,6),(16,6),(16,14),(16,22));join('back','wheel')
poly('seat',(16,22),(28,22),(32,22),(40,30),(42,30));join('seat','wheel');join('seat','back')
poly('armrest',(16,14),(28,14),(28,22));join('armrest','back');join('armrest','seat')
circle(m,'caster',40,40,2)
""")
add(16,'SQUARE','The rejected excavator bucket is a small hook and the wheels are undersized.','Enlarge the wheels, lower the cab/body band and open the bucket into a broad curved scoop.','No useful exact local Lucide excavator match; reference owns wheeled chassis, articulated boom and scoop.','Hydraulic lines and interior cab detail omitted.',"""
circle(m,'rear-wheel',10,38,4);circle(m,'front-wheel',23,39,3)
box(m,'body',6,18,28,26,3)
poly('cab',(10,18),(10,10),(20,10),(24,18));join('cab','body')
poly('boom',(28,18),(38,6),(42,24));join('boom','body')
path(m,'bucket',(42,24),('L',(42,28)),('C',(34,34),(42,34),(38,36)),('L',(31,30)));join('bucket','boom')
""")
add(17,'SQUARE','The rejected passion fruit half is a flat circle, with no bowl depth.','Restore a horizontal cut opening and rounded lower shell in front of the whole fruit.','Lucide citrus original/atomic-debug: distinct cut face and shell; source owns the front-left cut half.','Scalloped supporting flourish and fine interior detail omitted; one seed mark retained.',"""
oval(m,'cut-face',18,26,12,8)
path(m,'shell',(6,26),('C',(18,42),(6,37),(10,42)),('C',(30,26),(26,42),(30,37)))
join('shell','cut-face')
path(m,'whole',(18,18),('C',(30,6),(18,10),(24,6)),('C',(42,20),(38,6),(42,12)),('C',(30,26),(42,29),(36,31)))
join('whole','cut-face');join('whole','shell');m.add_dot('seed',(18,26))
""")
add(18,'SQUARE','The rejected lemon is a small rounded bulb under a disproportionately distant leaf.','Elongate the lemon body, smooth its lower tip and bring its mass upward toward the single leaf.','Lucide leaf original/atomic-debug: pointed closed leaf and a short attached stem.','None.',"""
path(m,'lemon',(6,42),('C',(6,30),(9,39),(6,35)),('C',(22,20),(6,23),(15,20)),('C',(28,35),(32,20),(34,27)),('C',(16,42),(24,40),(21,42)),('C',(6,42),(12,42),(12,38)),closed=True)
path(m,'leaf',(32,14),('C',(42,6),(32,6),(36,6)),('C',(32,14),(42,14),(38,14)),closed=True)
line('stem',(32,14),(22,20));join('stem','leaf');join('stem','lemon')
""")
add(19,'SQUARE','The rejected nutmeg groove is a short tick and the cut kernel is a solid dot.','Lengthen the whole-nut groove and restore a hollow kernel in the foreground half.','No useful exact local Lucide nutmeg match. Source owns the asymmetric overlap and groove.','Irregular kernel contour reduced to a small circular outline.',"""
path(m,'whole',(20,31),('C',(6,22),(10,34),(6,30)),('C',(24,6),(6,10),(16,6)),('C',(31,20),(32,6),(34,12)))
circle(m,'half',31,31,11);circle(m,'kernel',31,31,3);join('whole','half')
line('groove',(15,22),(22,14))
""")
add(20,'SQUARE','The rejected coconut half is a front-facing circle bisected by a horizontal line.','Tilt the cut rim and give the half a deeper rounded shell in front of the whole coconut.','Lucide citrus original/atomic-debug: clear cut-surface boundary. Reference owns the diagonal foreground half.','Fine concentric inner rim omitted.',"""
path(m,'whole',(10,30),('C',(6,20),(7,28),(6,24)),('C',(20,6),(6,12),(12,6)),('C',(27,8),(23,6),(25,7)))
path(m,'half',(18,30),('C',(38,18),(16,21),(30,13)),('C',(42,30),(42,21),(42,25)),('C',(30,42),(42,38),(37,42)),('C',(18,30),(24,42),(20,37)),closed=True)
path(m,'rim',(18,30),('C',(38,18),(26,34),(39,24)));join('rim','half')
""")

# Second construction pass; every create() writes a fresh run.
SPECS[1]['code']=SPECS[1]['code'].replace("16,12","18,12").replace("(16,24),(16,30)","(18,24),(18,32)").replace("(10,24),(16,24),(22,26)","(10,24),(18,24),(24,26)").replace("(16,30),(24,34),(26,40)","(18,32),(26,36),(28,40)").replace("(36,34),(44,40)","(38,36),(44,40)")
SPECS[3]['code']=SPECS[3]['code'].replace("((24,12),(34,18),(34,30),(24,36),(14,30),(14,18))","((16,16),(32,16),(32,32),(16,32))")
SPECS[3]['change']=SPECS[3]['change'].replace('six','four');SPECS[3]['omissions']='Satellite count reduced to four to preserve the hollow central ring.'
SPECS[4]['code']=SPECS[4]['code'].replace("(30,26)","(30,25)")
SPECS[7]['code']=SPECS[7]['code'].replace("('C',(12,32),(20,36),(16,35))","('C',(12,36),(20,38),(16,40))").replace("(4,20),(8,22)","(4,18),(8,22)")
SPECS[9]['code']=SPECS[9]['code'].replace("('C',(28,34),(27,24),(28,30)),('L',(28,44))","('C',(32,34),(30,24),(32,30)),('L',(32,44))")
SPECS[10]['code']=SPECS[10]['code'].replace("(16,33),('C',(18,35),(16,35),(17,35))","(17,33),('C',(18,35),(17,34),(17,35))").replace("(32,33),('C',(30,35),(32,35),(31,35))","(31,33),('C',(30,35),(31,34),(31,35))")
SPECS[11]['code']=SPECS[11]['code'].replace("('C',(16,10),(20,2),(16,6))","('A',(16,10),4,4,False)").replace("('C',(24,10),(32,6),(28,2))","('A',(24,10),4,4,False)").replace('(24,15)','(24,14)').replace("x,23,3","x,24,3").replace('(17,34)','(17,35)').replace('(13,34)','(14,35)').replace('(21,34)','(20,35)').replace('(31,34)','(31,35)')
SPECS[11]['code']=SPECS[11]['code'].replace("path(m,'arch'+str(side),p(18,42),('L',p(18,22)),('C',p(8,10),p(18,14),p(14,10)))","line('post'+str(side),p(18,42),p(18,22))\n path(m,'arch'+str(side),p(18,22),('C',p(8,10),p(18,14),p(14,10)))\n join('post'+str(side),'arch'+str(side))")
SPECS[11]['construction']=SPECS[11]['construction'].replace('bottom26 to body34','bottom27 to body35')
SPECS[12]['code']=SPECS[12]['code'].replace("(18,33),(30,33)","(18,34),(30,34)")
SPECS[13]['code']=SPECS[13]['code'].replace("p(0,28),p(10,24)","p(6,30),p(10,26)")
SPECS[16]['code']=SPECS[16]['code'].replace("'front-wheel',23,39,3","'front-wheel',26,39,3").replace("('L',(31,30))","('L',(33,30))")
SPECS[17]['code']=SPECS[17]['code'].replace("18,26,12,8","18,25,12,9").replace('(6,26)','(6,25)').replace('(30,26)','(30,25)').replace('(18,18)','(18,16)').replace("(18,26)","(18,25)")
SPECS[19]['code']=SPECS[19]['code'].replace("circle(m,'kernel',31,31,3)","path(m,'kernel',(29,32),('C',(33,30),(31,32),(31,30)))").replace("(15,22),(22,14)","(14,20),(18,15)")
SPECS[19]['change']='Lengthen the whole-nut groove and restore an irregular kernel mark in the foreground half.'
SPECS[19]['omissions']='Irregular kernel outline simplified to a compact wavy stroke.'
SPECS[20]['code']=SPECS[20]['code'].replace("(10,30)","(9,29)")
# Semicircular loops preserve exact cardinal human clearance analytically.
HELPERS=HELPERS.replace("('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)","('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)")

SPECS[1]['code']=SPECS[1]['code'].replace('(18,32)','(18,33)').replace('(26,36)','(26,37)')
SPECS[11]['code']=SPECS[11]['code'].replace('(24,14)','(24,15)').replace('x,24,3','x,25,3').replace('(17,35)','(17,36)').replace('(14,35)','(14,36)').replace('(20,35)','(20,36)').replace('(31,35)','(31,36)')
SPECS[11]['construction']=SPECS[11]['construction'].replace('bottom27 to body35','bottom28 to body36')
SPECS[14]['code']=SPECS[14]['code'].replace("('A',(6,32),10,10,False),('A',(16,42),10,10,False),('A',(22,40),10,10,False)","('C',(6,32),(10,22),(6,26)),('C',(16,42),(6,38),(10,42)),('C',(22,40),(18,42),(20,41))")
SPECS[16]['code']=SPECS[16]['code'].replace("'rear-wheel',10,38,4","'rear-wheel',9,39,3").replace("'front-wheel',26,39,3","'front-wheel',24,39,3")
SPECS[16]['change']='Rebalance the paired wheels, lower the cab/body band and open the bucket into a broad curved scoop.'
SPECS[19]['code']=SPECS[19]['code'].replace('(18,15)','(18,16)')
SPECS[13]['code']="""
oval(m,'terminal',24,10,4,6)
line('stem',(24,16),(24,44));join('stem','terminal')
for side in (-1,1):
 def p(x,y):return (24+side*x,y)
 path(m,'grains'+str(side),p(0,16),('C',p(16,12),p(6,14),p(10,12)),('C',p(0,28),p(16,24),p(8,28)),('C',p(16,24),p(6,26),p(10,24)),('C',p(0,40),p(16,36),p(8,40)))
 join('grains'+str(side),'stem');join('grains'+str(side),'terminal')
join('grains-1','grains1')
"""
SPECS[13]['change']='Restore two mirrored tiers of pointed slanted grains around a terminal grain and a shared upright stem.'
SPECS[13]['omissions']='Three pairs reduced to two broad pairs to preserve open grain interiors.'

SPECS[13]['code']=SPECS[13]['code'].replace("('C',p(16,24),p(6,26),p(10,24))","('C',p(16,28),p(6,28),p(10,28))")
SPECS[13]['change']='Restore two mirrored tiers of grains with rising pointed upper tips and a shared upright stem.'
SPECS[19]['code']=SPECS[19]['code'].replace('(14,20)','(15,20)')
if __name__=='__main__':
    chosen=[int(v) for v in sys.argv[1:]] or list(SPECS)
    ledger=json.loads((ROOT/'runs.json').read_text()) if (ROOT/'runs.json').exists() else {}
    for i in chosen:
        r=create(i);ledger[str(i)]=r;(ROOT/'runs.json').write_text(json.dumps(ledger,indent=2)+'\n');print(json.dumps(r),flush=True)
