from pathlib import Path
import json, sys, textwrap
ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))
HERE = Path(__file__).resolve().parent
ITEMS = json.loads((HERE / 'items.json').read_text())
AUTHOR = 'gpt-6'
SOURCE_ICON_ID = None  # Each authored module and metadata record retains its exact input UUID.
SOURCE_PATH = str(HERE / 'items.json')
HELPERS = '''
        def path(name, start, commands, closed=False):
            members = []
            here = start
            for i, cmd in enumerate(commands):
                kind, end, *args = cmd
                if kind == 'L' and end == here:
                    continue
                key = f'{name}-{i}'
                if kind == 'L': self.add_line(key, here, end)
                elif kind == 'A':
                    rx, ry, sweep = args
                    self.add_arc(key, here, end, radius_x=rx, radius_y=ry, sweep=sweep)
                elif kind == 'C': self.add_bezier(key, here, (args[0], args[1], end))
                members.append(key)
                here = end
            self.add_contour(name, *members, closed=closed)
        def oval(name, x, y, rx, ry):
            path(name,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def circle(name,x,y,r): oval(name,x,y,r,r)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line, poly = self.add_line, self.add_polyline
        join = lambda a,b: self.relate('connect',a,b)
'''
DESIGNS = {}
def design(i, shape, finding, plan, code, lucide='No useful subject match; geometric construction from the supplied original.'):
    DESIGNS[i] = dict(shape=shape,finding=finding,plan=plan,code=textwrap.dedent(code),lucide=lucide)

design(0,'SQUARE','The rejected jaws are angular and the lower marker loses its return edge; the source uses rounded left ends and fine horizontal measurement rules.',
 'Two matching rounded left jaw ends with sloping right closures; separate central marker and lower right rule. Centerline extremes (6,6)-(42,42).', '''
path('upper-jaw',(24,6),[('L',(10,6)),('A',(10,14),4,4,False),('L',(19,14)),('L',(24,6)),('L',(42,6))])
line('measure',(28,23),(42,23))
path('lower-jaw',(24,34),[('L',(19,26)),('L',(10,26)),('A',(10,34),4,4,False),('L',(24,34)),('L',(42,34)),('L',(42,42))])
''','Lucide ruler: coherent rule strokes and consistent round joins; original supplies the jaw geometry.')
design(1,'SQUARE','The rejected wolf has polygonal shoulders, a blocky tail and rectangular legs; the original has a long rising neck, curved back and hanging tail.',
 'One flowing side silhouette, lifted muzzle, two grounded legs and a curved hanging tail; asymmetry preserves the howling pose.', '''
path('outline',(6,42),[('C',(10,31),(9,40),(8,35)),('C',(17,23),(11,27),(13,24)),('C',(28,17),(23,21),(27,20)),('L',(26,17)),('L',(30,10)),('L',(35,8)),('L',(39,6)),('C',(41,10),(41,6),(41,8)),('L',(41,24)),('C',(38,31),(41,27),(40,29)),('L',(38,42))])
path('rear-leg',(17,23),[('C',(16,33),(15,26),(15,30)),('L',(16,42))])
path('belly',(16,35),[('C',(31,31),(23,37),(27,33)),('L',(33,42)),('L',(42,42))])
path('tail',(6,42),[('C',(16,35),(10,41),(13,38))])
for a,b in [('outline','rear-leg'),('rear-leg','belly'),('outline','tail'),('tail','belly')]: join(a,b)
''')
design(2,'SQUARE','The rejected dam has blocklike towers, only one water stroke and a crowded scalloped baseline; the source has sloped retaining walls and a separate lower wave.',
 'Paired sloping dam towers, horizontal upper spillway, two falling water strokes and separated coherent waves.', '''
for name,x in [('left',6),('right',34)]:
    poly(name,(x,34),(x+3,6),(x+8,6),(x+8,16),(x+5,34))
line('bridge-top',(14,10),(34,10)); line('bridge-bottom',(14,18),(34,18))
for j,x in enumerate((22,30)): line(f'water-{j}',(x,24),(x-2,30))
for name,y in [('waterline',34),('river',42)]:
    path(name,(6,y),[('C',(15,y),(9,y-4),(12,y+4)),('C',(24,y),(18,y-4),(21,y+4)),('C',(33,y),(27,y-4),(30,y+4)),('C',(42,y),(36,y-4),(39,y+4))])
for t in ['left','right']:
    for b in ['bridge-top','bridge-bottom','waterline']: join(t,b)
''')
design(3,'VRECT_L','The rejected mark bends and thickens its arrow arms; the source has a thin straight central stem and two straight rising arrows.',
 'Circular top ring, central stem and mirrored diagonal arrows, with one shared bottom node; centerline extremes x8..40, y4..44.', '''
circle('ring',24,10,6)
line('stem',(24,16),(24,44))
poly('arms',(8,26),(24,44),(40,26))
for side in (-1,1):
    x=24+16*side
    poly(f'tip-{side}',(x-side,34),(x,26),(x-7*side,29))
    join('arms',f'tip-{side}')
join('ring','stem');join('stem','arms')
''','Lucide anchor: one circular ring and actual stem attachments; source retains straight arrow arms.')
design(4,'HRECT_L','The rejected picture drops the small sun and has an abrupt, heavy mountain peak; the source has a spacious landscape frame and a smooth summit.',
 'Rounded rectangular image frame, a small sun and a gently rounded mountain; actual frame connections are split at the shared nodes.', '''
path('frame',(4,12),[('A',(8,8),4,4,True),('L',(40,8)),('A',(44,12),4,4,True),('L',(44,31)),('L',(44,36)),('A',(40,40),4,4,True),('L',(13,40)),('L',(8,40)),('A',(4,36),4,4,True),('L',(4,12))],True)
self.add_dot('sun',(15,19))
path('mountain',(13,40),[('L',(28,25)),('A',(34,25),4,4,True),('L',(44,35))])
join('frame','mountain')
''','Lucide image: rounded enclosure and rounded mountain summit with a separate sun.')
design(5,'HRECT_L','The rejected bubble has a thick pinched tail notch and an uneven oval; the original is a broad smooth bubble with a sweeping lower-left tail.',
 'Four smooth oval quadrants with one integrated curved tail; avoid an acute interior kink.', '''
path('bubble',(24,8),[('C',(44,23),(35,8),(44,14)),('C',(24,36),(44,31),(35,36)),('C',(19,35),(22,36),(20,36)),('C',(7,40),(16,39),(11,40)),('C',(11,33),(10,38),(12,35)),('C',(4,23),(6,30),(4,27)),('C',(24,8),(4,14),(13,8))],True)
''','Lucide message-circle: one continuous bubble/tail contour; original supplies the oval proportions.')
design(6,'SQUARE','The rejected tag substitutes a bent narrow arrow with a tiny tip for the original broad upward-right arrow and has uneven corner construction.',
 'Clipped rounded tag enclosing a wide outlined diagonal arrow; retain the distinctive source composition.', '''
path('tag',(20,6),[('L',(38,6)),('A',(42,10),4,4,True),('L',(42,28)),('L',(28,42)),('L',(10,42)),('A',(6,38),4,4,True),('L',(6,20)),('L',(20,6))],True)
path('arrow',(22,14),[('L',(34,14)),('L',(34,26)),('L',(29,21)),('L',(22,28)),('A',(16,22),4,4,True),('L',(23,15)),('L',(22,14))],True)
''')
design(7,'HRECT_L','The rejected logo changes the inner circular counter to a dot and uses a squared hook; the reference has a broad curved left emblem and a rounded vertical bar.',
 'A continuous thick-outline J-shaped emblem, circular counter and matched vertical capsule; retain three separate components.', '''
path('hook',(8,8),[('L',(24,8)),('A',(28,12),4,4,True),('L',(28,24)),('A',(12,40),16,16,True),('L',(8,40)),('A',(8,32),4,4,True),('L',(12,32)),('A',(20,24),8,8,False),('L',(20,16)),('L',(8,16)),('A',(8,8),4,4,True)],True)
circle('counter',11,24,3)
rounded('bar',36,8,44,40,4)
''')
design(8,'SQUARE','The rejected logo removes the rounded-square enclosure and loses the reference composition; the remaining lettering is oversized and uneven.',
 'Rounded square enclosing a small dot, italic i and smooth n with a finishing hook; lettering remains an intentional compact logo exception if required.', '''
rounded('frame',6,6,42,42,5)
self.add_dot('dot',(17,15))
path('i',(16,23),[('L',(13,32)),('C',(18,33),(12,36),(16,36))])
path('n',(22,34),[('L',(25,23)),('C',(34,27),(30,19),(36,21)),('L',(32,32)),('C',(37,33),(31,36),(35,36))])
''')
design(9,'HRECT_M','The rejected infinity is vertically pinched into a bow-tie; the original uses broad round lobes and a clear interweaving diagonal.',
 'Two equal round lobes linked by smooth diagonal transitions; deliberate interweaving break at the crossing.', '''
path('left-to-right',(24,24),[('C',(14,10),(19,18),(18,10)),('C',(4,24),(7,10),(4,16)),('C',(14,38),(4,32),(7,38)),('C',(29,18),(21,38),(24,24)),('C',(34,10),(31,13),(32,10)),('C',(44,24),(41,10),(44,16)),('C',(34,38),(44,32),(41,38)),('C',(27,29),(31,38),(29,32))])
''','Lucide infinity: paired rounded lobes and coherent diagonal transitions; reference supplies the open crossing.')

design(10,'SQUARE','The rejected figure has a bar-like shoulder and sprawling legs with no guard; the source shows a compact fighting stance and a raised bent arm.',
 'Shared human reference: circular radius-4 head at (24,10), neck at (24,22), exactly four visible units apart. Bent guard and grounded wide stance.', '''
circle('head',24,10,4)
line('torso',(24,22),(22,30))
path('guard',(24,22),[('L',(33,25)),('L',(38,16)),('L',(42,16))])
path('other-arm',(24,22),[('L',(16,21)),('L',(10,27)),('L',(17,27))])
poly('legs',(6,42),(16,32),(22,30),(32,33),(38,42))
for name in ['guard','other-arm','legs']:join('torso',name)
join('guard','other-arm')
self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
''','Shared human_ref/full_body_ref.png: circular head, coherent round-ended limbs; no useful Lucide pose match.')
design(11,'VRECT_L','The rejected high kicker has a disconnected-looking head and a stiff zigzag arm; the source shows a raised leg, leaning trunk and a compact guard.',
 'Radius-4 head at (17,8); upper torso starts (17,20), initially vertical, then bends into the hip. Head-to-neck ink gap exactly 4. Raised right leg and bent guard.', '''
circle('head',17,8,4)
path('torso',(17,20),[('C',(26,32),(17,25),(21,29))])
poly('guard',(17,20),(27,18),(29,13))
poly('arm',(17,20),(8,28),(13,32))
poly('legs',(26,44),(26,32),(40,8))
for name in ['guard','arm','legs']:join('torso',name)
join('guard','arm')
self.mark_human_figure('person',head='head',torso='torso-0',torso_junction='start')
''','Shared human_ref/full_body_ref.png: circular outlined head and simple bent limbs; source pose supplies the high kick.')
for i in (12,13):
    design(i,'SQUARE','The rejected boat is short and wide, its paddle blades become hook-like fragments, and its cockpit is cramped. The source has a long pointed hull and two complete diagonal paddle blades.',
     'Vertically pointed hull with mirrored smooth sides, oval cockpit, and complete diagonal double-ended paddle behind the hull. Paddle remains deliberately asymmetric relative to boat axis.', f'''
path('hull',(24,6),[('C',(34,24),(30,12),(34,18)),('C',(24,42),(34,30),(30,36)),('C',(14,24),(18,36),(14,30)),('C',(24,6),(14,18),(18,12))],True)
oval('cockpit',24,25,4,{5 if i == 12 else 8})
path('blade-upper',(35,15),[('C',(34,12),(34,14),(34,13)),('L',(39,6)),('L',(42,9)),('L',(37,15)),('C',(35,15),(36,16),(35,16))],True)
path('blade-lower',(13,33),[('C',(14,36),(14,34),(14,35)),('L',(9,42)),('L',(6,39)),('L',(11,33)),('C',(13,33),(12,32),(13,32))],True)
line('shaft-upper',(35,15),(33,18));line('shaft-lower',(13,33),(15,30))
join('blade-upper','shaft-upper');join('blade-lower','shaft-lower')
''','Lucide kayak: pointed hull with smooth curved sides and complete paired blades; source supplies vertical orientation and cockpit.')
design(14,'SQUARE','The rejected glove uses a sharp thumb and box-shaped palm with stubby fingers; the source has differentiated rounded fingertips, a smooth thumb and a wrist cuff.',
 'Four rounded fingers from shared 7-unit spacing, rounded thumb, broad palm and short cuff. Preserve five-digit glove identity while allowing compact finger spacing.', '''
path('glove',(14,25),[('L',(14,14)),('C',(21,14),(14,8),(21,8)),('L',(21,10)),('C',(28,10),(21,4),(28,4)),('L',(28,12)),('C',(35,12),(28,6),(35,6)),('L',(35,17)),('C',(42,17),(35,11),(42,11)),('L',(42,29)),('C',(37,38),(42,33),(38,36)),('L',(37,42)),('L',(18,42)),('L',(18,38)),('C',(13,32),(18,36),(15,34)),('L',(6,23)),('C',(11,20),(3,19),(7,16)),('L',(17,27))])
for j,(x,y) in enumerate([(21,14),(28,12),(35,17)]):
    line(f'finger-{j}',(x,y),(x,26));join('glove',f'finger-{j}')
''','Lucide hand: rounded finger tips, shared finger junctions, smooth thumb-to-palm contour; source adds the glove cuff.')
design(15,'HRECT_L','The rejected antelope is reduced to a rigid outline with stick legs and loses its swept horns, hind hoof and slender neck; the reference conveys a long airborne leap.',
 'Continuous outlined airborne body, bent foreleg, extended hind hoof, slender neck and swept horn. Preserve intentional forward motion and asymmetry.', '''
path('deer',(4,40),[('L',(8,30)),('L',(12,28)),('L',(12,23)),('C',(27,16),(18,21),(23,18)),('L',(31,10)),('L',(36,10)),('L',(44,15)),('C',(38,18),(45,18),(41,18)),('L',(37,24)),('L',(42,24)),('L',(42,34)),('L',(38,31)),('L',(37,28)),('L',(21,34)),('L',(17,39)),('L',(4,40))],True)
path('horn',(32,10),[('C',(34,8),(30,8),(31,8)),('L',(42,8))]);join('deer','horn')
path('tail',(12,23),[('C',(6,20),(9,23),(7,22))]);join('deer','tail')
''')
design(16,'SQUARE','The rejected dog has a jagged block muzzle and a cramped ball and drops the trainer hand; the reference shows a dog reaching toward a ball with a separate hand.',
 'Smooth dog head in profile, upright ear, curved neck and throat, separate ball and a minimal presenting hand. Keep the complete source composition.', '''
path('dog',(42,42),[('C',(37,29),(38,38),(37,34)),('C',(29,31),(34,33),(32,34)),('L',(31,25)),('L',(26,25)),('C',(23,21),(24,25),(23,24)),('L',(23,18)),('L',(29,18)),('C',(33,15),(31,18),(31,15)),('L',(36,15)),('L',(39,6)),('C',(42,13),(41,8),(42,11))])
circle('ball',24,33,4)
path('hand',(6,23),[('C',(14,28),(11,24),(12,25)),('L',(17,32)),('C',(14,35),(19,34),(17,35)),('L',(11,33))])
path('palm',(7,36),[('C',(11,40),(8,39),(9,40)),('L',(18,42))])
''','Lucide dog: smooth muzzle and distinct ear; source controls side profile, ball and hand.')
design(17,'HRECT_L','The rejected massage scene collapses the patient into disconnected short bars and fails to show a bent leg; the original has an upright therapist holding a reclining patient’s raised knee.',
 'Two figures with matching radius-4 heads. Therapist neck (15,22) lies 12 below head (15,10); patient neck (30,32) lies 12 left of head (42,32). Bent leg joins the reclined torso and therapist hand.', '''
circle('therapist-head',15,10,4)
line('therapist-torso',(15,22),(15,31))
poly('therapist-leg',(15,31),(8,40),(4,40))
path('therapist-arm',(15,22),[('L',(23,26)),('L',(26,22))])
circle('patient-head',42,32,4)
line('patient-torso',(30,32),(23,32))
poly('raised-leg',(23,32),(26,22),(21,18))
path('resting-leg',(23,32),[('L',(16,37)),('L',(25,40))])
join('therapist-torso','therapist-leg');join('therapist-torso','therapist-arm')
join('therapist-arm','raised-leg');join('patient-torso','raised-leg');join('patient-torso','resting-leg');join('raised-leg','resting-leg')
self.mark_human_figure('therapist',head='therapist-head',torso='therapist-torso',torso_junction='start')
self.mark_human_figure('patient',head='patient-head',torso='patient-torso',torso_junction='start')
''','Shared human_ref/full_body_ref.png: equal circular heads and coherent torso/limb runs; source supplies the interacting pose.')
design(18,'HRECT_L','The rejected log becomes a pill with a hook on top; it loses the concentric cut end and the open branch stump that distinguish the source.',
 'Circular cut end with a concentric growth ring, cylindrical log body and a short open branch stump. Retain the asymmetry of a real branch.', '''
circle('cut-face',16,28,12)
circle('growth-ring',16,28,4)
path('body',(16,16),[('L',(26,16)),('C',(30,13),(28,16),(29,15)),('L',(33,8)),('L',(42,8)),('L',(37,18)),('C',(44,28),(42,20),(44,24)),('C',(32,40),(44,35),(39,40)),('L',(16,40))])
path('stump',(33,8),[('C',(42,8),(35,11),(39,11))])
join('cut-face','body');join('body','stump')
''')
design(19,'HRECT_L','The rejected jumper has a tiny dot-like head and a crouched rather than airborne silhouette; the reference has a larger head, bent arms, split legs and a distinct ground line.',
 'Radius-4 head at (28,12), torso starts (23,23), yielding diagonal gap sqrt(146)-4 on centerline. Revise to exact 5-12-13 head placement with radius 5. Extended front leg, bent rear leg, and separated ground.', '''
circle('head',28,8,4)
path('torso',(28,20),[('C',(23,29),(28,24),(25,27))])
poly('back-arm',(28,20),(17,17),(12,23))
poly('front-arm',(28,20),(35,24),(40,22))
poly('front-leg',(23,29),(31,31),(40,36))
poly('back-leg',(23,29),(18,34),(10,32))
line('ground',(4,40),(44,40))
for n in ['back-arm','front-arm','front-leg','back-leg']:join('torso',n)
join('back-arm','front-arm');join('front-leg','back-leg')
self.mark_human_figure('person',head='head',torso='torso-0',torso_junction='start')
''','Shared human_ref/full_body_ref.png: outlined circular head and connected round-ended limbs; source supplies airborne split-leg motion.')

def write(i, attempt='01'):
    it, ds = ITEMS[i], DESIGNS[i]
    ref=Path(it['ref']); uuid=ref.stem[-36:]; concept=ref.stem[:-37]
    run=ROOT/'icon_set/work/primitive-make-ray'/uuid/f'20260928T175102Z-stroke-{attempt}'
    run.mkdir(parents=True,exist_ok=False)
    meta=dict(concept=concept,source_uuid=uuid,reference_path=it['ref'])
    (run/f"{it['id']}.metadata.json").write_text(json.dumps(meta,indent=2))
    (run/'review-before.md').write_text(f"Reference compared with rejected drawing: {ds['finding']}\n\nFeedback: Bad stroke drawn.\n\nRevision: {ds['plan']}\n\nConstruction reference: {ds['lucide']}\n")
    source=f'''"""{ds['plan']}\nConstruction: {ds['lucide']}"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = {uuid!r}
SOURCE_PATH = {it['ref']!r}
AUTHOR = {AUTHOR!r}

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
    module=run/(it['id'].replace('-','_')+'_'+uuid.replace('-','_')+'.py')
    module.write_text(source)
    it.update(run=str(run.relative_to(ROOT)),module=str(module.relative_to(ROOT)),finding=ds['finding'],change=ds['plan'],lucide=ds['lucide'])
    return it

if __name__ == '__main__':
    for i in map(int,sys.argv[1:]):
        write(i)
    (HERE/'items.json').write_text(json.dumps(ITEMS,indent=2))
