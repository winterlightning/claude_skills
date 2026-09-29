from pathlib import Path
import json,sys,hashlib,shutil
ROOT=Path.cwd();sys.path.insert(0,str(ROOT))
from icon_set.scripts.primitive_fix import load_icon,render_previews
from icon_set.scripts.build_gate import gate
B=ROOT/'icon_set/work/primitive-fix-thuan/batch-20260929T085904Z-meaning'
ITEMS=json.loads((B/'items.json').read_text())
SOURCE_ICON_ID=None
SOURCE_PATH=None
AUTHOR='gpt-6'
DESIGNS={}
def design(i,keyshape,problem,change,body):DESIGNS[i]=(keyshape,problem,change,body)
design(0,'SQUARE','The face perimeter was missing its lower half and the rigid stream read as a lampshade.','Restore the round face and open mouth; draw a downward stream with a scalloped puddle and strained eyes.', '''
path(self,'face',(12,38),('C',(3,30),(4,16),(12,10)),('C',(19,4),(30,4),(37,12)),('C',(45,21),(43,31),(36,38)))
poly(self,'left-eye',(13,17),(17,20),(12,22))
poly(self,'right-eye',(35,17),(31,20),(36,22))
path(self,'mouth',(14,33),('C',(10,25),(38,25),(34,33)))
path(self,'vomit',(18,31),('C',(18,36),(16,37),(13,39)),('C',(9,42),(14,45),(19,41)),('C',(23,45),(26,45),(29,41)),('C',(34,45),(39,42),(35,39)),('C',(32,37),(30,36),(30,31)))
''')
design(1,'VRECT_L','The visor merged into the skull and the face had a stair-step jaw rather than a recognizable profile.','Separate the broad visor, horizontal strap, forehead, nose and rounded chin in a coherent head silhouette.', '''
path(self,'skull',(14,44),('L',(14,36)),('C',(5,27),(5,16),(12,9)),('C',(20,1),(30,4),(35,12)))
box(self,'visor',25,12,42,26,4)
line(self,'strap',(8,21),(25,21))
path(self,'face',(37,26),('L',(40,33)),('L',(35,34)),('L',(35,36)),('A',5,5,True,(30,41)),('L',(26,41)),('L',(26,44)))
''')
design(2,'VRECT_L','The lower face collapsed into a stair-step hook and the headset looked like a loose oval.','Rebuild a left-facing head with a broad visor, strap, distinct nose and rounded chin.', '''
path(self,'skull',(34,44),('L',(34,36)),('C',(43,27),(43,16),(36,9)),('C',(28,1),(18,4),(13,12)))
box(self,'visor',6,12,23,26,4)
line(self,'strap',(40,21),(23,21))
path(self,'face',(11,26),('L',(8,33)),('L',(13,34)),('L',(13,36)),('A',5,5,False,(18,41)),('L',(22,41)),('L',(22,44)))
''')
design(3,'SQUARE','The stylus was reduced to a floating dash, cube became an angular fragment, and goggles lost both lenses.','Restore a pointed stylus, a three-face cube and a compact VR mask with paired lenses.', '''
poly(self,'stylus',(7,5),(15,13),(17,19),(11,17),(3,9),closed=True)
poly(self,'cube-left',(6,22),(18,27),(18,40),(6,34),closed=True)
poly(self,'cube-top',(6,22),(17,17),(29,22),(18,27))
line(self,'cube-right',(29,22),(29,26))
path(self,'goggles',(26,29),('L',(40,29)),('A',4,4,True,(44,33)),('L',(44,41)),('A',3,3,True,(41,44)),('L',(37,44)),('L',(33,40)),('L',(29,44)),('L',(25,44)),('A',3,3,True,(22,41)),('L',(22,33)),('A',4,4,True,(26,29)),closed=True)
self.add_dot('lens-left',(28,35));self.add_dot('lens-right',(38,35))
''')
design(4,'SQUARE','The clock was a C and the two people were disconnected dots and tiny feet.','Close the clock with clear hands; restore two seated bodies with bent knees and short chair backs.', '''
ellipse(self,'clock',11,11,7)
poly(self,'clock-hands',(11,7),(11,11),(14,11))
for x in (25,39):
 ellipse(self,f'head-{x}',x,20,3)
 line(self,f'torso-{x}',(x,31),(x,35))
 self.mark_human_figure(f'person-{x}',head=f'head-{x}',torso=f'torso-{x}',torso_junction='start')
 if x==25:
  poly(self,'legs-left',(25,35),(17,35),(13,43))
  poly(self,'chair-left',(30,30),(30,40),(21,40),(21,44))
 else:
  poly(self,'legs-right',(39,35),(44,35),(44,44))
  poly(self,'chair-right',(34,30),(34,40),(38,40),(38,44))
''')
design(5,'SQUARE','The farmer hat became a rectangular bar, the hoe lost its blade, and the holding arm disappeared.','Restore a brimmed hat, hanging hoe blade and bent supporting arm above a walking pose.', '''
poly(self,'hat',(18,9),(19,4),(27,4),(30,9))
line(self,'brim',(15,10),(32,10))
path(self,'head',(20,12),('A',4,4,False,(28,12)))
line(self,'torso',(24,24),(21,32))
self.mark_human_figure('farmer',head='head',torso='torso',torso_junction='start')
poly(self,'hoe-shaft',(7,18),(42,25))
poly(self,'hoe-blade',(7,18),(6,27),(12,28),(14,20))
poly(self,'supporting-arm',(24,24),(30,30),(36,24))
poly(self,'front-leg',(21,32),(29,38),(32,44))
poly(self,'back-leg',(21,32),(12,44))
''')
design(6,'VRECT_L','The head floated above the torso and the rigid arm arrangement weakened the fast walking action.','Align the head with the leaning torso, open the stride and use opposed bent arms.', '''
ellipse(self,'head',29,9,5)
line(self,'torso',(24,21),(19,33))
self.mark_human_figure('walker',head='head',torso='torso',torso_junction='start')
path(self,'back-arm',(24,21),('C',(17,18),(12,22),(8,29)))
poly(self,'front-arm',(24,21),(31,28),(40,26))
poly(self,'front-leg',(19,33),(29,37),(33,44))
line(self,'back-leg',(19,33),(10,44))
''')
design(7,'HRECT_L','The cash opening merged into the wallet silhouette and the snap tab had no fastener.','Show a separate angled banknote above a rounded wallet and add a clear snap on its closing tab.', '''
path(self,'wallet',(40,23),('L',(40,18)),('A',4,4,False,(36,14)),('L',(8,14)),('A',4,4,False,(4,18)),('L',(4,36)),('A',4,4,False,(8,40)),('L',(36,40)),('A',4,4,False,(40,36)),('L',(40,33)))
poly(self,'banknote',(12,14),(32,8),(35,14))
path(self,'snap-tab',(44,23),('L',(33,23)),('A',5,5,False,(33,33)),('L',(44,33)),('L',(44,23)),closed=True)
self.add_dot('snap',(37,28))
''')
design(8,'SQUARE','The fingers became an angular zigzag and the second hand became a detached diagonal bar.','Reconstruct two overlapping rounded hands with visible finger divisions and soap bubbles.', '''
path(self,'front-hand',(10,41),('C',(2,38),(4,30),(10,25)),('L',(22,17)),('A',3,3,True,(25,22)),('L',(18,28)),('L',(36,28)),('A',3,3,True,(36,34)),('L',(24,34)))
path(self,'fingers',(34,34),('L',(39,34)),('A',3,3,True,(39,40)),('L',(32,40)),('L',(24,40)))
path(self,'palm',(32,40),('A',3,3,True,(29,44)),('L',(17,44)),('C',(14,44),(12,43),(10,41)))
path(self,'back-hand',(22,12),('C',(25,9),(28,12),(31,14)),('L',(40,22)),('C',(43,25),(44,28),(43,31)))
ellipse(self,'bubble-left',10,12,3)
ellipse(self,'bubble-right',37,6,3)
''')
design(9,'HRECT_L','The ball was fused onto a pole-like arm, and the athlete had no readable throwing pose.','Restore a circular ball above a bent throwing arm, a separate aligned head, a reaching arm and water waves.', '''
ellipse(self,'head',20,15,5)
ellipse(self,'ball',38,8,4)
line(self,'torso',(20,28),(22,37))
self.mark_human_figure('player',head='head',torso='torso',torso_junction='start')
poly(self,'throwing-arm',(20,28),(33,27),(38,15),(38,12))
path(self,'reaching-arm',(20,28),('C',(12,26),(8,29),(5,34)))
path(self,'water',(4,39),('C',(9,33),(14,43),(21,39)),('C',(28,33),(34,43),(44,38)))
''')
design(10,'SQUARE','The skier became a head, diagonal arm and wave with no recognizable ski or crouched legs.','Show a crouched skier gripping a tow rope, with bent knees and a separate upturned ski.', '''
ellipse(self,'head',13,9,5)
line(self,'torso',(13,22),(16,30))
self.mark_human_figure('skier',head='head',torso='torso',torso_junction='start')
poly(self,'arms',(13,22),(24,25),(31,21))
line(self,'tow-rope',(31,21),(44,16))
poly(self,'legs',(16,30),(26,32),(29,39))
path(self,'ski',(6,39),('L',(37,39)),('A',5,5,False,(42,34)))
path(self,'water',(6,45),('C',(13,41),(18,47),(25,44)),('C',(31,41),(38,47),(43,43)))
''')
design(11,'SQUARE','The horizontal tow line and gripping arms disappeared, leaving a seated shape on a wave.','Restore forward gripping hands on a straight tow line, a crouched torso and feet on an upturned ski.', '''
ellipse(self,'head',12,9,5)
path(self,'torso',(12,22),('C',(12,27),(13,30),(18,32)))
self.mark_human_figure('skier',head='head',torso='torso-1',torso_junction='start')
poly(self,'arm',(12,22),(26,22),(29,18))
line(self,'rope',(29,18),(44,18))
poly(self,'leg',(18,32),(24,33),(27,39))
path(self,'ski',(5,39),('L',(36,39)),('A',5,5,False,(41,34)))
path(self,'water',(5,45),('C',(13,40),(19,47),(26,44)),('C',(33,40),(38,47),(44,42)))
''')
design(12,'SQUARE','The waving hand had too few fingers and only one motion stroke, making the gesture generic.','Restore four splayed fingertips, the raised thumb and two motion cues around a rounded palm.', '''
path(self,'hand',(12,25),('L',(13,17)),('C',(13,12),(8,12),(8,17)),('L',(6,29)),('C',(5,38),(12,44),(21,43)),('C',(26,42),(29,38),(32,35)),('L',(42,25)),('A',3,3,False,(38,21)),('L',(31,28)),('L',(43,16)),('A',3,3,False,(39,12)),('L',(28,23)),('L',(39,12)),('A',3,3,False,(35,8)),('L',(24,19)),('L',(32,11)),('A',3,3,False,(28,7)),('L',(12,25)),closed=True)
path(self,'motion-left',(3,17),('C',(3,10),(6,6),(11,4)))
path(self,'motion-right',(35,43),('C',(40,41),(43,37),(44,32)))
''')
design(13,'HRECT_L','The dollar sign looked like an S because the vertical stroke had been reduced to tiny end knobs.','Restore an unmistakable vertical dollar bar crossing a smooth S, centered inside the waving banknote.', '''
path(self,'bill',(4,11),('C',(17,2),(31,16),(44,9)),('L',(44,37)),('C',(31,44),(17,30),(4,39)),('L',(4,11)),closed=True)
path(self,'dollar',(29,19),('C',(21,13),(15,23),(24,24)),('C',(34,25),(27,35),(19,29)))
line(self,'dollar-bar',(24,14),(24,34))
''')
design(14,'SQUARE','The earthworm lost its two bends and became a closed peanut-shaped loop.','Rebuild a continuous worm with two alternating bends, rounded endpoints and a clearly tubular silhouette.', '''
path(self,'worm',(6,36),('C',(12,36),(8,10),(18,10)),('C',(30,10),(22,34),(32,34)),('C',(39,34),(29,6),(42,6)),('A',4,4,True,(42,14)),('C',(36,14),(47,42),(32,42)),('C',(15,42),(24,18),(18,18)),('C',(14,18),(22,44),(6,44)),('A',4,4,True,(6,36)),closed=True)
''')
design(15,'SQUARE','The rigid square grip and rectangular stair-step teeth read as a key rather than a wood saw.','Restore an ergonomic rounded grip, enclosed finger opening and repeated saw teeth on a tapered diagonal blade.', '''
path(self,'handle',(6,30),('L',(15,22)),('L',(24,31)),('C',(26,35),(23,38),(20,41)),('L',(16,44)),('C',(14,46),(11,44),(9,42)),('L',(4,37)),('C',(2,35),(3,33),(6,30)),closed=True)
path(self,'grip',(9,34),('L',(14,29)),('L',(19,34)),('A',4,4,True,(14,39)),('L',(9,34)),closed=True)
poly(self,'blade',(16,23),(36,4),(44,11),(39,14),(39,18),(34,20),(33,25),(28,27),(26,32),(24,33))
''')
design(16,'SQUARE','The three hooked nodes lost all connecting arms, so the webhook logo became unrelated curved fragments.','Restore three open circular terminals linked in a triangular cycle, preserving their hook openings.', '''
path(self,'top-hook',(28,7),('A',8,8,False,(16,16)),('L',(10,30)))
path(self,'left-hook',(4,31),('A',8,8,False,(18,38)),('L',(35,38)))
path(self,'right-hook',(36,44),('A',8,8,False,(35,29)),('L',(24,12)))
''')
design(17,'SQUARE','The wheelchair wheel was an isolated C and the person lacked bent knees and feet.','Restore a circular wheel, aligned head and seated torso with a forward arm and bent leg beside a sloped ramp.', '''
ellipse(self,'head',16,8,4)
line(self,'torso',(16,20),(16,29))
self.mark_human_figure('rider',head='head',torso='torso',torso_junction='start')
line(self,'arm',(16,20),(25,22))
poly(self,'leg',(16,29),(24,29),(30,37))
path(self,'wheel',(10,23),('A',10,10,False,(22,39)))
poly(self,'ramp',(24,44),(44,33),(44,44))
''')
design(18,'VRECT_M','The mouse was too round and the two signal arcs crowded it, so it read as a wireless power button.','Give the mouse a long capsule body and scroll wheel with two separated wireless arcs above it.', '''
path(self,'mouse',(14,28),('A',10,10,True,(34,28)),('L',(34,34)),('A',10,10,True,(14,34)),('L',(14,28)),closed=True)
line(self,'scroll-wheel',(24,26),(24,30))
path(self,'signal-outer',(10,9),('C',(18,2),(30,2),(38,9)))
path(self,'signal-inner',(18,14),('C',(22,10),(26,10),(30,14)))
''')
design(19,'SQUARE','The witch lost her eye, mouth, chin and bent hat tip, becoming a pointed hat over an anonymous hook.','Restore a hooked nose, eye and smiling mouth beneath a floppy pointed hat, with flowing hair at the back.', '''
path(self,'hat',(14,18),('C',(21,9),(31,4),(38,4)),('C',(45,4),(42,13),(44,20)),('L',(36,12)),('L',(32,25)))
path(self,'brim',(14,18),('C',(9,12),(5,12),(7,17)),('C',(12,25),(25,31),(35,32)))
path(self,'face',(12,24),('L',(7,29)),('L',(4,30)),('A',3,3,False,(7,33)),('L',(9,33)),('L',(8,38)),('C',(7,44),(16,46),(23,41)))
self.add_dot('eye',(15,29))
path(self,'smile',(10,37),('C',(14,38),(17,37),(19,35)))
path(self,'hair',(27,30),('C',(25,37),(35,36),(34,44)))
''')

def author(indices):
 out=[]
 for i in indices:
  item=ITEMS[i];keyshape,problem,change,body=DESIGNS[i]
  ref=Path(item['reference']);source_uuid=ref.stem[-36:];concept=ref.stem[:-37]
  run=ROOT/'icon_set/work/primitive-make-ray'/source_uuid/'20260929T085904Z-meaning-v1'
  if run.exists():raise RuntimeError(f'Run exists: {run}')
  run.mkdir(parents=True)
  metadata=dict(concept=concept,source_uuid=source_uuid,reference_path=str(ref))
  (run/f"{item['icon_id']}.metadata.json").write_text(json.dumps(metadata,indent=2))
  # All coordinates below are independently authored after viewing the supplied reference.
  code='''from icon_set.model.keyshapes import Keyshape\nfrom icon_set.model.icons.solo._base import Solo48\nfrom icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts\n'''
  code+=f'\nSOURCE_ICON_ID = {source_uuid!r}\nSOURCE_PATH = {str(ref)!r}\nAUTHOR = "gpt-6"\n\n'
  code+=f'# Comparison: {problem}\n# Revision: {change}\n# Plan: coherent subject contours; named parts own attachments; paired features share parameters.\n'
  if i in (4,5,6,9,10,11,17):code+='# Human construction: icon_set/references/human_ref/full_body_ref.png; detached heads use 8 centerline / 4 ink gap at torso junction.\n'
  code+=f'class Drawing(Solo48):\n    icon_id = {item["icon_id"]!r}\n    keyshape = Keyshape.{keyshape}\n    semantic_role = "MAIN"\n    semantic_kind = "noun"\n    category = "objects"\n    aliases = ()\n    keywords = {tuple(concept.split())!r}\n\n    def build(self):\n'
  code+='\n'.join('        '+s for s in body.strip().splitlines())+'\n        contacts(self)\n'
  module=run/(item['icon_id'].replace('-','_')+'_'+source_uuid.replace('-','_')+'.py');module.write_text(code)
  icon=load_icon(module);report=icon.validate_icon();svg=icon.to_svg()
  (run/(item['icon_id']+'.svg')).write_text(svg);(run/'validation.txt').write_text(report.describe())
  render_previews(svg,item['icon_id'],48,run)
  shutil.copyfile(B/f'{i}-reference.png',run/'reference.png');shutil.copyfile(B/f'{i}-before.png',run/'before.png')
  evidence=dict(index=i,**item,**metadata,result_dir=str(run.relative_to(ROOT)),module=str(module.relative_to(ROOT)),author=AUTHOR,comparison=problem,change=change,keyshape=keyshape,validation_status=report.status,errors=report.errors,warnings=report.warnings,omissions='Secondary contour detail simplified to preserve native-size legibility.',lucide='mouse: capsule and scroll wheel; wallet: rounded body and attached tab; accessibility: separated wheel and seated limbs' if i in (7,17,18) else 'No close Lucide subject match; shared smooth contour principles used.',visual_review='pending')
  (run/'review.json').write_text(json.dumps(evidence,indent=2));out.append(evidence)
  print(i,item['icon_id'],report.status,len(report.errors),len(report.warnings),flush=True)
 (B/'runs.json').write_text(json.dumps(out,indent=2))
if __name__=='__main__':author(range(20))
