from pathlib import Path
import json,sys,textwrap,runpy
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[3]
sys.path.insert(0,str(ROOT))
ITEMS=json.loads((HERE/'items.json').read_text())
HELPERS=runpy.run_path(str(ROOT/'icon_set/work/primitive-fix-thuan/batch-20260928T175102Z/_author_batch.py'))['HELPERS']
AUTHOR='gpt-6'
SOURCE_PATH=str(HERE/'items.json')
SOURCE_ICON_ID={it['id']:Path(it['ref']).stem[-36:] for it in ITEMS}
DESIGNS={}
def design(i,shape,finding,change,code,reference='Supplied original; no useful local Lucide subject match.',omissions='No identifying features omitted.'):
 DESIGNS[i]=dict(shape=shape,finding=finding,change=change,code=textwrap.dedent(code),reference=reference,omissions=omissions)

design(0,'SQUARE','The rejected horse is a squared chair-like outline; the rider has no recognizable seated leg or forward lean. The source shows a leaning rider on an elevated horse neck.',
 'Restore a curved horse back, sloping neck, muzzle, pointed ear and bent foreleg. Draw a separate circular rider head, leaning torso and bent seated leg, preserving the source close crop.', '''
path('horse',(4,33),[('C',(15,27),(6,28),(10,27)),('L',(28,27)),('L',(33,17)),('L',(36,14)),('L',(36,18)),('L',(44,25)),('C',(41,28),(46,27),(43,29)),('L',(35,26)),('L',(30,35)),('L',(35,39)),('L',(34,44))])
poly('foreleg',(30,35),(27,39),(26,44));join('horse','foreleg')
circle('head',24,8,4)
path('torso',(24,20),[('C',(18,27),(24,23),(20,24))])
poly('arm',(24,20),(29,25),(33,24))
poly('rider-leg',(18,27),(22,33),(18,39))
join('torso','arm');join('torso','rider-leg');join('rider-leg','horse')
self.mark_human_figure('rider',head='head',torso='torso-0',torso_junction='start')
''','human_ref/full_body_ref.png: outlined head and coherent bent limbs; source defines equestrian action.','Fine helmet seam omitted; source cropped horse retained.')
design(1,'HRECT_M','The rejected chain ends flare into angular brackets and the links are too tall. The source has two horizontal rounded-rectangle links with a central connecting bar.',
 'Rebuild two equally sized, low rounded links with inward openings and a centered horizontal connector. Keep the broad natural chain proportions.', '''
path('left-link',(21,19),[('A',(17,14),5,5,False),('L',(10,14)),('A',(4,20),6,6,False),('L',(4,28)),('A',(10,34),6,6,False),('L',(17,34)),('A',(21,29),5,5,False)])
path('right-link',(27,19),[('A',(31,14),5,5,True),('L',(38,14)),('A',(44,20),6,6,True),('L',(44,28)),('A',(38,34),6,6,True),('L',(31,34)),('A',(27,29),5,5,True)])
line('connector',(16,24),(32,24))
''','Lucide link-2 original and atomic-debug: two opposed rounded ends and a separate central connector.')
design(2,'HRECT_L','The rejected figure merges into the horse back and has neither a tow rope nor a recognizable ski; it reads as a malformed rider rather than skijoring.',
 'Separate a crouching skier behind the horse, with a long ski and a taut tow line to the horse harness. Restore the horse muzzle, curved neck, body and two legs.', '''
circle('head',10,7,3)
path('torso',(10,18),[('C',(7,27),(10,21),(8,24))])
poly('arm',(10,18),(16,23),(20,23))
poly('skier-leg',(7,27),(13,31),(11,39))
path('ski',(3,40),[('L',(17,40)),('A',(20,37),3,3,False)])
line('tow-rope',(20,23),(32,25))
path('horse',(24,40),[('L',(24,30)),('C',(28,26),(24,27),(26,26)),('L',(32,26)),('C',(37,15),(33,20),(33,16)),('L',(40,14)),('L',(39,18)),('L',(45,23)),('L',(40,24)),('L',(38,30)),('L',(38,40))])
line('belly',(24,33),(38,33))
for n in ['arm','skier-leg']:join('torso',n)
join('arm','tow-rope');join('horse','belly')
self.mark_human_figure('skier',head='head',torso='torso-0',torso_junction='start')
''','human_ref/full_body_ref.png: circular head, bent limbs; source defines the ski/tow-line/horse relationship.','Far horse legs and a second ski omitted for legibility.')
design(3,'SQUARE','The rejected horse is a rigid rectangular frame and the rider looks like a vertical post; the original has a full animal body, tail, muzzle and seated rider.',
 'Restore the full horse silhouette with curved rump, tail, sloping chest and separate front/rear legs. Add an upright rider with a bent leg and forward arm.', '''
path('horse',(8,42),[('L',(8,32)),('C',(14,26),(8,28),(10,26)),('L',(29,26)),('L',(35,15)),('L',(36,20)),('L',(44,26)),('L',(42,29)),('L',(36,27)),('L',(33,34)),('L',(34,44)),('L',(29,44)),('L',(27,35)),('L',(15,35)),('L',(13,44)),('L',(8,44)),('L',(8,42))],True)
path('tail',(10,28),[('C',(4,34),(5,26),(5,29))]);join('horse','tail')
circle('head',20,7,3)
line('torso',(20,18),(20,27))
poly('arm',(20,18),(25,23),(30,23))
poly('rider-leg',(20,27),(24,30),(24,34))
join('torso','arm');join('torso','rider-leg')
self.mark_human_figure('rider',head='head',torso='torso',torso_junction='start')
''','human_ref/full_body_ref.png: upright rider head/body alignment; source defines complete horse silhouette.','Fine garment outline and far-side legs omitted.')
design(4,'SQUARE','The rejected drawing is an open U with one floating bean; it lacks the soup surface, a complete bowl and a foot. The source is a steaming bowl with two beans on an oval surface.',
 'Restore a broad oval soup rim, closed curved bowl with a foot, two distinct beans and two steam wisps. Keep the beans on the soup surface.', '''
oval('rim',24,23,20,7)
path('bowl',(4,23),[('C',(16,40),(5,33),(9,38)),('L',(32,40)),('C',(44,23),(39,38),(43,33))]);join('rim','bowl')
path('foot',(16,40),[('L',(16,44)),('L',(32,44)),('L',(32,40))]);join('bowl','foot')
path('bean-left',(16,21),[('C',(13,25),(12,21),(11,24)),('C',(19,24),(15,28),(19,26)),('C',(16,21),(21,21),(19,20))],True)
path('bean-right',(29,20),[('C',(26,24),(26,19),(25,22)),('C',(35,25),(28,27),(34,28)),('C',(32,22),(36,22),(33,24)),('C',(29,20),(31,22),(30,20))],True)
for j,x in enumerate((18,30)):
    path(f'steam-{j}',(x,4),[('C',(x,12),(x-4,6),(x+4,10))])
''','Lucide soup: curved bowl and coherent steam strokes; original supplies oval surface, beans and bowl foot.','Reduced three steam wisps to two.')
design(5,'VRECT_L','The rejected heads merge into a single mask-like shape and the heart is tiny. The source shows two opposing side profiles and a large heart between them.',
 'Restore distinct outward-facing noses, chins and necks, with an offset rear skull and a central heart. Preserve the source open contour arrangement.', '''
path('left-profile',(13,13),[('C',(7,22),(9,15),(8,18)),('L',(4,29)),('L',(8,29)),('L',(8,34)),('A',(12,38),4,4,False),('L',(15,38)),('L',(15,44))])
path('right-profile',(18,9),[('C',(28,4),(20,5),(24,4)),('C',(39,16),(35,4),(38,9)),('L',(44,25)),('L',(40,25)),('L',(40,31)),('A',(36,35),4,4,True),('L',(33,35)),('L',(33,40))])
poly('inner-neck',(25,44),(25,37),(27,32))
path('heart',(24,17),[('C',(16,18),(20,12),(16,13)),('C',(24,28),(16,21),(20,25)),('C',(32,18),(28,25),(32,21)),('C',(24,17),(32,13),(28,12))],True)
''','Shared human profile guidance and supplied opposing-head reference; no useful exact Lucide composition.')
design(6,'VRECT_L','The rejected interior mark is an open comma and no longer reads as the enclosed brain region shown in the original.',
 'Close the brain region as a broad organic lobe inside a recognizable side-profile head, with forehead, nose, chin and neck.', '''
path('head',(14,44),[('L',(14,34)),('C',(6,20),(8,31),(6,26)),('C',(24,4),(6,10),(14,4)),('C',(39,17),(33,4),(37,8)),('L',(44,27)),('L',(39,27)),('L',(39,33)),('A',(33,39),6,6,True),('L',(31,39)),('L',(31,44))])
path('brain',(13,22),[('C',(24,12),(13,15),(18,12)),('C',(34,19),(31,12),(34,15)),('C',(26,24),(34,22),(28,22)),('C',(20,28),(24,25),(23,28)),('C',(13,22),(16,29),(13,27))],True)
''','Lucide brain: closed organic lobes; source requires one simplified side-view brain region.')
design(7,'SQUARE','The rejected headset has short square ear blocks and its cable ends as a blunt bar; the reference has tall cushions and a long cable with a plug.',
 'Use a broad arched headband, paired tall padded earcups and a long looping cable terminating in an explicit plug and jack.', '''
path('headband',(8,24),[('A',(40,24),16,18,True)])
rounded('left-pad',8,18,16,35,4);rounded('right-pad',32,18,40,35,4)
join('headband','left-pad');join('headband','right-pad')
path('cable',(40,31),[('C',(40,43),(47,31),(47,43)),('L',(14,43))]);join('right-pad','cable')
rounded('plug',6,40,14,46,3);line('jack',(2,43),(6,43));join('cable','plug');join('plug','jack')
''','Lucide headphones original and atomic-debug: continuous arch and paired rounded pads; source adds cable and plug.')
design(8,'VRECT_L','The rejected drink is a wide shallow container with two square holes. The source is a tall glass with a liquid surface, diagonally staggered ice cubes and a bent straw.',
 'Restore a tall tapered glass, wavy liquid level, two staggered diamond ice cubes and a bent straw extending into the drink.', '''
path('glass',(8,14),[('L',(40,14)),('L',(36,40)),('A',(32,44),4,4,True),('L',(16,44)),('A',(12,40),4,4,True),('L',(8,14))],True)
path('liquid',(9,21),[('C',(24,21),(14,17),(19,25)),('C',(39,21),(29,17),(34,25))]);join('glass','liquid')
poly('straw',(29,20),(33,6),(39,4));join('glass','straw')
poly('ice-upper',(20,22),(25,27),(20,32),(15,27),closed=True)
poly('ice-lower',(28,32),(33,37),(28,42),(23,37),closed=True)
''','Lucide cup-soda: tapered glass and wavy level; source supplies two diamond ice cubes and tall proportions.')
design(9,'VRECT_L','The rejected plant loses both side heart leaves and becomes a single heart on two bare branches. The source clearly has three heart-shaped leaves and a deep pot.',
 'Restore one upright heart leaf, two smaller outward-facing heart leaves and three stems entering a deep tapered pot.', '''
path('top-leaf',(24,8),[('C',(17,8),(18,1),(15,4)),('C',(24,18),(17,12),(20,15)),('C',(31,8),(28,15),(31,12)),('C',(24,8),(33,4),(30,1))],True)
path('left-leaf',(17,27),[('C',(7,26),(12,29),(5,29)),('C',(10,21),(5,23),(8,20)),('C',(11,17),(7,17),(8,15)),('C',(17,27),(15,17),(17,23))],True)
path('right-leaf',(31,27),[('C',(41,26),(36,29),(43,29)),('C',(38,21),(43,23),(40,20)),('C',(37,17),(41,17),(40,15)),('C',(31,27),(33,17),(31,23))],True)
line('stem',(24,18),(24,32));line('stem-left',(17,27),(20,32));line('stem-right',(31,27),(28,32))
path('pot',(12,32),[('L',(36,32)),('L',(33,42)),('A',(30,44),3,3,True),('L',(18,44)),('A',(15,42),3,3,True),('L',(12,32))],True)
for leaf,stem in [('top-leaf','stem'),('left-leaf','stem-left'),('right-leaf','stem-right')]:join(leaf,stem);join('pot',stem)
''','Lucide sprout: joined leaf/stem structure; source supplies three heart leaves and pot.')
design(10,'VRECT_L','The rejected logo reads as a generic cube and omits the two diagonal code marks. The reference uses a tall shield/cube outline and marks on its upper face.',
 'Restore the tall shield outline, diamond face, lower center seam and two diagonal face marks that distinguish the HTML Academy logo.', '''
poly('shield',(8,8),(24,4),(40,8),(40,24),(40,34),(24,44),(8,34),(8,24),closed=True)
poly('face',(8,24),(24,14),(40,24),(24,34),closed=True)
line('seam',(24,34),(24,44));line('code-upper',(22,22),(27,25));line('code-lower',(20,27),(24,30))
join('shield','face');join('shield','seam');join('face','seam')
''')
design(11,'SQUARE','The rejected pipe has one disconnected blob of discharge and angular zigzags for water. The source has a cylindrical outlet collar and two falling flow strokes above rounded waves.',
 'Restore the pipe collar, two curved falling streams and two coherent water-wave rows. Retain the source left-hand pipe and right-hand discharge direction.', '''
poly('pipe',(4,10),(24,10),(24,22),(4,22))
poly('collar',(24,7),(32,7),(32,25),(24,25),closed=True);join('pipe','collar')
poly('upper-fitting',(4,4),(12,4),(12,10));join('pipe','upper-fitting')
path('stream-one',(38,18),[('C',(44,25),(41,19),(43,23))])
path('stream-two',(35,27),[('C',(39,31),(37,28),(38,30))])
for name,y in [('wave-top',33),('wave-bottom',42)]:
    path(name,(4,y),[('C',(14,y-3),(9,y+1),(11,y-1)),('C',(24,y),(17,y+1),(20,y+1)),('C',(34,y-3),(28,y+1),(31,y-1)),('C',(44,y),(38,y+1),(41,y+1))])
''','Supplied original; smooth coherent wave curves follow shared geometric construction.')
design(12,'VRECT_L','The rejected lantern is a jar with a droplet. It loses the protective outer frame, lower foot and irregular flame that identify a hurricane lantern.',
 'Restore the outer protective frame, curved glass chimney, top cap, broad base and asymmetric flame.', '''
poly('cap',(16,4),(32,4),(32,10),(16,10),closed=True)
path('glass',(18,10),[('C',(12,29),(14,16),(12,23)),('C',(24,38),(12,35),(17,38)),('C',(36,29),(31,38),(36,35)),('C',(30,10),(36,23),(34,16))])
path('left-rail',(16,10),[('L',(13,10)),('C',(10,15),(11,10),(10,12)),('L',(8,34)),('A',(12,38),4,4,False),('L',(16,38))])
path('right-rail',(32,10),[('L',(35,10)),('C',(38,15),(37,10),(38,12)),('L',(40,34)),('A',(36,38),4,4,True),('L',(32,38))])
poly('base',(14,38),(34,38),(36,44),(12,44),closed=True)
path('flame',(24,20),[('C',(18,30),(25,25),(18,26)),('A',(30,30),6,6,False),('C',(24,20),(30,26),(26,22))],True)
for n in ['glass','left-rail','right-rail']:join('cap',n);join('base',n)
''','Lucide flame: asymmetric flowing flame; supplied original determines glass and protective frame.')
design(13,'SQUARE','The rejected roof is interrupted by a large rectangular notch, so the chimney dominates and the gable is lost. The source retains a complete pitched roof and a small separate chimney.',
 'Draw a complete symmetric pitched roof, small chimney above the right slope, rounded lower walls and an arched doorway.', '''
poly('roof',(4,24),(24,4),(44,24))
poly('chimney',(33,6),(40,6),(40,14))
path('walls',(8,27),[('L',(8,40)),('A',(12,44),4,4,False),('L',(18,44)),('L',(18,36)),('A',(30,36),6,6,True),('L',(30,44)),('L',(36,44)),('A',(40,40),4,4,False),('L',(40,27))])
''','Lucide house: symmetric gable and rounded wall turns; supplied original retains detached chimney and arched doorway.')
design(14,'VRECT_L','The rejected portrait is a detached head over a shallow arc, without the neck and shoulders that define the source human bust.',
 'Restore a continuous frontal bust with a broad cranium, ears, circular jaw transition, visible neck and sloping shoulders.', '''
path('bust',(4,44),[('C',(9,39),(4,41),(6,40)),('L',(18,35)),('L',(18,30)),('A',(14,22),10,10,True),('C',(12,20),(10,23),(10,17)),('L',(14,20)),('L',(14,12)),('C',(24,4),(14,6),(18,4)),('C',(34,12),(30,4),(34,6)),('L',(34,20)),('L',(36,20)),('C',(34,22),(38,17),(38,23)),('A',(30,30),10,10,True),('L',(30,35)),('L',(39,39)),('C',(44,44),(42,40),(44,41))])
''','human_ref/user.svg: broad head and smooth shoulders; source specifically requires a connected neck and ear-bearing silhouette.')
design(15,'CIRCLE','The rejected face has a broken outline and eye curls that resemble loose blobs. The source is a complete circular face with two inward spirals and a short neutral mouth.',
 'Restore the complete circular face, a matched pair of inward eye spirals and a short straight mouth.', '''
circle('face',24,24,20)
for j,cx in enumerate((15,33)):
    path(f'spiral-{j}',(cx-3,26),[('C',(cx,14),(cx-10,23),(cx-7,14)),('C',(cx+1,25),(cx+8,14),(cx+8,25)),('C',(cx-1,19),(cx-4,25),(cx-5,19)),('C',(cx+1,22),(cx+2,19),(cx+3,21))])
line('mouth',(19,35),(29,35))
''','Supplied face reference; repeated spirals share one construction.','Reduced spiral turn count to preserve visible openings.')
design(16,'SQUARE','The rejected logo is a generic serif H drawn as single strokes; it loses the outlined slab-serif letterform and broad center bar of the original.',
 'Restore the complete outlined H with slab serifs, curved serif shoulders and one broad center bar.', '''
path('letter',(6,6),[('L',(22,6)),('L',(22,10)),('C',(18,14),(18,10),(18,12)),('L',(18,20)),('L',(30,20)),('L',(30,14)),('C',(26,10),(30,12),(30,10)),('L',(26,6)),('L',(42,6)),('L',(42,10)),('C',(38,14),(38,10),(38,12)),('L',(38,34)),('C',(42,38),(38,36),(38,38)),('L',(42,42)),('L',(26,42)),('L',(26,38)),('C',(30,34),(30,38),(30,36)),('L',(30,28)),('L',(18,28)),('L',(18,34)),('C',(22,38),(18,36),(18,38)),('L',(22,42)),('L',(6,42)),('L',(6,38)),('C',(10,34),(10,38),(10,36)),('L',(10,14)),('C',(6,10),(10,12),(10,10)),('L',(6,6))],True)
''')
design(17,'SQUARE','The rejected skate has four dots detached far beneath a shallow boot, so the wheels do not read as wheels. The source has a tall boot over four outlined wheels.',
 'Restore a tall ankle boot, shaped toe, short buckle and four evenly spaced outlined wheels mounted beneath its sole.', '''
path('boot',(8,6),[('L',(24,6)),('L',(24,18)),('C',(31,23),(24,22),(26,23)),('L',(34,23)),('C',(42,28),(39,23),(42,25)),('C',(36,32),(42,31),(40,32)),('L',(12,32)),('C',(6,26),(8,32),(6,30)),('L',(8,6))],True)
line('buckle',(18,14),(24,14));join('boot','buckle')
for j,x in enumerate((6,18,30,42)):circle(f'wheel-{j}',x,42,3)
''','Supplied inline skate reference; repeated circles share one radius and spacing.')
design(18,'SQUARE','The rejected pose has one flat ground bar and no recognizable skates or wheels; the tiny head and stiff torso weaken the forward skating action.',
 'Restore an outlined head, forward skating lean, one bent supporting leg, a lifted rear leg, two boot strokes and paired wheel sets.', '''
circle('head',28,8,4)
path('torso',(28,20),[('C',(21,28),(28,23),(25,26))])
poly('back-arm',(28,20),(18,20),(12,20));poly('front-arm',(28,20),(35,24),(42,24))
poly('front-leg',(21,28),(30,32),(28,37));poly('back-leg',(21,28),(15,33),(8,31),(6,35))
line('front-boot',(27,37),(36,37));line('back-boot',(5,35),(12,37))
for j,(x,y) in enumerate([(6,41),(13,43),(28,43),(36,43)]):circle(f'wheel-{j}',x,y,2)
for n in ['back-arm','front-arm','front-leg','back-leg']:join('torso',n)
join('back-arm','front-arm');join('front-leg','back-leg');join('front-leg','front-boot');join('back-leg','back-boot')
self.mark_human_figure('skater',head='head',torso='torso-0',torso_junction='start')
''','human_ref/full_body_ref.png: outlined head, flowing torso and connected bent limbs; source requires two visible skates.','Simplified clothing and reduced each wheel set to two circles.')
design(19,'SQUARE','The rejected drawing removes three sides of the room and combines the door with a baseline. The source is an enclosed interior wall with a tall door, four-pane window and floor strip.',
 'Restore the complete room boundary and floor strip, a tall door and a separate four-pane window. Preserve the source orthogonal room layout.', '''
poly('room',(4,4),(44,4),(44,36),(44,44),(4,44),(4,36),closed=True)
poly('floor',(4,36),(10,36),(18,36),(44,36));join('room','floor')
poly('door',(10,36),(10,14),(18,14),(18,36));join('floor','door')
poly('window',(26,14),(32,14),(38,14),(38,20),(38,26),(32,26),(26,26),(26,20),closed=True)
line('window-vertical',(32,14),(32,26));line('window-horizontal',(26,20),(38,20))
join('window','window-vertical');join('window','window-horizontal');join('window-vertical','window-horizontal')
''','Supplied interior reference; shared rectangular dimensions and equal window panes.','Tiny door handle omitted to keep the door opening clear.')

def write(i,attempt='01'):
 it=ITEMS[i];ds=DESIGNS[i];ref=Path(it['ref']);uid=ref.stem[-36:];concept=ref.stem[:-37]
 run=ROOT/'icon_set/work/primitive-make-ray'/uid/f'20260929T033605Z-meaning-{attempt}';run.mkdir(parents=True,exist_ok=False)
 meta=dict(concept=concept,source_uuid=uid,reference_path=it['ref'])
 (run/f"{it['id']}.metadata.json").write_text(json.dumps(meta,indent=2))
 (run/'review-before.md').write_text(ds['finding']+'\n\nFeedback: '+it['feedback']+'\n\nRevision: '+ds['change']+'\n')
 source=f'''"""{ds['change']}\nConstruction reference: {ds['reference']}"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = {uid!r}
SOURCE_PATH = {it['ref']!r}
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = {it['id']!r}
    keyshape = Keyshape.{ds['shape']}
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives'
    aliases = ()
    keywords = ({concept!r},)

    def build(self):
'''+HELPERS+textwrap.indent(ds['code'],'        ')
 module=run/(it['id'].replace('-','_')+'_'+uid.replace('-','_')+'.py');module.write_text(source)
 it.update(run=str(run.relative_to(ROOT)),module=str(module.relative_to(ROOT)),finding=ds['finding'],change=ds['change'],lucide=ds['reference'],omissions=ds['omissions'])

if __name__=='__main__':
 for i in map(int,sys.argv[1:]):write(i)
 (HERE/'items.json').write_text(json.dumps(ITEMS,indent=2))
