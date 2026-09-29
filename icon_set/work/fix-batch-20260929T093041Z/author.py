"""Fresh primitive-make-ray runs for the twenty explicitly claimed references.
Each generated module records its own SOURCE_ICON_ID, SOURCE_PATH and AUTHOR.
"""
from pathlib import Path
import json, sys, textwrap, io
from datetime import datetime, timezone
import cairosvg
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[2]
sys.path.insert(0, str(REPO))
from icon_set.scripts.primitive_fix import load_icon, render_previews
from icon_set.scripts.build_gate import gate

HELPERS = '''
    def path(self, name, start, steps, closed=False):
        members = []
        here = start
        for i, step in enumerate(steps):
            member = f"{name}-{i}"
            if step[0] == "L":
                self.add_line(member, here, step[1])
            else:
                self.add_arc(member, here, step[1], radius_x=step[2], radius_y=step[3], sweep=step[4])
            here = step[1]
            members.append(member)
        self.add_contour(name, *members, closed=closed)

    def circle(self, name, x, y, r):
        self.path(name, (x-r,y), [("A",(x+r,y),r,r,True),("A",(x-r,y),r,r,True)], True)

    def oval(self, name, x, y, rx, ry):
        self.path(name, (x-rx,y), [("A",(x+rx,y),rx,ry,True),("A",(x-rx,y),rx,ry,True)], True)

    def poly(self, name, *points, closed=False):
        self.add_polyline(name, *points, closed=closed)

    def line(self, name, a, b):
        self.add_line(name, a, b)
'''

# Subject-specific plans and critique are saved before the geometry is authored.
SPECS = [
('VRECT_L', 'The old parallel bent strokes read like plumbing, losing the mouth, tongue and anatomical neck.', 'Restore a left-facing skull profile and an open oral passage flowing into the throat; keep the tongue separate.', '''
self.path('skull', (12,20), [('A',(40,20),14,16,True),('A',(35,33),18,18,True),('L',(35,44))])
self.poly('nose-mouth', (12,20),(8,27),(18,27))
self.path('throat', (18,27), [('A',(29,38),11,11,True),('L',(29,44))])
self.path('tongue', (12,34), [('L',(19,34)),('A',(22,37),3,3,True),('L',(22,44))])
self.line('lip', (12,30),(12,34))
self.relate('connect','skull','nose-mouth')
self.relate('connect','nose-mouth','throat')
self.relate('connect','lip','tongue')
'''),
('SQUARE', 'The rejected avatar has square hair and no shoulders; its hat and face merge into a stick-like symbol.', 'Use a curved cowboy brim, creased crown, circular jaw, flowing hair and shoulder lines.', '''
self.poly('crown',(13,17),(16,6),(24,9),(32,6),(35,17))
self.path('brim',(6,16), [('A',(42,16),21,12,False)])
self.path('face',(14,22), [('A',(34,22),10,10,False)])
for side in (-1,1):
    x=lambda v:24+side*v
    self.path(f'hair-{side}',(x(13),24), [('L',(x(15),31)),('A',(x(12),38),7,7,side<0)])
    self.line(f'shoulder-{side}',(x(5),36),(x(13),42))
'''),
('VRECT_L', 'The old masseur and client merge into a table-like loop; hands do not clearly touch the client head.', 'Show the therapist behind, two hands at the temples, a larger seated head and curved shoulders.', '''
self.circle('therapist-head',24,8,4)
self.path('therapist-body',(16,31), [('L',(12,31)),('A',(8,27),4,4,True),('L',(8,25)),('A',(16,20),8,5,True),('L',(32,20)),('A',(40,25),8,5,True),('L',(40,27)),('A',(36,31),4,4,True),('L',(32,31))])
self.circle('client-head',24,30,6)
self.path('client-shoulders',(12,44), [('A',(24,44),6,5,True),('A',(36,44),6,5,True)])
self.line('left-hand',(16,27),(16,33))
self.line('right-hand',(32,27),(32,33))
self.relate('connect','therapist-body','left-hand')
self.relate('connect','therapist-body','right-hand')
'''),
('VRECT_L', 'The rejected mask is a rectangular box across a generic helmet, with no eye or visible head profile.', 'Restore the domed skull, one eye, projecting mask cup, two straps and neck.', '''
self.path('head',(12,22), [('A',(40,22),14,18,True),('A',(34,35),17,17,True),('L',(34,44))])
self.path('mask',(12,22), [('L',(25,25)),('L',(25,37)),('L',(17,39)),('A',(8,30),9,9,True),('L',(8,25)),('A',(12,22),4,3,True)],True)
self.line('upper-strap',(25,25),(40,21))
self.line('lower-strap',(25,37),(37,32))
self.line('neck',(19,40),(19,44))
self.add_dot('eye',(18,17))
self.relate('connect','head','mask')
self.relate('connect','mask','upper-strap')
self.relate('connect','mask','lower-strap')
'''),
('HRECT_L', 'The center ridge of the rejected hard hat is flush with the dome, making it look like a beanie or cage.', 'Raise the rectangular center ridge above two round shell lobes and preserve a broad protective brim.', '''
self.path('ridge',(20,28), [('L',(20,10)),('A',(22,8),2,2,True),('L',(26,8)),('A',(28,10),2,2,True),('L',(28,28))])
self.path('shell-left',(8,32), [('L',(8,28)),('A',(20,14),12,14,True)])
self.path('shell-right',(28,14), [('A',(40,28),12,14,True),('L',(40,32))])
self.path('brim',(6,32), [('L',(42,32)),('A',(44,34),2,2,True),('L',(44,38)),('A',(42,40),2,2,True),('L',(6,40)),('A',(4,38),2,2,True),('L',(4,34)),('A',(6,32),2,2,True)],True)
'''),
('SQUARE', 'The rejected harp is a rigid triangular ladder; it loses the curved neck and sounding-board shape.', 'Give the harp a curved neck, upright pillar, sloping soundboard, three unequal strings and a distinct foot.', '''
self.path('neck',(10,10), [('A',(24,15),15,12,True),('A',(38,17),10,8,False),('L',(42,15))])
self.poly('frame',(10,6),(10,38),(16,38),(42,15))
self.line('base',(6,42),(27,42))
for i,(x,top,bottom) in enumerate(((18,12,34),(25,16,28),(32,18,22))):
    self.line(f'string-{i}',(x,top),(x,bottom))
'''),
('HRECT_M', 'The open wrist and bulbous hooked finger of the old drawing read like a bent arrow.', 'Restore a closed wrist, horizontal back of hand, angled pointing index, thumb and palm crease.', '''
self.path('hand',(4,15), [('L',(12,15)),('L',(23,11)),('A',(29,12),8,8,True),('L',(42,24)),('A',(38,30),4,4,True),('L',(29,23)),('L',(24,31)),('A',(17,35),9,8,True),('L',(4,31)),('L',(4,15))],True)
self.path('thumb',(16,25), [('L',(26,22)),('A',(30,25),4,4,True)])
'''),
('VRECT_L', 'The old roll resembles a hanging label; it has no paper/roll boundary or perforation marks.', 'Draw a side ellipse and core, a broad hanging sheet, perforations and a gently uneven torn edge.', '''
self.oval('roll-end',33,15,7,11)
self.oval('core',33,15,2,4)
self.path('sheet',(33,4), [('L',(18,4)),('A',(8,14),10,10,False),('L',(8,41)),('L',(14,44)),('L',(20,41)),('L',(26,44)),('L',(26,15))])
self.line('perforation-a',(13,23),(16,23))
self.line('perforation-b',(21,23),(23,23))
self.relate('connect','sheet','roll-end')
'''),
('VRECT_L', 'The old pointer has only two curled fingertips and an oversized thumb, weakening its hand silhouette.', 'Keep the upright index and add three distinct curled fingers, a natural thumb and a round palm.', '''
self.path('hand',(8,27), [('L',(8,24)),('A',(14,24),3,3,True),('L',(14,21)),('A',(20,21),3,3,True),('L',(20,19)),('A',(26,19),3,3,True),('L',(26,8)),('A',(34,8),4,4,True),('L',(34,25)),('A',(40,27),5,4,True),('L',(40,30)),('L',(33,40)),('A',(25,44),10,10,True),('L',(23,44)),('A',(8,29),15,15,True),('L',(8,27))],True)
self.line('finger-fold-a',(14,24),(14,29))
self.line('finger-fold-b',(20,21),(20,28))
self.line('finger-fold-c',(26,19),(26,27))
'''),
('SQUARE', 'The rejected drawing substitutes an exclamation mark for the inner triangle of the automotive hazard switch.', 'Restore two nested upright triangles with a generous open central triangle.', '''
self.poly('outer',(24,6),(42,42),(6,42),closed=True)
self.poly('inner',(24,23),(32,35),(16,35),closed=True)
'''),
('HRECT_M', 'The old B is narrow and pointed and the O is a thin ellipse; the lettering reads as unrelated symbols.', 'Restore aligned H, rounded double-bowl B and a broader O; preserve the reference wordmark without extra symbols.', '''
self.line('h-left',(4,10),(4,38))
self.line('h-right',(13,10),(13,38))
self.line('h-crossbar',(4,24),(13,24))
self.path('b',(21,10), [('L',(24,10)),('A',(24,24),7,7,True),('A',(24,38),7,7,True),('L',(21,38)),('L',(21,10))],True)
self.line('b-middle',(21,24),(24,24))
self.oval('o',39,24,5,14)
'''),
('VRECT_L', 'The old view-angle strokes float beside a generic round head; the dotted cone and top-view nose are unclear.', 'Restore two dashed diverging sight rays, top-view nose and lateral ears around a round head.', '''
self.path('head',(22,21), [('L',(24,18)),('L',(26,21)),('A',(36,32),11,11,True),('L',(38,33)),('L',(36,35)),('A',(12,35),12,9,True),('L',(10,33)),('L',(12,32)),('A',(22,21),11,11,True)],True)
for side in (-1,1):
    self.line(f'ray-far-{side}',(24+side*16,4),(24+side*12,9))
    self.line(f'ray-near-{side}',(24+side*8,14),(24+side*6,17))
'''),
('VRECT_L', 'The old niqab reads as a smiling helmet; the entire lower face is exposed by the U-shaped opening.', 'Make a narrow eye opening and a full draped face veil with a diagonal fabric fold and broad shoulders.', '''
self.path('hood',(11,21), [('A',(37,21),13,17,True),('L',(40,44))])
self.path('left-drape',(11,21), [('L',(8,44))])
self.line('slit-top',(11,21),(37,21))
self.path('slit-bottom',(12,28), [('A',(36,28),25,8,False)])
self.path('fold',(12,28), [('A',(37,38),27,15,False)])
self.path('shoulders',(8,44), [('A',(18,39),14,14,True)])
'''),
('CIRCLE', 'The old monocle face is an open C with a disconnected lens and no eye, losing the full-face emoji.', 'Restore the circular head, monocle lens, one uncovered eye, short mouth and hanging curved cord.', '''
self.circle('face',24,24,20)
self.circle('monocle',31,19,7)
self.add_dot('eye',(15,19))
self.line('mouth',(20,33),(26,33))
self.path('cord',(38,19), [('L',(38,30)),('A',(34,34),4,4,True)])
'''),
('VRECT_L', 'The old pain marks are stacked dots and the head looks like a question-mark bulb.', 'Restore two continuous heat/pain waves and a recognizable forehead, nose, chin and neck.', '''
self.path('skull',(13,22), [('A',(40,28),14,13,True),('A',(35,37),13,13,True),('L',(35,44))])
self.path('profile',(13,22), [('L',(8,31)),('L',(14,31)),('L',(14,35)),('A',(21,40),7,5,False),('L',(21,44))])
for n,x in enumerate((22,31)):
    self.path(f'pain-wave-{n}',(x,4), [('A',(x+2,9),5,4,False),('A',(x,14),5,4,True)])
self.relate('connect','skull','profile')
'''),
('SQUARE', 'The rejected figure appears seated or running, and the large diagonal stroke obscures the pistol.', 'Use upright torso, two grounded legs, a straight aiming arm and a distinct barrel above the hand.', '''
self.circle('head',16,10,4)
self.line('torso',(16,22),(16,32))
self.poly('legs',(9,42),(16,32),(23,42))
self.line('aiming-arm',(16,22),(33,22))
self.line('resting-arm',(16,22),(6,31))
self.poly('pistol',(33,25),(34,16),(42,16),(42,20),(34,20))
self.mark_human_figure('shooter',head='head',torso='torso',torso_junction='start')
self.relate('connect','torso','legs')
self.relate('connect','torso','aiming-arm')
self.relate('connect','torso','resting-arm')
'''),
('HRECT_L', 'The old horse is a blocky dog shape with a short neck, square legs and no mane.', 'Restore an upright equine neck, pointed ear, long muzzle, slim separated legs and curved tail.', '''
self.path('horse',(6,20), [('L',(13,16)),('L',(17,8)),('L',(21,17)),('L',(23,24)),('A',(27,27),4,4,False),('L',(35,27)),('A',(40,32),5,5,True),('L',(39,40)),('L',(34,40)),('L',(33,33)),('L',(21,33)),('L',(19,40)),('L',(14,40)),('L',(15,25)),('L',(8,27)),('A',(6,20),4,4,True)],True)
self.path('tail',(38,28), [('A',(44,36),8,8,True)])
self.line('mane',(21,18),(25,25))
'''),
('HRECT_L', 'The rejected hyena is a generic boxy dog; it lacks the sloping back, heavy front and low hindquarters.', 'Restore low rump, rising back, large rounded ear, heavy muzzle, long front legs and lowered tail.', '''
self.path('body',(10,27), [('A',(16,22),7,6,True),('L',(30,16)),('L',(31,12)),('A',(36,12),3,4,True),('L',(37,18)),('L',(44,23)),('L',(41,28)),('L',(36,27)),('L',(34,40)),('L',(29,40)),('L',(28,31)),('A',(18,32),12,6,True),('L',(15,40)),('L',(10,40)),('L',(12,31)),('L',(10,27))],True)
self.path('tail',(10,27), [('A',(4,35),9,9,False)])
self.add_dot('eye',(35,21))
'''),
('VRECT_L', 'The owl has only one eye and no beak or feet, so its silhouette reads as an abstract leaf.', 'Restore paired eyes, V-shaped beak, brow, one folded wing and a visible standing foot.', '''
self.path('outline',(13,18), [('A',(37,18),12,14,True),('L',(36,27)),('A',(26,38),13,13,True),('L',(8,40)),('A',(13,18),58,58,True)],True)
self.poly('brow',(12,7),(25,17),(39,7))
self.add_dot('eye-left',(19,21))
self.add_dot('eye-right',(31,21))
self.poly('beak',(23,26),(25,28),(27,26))
self.path('wing',(26,31), [('A',(15,39),15,15,True)])
self.poly('foot',(29,38),(32,44),(38,44))
'''),
('VRECT_L', 'The owl has only one eye and no beak or feet, so its silhouette reads as an abstract leaf.', 'Restore paired eyes, V-shaped beak, brow, one folded wing and a visible standing foot.', '''
self.path('outline',(13,18), [('A',(37,18),12,14,True),('L',(36,27)),('A',(26,38),13,13,True),('L',(8,40)),('A',(13,18),58,58,True)],True)
self.poly('brow',(12,7),(25,17),(39,7))
self.add_dot('eye-left',(19,21))
self.add_dot('eye-right',(31,21))
self.poly('beak',(23,26),(25,28),(27,26))
self.path('wing',(26,31), [('A',(15,39),15,15,True)])
self.poly('foot',(29,38),(32,44),(38,44))
'''),
]

# Native-size review repairs. Re-running creates new folders and preserves candidates.
def revise(i, body):
    k,w,c,_=SPECS[i]
    SPECS[i]=(k,w,c,body)

revise(0, '''
self.path('skull',(12,20), [('A',(40,20),14,16,True),('L',(40,27)),('A',(37,34),10,10,True),('L',(37,44))])
self.poly('nose-mouth',(12,20),(8,27),(18,27))
self.path('throat',(18,27), [('A',(29,38),11,11,True),('L',(29,44))])
self.path('tongue',(12,35), [('L',(18,35)),('A',(21,38),3,3,True),('L',(21,44))])
self.relate('connect','skull','nose-mouth')
self.relate('connect','nose-mouth','throat')
''')
revise(1, '''
self.poly('crown',(13,18),(16,6),(24,9),(32,6),(35,18))
self.path('brim',(6,16), [('A',(42,16),21,12,False)])
self.path('face',(14,22), [('A',(34,22),10,10,False)])
for side in (-1,1):
    x=lambda v:24+side*v
    self.path(f'hair-{side}',(x(13),24), [('A',(x(15),33),15,15,side>0),('A',(x(12),37),5,5,side>0)])
    self.line(f'shoulder-{side}',(x(5),36),(x(13),42))
''')
revise(2, '''
self.circle('therapist-head',24,8,4)
self.path('therapist-body',(17,30), [('L',(12,30)),('A',(8,26),4,4,True),('L',(8,25)),('A',(16,20),8,5,True),('L',(32,20)),('A',(40,25),8,5,True),('L',(40,26)),('A',(36,30),4,4,True),('L',(31,30))])
self.circle('client-head',24,27,5)
self.path('client-shoulders',(12,44), [('A',(36,44),12,4,True)])
self.line('left-hand',(17,25),(17,31))
self.line('right-hand',(31,25),(31,31))
self.relate('connect','therapist-body','left-hand')
self.relate('connect','therapist-body','right-hand')
''')
revise(4, '''
self.path('ridge',(20,28), [('L',(20,14)),('L',(20,10)),('A',(22,8),2,2,True),('L',(26,8)),('A',(28,10),2,2,True),('L',(28,14)),('L',(28,28))])
self.path('shell-left',(8,32), [('L',(8,28)),('A',(20,14),12,14,True)])
self.path('shell-right',(28,14), [('A',(40,28),12,14,True),('L',(40,32))])
self.path('brim',(6,32), [('L',(42,32)),('A',(44,34),2,2,True),('L',(44,38)),('A',(42,40),2,2,True),('L',(6,40)),('A',(4,38),2,2,True),('L',(4,34)),('A',(6,32),2,2,True)],True)
self.relate('connect','ridge','shell-left')
self.relate('connect','ridge','shell-right')
''')
revise(5, '''
self.path('neck',(10,10), [('A',(24,15),15,12,True),('A',(38,17),10,8,False),('L',(42,15))])
self.poly('frame',(10,6),(10,42),(42,15))
self.line('base',(6,42),(27,42))
for i,(x,top,bottom) in enumerate(((18,12,35),(26,16,28))):
    self.line(f'string-{i}',(x,top),(x,bottom))
self.relate('connect','frame','base')
''')
revise(7, '''
self.oval('roll-end',33,15,7,11)
self.line('core',(33,12),(33,18))
self.path('sheet',(33,4), [('L',(18,4)),('A',(8,14),10,10,False),('L',(8,41)),('L',(14,44)),('L',(20,41)),('L',(26,44)),('L',(26,15))])
self.line('perforation',(16,23),(18,23))
self.relate('connect','sheet','roll-end')
''')
revise(10, '''
self.line('h-left',(4,12),(4,36))
self.line('h-right',(10,12),(10,36))
self.line('h-crossbar',(4,24),(10,24))
self.path('b',(17,12), [('A',(17,24),6,6,True),('A',(17,36),6,6,True),('L',(17,12))],True)
self.oval('o',37,24,7,12)
''')
revise(11, SPECS[11][3].replace('(24+side*8,14),(24+side*6,17)','(24+side*8,13),(24+side*6,15)'))
revise(14, '''
self.path('skull',(12,30), [('A',(40,30),14,10,True),('A',(35,39),11,11,True),('L',(35,44))])
self.path('profile',(12,30), [('L',(8,36)),('L',(15,36)),('L',(15,38)),('A',(22,42),7,4,False),('L',(22,44))])
for n,x in enumerate((21,32)):
    self.path(f'pain-wave-{n}',(x,4), [('A',(x+2,8),4,4,False),('A',(x,12),4,4,True)])
self.relate('connect','skull','profile')
''')
revise(15, '''
self.circle('head',16,10,4)
self.line('torso',(16,22),(16,32))
self.poly('legs',(9,42),(16,32),(23,42))
self.line('aiming-arm',(16,22),(33,22))
self.line('resting-arm',(16,22),(6,31))
self.poly('pistol',(33,26),(33,22),(33,14),(42,14))
self.mark_human_figure('shooter',head='head',torso='torso',torso_junction='start')
self.relate('connect','torso','legs')
self.relate('connect','torso','aiming-arm')
self.relate('connect','torso','resting-arm')
self.relate('connect','pistol','aiming-arm')
''')
revise(17, SPECS[17][3].replace("self.add_dot('eye',(35,21))",''))
for i in (18,19):
    revise(i,SPECS[i][3].replace("(26,31), [('A',(15,39),15,15,True)]", "(24,35), [('A',(15,39),15,15,True)]"))

revise(0,SPECS[0][3].replace("(12,35), [('L',(18,35)),('A',(21,38),3,3,True),('L',(21,44))]", "(12,36), [('L',(17,36)),('A',(20,39),3,3,True),('L',(20,44))]"))
revise(2,SPECS[2][3].replace("'client-head',24,27,5", "'client-head',24,30,4").replace("(36,44),12,4,True", "(36,44),12,2,True").replace("(17,25),(17,31)","(17,27),(17,33)").replace("(31,25),(31,31)","(31,27),(31,33)"))
for i in (18,19):
    revise(i,SPECS[i][3].replace("(24,35), [('A',(15,39),15,15,True)]", "(24,34), [('A',(14,40),15,15,True)]"))

def run(indices):
    claims=json.loads((ROOT/'claims.json').read_text())
    previous=json.loads((ROOT/'runs.json').read_text()) if (ROOT/'runs.json').exists() else {}
    stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    for i in indices:
        c=claims[i]; key,wrong,change,body=SPECS[i]
        ref=Path(c['reference']); uuid=ref.stem[-36:]; concept=ref.stem[:-37]
        out=REPO/'icon_set/work/primitive-make-ray'/uuid/(stamp+f'-meaning-{i:02d}')
        out.mkdir(parents=True)
        metadata=dict(concept=concept,source_uuid=uuid,reference_path=str(ref),icon_id=c['icon_id'],feedback=c['feedback'],before_findings=wrong,revision_plan=change,keyshape=key,author='gpt-6')
        (out/(c['icon_id']+'.metadata.json')).write_text(json.dumps(metadata,indent=2))
        module=out/(c['icon_id'].replace('-','_')+'_'+uuid.replace('-','_')+'.py')
        source=f'''from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = {uuid!r}
SOURCE_PATH = {str(ref)!r}
AUTHOR = "gpt-6"

class Revision(Solo48):
    icon_id = {c['icon_id']!r}
    keyshape = Keyshape.{key}
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()
    # Plan: {change}
    # Original/current comparison: {wrong}
    # References: claimed original; Lucide hand/hard-hat/ear/triangle-alert
    # construction where applicable; human_ref/user.svg and full_body_ref.png.
    # Paired anatomical parts share parameters; directional profiles stay asymmetric.
{HELPERS}
    def build(self):
{textwrap.indent(textwrap.dedent(body).strip(), '        ')}
'''
        module.write_text(source)
        try:
            icon=load_icon(module); report=icon.validate_icon(); svg=icon.to_svg()
            (out/(c['icon_id']+'.svg')).write_text(svg)
            (out/'validation.txt').write_text(report.describe())
            render_previews(svg,c['icon_id'],48,out)
            cairosvg.svg2png(url=str(REPO/ref),write_to=str(out/'reference.png'),output_width=384,output_height=384)
            result=gate(module); (out/'gate.json').write_text(json.dumps(result,indent=2))
            print(i,c['icon_id'],report.status,result['status'],len(result['errors']),len(result['warnings']),flush=True)
        except Exception as e:
            print(i,type(e).__name__,str(e),flush=True)
            raise
        previous[str(i)]=str(out.relative_to(REPO))
        (ROOT/'runs.json').write_text(json.dumps(previous,indent=2))

def sheets():
    runs=json.loads((ROOT/'runs.json').read_text());claims=json.loads((ROOT/'claims.json').read_text())
    for page in range(4):
        im=Image.new('RGB',(1000,1000),'#eee');d=ImageDraw.Draw(im)
        for row in range(5):
            i=page*5+row
            if str(i) not in runs:continue
            out=REPO/runs[str(i)];y=row*200
            d.text((8,y+5),f'{i}: '+claims[i]['icon_id'],fill='black')
            for x,theme in ((10,'light'),(510,'dark')):
                pic=Image.open(out/f'preview-{theme}-384.png').resize((168,168))
                im.paste(pic,(x,y+25))
                native=Image.open(out/f'preview-{theme}-48.png');im.paste(native,(x+195,y+65))
        im.save(ROOT/f'after-{page}.png')

if __name__=='__main__':
    if len(sys.argv)>1 and sys.argv[1]=='sheets':sheets()
    else:run([int(x) for x in sys.argv[1:]] if len(sys.argv)>1 else range(20));sheets()
