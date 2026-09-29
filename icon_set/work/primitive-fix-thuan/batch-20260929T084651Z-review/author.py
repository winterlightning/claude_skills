"""Standalone primitive-make-ray revisions; no registered artwork is changed."""
from pathlib import Path
import json, re, sys, textwrap, datetime, io
import cairosvg
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))
from icon_set.scripts.primitive_fix import load_icon, render_previews
from icon_set.scripts.build_gate import gate
SOURCE_ICON_ID = None
SOURCE_PATH = str(Path(__file__))
AUTHOR = 'gpt-6'
BATCH = Path(__file__).parent

HELPERS = '''
def path(s, name, start, *steps, closed=False):
    members=[]; here=start
    for i, step in enumerate(steps):
        kind, end, *p = step
        ident=f'{name}-{i}'
        if kind == 'L': s.add_line(ident, here, end)
        elif kind == 'A': s.add_arc(ident, here, end, radius_x=p[0], radius_y=p[1], sweep=p[2])
        elif kind == 'C': s.add_bezier(ident, here, (p[0], p[1], end))
        members.append(ident); here=end
    s.add_contour(name, *members, closed=closed)

def circle(s, name, x, y, r):
    path(s,name,(x-r,y),('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True),closed=True)
'''

# Each comparison was written after opening the original and displayed rejected SVG.
DESIGNS = [
('romance-pride-gay-lgbt-heart','HRECT_L',
 'The rejected rainbow has only two detached bands and the heart is cramped and angular. Restore the rainbow above a clearly lobed heart.',
 'Three concentric semicircular rainbow bands and a larger smooth heart preserve pride and love; omit one fine rainbow band for 48px clarity.',
 '''
 # Plan: shared rainbow center, regular radius series; symmetric heart below.
 for i,r in enumerate((20,14,8)):
     s.add_arc(f'rainbow-{i}',(24-r,22),(24+r,22),radius_x=r,sweep=True)
 path(s,'heart',(24,31),('C',(13,34),(18,25),(10,28)),('C',(24,44),(14,37),(20,41)),('C',(35,34),(28,41),(34,37)),('C',(24,31),(38,28),(30,25)),closed=True)
 '''),
('running-person-motion-marks','SQUARE',
 'The rejected sensor marks became a chevron and dot, so the detection cue is missing. Restore curved motion marks around a running person.',
 'Rebuilt a forward running pose with round head, bent elbows and knees, and paired curved sensor marks.',
 '''
 # Plan: head axis follows upper torso; circular head r4, shoulder 12u below center.
 circle(s,'head',28,8,4)
 s.add_line('torso',(28,20),(22,30))
 s.add_polyline('arms',(15,23),(19,18),(28,20),(35,25),(39,21))
 s.add_polyline('rear-leg',(22,30),(16,39),(10,39))
 s.add_polyline('front-leg',(22,30),(30,35),(33,44))
 for part in ('arms','rear-leg','front-leg'): s.relate('connect','torso',part)
 s.relate('connect','rear-leg','front-leg')
 for side, x, sweep in [('left',6,False),('right',42,True)]:
     s.add_arc('sensor-'+side,(x,26),(x,34),radius_x=8,sweep=sweep)
 s.mark_human_figure('runner',head='head',torso='torso',torso_junction='start')
 '''),
('sad-face-profile','VRECT_L',
 'The rejected mouth merges with the chin into a heavy smiling-looking hook. Preserve the closed eye and separate a downturned mouth from the jaw.',
 'Rebuilt the skull and anatomical neck with a clearer nose, lower rounded jaw and a separate frown.',
 '''
 # Plan: continuous right-facing anatomical silhouette; detached eye and frown.
 path(s,'profile',(13,44),('L',(13,35)),('C',(8,22),(10,32),(8,28)),('L',(8,18)),('A',(36,18),14,14,True),('L',(40,24)),('L',(34,25)),('L',(34,31)),('A',(26,39),8,8,True),('L',(26,44)))
 s.add_line('closed-eye',(24,17),(28,17))
 path(s,'frown',(22,32),('C',(29,30),(24,30),(27,29)))
 '''),
('sad-head-profile','VRECT_L',
 'The rejected face has a compressed jaw and a heavy mouth joined to the chin. Restore the sorrowful slanted eye and delicate downturned mouth.',
 'Separated the frown from the chin and reshaped the skull, nose and neck; retained the reference slanted eye.',
 '''
 # Plan: continuous right-facing anatomical silhouette, slanted eyelid and frown.
 path(s,'profile',(13,44),('L',(13,35)),('C',(8,22),(10,32),(8,28)),('L',(8,18)),('A',(36,18),14,14,True),('L',(40,24)),('L',(34,25)),('L',(34,31)),('A',(26,39),8,8,True),('L',(26,44)))
 s.add_line('closed-eye',(23,19),(28,16))
 path(s,'frown',(22,32),('C',(29,30),(24,30),(27,29)))
 '''),
('sailboard-on-waves','SQUARE',
 'The rejected straight triangle and disconnected bars lose the leaning mast, curved sail and board-like hull. Restore that sailing silhouette.',
 'Added a curved wind-filled sail, diagonal mast and boom, shallow board hull and smooth water.',
 '''
 # Plan: curved sail on a leaning mast; shallow hull and regular wave rhythm.
 path(s,'sail',(19,4),('C',(7,29),(9,10),(7,18)),('L',(26,24)),('L',(19,4)),closed=True)
 s.add_line('mast',(26,24),(29,33));s.relate('connect','mast','sail')
 s.add_line('boom',(8,22),(29,16));s.relate('connect','boom','sail')
 path(s,'board',(8,35),('L',(42,29)),('C',(29,38),(41,36),(35,38)))
 path(s,'water',(4,42),('C',(14,39),(8,42),(11,42)),('C',(24,42),(17,42),(20,42)),('C',(34,39),(28,42),(31,42)),('C',(44,42),(37,42),(40,42)))
 '''),
('sailboat-on-waves','SQUARE',
 'The rejected straight triangular sail and extra crossbar replace the reference curved sail. Restore the distinctive bowed sail above the hull.',
 'Redrew a single bowed sail, a shallow curved boat hull and two broad waves, removing the invented crossbar.',
 '''
 # Plan: single asymmetric curved sail; boat below; two repeating broad waves.
 path(s,'sail',(17,4),('C',(37,25),(28,5),(36,14)),('L',(22,27)),('L',(17,4)),closed=True)
 path(s,'hull',(4,32),('L',(44,32)),('C',(38,40),(43,35),(41,38)))
 path(s,'hull-left',(4,32),('C',(9,40),(5,35),(7,38)))
 s.relate('connect','hull','hull-left')
 path(s,'water',(5,44),('C',(15,41),(9,45),(12,44)),('C',(25,44),(18,44),(21,45)),('C',(35,41),(29,45),(32,44)),('C',(43,44),(38,44),(41,45)))
 '''),
('scattered-sesame-seed','SQUARE',
 'The rejected five identical droplets read as water, not irregular scattered sesame. Restore seed-shaped ovals with varied orientation.',
 'Rebuilt five gently pointed oval seeds with distinct orientations and sizes while preserving the scattered layout.',
 '''
 # Plan: five seed instances, each a smooth asymmetric tapered oval, not a flame.
 path(s,'seed-a',(14,6),('C',(7,20),(5,11),(3,18)),('C',(18,16),(14,24),(20,22)),('C',(14,6),(18,12),(15,10)),closed=True)
 path(s,'seed-b',(31,6),('C',(30,20),(28,11),(26,18)),('C',(42,17),(35,26),(44,22)),('C',(31,6),(43,12),(36,10)),closed=True)
 path(s,'seed-c',(25,23),('C',(19,32),(19,24),(16,29)),('C',(29,32),(21,38),(28,37)),('C',(25,23),(31,28),(27,25)),closed=True)
 path(s,'seed-d',(9,30),('C',(6,42),(6,33),(2,38)),('C',(17,39),(12,47),(19,44)),('C',(9,30),(17,34),(12,33)),closed=True)
 path(s,'seed-e',(40,31),('C',(31,39),(34,31),(31,34)),('C',(42,42),(35,45),(42,46)),('C',(40,31),(47,38),(45,32)),closed=True)
 '''),
('scientist-woman-avatar','VRECT_L',
 'The rejected portrait has a rigid brim and hanging ends that read as a hat. The original shows parted hair, a rounded face and jacket lapels.',
 'Replaced the hat-like geometry with parted shoulder-length hair, circular jaw and smooth jacket shoulders with lapels.',
 '''
 # Plan: symmetric parted hair, circular jaw; broad shoulders and V lab-coat lapels.
 path(s,'hair',(7,27),('C',(11,8),(11,22),(8,14)),('C',(24,8),(13,1),(19,8)),('C',(37,8),(29,8),(35,1)),('C',(41,27),(40,14),(37,22)))
 path(s,'part',(12,14),('C',(24,10),(17,15),(22,13)),('C',(36,14),(26,13),(31,15)))
 s.add_arc('jaw',(36,14),(12,14),radius_x=12,sweep=True)
 s.relate('connect','part','jaw')
 path(s,'shoulders',(6,44),('L',(6,40)),('C',(24,30),(6,34),(16,30)),('C',(42,40),(32,30),(42,34)),('L',(42,44)))
 s.add_polyline('lapels',(17,32),(24,44),(31,32))
 s.human_construction='bust'
 '''),
('scientist-woman-avatar-solo','VRECT_L',
 'The rejected silhouette reads as a brimmed hat with an oversized V. Restore the reference woman portrait with parted hair and jacket.',
 'Reconstructed parted shoulder-length hair, a circular face and jacket lapels balanced around the center axis.',
 '''
 # Plan: symmetric parted hair, circular jaw; broad shoulders and V lab-coat lapels.
 path(s,'hair',(7,27),('C',(11,8),(11,22),(8,14)),('C',(24,8),(13,1),(19,8)),('C',(37,8),(29,8),(35,1)),('C',(41,27),(40,14),(37,22)))
 path(s,'part',(12,14),('C',(24,10),(17,15),(22,13)),('C',(36,14),(26,13),(31,15)))
 s.add_arc('jaw',(36,14),(12,14),radius_x=12,sweep=True)
 s.relate('connect','part','jaw')
 path(s,'shoulders',(6,44),('L',(6,40)),('C',(24,30),(6,34),(16,30)),('C',(42,40),(32,30),(42,34)),('L',(42,44)))
 s.add_polyline('lapels',(17,32),(24,44),(31,32))
 s.human_construction='bust'
 '''),
('sea-lion','SQUARE',
 'The rejected silhouette has squared elephant-like feet and lacks the seal back and flippers. Restore the raised neck and tapered flipper anatomy.',
 'Rebuilt a long-necked seal with a rounded muzzle, smoothly arched back, broad foreground flipper and tapered rear flipper.',
 '''
 # Plan: naturally asymmetric marine mammal, raised head left and sweeping body right.
 path(s,'outline',(10,10),('C',(23,14),(16,0),(23,6)),('L',(23,21)),('C',(43,35),(35,20),(43,25)),('C',(38,44),(45,40),(42,44)),('L',(32,44)),('L',(36,37)),('L',(32,32)),('C',(19,36),(28,35),(25,36)),('C',(8,18),(11,32),(8,25)),('C',(4,14),(3,18),(2,15)),('C',(10,10),(4,12),(7,12)),closed=True)
 path(s,'front-flipper',(19,32),('C',(24,44),(18,38),(20,42)),('C',(13,40),(18,44),(14,43)))
 path(s,'far-flipper',(11,32),('C',(5,39),(10,36),(7,38)),('C',(14,40),(8,41),(11,41)))
 s.add_dot('eye',(14,13))
 '''),
('sea-lion-solo','SQUARE',
 'The rejected animal reads as a four-legged mammal because its flippers became squared feet. Restore the seal silhouette and swept flippers.',
 'Redrew a rounded muzzle, upright neck, arched back and broad tapering flippers; retained intentional left-facing asymmetry.',
 '''
 # Plan: naturally asymmetric marine mammal, raised head left and sweeping body right.
 path(s,'outline',(10,10),('C',(23,14),(16,0),(23,6)),('L',(23,21)),('C',(43,35),(35,20),(43,25)),('C',(38,44),(45,40),(42,44)),('L',(32,44)),('L',(36,37)),('L',(32,32)),('C',(19,36),(28,35),(25,36)),('C',(8,18),(11,32),(8,25)),('C',(4,14),(3,18),(2,15)),('C',(10,10),(4,12),(7,12)),closed=True)
 path(s,'front-flipper',(19,32),('C',(24,44),(18,38),(20,42)),('C',(13,40),(18,44),(14,43)))
 path(s,'far-flipper',(11,32),('C',(5,39),(10,36),(7,38)),('C',(14,40),(8,41),(11,41)))
 s.add_dot('eye',(14,13))
 '''),
('sea-serpent-head','SQUARE',
 'The rejected head is a blocky question mark with no eye, mouth or crest. Restore the sea-dragon face and curved neck.',
 'Added a tapered snout, eye, open angular mouth and rear crest to a smooth S-shaped neck.',
 '''
 # Plan: one dragon profile with detached eye and mouth; three ridge segments on crest.
 path(s,'profile',(16,44),('C',(28,29),(16,36),(21,33)),('C',(28,20),(34,25),(32,20)),('L',(24,20)),('C',(18,26),(24,25),(22,26)),('L',(7,26)),('A',(4,23),3,3,True),('L',(4,16)),('A',(8,12),4,4,True),('L',(14,12)),('C',(25,9),(18,7),(20,9)),('C',(40,22),(34,8),(40,15)),('C',(33,36),(42,29),(37,33)),('C',(27,44),(29,39),(27,41)))
 s.add_polyline('mouth',(4,22),(9,19),(14,22),(18,20));s.relate('connect','mouth','profile')
 s.add_dot('eye',(19,15))
 path(s,'crest',(25,9),('C',(42,9),(30,0),(37,3)),('L',(44,18)),('L',(40,20)))
 s.relate('connect','crest','profile')
 s.add_line('ridge',(34,5),(32,11));s.relate('connect','ridge','crest')
 '''),
('seated-adult-with-child','SQUARE',
 'The rejected disconnected figures look like two unrelated seated adults. Restore a visibly smaller child seated on the adult lap and the chair.',
 'Rebuilt the adult chair and seated posture with a smaller child placed above the adult thigh.',
 '''
 # Plan: adult and child share lap relationship, with distinct head radii and coherent limbs.
 circle(s,'adult-head',13,9,5)
 s.add_line('adult-torso',(13,22),(15,32))
 s.add_polyline('adult-leg',(15,32),(27,32),(31,44))
 s.relate('connect','adult-torso','adult-leg')
 path(s,'chair',(5,24),('L',(5,35)),('A',(11,41),6,6,False),('L',(20,41)))
 circle(s,'child-head',31,16,3)
 s.add_line('child-torso',(31,27),(32,32))
 s.add_polyline('child-leg',(32,32),(37,33),(41,40))
 s.relate('connect','child-torso','child-leg')
 s.add_line('holding-arm',(15,25),(24,28))
 s.mark_human_figure('adult',head='adult-head',torso='adult-torso',torso_junction='start')
 s.mark_human_figure('child',head='child-head',torso='child-torso',torso_junction='start')
 '''),
('seated-angler-with-catch','SQUARE',
 'The rejected fish is oversized and the body and fishing line merge into an ambiguous shape. Restore the seated angler, stool and suspended catch.',
 'Balanced the smaller fish against a seated person, using a curved fishing rod, fine clear line and explicit stool.',
 '''
 # Plan: right-facing seated body on stool, left arcing rod, hanging fish at left.
 circle(s,'head',35,10,5)
 s.add_line('torso',(35,23),(35,33))
 s.add_polyline('leg',(35,33),(25,33),(24,44))
 s.add_polyline('arm',(35,23),(29,28),(22,23))
 for p in ('leg','arm'): s.relate('connect','torso',p)
 path(s,'rod',(22,23),('C',(7,5),(19,12),(13,5)))
 s.add_line('line',(7,5),(7,24));s.relate('connect','line','rod')
 path(s,'fish',(7,24),('C',(7,36),(0,28),(2,33)),('C',(7,24),(12,32),(13,28)),closed=True)
 s.relate('connect','line','fish')
 s.add_polyline('tail',(7,36),(3,41),(11,41),(7,36),closed=True);s.relate('connect','tail','fish')
 s.add_polyline('stool',(33,41),(43,41),(43,46))
 s.mark_human_figure('angler',head='head',torso='torso',torso_junction='start')
 '''),
('seated-forward-fold','HRECT_M',
 'The rejected figure is a D-shaped curve with a detached head and rigid vertical arm. Restore a bent back and arms reaching toward the feet.',
 'Rebuilt a low folded torso, forward-reaching arm, rounded hip and extended seated legs.',
 '''
 # Plan: head left of upper torso, exact 13u center distance for r5 head; low horizontal pose.
 circle(s,'head',10,20,5)
 s.add_bezier('torso',(23,20),((32,20),(44,19),(44,30)))
 path(s,'hip-leg',(44,30),('C',(26,40),(44,39),(37,40)),('L',(4,40)))
 s.relate('connect','torso','hip-leg')
 s.add_polyline('arm',(23,20),(19,31),(4,31));s.relate('connect','arm','torso')
 s.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
 '''),
('seated-huddled-person','VRECT_L',
 'The rejected head floats above a horizontal bar and zigzag. Restore a bowed person embracing raised knees.',
 'Drew a bowed head close to a sloping shoulder, curved seated back, folded leg and embracing arm.',
 '''
 # Plan: bowed head, shoulder to back curve, knees and embracing forearm.
 circle(s,'head',25,9,5)
 s.add_bezier('torso',(20,21),((14,24),(10,29),(10,35)))
 path(s,'hips',(10,35),('A',(21,41),7,7,False),('L',(29,30)),('L',(38,43)))
 s.relate('connect','torso','hips')
 s.add_polyline('embracing-arm',(20,21),(34,26),(23,28));s.relate('connect','torso','embracing-arm')
 s.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
 '''),
('seated-kitten','VRECT_L',
 'The rejected kitten loses its curled tail and distinct paws and looks like a generic cat-shaped bag. Restore the large kitten head and sitting anatomy.',
 'Rebuilt a broad rounded head with pointed ears, small eyes, two front paws and a curled side tail.',
 '''
 # Plan: symmetric broad head and narrow seated torso; tail intentionally left-sided.
 path(s,'head',(16,26),('C',(11,14),(10,24),(9,20)),('L',(10,4)),('L',(18,10)),('C',(30,10),(22,8),(26,8)),('L',(38,4)),('L',(37,14)),('C',(32,26),(39,20),(38,24)))
 path(s,'body',(16,26),('C',(14,40),(14,30),(12,35)),('A',(18,44),4,4,False),('L',(32,44)),('A',(36,40),4,4,False),('C',(32,26),(36,35),(34,30)))
 s.relate('connect','head','body')
 s.add_line('paws',(25,34),(25,44));s.relate('connect','paws','body')
 path(s,'tail',(13,31),('C',(5,37),(7,29),(5,34)),('C',(15,44),(5,43),(9,44)));s.relate('connect','tail','body')
 s.add_dot('eye-left',(19,18));s.add_dot('eye-right',(29,18))
 '''),
('seated-laptop-worker-edited-upload-289b77a645eb9952','SQUARE',
 'No original is available; the displayed drawing has a floating head, no torso and a laptop that resembles a chair back. Restore an explicit person using a laptop at a desk.',
 'Rebuilt the torso and seated legs beside an open laptop and desk, with forearm reaching the keyboard.',
 '''
 # Plan: laptop and desk at left, seated worker at right; head r5 and vertical 13u neck distance.
 circle(s,'head',35,9,5)
 s.add_line('torso',(35,22),(35,33))
 s.add_polyline('arm',(35,22),(30,27),(24,27));s.relate('connect','torso','arm')
 s.add_polyline('leg',(35,33),(25,33),(22,44));s.relate('connect','torso','leg')
 s.add_polyline('laptop',(7,14),(11,27),(21,27))
 s.add_polyline('desk',(4,32),(18,32))
 s.add_line('desk-leg',(8,32),(8,44));s.relate('connect','desk','desk-leg')
 s.add_polyline('chair',(35,36),(43,36),(43,44))
 s.mark_human_figure('worker',head='head',torso='torso',torso_junction='start')
 '''),
('seated-meditation-curved-arms','SQUARE',
 'The rejected torso forms an angular tent over a large X; the hands and curved arms disappear. Restore relaxed inward-curving arms and lotus legs.',
 'Added rounded shoulders with inward-curving hands and a low crossing-leg silhouette, preserving the upright meditating head.',
 '''
 # Plan: mirrored shoulders/curved forearms, separate hands, crossed seated legs.
 circle(s,'head',24,9,5)
 s.add_line('torso',(24,22),(24,32))
 for side,sgn in [('left',-1),('right',1)]:
     p=lambda x,y:(24+sgn*x,y)
     path(s,'arm-'+side,(24,22),('C',p(15,30),p(10,22),p(15,23)),('C',p(7,33),p(15,35),p(10,33)))
     s.relate('connect','torso','arm-'+side)
 s.relate('connect','arm-left','arm-right')
 path(s,'leg-front',(8,36),('L',(37,44)),('C',(41,37),(43,45),(44,40)),('L',(35,35)))
 path(s,'leg-back',(8,36),('C',(7,44),(2,36),(3,43)),('L',(20,40)))
 s.relate('connect','leg-front','leg-back')
 s.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
 '''),
('seated-meditation-upright','SQUARE',
 'The rejected broad triangular arms and X-shaped legs no longer resemble the upright lotus pose. Restore upright sides and visibly seated crossed legs.',
 'Drew rounded shoulders, straight lowered arms and a low folded-leg base around a centered upright head.',
 '''
 # Plan: upright symmetric torso and lowered arms; asymmetric leg overlap from source.
 circle(s,'head',24,9,5)
 s.add_line('torso',(24,22),(24,33))
 path(s,'shoulders',(12,34),('L',(12,30)),('A',(20,22),8,8,True),('L',(28,22)),('A',(36,30),8,8,True),('L',(36,34)))
 s.relate('connect','torso','shoulders')
 path(s,'leg-front',(9,35),('L',(30,42)),('C',(28,46),(35,43),(33,47)),('L',(8,40)),('A',(9,35),3,3,True),closed=True)
 path(s,'leg-back',(27,37),('L',(38,34)),('A',(40,42),4,4,True),('L',(33,44)))
 s.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
 '''),
]

def author(indices=None):
    items=json.loads((BATCH/'items.json').read_text())
    outputs=[]
    for i,(ident,keyshape,comparison,change,body) in enumerate(DESIGNS):
        if indices is not None and i+1 not in indices: continue
        item=next(x for x in items if x['id']==ident)
        ref=Path(item['reference']);uid=re.search(r'[0-9a-f-]{36}$',ref.stem).group()
        stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
        run=ROOT/'icon_set/work/primitive-make-ray'/uid/(stamp+'-meaning-fix')
        run.mkdir(parents=True)
        meta={'concept':ref.stem[:-37],'source_uuid':uid,'reference_path':str(ref),'icon_id':ident,'author':AUTHOR}
        (run/(ident+'.metadata.json')).write_text(json.dumps(meta,indent=2))
        (run/'comparison.md').write_text(f"Reference: {ref}\n\nRejected: {item['fix']}/before/{ident}.svg\n\nFinding: {comparison}\n\nFeedback: {item['feedback']}\n\nRevision: {change}\n")
        module=run/(ident.replace('-','_')+'_'+uid.replace('-','_')+'.py')
        source=f'"""{change}\n{comparison}\nKeyshape {keyshape}; preserve reference proportions where a documented visual exception is needed.\nConstruction refs: human_ref/user.svg and full_body_ref.png for human vocabulary; Lucide heart/cat/sailboat for related contour construction.\n"""\nfrom icon_set.model.keyshapes import Keyshape\nfrom icon_set.model.icons.solo._base import Solo48\nSOURCE_ICON_ID = {uid!r}\nSOURCE_PATH = {str(ref)!r}\nAUTHOR = {AUTHOR!r}\n'+HELPERS+f'\nclass Drawing(Solo48):\n    icon_id = {ident!r}\n    keyshape = Keyshape.{keyshape}\n    semantic_role = "MAIN"\n    semantic_kind = "noun"\n    category = "primitives"\n    aliases = ()\n    keywords = {tuple(meta["concept"].split())!r}\n\n    def build(self):\n        s=self\n'+textwrap.indent(textwrap.dedent(body).strip(),'        ')+'\n'
        module.write_text(source)
        icon=load_icon(module);report=icon.validate_icon();svg=icon.to_svg()
        (run/(ident+'.svg')).write_text(svg)
        (run/'validation.txt').write_text(report.describe())
        render_previews(svg,ident,48,run)
        cairosvg.svg2png(url=str(ROOT/ref),write_to=str(run/'reference.png'),output_width=384,output_height=384,background_color='white')
        result={**meta,'run':str(run.relative_to(ROOT)),'module':module.name,'svg':ident+'.svg','comparison':comparison,'change':change,'validation_status':report.status,'errors':list(report.errors),'warnings':list(report.warnings),'visual_review':'pending','omissions':change}
        (run/'candidate.json').write_text(json.dumps(result,indent=2))
        outputs.append(result)
        print(i+1,ident,report.status,len(report.errors),len(report.warnings),flush=True)
    existing=json.loads((BATCH/'runs.json').read_text()) if (BATCH/'runs.json').exists() else []
    byid={r['icon_id']:r for r in existing};byid.update({r['icon_id']:r for r in outputs})
    (BATCH/'runs.json').write_text(json.dumps([byid[d[0]] for d in DESIGNS if d[0] in byid],indent=2))

if __name__=='__main__': author([int(x) for x in sys.argv[1:]] or None)
