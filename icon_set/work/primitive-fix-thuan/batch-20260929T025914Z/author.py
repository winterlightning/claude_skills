from pathlib import Path
import json, re, sys, io, hashlib
from datetime import datetime, timezone
from PIL import Image, ImageDraw
from icon_set.scripts.primitive_fix import load_icon, render_previews
from icon_set.scripts.build_gate import gate
BATCH=Path(__file__).resolve().parent
ITEMS=json.loads((BATCH/'items.json').read_text())
SOURCE_ICON_ID=None
SOURCE_PATH=None
AUTHOR='gpt-6'
# Every generated module below stores its exact individual source UUID/path.
HELPER='''
    def path(self, name, start, *steps, closed=False):
        members=[]
        point=start
        for i, step in enumerate(steps):
            ident=f"{name}-{i}"
            end=tuple(step[:2])
            if len(step)==2:
                self.add_line(ident, point, end)
            else:
                self.add_arc(ident, point, end, radius_x=step[2], radius_y=step[3], sweep=step[4])
            members.append(ident)
            point=end
        self.add_contour(name, *members, closed=closed)

    def circle(self, name, cx, cy, r):
        self.path(name,(cx-r,cy),(cx+r,cy,r,r,True),(cx-r,cy,r,r,True),closed=True)
'''
D={}
def add(n,observation,change,body,exception_reason,keyshape='SQUARE',omissions='Minor surface details omitted for native-size clarity.'):
 D[n]=dict(observation=observation,change=change,body=body,exception_reason=exception_reason,keyshape=keyshape,omissions=omissions)
add(1,'The rejected icon reduces the two-person folded acro-yoga pose to one upside-down stick figure; the second head and curled supporting body disappear.',
 'Restored the folded upper flyer, its small head, and the reclining supporting person with raised limbs.', '''
        # Two outlined figures; upper folded legs and torso rest over a reclining base.
        self.path('flyer',(28,4),(33,11,8,8,True),(32,19),(29,24),(13,26),(12,20,3,3,True),(25,18),(25,11),(12,18),(8,14,3,3,True),(23,5),(28,4,8,8,True),closed=True)
        self.path('flyer-head',(30,24),(31,32,5,5,True),(29,32))
        self.path('base-body',(22,26),(20,38),(26,44,6,6,False),(37,44),(43,38,6,6,False),(43,31),(37,31,3,3,False),(37,37),(28,37),(27,26))
        self.circle('base-head',8,38,4)
        # Base head right edge x12 and its own body x20 at y38: exact 4px ink gap.
''','The original is an interlocked two-person pose; compact contacts and an optical envelope preserve its folded arrangement.','VRECT_L')
add(2,'The reference shows two hands of different sizes meeting; the rejected drawing instead shows two complete people.',
 'Replaced the people with overlapping adult and child palms, oppositely angled fingers and visible thumbs.', '''
        # Larger palm behind; smaller hand in front. Overlap removes hidden finger edges.
        self.path('adult-back',(44,42),(42,32),(41,15),(35,15,3,3,False),(34,22),(19,7),(13,11,4,4,False),(25,23))
        self.path('adult-finger',(13,11),(10,10),(7,15,4,4,False),(18,25))
        self.path('adult-lower',(8,17),(5,20,3,3,False),(10,26))
        self.path('child',(8,30),(19,19),(24,24,4,4,True),(18,30),(26,22),(31,27,4,4,True),(23,35),(29,29),(34,34,4,4,True),(27,41),(33,39),(35,43,3,3,True),(25,45),(16,45),(7,39,9,9,True),(8,30),closed=True)
''','Multiple fingers on two overlapping hands require compact spacing; unequal palm sizes carry the adult/child high-five meaning.')
add(3,'The rejected aircraft loses the prominent downward wing and looks like a sloping boat above a line.',
 'Restored the swept lower wing, tail fin, rounded nose and rising aircraft silhouette above the ground.', '''
        # Plane rises right; a distinct lower swept wing interrupts the fuselage underside.
        self.path('plane',(4,19),(9,18),(15,23),(37,10),(43,12,5,4,True),(41,18,5,4,True),(31,23),(26,34),(20,37),(22,27),(14,30),(9,28,6,6,True),(4,19),closed=True)
        self.add_line('ground',(4,42),(44,42))
''','The swept wing and natural aircraft angle take precedence over exact rectangle fitting.','HRECT_L')
add(4,'The rejected bottle is upright with two loose hooks; the diagonal bottle and enclosed side handles from the reference are lost.',
 'Restored the diagonal feeding bottle, closed side grips, wide collar and shaped nipple.', '''
        # Diagonal bottle owns a collar, a nipple, and two opposite closed-loop grips.
        self.path('bottle',(8,28),(21,15),(34,28),(21,41),(15,41,4,4,True),(8,34),(8,28,4,4,True),closed=True)
        self.path('collar',(20,12),(24,8,3,3,True),(39,23),(35,27,3,3,True),(20,12),closed=True)
        self.path('nipple',(27,11),(30,6),(36,5,4,4,True),(39,10,4,4,True),(35,19))
        self.path('handle-left',(10,26),(6,22),(16,12,7,7,True),(20,16))
        self.path('handle-right',(26,36),(31,40),(41,30,7,7,False),(37,26))
''','The diagonal collar and two closed handles need compact joins to retain the reference bottle design.')
add(5,'The rejected truck omits the windshield divider and makes the front wheel too close to the cargo box, weakening the delivery-truck silhouette.',
 'Rebalanced the cargo box and cab, restored the windshield line and used equal separated wheels.', '''
        # Cargo box, cab and wheel pair share a common axle and floor line.
        self.path('cargo',(7,35),(4,35),(4,8),(28,8),(28,35))
        self.path('cab',(28,16),(36,16),(44,26),(44,35),(41,35))
        self.add_line('windshield',(28,26),(44,26))
        self.add_line('floor',(17,35),(31,35))
        for i,x in enumerate((12,36)):self.circle(f'wheel-{i}',x,35,5)
        self.relate('connect','cargo','floor')
        self.relate('connect','cab','windshield')
        self.relate('connect','cargo','windshield')
        self.relate('connect','cargo','cab')
        self.relate('connect','cargo','wheel-0')
        self.relate('connect','floor','wheel-0')
        self.relate('connect','floor','wheel-1')
        self.relate('connect','cab','wheel-1')
''','The cab and equal wheel pair keep the vehicle readable at 48px; compact wheel-to-body junctions are intentional.','HRECT_L')
add(6,'The rejected full stick figure reverses the waving arm and reduces the briefcase to a small square; the reference shows a waving upper-body figure with a handled case.',
 'Restored the raised left arm, broad upper-body silhouette, lowered right hand and handled briefcase.', '''
        # Circular head above broad shoulders; left arm hails, right arm holds a case.
        self.circle('head',24,9,5)
        self.path('body',(16,44),(16,28),(6,15),(10,11,3,3,True),(20,22),(31,22),(36,27,5,5,True),(36,32))
        self.add_line('arm-inside',(31,28),(31,32))
        self.path('case-handle',(31,34),(31,31),(37,31,3,3,True),(37,34))
        self.path('case',(28,34),(41,34),(44,37,3,3,True),(44,42),(41,45,3,3,True),(28,45),(25,42,3,3,True),(25,37),(28,34,3,3,True),closed=True)
        # Head lower centerline y14 to shoulder y22 is exactly 8: 4px clear ink.
''','The raised arm and handled briefcase define the hailing action; close handle/case anatomy is retained.','VRECT_L')
add(7,'The rejected carrot is a thin upright spike beside a squat broccoli; the reference shows a rounded diagonal carrot and a branching broccoli stalk.',
 'Restored a broad diagonal carrot with greens and score mark, plus a scalloped broccoli crown and branched stem.', '''
        # Broccoli canopy at upper left; carrot tilts down-left beside it.
        self.path('crown',(7,22),(4,17,5,5,True),(8,11,6,6,True),(15,6,6,6,True),(22,10,6,6,True),(28,15,6,6,True),(23,22,6,6,True),(17,23),(12,25),(7,22,5,5,True),closed=True)
        self.path('stalk',(12,25),(15,35),(20,36),(22,24))
        self.path('carrot',(24,42),(23,37),(32,24),(39,22,6,6,True),(44,28,6,6,True),(39,35),(28,43),(24,42,4,4,True),closed=True)
        self.add_line('green-up',(38,21),(38,13))
        self.add_line('green-side',(41,23),(45,19))
        self.add_line('carrot-score',(30,29),(33,32))
''','The natural diagonal carrot and lobed crown need modest optical-envelope departures to avoid generic symbols.')
add(8,'The rejected browser has short inward tabs rather than a full header separator; reviewer explicitly asks for Browser.',
 'Restored the full browser chrome, header controls, and centered user profile inside the page.', '''
        # Rounded browser frame with full-width header; centered detached avatar beneath.
        self.path('frame',(10,6),(38,6),(42,10,4,4,True),(42,38),(38,42,4,4,True),(10,42),(6,38,4,4,True),(6,10),(10,6,4,4,True),closed=True)
        self.add_line('header',(6,14),(42,14))
        for i,x in enumerate((14,22)):self.add_dot(f'control-{i}',(x,10))
        self.circle('head',24,22,3)
        self.path('shoulders',(16,36),(32,36,8,3,True))
        self.relate('connect','frame','header')
        # Head lower edge y25 to shoulder apex y33: exact 4px visible gap.
''','Full browser chrome and the enclosed profile need compact header spacing; the content remains distinct from the frame.')
add(9,'The rejected canoe has two vertical towers and interior braces; the original is a shallow curved hull with a continuous rim.',
 'Rebuilt a shallow canoe hull with raised ends and a gently dipping rim, removing the invented braces.', '''
        # One closed hull contour; raised bow/stern and a dipping gunwale, no interior struts.
        self.path('hull',(6,14),(42,14,18,8,False),(44,25),(4,25,20,10,True),(6,14),closed=True)
''','A canoe naturally needs a shallow wide envelope; expanding it vertically would recreate the rejected U-shaped frame.','HRECT_M','No defining feature omitted; removed the rejected drawing’s invented braces.')
add(10,'The rejected wrench is a small incomplete ring on a line, and the hand is an abstract zigzag.',
 'Restored a diagonal open-jaw wrench with a broad head and a rounded fist around its shaft.', '''
        # Broad open jaw above a diagonal shaft and two-finger grip.
        self.path('wrench',(25,21),(25,14),(31,6,9,9,True),(40,4),(34,10),(38,14),(44,8),(44,17),(38,25,9,9,True),(31,25))
        self.add_line('shaft-top',(27,23),(21,29))
        self.add_line('shaft-bottom',(14,36),(6,44))
        self.path('fist',(15,39),(7,31),(7,27,3,3,True),(14,22),(18,22,3,3,True),(27,31))
        self.path('thumb',(24,28),(29,33),(29,39,6,6,True),(31,44))
        self.add_line('finger-seam',(10,26),(17,33))
''','The diagonal open jaw and wrapping fingers retain tool identity despite compact grip spacing.','VRECT_L')
add(11,'The rejected foot is a rectangular shape with tiny bumps and the hand becomes a large angular hook, losing the massage action.',
 'Restored a rounded sole, stepped toes, a pressure thumb on the sole and curved fingers around the outside.', '''
        # Left foot sole with distinct toes; right hand wraps and presses the arch.
        self.path('foot',(6,11),(6,32),(15,41,9,9,False),(23,38))
        self.path('toes',(6,11),(14,11,4,4,True),(14,14),(14,12),(20,12,3,3,True),(20,15),(20,13),(26,13,3,3,True),(26,16),(26,15),(32,15,3,3,True),(32,19))
        self.path('thumb',(31,32),(23,25),(18,30,4,4,False),(29,44))
        self.path('hand-back',(29,44),(40,44),(42,32),(39,24),(33,20),(28,18),(26,22,3,3,False),(31,26),(31,32))
        self.path('arch',(12,30),(17,24,7,7,True))
''','Toe and gripping-finger spacing is intentionally compact so the foot massage remains recognizable.','VRECT_L')
add(12,'The rejected hand blends into a large hook at the side of the head and obscures the scalp massage gesture.',
 'Restored a clean side-profile head and separate fingers descending from a wrist onto the scalp.', '''
        # Side-profile head on left; hand descends from upper right onto the crown and temple.
        self.path('head',(18,44),(18,38),(14,38),(10,34,4,4,True),(10,30),(6,30),(10,22),(10,20),(21,12,12,12,True),(25,12))
        self.add_line('neck',(32,35),(32,44))
        self.path('hand',(25,4),(22,11),(29,12),(25,23),(30,26,3,3,False),(34,17))
        self.path('finger-two',(34,17),(31,27),(36,29,3,3,False),(39,20))
        self.path('hand-outside',(42,4),(39,13),(42,22),(39,30),(36,29))
''','Three separate descending fingers and the scalp profile require compact spacing; the face remains unobstructed.','VRECT_L')
add(13,'The rejected hand is an angular downward hook, rather than the flat hovering palm in the reference.',
 'Restored the extended horizontal fingers, gently curved palm, and three rising heat waves beneath.', '''
        # Flat hand enters from upper right above a three-wave heat series.
        self.path('fingers',(34,6),(25,6),(8,13),(5,18,4,4,False),(9,21,4,4,False),(19,16),(26,16))
        self.path('palm',(16,18),(20,22),(30,22),(35,18,8,8,False),(42,6))
        for i,x in enumerate((11,24,37)):
            self.path(f'heat-{i}',(x,30),(x-1,36,5,5,False),(x,43,6,6,True))
''','The flat hovering hand and repeated heat waves keep their natural silhouette despite keyshape and compact palm-spacing findings.','HRECT_L')
add(14,'The rejected pad controller becomes the letter E and loses the complete pad grid; the music cue shrinks to one note.',
 'Restored the controller’s outer frame and pad grid, the pressing index finger, and a paired musical-note cue.', '''
        # Pad grid at left is partly occluded by the foreground pointing hand.
        self.path('controller',(22,38),(7,38),(4,35,3,3,True),(4,11),(7,8,3,3,True),(29,8))
        self.add_line('grid-vertical',(14,8),(14,38))
        for i,y in enumerate((18,28)):self.add_line(f'grid-row-{i}',(4,y),(23,y))
        self.path('hand',(25,44),(20,38),(24,34,3,3,True),(28,38),(28,24),(34,24,3,3,True),(34,31),(39,31),(44,36,5,5,True),(44,44))
        self.path('note-stems',(34,16),(34,7),(44,4),(44,14))
        self.circle('note-left',31,17,2)
        self.circle('note-right',41,15,2)
        self.relate('connect','controller','grid-vertical')
        self.relate('connect','controller','grid-row-0')
        self.relate('connect','controller','grid-row-1')
        self.relate('connect','grid-vertical','grid-row-0')
        self.relate('connect','grid-vertical','grid-row-1')
''','The controller grid, pointing fingertip and paired notes all carry meaning; their compact spacing is deliberate.')
add(15,'The rejected yo-yo has a broken second circle and a thick connector, losing the thin string and spinning motion.',
 'Restored a pinching hand, a diagonal string, a complete yo-yo with central axle, and two motion arcs.', '''
        # Pinching hand above a hanging yo-yo; twin arcs indicate swinging/spinning motion.
        self.path('hand-top',(42,6),(31,6),(20,10),(11,10),(6,14,4,4,False),(10,20,4,4,False),(17,15),(25,17))
        self.path('hand-bottom',(18,17),(27,21),(35,18),(42,14))
        self.add_line('string',(16,16),(24,29))
        self.circle('yoyo',32,35,9)
        self.circle('axle',32,35,2)
        self.path('motion-outer',(8,28),(8,43,12,12,False))
        self.path('motion-inner',(14,31),(14,40,8,8,False))
''','The thin string, axle and two motion arcs require close spacing but keep the toy’s mechanism legible.','VRECT_L')
add(16,'The rejected fist has an uneven row of fused circular finger bumps; the reference has a clearly extended index and stepped curled fingers.',
 'Rebalanced the wrist and palm, lengthened the pointing index, and gave the curled fingers distinct stepped ends.', '''
        # Continuous pointing-hand outline; finger seams terminate on the shared outer contour.
        self.path('outline',(17,6),(27,6),(40,19,13,13,True),(40,29),(34,29,3,3,True),(34,31),(28,31,3,3,True),(28,34),(22,34,3,3,True),(22,40),(14,40,4,4,True),(14,21),(11,24),(7,20,3,3,True),(17,6),closed=True)
        for i,(x,y) in enumerate(((34,29),(28,31),(22,34))):
            self.add_line(f'finger-{i}',(x,y-5),(x,y))
            self.relate('connect','outline',f'finger-{i}')
''','The curled finger divisions are tighter than the general spacing rule but preserve a familiar pointing-hand silhouette.','VRECT_L')
add(17,'The rejected hand becomes a robotic three-prong claw sitting above the card; the reference shows a hand pinching and taking its upper-right edge.',
 'Restored the reaching hand and diagonal pinch across the identity card’s corner, keeping the portrait centered.', '''
        # Card and avatar behind a right-entering hand; thumb crosses the upper-right card corner.
        self.path('card',(25,18),(10,18),(6,22,4,4,False),(6,38),(10,42,4,4,False),(31,42),(35,38,4,4,False),(35,25))
        self.circle('portrait-head',18,27,3)
        self.path('portrait-shoulders',(11,38),(25,38,7,3,True))
        self.path('hand-top',(44,4),(37,9),(29,9),(23,14),(19,18))
        self.path('thumb',(31,15),(25,21),(29,25,3,3,False),(36,20),(40,19),(44,16))
        # Portrait head ends y30 and shoulders apex y35: compact enclosed portrait, flagged for optical review.
''','The pinching thumb overlaps the card deliberately; the small enclosed portrait and compact gap preserve identity-card meaning.')
add(18,'The rejected cuffs are single hollow bell shapes, with no separate wrist openings or lock housings.',
 'Restored two closed cuff bodies with circular wrist openings, narrowed lock housings, and the arch connector.', '''
        # Mirrored cuffs with separate wrist holes and shared arch connector.
        self.path('connector',(12,22),(12,15),(36,15,12,11,True),(36,22))
        for i,cx in enumerate((12,36)):
            self.path(f'cuff-{i}',(cx-4,22),(cx+4,22),(cx+5,27),(cx+9,35,9,9,True),(cx,44,9,9,True),(cx-9,35,9,9,True),(cx-5,27),(cx-4,22),closed=True)
            self.circle(f'opening-{i}',cx,35,4)
            self.relate('connect','connector',f'cuff-{i}')
''','Double cuff boundaries and lock housings need small annular gaps at 48px; the pair remains separate and legible.','VRECT_L')
add(19,'The rejected drawing shows two plain rings connected by a hook, omitting the cuff thickness and locking shoulders.',
 'Restored double-walled cuffs with locking shoulders and a curved link in the reference’s diagonal arrangement.', '''
        # Lower-left and upper-right cuff assemblies share a loose curved connector.
        self.path('link',(11,26),(8,21),(5,14,9,9,True),(10,6,8,8,True),(20,7,10,10,True),(28,13))
        self.path('lower-cuff',(8,26),(16,26),(17,30),(21,36,8,8,True),(12,44,9,8,True),(3,36,9,8,True),(7,30),(8,26),closed=True)
        self.circle('lower-hole',12,36,4)
        self.path('upper-cuff',(27,12),(26,9),(30,5),(34,9),(35,8),(44,17,9,9,True),(35,26,9,9,True),(26,17,9,9,True),(27,12),closed=True)
        self.circle('upper-hole',35,17,4)
''','Small annular gaps and locking shoulders are essential for cuffs rather than generic rings; the diagonal link stays clear.')
add(20,'The rejected comb has three large teeth attached to a short rounded spine; the long grip and finer tooth row disappear.',
 'Restored the extended lower-left handle, curved diagonal spine and four equally spaced comb teeth.', '''
        # Diagonal comb spine and extended rounded handle; one repeated tooth definition.
        self.path('spine',(44,16),(37,9),(30,9,5,5,False),(6,33),(5,40,5,5,False),(11,42,5,5,False),(16,37),(34,19))
        for i in range(4):
            x,y=34-5*i,19+5*i
            self.add_line(f'tooth-{i}',(x,y),(x+7,y+7))
            self.relate('connect','spine',f'tooth-{i}')
''','Four evenly spaced teeth and the long handle need tighter diagonal spacing than the general rule, while remaining distinct.')
def make(n,rev='r1'):
 item=ITEMS[n-1]; data=D[n]; ref=Path(item['reference']); source_uuid=re.search(r'[0-9a-f-]{36}$',ref.stem).group(); concept=ref.stem[:-37]
 run=Path('icon_set/work/primitive-make-ray')/source_uuid/f'20260929T025914Z-fix-{n:02d}-{rev}'
 run.mkdir(parents=True,exist_ok=False)
 ident=item['key'].split('/',1)[1]
 metadata=dict(concept=concept,source_uuid=source_uuid,reference_path=str(ref),icon_id=ident,author=AUTHOR,feedback=item['feedback'],comparison=data['observation'],change=data['change'])
 (run/f'{ident}.metadata.json').write_text(json.dumps(metadata,indent=2)+'\n')
 source=f'''"""{data['change']}
Before: {data['observation']}
Construction: Relevant local Lucide primitives for coherent rounded contours;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected for human proportions where applicable.
Keyshape {data['keyshape']}; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = {source_uuid!r}
SOURCE_PATH = {str(ref)!r}
AUTHOR = {AUTHOR!r}

class Drawing(Solo48):
    icon_id = {ident!r}
    keyshape = Keyshape.{data['keyshape']}
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hands'
    aliases = ()
    keywords = ('hand', {concept!r})
{HELPER}
    def build(self):
{data['body']}
'''
 module=run/(ident.replace('-','_')+'_'+source_uuid.replace('-','_')+'.py'); module.write_text(source)
 icon=load_icon(module); report=icon.validate_icon(); svg=icon.to_svg(); (run/f'{ident}.svg').write_text(svg)
 (run/'validation.txt').write_text(report.describe())
 render_previews(svg,ident,48,run)
 import cairosvg
 cairosvg.svg2png(url=str(ref),write_to=str(run/'reference.png'),output_width=384,output_height=384)
 entry=dict(metadata,run=str(run),module=str(module),svg=str(run/f'{ident}.svg'),validation=report.status,errors=report.errors,warnings=report.warnings,exception_reason=data['exception_reason'],omissions=data['omissions'],keyshape=data['keyshape'])
 (run/'draft.json').write_text(json.dumps(entry,indent=2))
 print(n,ident,report.status,len(report.errors),len(report.warnings),flush=True)
 return entry

def sheet(entries,filename):
 out=Image.new('RGB',(1000,len(entries)*210),'#e8e8e8'); draw=ImageDraw.Draw(out)
 for row,e in enumerate(entries):
  y=row*210; draw.text((10,y+2),e['icon_id'],fill='black')
  ref=Image.open(Path(e['run'])/'reference.png').convert('RGBA'); ref.thumbnail((165,165)); bg=Image.new('RGBA',ref.size,'white');bg.alpha_composite(ref);out.paste(bg.convert('RGB'),(10,y+25))
  for col,theme in enumerate(('light','dark')):
   p=Path(e['run'])/f'preview-{theme}-384.png'; im=Image.open(p).convert('RGB'); im.thumbnail((165,165));out.paste(im,(220+col*360,y+25))
   small=Image.open(Path(e['run'])/f'preview-{theme}-48.png');out.paste(small,(410+col*360,y+75))
 out.save(BATCH/filename)
if __name__=='__main__':
 nums=[int(a) for a in sys.argv[1:]] or list(D)
 entries=[make(n) for n in nums]
 (BATCH/'drafts.json').write_text(json.dumps(entries,indent=2))
 for p in range(0,len(entries),5): sheet(entries[p:p+5],f'drafts-{p//5+1}.png')
