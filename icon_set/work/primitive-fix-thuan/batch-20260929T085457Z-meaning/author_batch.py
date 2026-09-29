"""Fresh, hand-authored SOLO48 revisions; no registered artwork is changed."""
from pathlib import Path
from datetime import datetime, timezone
import json, sys, re, importlib.util

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))
HERE = Path(__file__).parent
AUTHOR = 'gpt-6'
SOURCE_ICON_ID = None  # Per-input identities are retained in every generated module.
SOURCE_PATH = str(HERE / 'inputs.json')

HELPERS = '''
    def path(self, name, start, *segments, closed=False):
        ids = []
        point = start
        for j, segment in enumerate(segments):
            eid = f"{name}-{j}"
            if len(segment) == 2:
                self.add_line(eid, point, segment)
                end = segment
            else:
                end, rx, ry, sweep, large = segment
                self.add_arc(eid, point, end, radius_x=rx, radius_y=ry,
                             sweep=sweep, large_arc=large)
            ids.append(eid)
            point = end
        self.add_contour(name, *ids, closed=closed)

    def circle(self, name, x, y, r):
        self.path(name, (x-r,y), ((x+r,y),r,r,True,False),
                  ((x-r,y),r,r,True,False), closed=True)

    def oval(self, name, x, y, rx, ry):
        self.path(name, (x-rx,y), ((x+rx,y),rx,ry,True,False),
                  ((x-rx,y),rx,ry,True,False), closed=True)

    def box(self, name, x1,y1,x2,y2,r=3):
        self.path(name, (x1+r,y1), (x2-r,y1),
                  ((x2,y1+r),r,r,True,False), (x2,y2-r),
                  ((x2-r,y2),r,r,True,False), (x1+r,y2),
                  ((x1,y2-r),r,r,True,False), (x1,y1+r),
                  ((x1+r,y1),r,r,True,False), closed=True)
'''

# Each plan follows inspection of both the actual reference and rejected SVG.
SPECS = {}
def spec(name, keyshape, wrong, change, body, refs='human_ref/full_body_ref.png'):
    SPECS[name] = dict(keyshape=keyshape, wrong=wrong, change=change,
                       body=body, construction_reference=refs)

spec('seated-mermaid-with-raised-tail','VRECT_L',
     'A generic stick head and bucket-like tail lost the long hair, human torso and raised split fin.',
     'Restore long flowing hair, a seated torso, supporting arm and a sweeping fish tail ending in two fin lobes.', '''
        # One flowing silhouette; profile face and hair remain continuous anatomy.
        self.path('hair', (10,25), ((8,17),7,9,True,False), (10,13), (10,10),
                  ((22,4),8,7,True,False), ((26,8),5,4,True,False),
                  ((17,11),8,4,True,False), (17,17), ((13,23),5,7,True,False))
        self.path('face-neck', (24,10), (25,15), (22,17), (22,21),
                  ((27,28),7,8,False,False), (31,30))
        self.path('body-tail', (13,24), (12,36), ((25,44),15,9,False,False),
                  ((39,27),15,18,False,False))
        self.path('tail-top', (18,32), ((35,29),14,7,False,False), (35,25))
        self.path('fin', (35,25), ((29,17),7,8,True,False),
                  ((36,21),10,8,True,False), ((42,17),9,8,False,False),
                  ((39,27),6,10,True,False))
        self.path('support-arm', (10,27), (8,40), (8,44))
     ''')

spec('seated-person','VRECT_M',
     'The legs spread backward and forward like a runner, and the raised arm did not read as seated.',
     'Put both bent legs in front of a rounded seated hip and extend a relaxed arm over the knees.', '''
        self.circle('head',20,9,5)
        self.path('torso', (20,22), (20,25), ((15,38),11,14,False,False),
                  ((21,40),6,5,False,False), (29,34), (38,44))
        self.path('arm', (20,22), (32,22), (32,27))
        self.path('near-leg', (21,40), (28,40), (31,44))
        self.relate('connect','torso','arm')
        self.relate('connect','torso','near-leg')
        self.mark_human_figure('person',head='head',torso='torso-0',torso_junction='start')
     ''')

spec('seated-prayer-pose','SQUARE',
     'A triangular crossbar replaced praying hands and the crossed legs became a disconnected V.',
     'Show hands joined upright at the chest, bent elbows and a closed crossed-leg seat.', '''
        self.circle('head',24,9,5)
        # Mirrored shoulder/elbow arcs leave an explicit upright prayer gesture.
        self.path('shoulders', (10,30), (12,25), ((19,22),10,5,True,False))
        self.path('shoulder-right',(29,22),((36,25),10,5,True,False),(38,30))
        self.path('praying-arms', (10,30), ((15,33),4,4,False,False),
                  (24,28), (24,22))
        self.path('right-forearm',(24,28),(33,33),((38,30),4,4,False,False))
        self.path('crossed-legs',(24,39),(12,35),((6,39),4,4,False,False),
                  ((11,43),5,4,False,False),(37,43),((42,39),5,4,False,False),
                  ((36,35),4,4,False,False),(24,39),(31,42))
        self.relate('connect','shoulders','praying-arms')
        self.relate('connect','shoulder-right','right-forearm')
        self.relate('connect','praying-arms','right-forearm')
     ''')

spec('seated-sauna-bather','SQUARE',
     'The squared torso read as a letter E, and the tiny broken bench did not support the bather.',
     'Use a relaxed seated pose on a continuous bench and three rising steam strokes.', '''
        self.circle('head',15,11,5)
        self.path('torso',(15,24),(15,27),((16,34),4,6,False,False),(28,34),(35,44))
        self.path('arm',(15,24),(22,26),(27,26))
        self.path('bench',(6,44),(6,34),(16,34))
        for j,x in enumerate((26,34,42)):
            self.path(f'steam-{j}',(x,5),((x,11),4,5,True,False),((x,17),4,5,False,False))
        self.relate('connect','torso','arm')
        self.mark_human_figure('bather',head='head',torso='torso-0',torso_junction='start')
     ''')

spec('seated-shoulder-massage','SQUARE',
     'A single straight connector between two stick figures looked like pushing rather than shoulder massage.',
     'Place a taller therapist behind the seated recipient, with two bent arms reaching the upper shoulders.', '''
        self.circle('therapist-head',12,8,4)
        self.add_line('therapist-torso',(12,20),(12,34))
        self.path('therapist-legs',(7,44),(12,34),(17,44))
        self.circle('client-head',34,16,4)
        self.path('client-torso',(34,28),(34,31),(32,35),((35,39),4,4,False,False),(42,39),(42,44))
        self.path('near-arm',(12,20),(23,24),(30,28))
        self.path('far-arm',(12,26),(22,31),(29,31))
        self.add_line('seat',(25,44),(36,44))
        self.relate('connect','therapist-torso','therapist-legs')
        self.relate('connect','therapist-torso','near-arm')
        self.relate('connect','therapist-torso','far-arm')
        self.mark_human_figure('therapist',head='therapist-head',torso='therapist-torso',torso_junction='start')
        self.mark_human_figure('recipient',head='client-head',torso='client-torso-0',torso_junction='start')
     ''')

spec('seated-teddy-bear','VRECT_L',
     'The lower outline looked like trousers and the head had no recognizable teddy muzzle.',
     'Separate two round seated paws, add rounded arms and a small central nose under the domed bear head.', '''
        # Bilateral head, ears and paws use shared dimensions.
        self.oval('head',24,16,11,10)
        self.path('left-ear',(14,14),((20,9),5,5,True,True))
        self.path('right-ear',(28,9),((34,14),5,5,True,True))
        self.add_dot('nose',(24,17))
        self.oval('left-paw',13,37,6,7)
        self.oval('right-paw',35,37,6,7)
        self.path('left-arm',(16,25),((7,32),10,10,False,False),(8,34))
        self.path('right-arm',(32,25),((41,32),10,10,True,False),(40,34))
        self.path('belly',(19,41),((29,41),12,4,False,False))
     ''','No useful Lucide teddy match; original reference controls the ears, belly and paws.')

spec('security-key-with-notched-shaft','HRECT_M',
     'The short stepped stem did not preserve the long horizontal key shaft and repeated lower teeth.',
     'Restore the round bow, enclosed keyhole, long shaft, pointed tip and two bottom notches.', '''
        # Circular bow and integrated notched shaft; asymmetric by key function.
        self.path('outline',(27,18),(39,18),(44,24),(40,30),(36,30),(33,27),
                  (30,30),(27,30),((27,18),12,12,True,True),closed=True)
        self.circle('keyhole',17,24,3)
     ''','lucide/original/key-round.svg and atomic-debug/key-round.svg: circular bow and integrated toothed contour.')

spec('security-officer','VRECT_L',
     'The skewed top-hat shape and M-shaped torso lost the peaked security cap and uniform.',
     'Restore a broad peaked cap, circular jaw, open uniform collar and one lowered arm.', '''
        self.path('cap',(16,13),(14,5),(34,8),(32,13),(16,13),closed=True)
        self.add_line('visor',(11,13),(16,13))
        self.path('jaw',(17,13),((31,13),7,7,False,False))
        self.path('uniform',(8,44),(9,36),((17,27),8,9,True,False),
                  (24,33),(30,27),((39,36),9,9,True,False),(39,44))
        self.add_line('left-seam',(17,37),(17,44))
        self.add_line('right-seam',(31,37),(31,44))
        self.relate('connect','cap','visor')
     ''','human_ref/user.svg: circular jaw and broad shoulders; original reference: peaked cap and collar.')

spec('security-officer-holding-passport','SQUARE',
     'A thick rectangular block looked like a sign; the officer lacked a peaked cap and uniform collar.',
     'Restore an open passport booklet, an extended bent arm, peaked cap and uniform neckline.', '''
        self.path('passport',(4,8),(12,11),(12,25),(4,22),(4,8),closed=True)
        self.path('back-cover',(4,8),(19,6),(19,21),(12,22))
        self.path('cap',(28,15),(25,8),(43,10),(41,15),(28,15),closed=True)
        self.add_line('visor',(24,15),(28,15))
        self.path('jaw',(28,15),((40,15),6,6,False,False))
        self.path('uniform',(25,44),(25,33),(19,36),(8,29))
        self.path('shoulders',(25,33),(29,29),(34,33),(39,29),
                  ((44,36),6,8,True,False),(44,44))
        self.relate('connect','uniform','shoulders')
     ''','human_ref/user.svg: circular jaw and shoulders; original reference: booklet and extended hand.')

spec('security-officer-with-bag','SQUARE',
     'The bag looked like a tall bottle and the officer torso collapsed to an M.',
     'Make a wide handled luggage case beside a uniformed officer with a peaked cap and connected carrying arm.', '''
        self.box('bag',4,29,19,43,3)
        self.path('bag-handle',(8,29),(8,24),((15,24),4,4,True,False),(15,29))
        self.path('cap',(28,13),(25,5),(43,8),(41,13),(28,13),closed=True)
        self.add_line('visor',(24,13),(28,13))
        self.path('jaw',(28,13),((40,13),6,6,False,False))
        self.path('body',(27,44),(27,33),(22,37),(19,37))
        self.path('shoulders',(27,33),(29,27),(34,32),(39,27),
                  ((44,35),6,9,True,False),(44,44))
        self.relate('connect','bag','bag-handle')
        self.relate('connect','body','bag')
        self.relate('connect','body','shoulders')
     ''','human_ref/user.svg: circular jaw and shoulders; original reference: squat handled luggage.')

spec('seeker','SQUARE',
     'The person was reduced to two disconnected bars beside an oversized magnifier.',
     'Restore a recognizable head-and-shoulders portrait and a magnifying lens in the foreground.', '''
        self.circle('head',16,11,6)
        self.path('shoulder',(6,43),(6,33),((15,25),9,8,True,False),(16,25))
        self.add_line('body-seam',(14,35),(14,43))
        self.circle('lens',32,29,10)
        self.add_line('handle',(39,36),(44,43))
        self.relate('connect','lens','handle')
     ''','human_ref/user.svg: circular head and rounded shoulder; original reference: foreground magnifier.')

spec('wide-leg-inversion-pose','VRECT_L',
     'The rigid Y and sideways crossbar did not show the folded pelvis and bent supporting arms of the inverted pose.',
     'Restore raised spread legs, a short inverted torso, low head, and two bent forearms reaching the floor.', '''
        self.path('legs',(8,4),(24,22),(40,4))
        self.add_line('torso',(24,22),(24,26))
        self.circle('head',24,39,5)
        self.path('left-arm',(24,26),(12,26),(8,34),(11,42))
        self.path('right-arm',(24,26),(36,26),(40,34),(37,42))
        self.relate('connect','legs','torso')
        self.relate('connect','torso','left-arm')
        self.relate('connect','torso','right-arm')
        self.mark_human_figure('inverted-person',head='head',torso='torso',torso_junction='end')
     ''')

spec('wild-bird','VRECT_L',
     'The beak and eye were missing, and a blunt tail turned the bird into an abstract leaf.',
     'Restore the left-facing pointed beak, small eye, rounded breast, swept wing and tapered tail with two legs.', '''
        self.path('body',(13,10),((27,8),9,8,True,False),(41,36),
                  (32,33),((17,35),15,8,True,False),((11,18),10,18,True,False),(13,10),closed=True)
        self.path('beak',(12,11),(6,15),(11,18))
        self.add_dot('eye',(19,14))
        self.path('wing',(22,23),((28,27),7,6,False,False))
        self.add_line('leg-left',(20,36),(17,44))
        self.add_line('leg-right',(29,35),(27,44))
        self.relate('connect','beak','body')
     ''','lucide/original/bird.svg and atomic-debug/bird.svg: simple beak, sweep of breast and two short legs.')

spec('windsurfer-on-waves','SQUARE',
     'The rigid figure and straight base looked like a person beside a sail, with no wave or bent surfing stance.',
     'Show a wind-filled sail, hand gripping the boom, bent surfing legs, an angled board and a low wave.', '''
        self.path('sail',(8,32),((29,4),31,32,True,False),(22,33),(8,32),closed=True)
        self.add_line('mast',(29,4),(21,36))
        self.circle('head',39,12,4)
        self.path('torso',(39,24),(39,26),(35,28))
        self.path('arm',(39,24),(31,24),(25,20))
        self.path('legs',(27,36),(29,31),(35,28),(42,32),(42,36))
        self.path('board',(5,36),(44,36))
        self.path('wave',(5,44),((15,44),8,4,False,False),((25,44),8,4,True,False),
                  ((35,44),8,4,False,False),((43,44),8,4,True,False))
        self.relate('connect','mast','sail')
        self.relate('connect','torso','arm')
        self.relate('connect','torso','legs')
        self.mark_human_figure('surfer',head='head',torso='torso-0',torso_junction='start')
     ''')

spec('winged-female-demon','SQUARE',
     'The arrow tail merged into the legs and the body lost the dress; the wings looked like drooping arms.',
     'Restore two horns, detached bat wings, a flared dress and an independent curved arrow tail.', '''
        self.circle('head',24,10,5)
        self.path('left-horn',(20,6),(18,3))
        self.path('right-horn',(28,6),(30,3))
        self.path('dress',(18,26),(15,38),(33,38),(30,26),((18,26),6,3,False,False),closed=True)
        self.add_line('left-leg',(20,38),(20,44))
        self.add_line('right-leg',(28,38),(28,44))
        self.path('left-wing',(13,25),(10,20),(5,21),(4,12),((14,15),12,6,True,False))
        self.path('right-wing',(35,25),(38,20),(43,21),(44,12),((34,15),12,6,False,False))
        self.path('tail',(33,35),((42,29),9,7,False,False),(43,26))
        self.path('tail-point',(38,28),(43,26),(45,31))
        self.relate('connect','tail','tail-point')
        self.relate('connect','head','left-horn')
        self.relate('connect','head','right-horn')
        self.relate('connect','dress','left-leg')
        self.relate('connect','dress','right-leg')
     ''','human_ref/full_body_ref.png: flared female silhouette; original reference: horns, bat wings and arrow tail.')

spec('winged-harpy-profile','SQUARE',
     'A stick person with a horizontal wing box lost the woman’s profile, hair, bird body, feathered wings and talons.',
     'Restore a profile head with flowing hair, feathered spread wings, tapered bird body and clawed feet.', '''
        self.path('hair',(17,21),(18,9),((27,4),7,6,True,False),
                  ((29,10),5,6,True,False),((23,12),7,5,True,False),(23,18))
        self.path('face-body',(29,10),(30,16),(27,18),(27,21),
                  ((25,33),8,10,True,False),(16,39),(20,30))
        self.path('left-wing',(18,21),((5,14),24,15,True,False),(6,24),
                  (10,27),(8,29),((18,31),11,5,False,False))
        self.path('right-wing',(28,22),((43,14),25,14,False,False),(42,24),
                  (38,27),(40,29),((29,32),11,5,True,False))
        self.path('left-claw',(22,36),(23,43),(19,44))
        self.path('right-claw',(28,35),(32,42),(36,44))
     ''','human_ref/user.svg: rounded human face; original reference controls continuous neck, hair and avian anatomy.')

spec('winged-person','SQUARE',
     'Oversized curled shapes replaced feather wings and the tiny body looked like an insect.',
     'Restore a full-height human body with separate arms and legs and compact scalloped wings attached behind the shoulders.', '''
        self.circle('head',24,9,5)
        self.path('body',(17,44),(17,24),((24,22),9,3,True,False),
                  ((31,24),9,3,True,False),(31,44))
        self.add_line('leg-divider',(24,35),(24,44))
        self.path('left-wing',(17,24),((4,22),9,6,False,False),
                  ((8,29),6,6,False,False),((12,33),4,4,False,False))
        self.path('right-wing',(31,24),((44,22),9,6,True,False),
                  ((40,29),6,6,True,False),((36,33),4,4,True,False))
        self.relate('connect','body','left-wing')
        self.relate('connect','body','right-wing')
     ''')

spec('winged-serpent-dragon','SQUARE',
     'The coiled lines lacked a readable dragon head and bat wing, becoming an abstract loop.',
     'Restore a left-facing long-snouted serpent with curved belly, a large pointed bat wing and a tapering tail.', '''
        self.path('head-back',(5,29),(5,24),(14,16),(13,22),
                  ((24,25),12,7,True,False))
        self.path('belly-tail',(5,29),(12,29),((23,30),11,8,True,False),
                  (38,40),((14,38),16,11,True,False))
        self.path('wing',(24,25),((19,4),27,25,False,False),
                  ((43,15),34,27,True,False),((38,22),7,8,False,False),
                  ((38,40),29,20,True,False),((29,23),25,22,False,False))
        self.relate('connect','head-back','belly-tail')
        self.relate('connect','head-back','wing')
        self.relate('connect','belly-tail','wing')
     ''','No useful Lucide fantasy match; original reference controls the asymmetrical wing and serpentine silhouette.')

spec('wireless-mobile-yuan-payment-solo','VRECT_L',
     'An open U-shaped device and one arc looked like a purse; the closed phone and second wireless wave were absent.',
     'Restore a closed rounded phone, two separated wireless arcs and a legible yuan symbol; omit the crowded bottom divider.', '''
        self.box('phone',13,18,35,44,3)
        self.path('wireless-outer',(8,8),((40,8),24,18,True,False))
        self.path('wireless-inner',(16,13),((32,13),14,10,True,False))
        self.path('yuan',(20,24),(24,30),(28,24))
        self.add_line('yuan-stem',(24,30),(24,36))
        self.add_line('yuan-bar',(20,32),(28,32))
        self.relate('connect','yuan','yuan-stem')
        self.relate('connect','yuan-stem','yuan-bar')
     ''','lucide/original/smartphone.svg and atomic-debug/smartphone.svg: closed rounded phone housing; source: two wireless arcs.')

spec('yen-currency-message-bubble-solo','SQUARE',
     'The bubble tail was nearly absent and two tiny dots replaced the message lines.',
     'Restore a distinct lower-right speech tail, two horizontal text strokes, and an open yuan/yen glyph.', '''
        self.path('bubble',(10,6),(38,6),((43,11),5,5,True,False),(43,32),
                  ((38,37),5,5,True,False),(34,37),(34,44),(25,37),(10,37),
                  ((5,32),5,5,True,False),(5,11),((10,6),5,5,True,False),closed=True)
        self.path('currency',(12,15),(18,23),(24,15))
        self.add_line('currency-stem',(18,23),(18,30))
        self.add_line('currency-bar',(13,24),(23,24))
        self.add_line('message-one',(30,20),(36,20))
        self.add_line('message-two',(30,28),(36,28))
        self.relate('connect','currency','currency-stem')
        self.relate('connect','currency','currency-bar')
        self.relate('connect','currency-stem','currency-bar')
     ''','Original reference: lower-right bubble tail, currency sign and two text lines; no additional Lucide match required.')

def create(names=None):
    from icon_set.scripts.primitive_fix import load_icon, render_previews
    inputs=json.loads((HERE/'inputs.json').read_text())
    outputs=[]
    for row in inputs:
        name=row['icon_id']
        if name not in SPECS or (names and name not in names): continue
        plan=SPECS[name]
        source_uuid=re.search(r'[0-9a-f-]{36}$',Path(row['reference']).stem).group()
        concept=Path(row['reference']).stem[:-37]
        stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
        out=ROOT/'icon_set/work/primitive-make-ray'/source_uuid/(stamp+'-meaning-fix')
        out.mkdir(parents=True)
        metadata=dict(concept=concept,source_uuid=source_uuid,reference_path=row['reference'])
        (out/f'{name}.metadata.json').write_text(json.dumps(metadata,indent=2))
        (out/'review-before-drawing.md').write_text(f"# {name}\n\nReference: {row['reference']}\n\nRejected drawing: {row['before']}\n\nObserved problem: {plan['wrong']}\n\nFeedback: Does not convey the intended meaning.\n\nRevision plan: {plan['change']}\n\nConstruction reference: {plan['construction_reference']}\n")
        filename=name.replace('-','_')+'_'+source_uuid.replace('-','_')+'.py'
        source=f'''"""{plan['change']}"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = {source_uuid!r}
SOURCE_PATH = {row['reference']!r}
AUTHOR = "gpt-6"

class RevisedIcon(Solo48):
    icon_id = {name!r}
    keyshape = Keyshape.{plan['keyshape']}
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/people" 
    aliases = ()
    keywords = ({concept!r},)
    # Symbol plan: {plan['change']}
    # Construction: {plan['construction_reference']}
{HELPERS}
    def build(self):
{plan['body']}
'''
        (out/filename).write_text(source)
        icon=load_icon(out/filename)
        report=icon.validate_icon()
        (out/'validation.txt').write_text(report.describe())
        svg=icon.to_svg();(out/f'{name}.svg').write_text(svg)
        render_previews(svg,name,48,out)
        row.update(result_dir=str(out.relative_to(ROOT)),module=filename,source_uuid=source_uuid,plan=plan)
        outputs.append(row)
        print(name,report.status,len(report.errors),len(report.warnings),flush=True)
    old=json.loads((HERE/'drafts.json').read_text()) if (HERE/'drafts.json').exists() else []
    updates={r['icon_id']:r for r in old}
    updates.update({r['icon_id']:r for r in outputs})
    (HERE/'drafts.json').write_text(json.dumps(list(updates.values()),indent=2))

if __name__=='__main__': create(sys.argv[1:] or None)
