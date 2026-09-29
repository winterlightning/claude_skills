from pathlib import Path
import json,sys,shutil
ROOT=Path.cwd();sys.path.insert(0,str(ROOT))
from icon_set.scripts.primitive_fix import load_icon,render_previews
B=Path('icon_set/work/primitive-fix-thuan/batch-20260929T091731Z-meaning');ITEMS=json.loads((B/'items.json').read_text())
AUTHOR='gpt-6';DESIGNS={}
def design(i,keyshape,problem,change,omissions,body):DESIGNS[i]=(keyshape,problem,change,omissions,body)
design(0,'SQUARE','The back pins became tall triangular ears and lost their rounded teardrop proportions.','Restore three rounded map pins in an overlapping triangular cluster, with a tapered foreground point.','Pin-center dots omitted because the reference has none.', '''
path(self,'pin-left',(20,15),('C',(21,2),(5,2),(4,12)),('C',(2,18),(8,26),(12,30)),('L',(15,27)))
path(self,'pin-right',(28,15),('C',(27,2),(43,2),(44,12)),('C',(46,18),(40,26),(36,30)),('L',(33,27)))
path(self,'pin-front',(24,44),('C',(21,37),(14,30),(14,25)),('C',(14,12),(34,12),(34,25)),('C',(34,30),(27,37),(24,44)),closed=True)
''')
design(1,'SQUARE','Three regular hollow ovals lost the kidney-bean silhouettes and seed crease.','Draw three organic beans with unequal tilted silhouettes and a clear crease on the upper bean.','Only the upper seed crease is retained, as in the original.', '''
path(self,'bean-top',(18,6),('C',(23,1),(40,7),(43,13)),('C',(49,24),(29,24),(20,16)),('C',(15,12),(14,9),(18,6)),closed=True)
path(self,'crease',(29,11),('C',(32,11),(34,13),(35,15)))
path(self,'bean-left',(5,28),('C',(12,17),(22,20),(18,29)),('C',(17,33),(13,34),(12,38)),('C',(7,46),(0,37),(5,28)),closed=True)
path(self,'bean-right',(26,29),('C',(33,25),(45,33),(44,40)),('C',(43,49),(30,43),(25,37)),('C',(22,34),(22,31),(26,29)),closed=True)
''')
design(2,'SQUARE','The front dumplings became plain circles, so the cluster read as fruit or balls.','Restore flattened dumpling bases, soft domes and short pinched folds on all three buns.','Use two folds per dumpling; no additional texture.', '''
path(self,'back-dumpling',(12,23),('C',(12,14),(15,6),(24,6)),('C',(33,6),(36,14),(36,23)))
path(self,'back-fold-left',(20,7),('C',(22,11),(19,12),(19,15)))
path(self,'back-fold-right',(28,7),('C',(26,11),(29,12),(29,15)))
path(self,'front-left',(24,28),('C',(18,17),(4,21),(4,34)),('C',(4,41),(8,43),(16,43)),('L',(25,42)))
path(self,'front-right',(24,28),('C',(27,21),(42,20),(44,32)),('C',(47,43),(35,44),(28,43)),('C',(21,42),(19,35),(24,28)),closed=True)
path(self,'left-fold-a',(11,23),('C',(13,26),(11,28),(11,29)))
path(self,'left-fold-b',(18,23),('L',(18,28)))
path(self,'right-fold-a',(29,24),('C',(30,27),(28,28),(28,30)))
path(self,'right-fold-b',(37,24),('C',(36,27),(38,28),(38,30)))
''')
design(3,'VRECT_M','The utensil looked like a short-handled trident, with no spoon bowl and no long handle.','Restore a rounded spoon bowl, three short tines and a long narrow handle with a round end.','No decoration or handle texture.', '''
path(self,'spork-outline',(14,4),('C',(7,16),(10,23),(20,25)),('L',(20,40)),('A',4,4,False,(28,40)),('L',(28,25)),('C',(38,23),(41,16),(34,4)))
path(self,'tines',(14,4),('L',(14,12)),('A',5,5,False,(24,12)),('L',(24,4)),('L',(24,12)),('A',5,5,False,(34,12)),('L',(34,4)))
''')
design(4,'HRECT_L','The locomotive lost its large driving wheel, cab window, boiler proportions and flared chimney.','Restore one large driving wheel, two smaller wheels, an upright cab, horizontal boiler and flared smokestack.','Fine wheel spokes and body panel seams omitted.', '''
line(self,'cab-roof',(4,7),(21,7))
poly(self,'cab',(6,26),(6,7),(19,7),(19,28))
box(self,'window',10,13,16,21,1)
path(self,'boiler',(19,18),('L',(39,18)),('A',3,3,True,(42,21)),('L',(42,30)),('L',(23,30)))
poly(self,'stack',(31,18),(31,12),(29,7),(39,7),(37,12),(37,18))
ellipse(self,'driver',13,35,9)
ellipse(self,'driver-hub',13,35,3)
for x in (28,39):ellipse(self,f'wheel-{x}',x,39,4)
poly(self,'front-pilot',(42,30),(45,34),(24,34))
''')
design(5,'SQUARE','Only the top portrait had a recognizable body; the bottom pair became hair-framed dots without shoulders.','Restore three female busts in a pyramid, with parted hair and visible shoulders for the lower pair.','Hair is reduced to a parted cap and short side locks.', '''
# Shared human bust reference; circular heads and shoulder contact at 4 centerline units.
for x,y,r in [(24,11,6),(11,30,6),(37,30,6)]:
 ellipse(self,f'head-{x}',x,y,r)
 path(self,f'hair-{x}',(x-r,y-1),('C',(x-3,y-1),(x-1,y-3),(x,y-4)),('C',(x+1,y-3),(x+3,y-1),(x+r,y-1)))
 poly(self,f'lock-left-{x}',(x-r,y),(x-r-2,y+6))
 poly(self,f'lock-right-{x}',(x+r,y),(x+r+2,y+6))
path(self,'shoulders-top',(17,25),('C',(17,22),(20,21),(24,21)),('C',(28,21),(31,22),(31,25)))
for x in (11,37):
 path(self,f'shoulders-{x}',(x-8,44),('A',8,4,True,(x,40)),('A',8,4,True,(x+8,44)))
 self.relate('connect',f'head-{x}',f'shoulders-{x}')
self.relate('connect','head-24','shoulders-top')
''')
design(6,'SQUARE','The three pens became nearly identical pointed bars and lost their clips and distinct nib shapes.','Restore a fountain nib, sharpened pencil and fine-tip pen, with different barrel tops and clear tip structures.','Clip detail retained on the outer pens; no microscopic nib slit.', '''
box(self,'fountain-barrel',4,6,14,29,2)
path(self,'fountain-nib',(4,29),('C',(3,34),(7,39),(9,43)),('C',(11,39),(15,34),(14,29)))
path(self,'clip-left',(4,10),('C',(2,10),(2,12),(2,16)),('L',(2,23)))
path(self,'pencil',(20,28),('L',(20,8)),('A',4,4,True,(28,8)),('L',(28,28)),('L',(24,44)),('L',(20,28)),closed=True)
line(self,'pencil-band',(20,13),(28,13))
box(self,'pen-barrel',34,6,42,32,1)
poly(self,'fine-nib',(36,32),(36,37),(40,37),(40,32))
line(self,'pen-tip',(38,37),(38,44))
path(self,'clip-right',(42,10),('C',(44,10),(44,12),(44,16)),('L',(44,23)))
''')
design(7,'VRECT_L','The section lost the forehead, mouth cavity and separate throat walls, reading as a bent pipe.','Restore a human head profile with nose and lips, a distinct oral cavity and two curved throat walls.','Small palate and tongue details simplified into continuous contours.', '''
path(self,'head',(12,14),('C',(12,6),(17,4),(24,4)),('C',(40,4),(48,20),(40,30)),('C',(36,35),(39,40),(40,44)))
poly(self,'nose-lip',(12,14),(6,22),(11,23),(11,27))
path(self,'palate',(11,23),('C',(29,16),(36,27),(36,44)))
path(self,'mouth-floor',(11,27),('C',(23,23),(29,29),(29,44)))
path(self,'chin',(12,32),('C',(12,38),(22,36),(22,40)),('L',(22,44)))
''')
for idx in (8,9):
 design(idx,'SQUARE','The shallow cloud and attached bolt read as a mushroom-shaped electric symbol; distinct cloud lobes and detached weather marks were lost.','Restore an asymmetric multi-lobed cloud with a separate zigzag lightning bolt and '+('one rain stroke.' if idx==8 else 'rain strokes on both sides.'),'Rain count follows the original; no extra texture.', '''
path(self,'cloud',(12,28),('C',(1,28),(1,14),(12,14)),('C',(12,2),(27,2),(31,10)),('C',(37,8),(41,12),(40,17)),('C',(48,21),(44,28),(37,28)),('L',(12,28)),closed=True)
poly(self,'lightning',(28,33),(21,39),(28,39),(23,45))
line(self,'rain-left',(12,35),(7,42))
'''+("line(self,'rain-right',(41,35),(36,42))\n" if idx==9 else ''))
design(10,'VRECT_L','The tick resembled a generic six-legged bug with antennae and no separate mouthpart.','Restore an oval tick body, a small front mouthpart and four mirrored pairs of bent legs.','No body spots; all eight legs retained.', '''
path(self,'body',(24,16),('C',(20,16),(18,17),(17,20)),('C',(15,22),(14,24),(14,27)),('L',(14,31)),('C',(14,36),(16,39),(19,42)),('C',(22,45),(26,45),(29,42)),('C',(32,39),(34,36),(34,31)),('L',(34,27)),('C',(34,24),(33,22),(31,20)),('C',(30,17),(28,16),(24,16)),closed=True)
path(self,'mouthpart',(20,17),('L',(20,12)),('A',4,4,True,(28,12)),('L',(28,17)))
for sign in (-1,1):
 def p(x,y):return (24+sign*x,y)
 poly(self,f'foreleg-{sign}',p(7,20),p(13,12),p(12,5))
 poly(self,f'midleg-a-{sign}',p(10,27),p(18,23),p(20,17))
 poly(self,f'midleg-b-{sign}',p(10,31),p(18,34),p(20,39))
 poly(self,f'hindleg-{sign}',p(5,42),p(12,44),p(14,46))
''')
design(11,'SQUARE','The basketball and ticket fused into an arched box, and the ball seams no longer read as a basketball.','Restore a round seamed basketball behind a diagonally notched ticket, plus the small upper ball.','Ticket text reduced to one short line; occluded ball edge is not drawn.', '''
path(self,'basketball',(10,30),('C',(1,26),(0,11),(10,6)),('C',(19,0),(31,8),(31,18)),('C',(31,22),(29,24),(27,26)))
path(self,'ball-seam-a',(4,18),('C',(14,20),(23,14),(28,10)))
path(self,'ball-seam-b',(10,6),('C',(20,13),(19,22),(24,27)))
line(self,'ball-diagonal',(5,10),(25,25))
ellipse(self,'small-ball',42,7,4)
path(self,'ticket',(14,30),('L',(39,22)),('L',(41,28)),('C',(35,30),(38,35),(43,33)),('L',(44,38)),('L',(19,46)),('L',(17,40)),('C',(23,38),(20,33),(15,35)),('L',(14,30)),closed=True)
line(self,'ticket-label',(26,36),(34,33))
''')
design(12,'SQUARE','The two people lost their torsos and legs and the ticket was placed between their shoulders instead of in a raised hand.','Restore two standing figures, with one raising a ticket and the other reaching to inspect it.','Figures use the shared stick-body vocabulary instead of full clothing outlines.', '''
for x in (10,38):
 ellipse(self,f'head-{x}',x,8,4)
 line(self,f'torso-{x}',(x,20),(x,32))
 self.mark_human_figure(f'person-{x}',head=f'head-{x}',torso=f'torso-{x}',torso_junction='start')
 poly(self,f'legs-{x}',(x-4,44),(x,32),(x+4,44))
poly(self,'raised-arm',(10,20),(19,20),(23,12))
box(self,'ticket',21,4,29,12,1)
path(self,'checking-arm',(38,20),('C',(30,20),(32,29),(22,30)))
line(self,'left-outer-arm',(10,20),(5,29))
line(self,'right-outer-arm',(38,20),(44,29))
''')
design(13,'SQUARE','The bag neck looked like a triangle on a circle, while the bin became an unrecognizable slanted frame.','Restore a tied soft garbage bag in front of a tapered open bin with protruding rubbish.','Only one protruding sheet is needed to indicate a full bin.', '''
path(self,'bin',(24,25),('L',(23,17)),('L',(44,17)),('L',(41,44)),('L',(24,44)))
poly(self,'rubbish',(28,17),(31,7),(41,9),(40,17))
poly(self,'bag-tie',(11,25),(9,17),(18,15),(16,25))
path(self,'bag',(13,25),('C',(5,25),(2,34),(4,41)),('C',(5,46),(25,46),(27,41)),('C',(29,35),(21,25),(13,25)),closed=True)
''')
design(14,'SQUARE','The curved basins became a trapezoid and an oval, and the water jets were reduced to two dots.','Restore two rounded basins, a central pedestal and paired arcing water jets.','Pedestal simplified to a short stem and base.', '''
path(self,'lower-basin',(4,32),('L',(44,32)),('A',20,10,True,(4,32)),closed=True)
path(self,'upper-basin',(12,20),('L',(36,20)),('A',12,7,True,(12,20)),closed=True)
line(self,'column',(24,27),(24,32))
line(self,'pedestal',(24,42),(24,45))
line(self,'base',(17,45),(31,45))
line(self,'jet',(24,20),(24,9))
path(self,'jet-left',(24,9),('C',(24,0),(14,1),(14,9)))
path(self,'jet-right',(24,9),('C',(24,0),(34,1),(34,9)))
''')
design(15,'VRECT_L','The champagne bottle became an angular lump with a cross-shaped top, while the bucket lost its rim.','Restore a diagonally tilted bottle with neck and cap, above a flared bucket with a visible rim.','Bottle label omitted because it is hidden inside the cooler.', '''
poly(self,'bottle-cap',(35,4),(43,10),(40,14),(32,8),closed=True)
path(self,'bottle-left',(32,8),('L',(27,15)),('C',(24,16),(20,18),(18,24)))
path(self,'bottle-right',(40,14),('L',(35,21)),('L',(35,24)))
box(self,'rim',6,24,42,30,2)
path(self,'bucket',(8,30),('L',(12,42)),('A',2,2,False,(14,44)),('L',(34,44)),('A',2,2,False,(36,42)),('L',(40,30)))
''')
design(16,'SQUARE','The open pail mouth became a pill-shaped capsule and the drip became a circular ring.','Restore an elliptical tilted opening, a deep pail body and a pointed paint drop.','No handle is added because the reference shows none.', '''
path(self,'rim',(23,5),('C',(27,1),(48,21),(43,25)),('C',(39,29),(18,9),(23,5)),closed=True)
path(self,'pail',(23,5),('L',(5,28)),('C',(2,32),(15,45),(20,43)),('L',(43,25)))
path(self,'paint-drop',(40,33),('C',(36,39),(35,42),(38,44)),('C',(45,47),(47,41),(40,33)),closed=True)
''')
design(17,'SQUARE','The square load shrank, the platform disappeared and the second wheel was omitted.','Restore a large tilted box, a continuous hand-truck frame and platform, and both wheels.','No box markings; keep the plain reference load.', '''
path(self,'handle',(4,4),('C',(8,4),(11,5),(11,9)),('L',(14,32)))
ellipse(self,'wheel-large',14,38,6)
ellipse(self,'wheel-small',40,41,3)
poly(self,'load',(20,18),(37,13),(42,30),(25,35),closed=True)
line(self,'platform',(20,39),(42,34))
''')
design(18,'SQUARE','The person was no longer visibly sitting on a toilet: the bowl and tank were fragmented strokes.','Restore a seated person, tank and bowl, with a bent leg and a clear check mark.','Use one visible leg and simple arms for native-size readability.', '''
ellipse(self,'head',24,8,4)
path(self,'torso',(24,20),('C',(24,23),(22,26),(22,31)))
self.mark_human_figure('person',head='head',torso='torso-1',torso_junction='start')
poly(self,'arm',(24,20),(31,27),(28,29))
poly(self,'leg',(22,31),(34,31),(40,44),(44,44))
poly(self,'tank',(4,34),(4,23),(12,23),(12,34))
path(self,'bowl',(4,34),('L',(27,34)),('C',(27,40),(19,41),(16,41)),('L',(16,44)))
line(self,'base',(14,44),(22,44))
poly(self,'check',(36,10),(39,13),(45,5))
''')
design(19,'SQUARE','The wrong-use figure looked like an ordinary seated person and the toilet was reduced to disconnected strokes.','Show a crouching person with feet on the toilet rim, a complete tank and bowl, and the X mark.','One visible leg carries the crouched pose; no extra arm detail.', '''
ellipse(self,'head',28,8,4)
path(self,'torso',(28,20),('C',(28,23),(26,25),(25,26)))
self.mark_human_figure('person',head='head',torso='torso-1',torso_junction='start')
poly(self,'leg',(25,26),(35,26),(35,34),(30,34))
poly(self,'tank',(4,34),(4,23),(12,23),(12,34))
path(self,'bowl',(4,34),('L',(37,34)),('C',(37,40),(19,41),(16,41)),('L',(16,44)))
line(self,'base',(14,44),(22,44))
line(self,'cross-a',(39,4),(45,10));line(self,'cross-b',(39,10),(45,4))
''')

def author():
 results=[]
 for idx,item in enumerate(ITEMS):
  keyshape,problem,change,omissions,body=DESIGNS[idx];ref=Path(item['reference']);SOURCE_ICON_ID=ref.stem[-36:];SOURCE_PATH=str(ref);concept=ref.stem[:-37]
  run=Path('icon_set/work/primitive-make-ray')/SOURCE_ICON_ID/'20260929T091731Z-meaning-v1';run.mkdir(parents=True,exist_ok=False)
  metadata=dict(concept=concept,source_uuid=SOURCE_ICON_ID,reference_path=SOURCE_PATH);(run/(item['icon_id']+'.metadata.json')).write_text(json.dumps(metadata,indent=2))
  code='from icon_set.model.keyshapes import Keyshape\nfrom icon_set.model.icons.solo._base import Solo48\nfrom icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts\n\n'
  code+=f'SOURCE_ICON_ID = {SOURCE_ICON_ID!r}\nSOURCE_PATH = {SOURCE_PATH!r}\nAUTHOR = "gpt-6"\n\n# Original/rejected comparison: {problem}\n# Revision: {change}\n# Symbol plan: named contours own silhouettes; paired features share dimensions and attachment nodes.\n'
  code+=f'class Drawing(Solo48):\n    icon_id = {item["icon_id"]!r}\n    keyshape = Keyshape.{keyshape}\n    semantic_role = "MAIN"\n    semantic_kind = "noun"\n    category = "objects"\n    aliases = ()\n    keywords = {tuple(concept.split())!r}\n'
  if idx==5:code+='    human_construction = "bust"\n'
  code+='\n    def build(self):\n'+'\n'.join('        '+line for line in body.strip().splitlines())+'\n        contacts(self)\n'
  module=run/(item['icon_id'].replace('-','_')+'_'+SOURCE_ICON_ID.replace('-','_')+'.py');module.write_text(code)
  icon=load_icon(module);rep=icon.validate_icon();svg=icon.to_svg();(run/(item['icon_id']+'.svg')).write_text(svg);(run/'validation.txt').write_text(rep.describe());render_previews(svg,item['icon_id'],48,run)
  for kind in ['reference','before']:shutil.copyfile(B/f'{idx}-{kind}.png',run/f'{kind}.png')
  r=dict(index=idx,**item,**metadata,result_dir=str(run),module=str(module),author=AUTHOR,comparison=problem,change=change,omissions=omissions,keyshape=keyshape,validation_status=rep.status,errors=rep.errors,warnings=rep.warnings,visual_review='pending')
  (run/'review.json').write_text(json.dumps(r,indent=2));results.append(r);print(idx,item['icon_id'],rep.status,flush=True)
 (B/'runs.json').write_text(json.dumps(results,indent=2))
if __name__=='__main__':author()
