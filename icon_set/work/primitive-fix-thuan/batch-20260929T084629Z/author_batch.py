"""Fresh SOLO48 originals from the twenty visually compared claimed references."""
import json, re, textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
BATCH = Path(__file__).resolve().parent
ROWS = json.loads((BATCH / 'batch.json').read_text())
AUTHOR = 'gpt-6'
SOURCE_ICON_ID = None  # assigned from each exact supplied reference below
SOURCE_PATH = None

HELPERS = '''
        def line(n, a, b): self.add_line(n, a, b)
        def poly(n, *p, closed=False): self.add_polyline(n, *p, closed=closed)
        def arc(n, a, b, rx, ry=None, sweep=True, large=False):
            self.add_arc(n, a, b, radius_x=rx, radius_y=ry or rx, sweep=sweep, large_arc=large)
        def ellipse(n, x, y, rx, ry=None):
            ry = ry or rx
            arc(n+'-top', (x-rx,y), (x+rx,y), rx, ry)
            arc(n+'-bottom', (x+rx,y), (x-rx,y), rx, ry)
            self.add_contour(n, n+'-top', n+'-bottom', closed=True)
        def path(n, start, segments, closed=False):
            p = start; members = []
            for i, seg in enumerate(segments):
                name = f'{n}-{i}'; q = seg[1]
                if seg[0] == 'L': line(name,p,q)
                else: arc(name,p,q,*seg[2:])
                members.append(name); p=q
            self.add_contour(n,*members,closed=closed)
        def rounded(n, x1,y1,x2,y2,r):
            path(n,(x1+r,y1), [('L',(x2-r,y1)),('A',(x2,y1+r),r),
                ('L',(x2,y2-r)),('A',(x2-r,y2),r),('L',(x1+r,y2)),
                ('A',(x1,y2-r),r),('L',(x1,y1+r)),('A',(x1+r,y1),r)],True)
'''

# Each specification records comparison BEFORE authoring, then the owning symbols.
SPECS = {
1: ('CIRCLE', 'The rejected cross-in-circle reads as a sun or target; the reference has a faceted spherical grid. Restore curved meridians, latitude bands and light rays.', 'Circular globe with shared-axis ellipse meridian and two latitude chords; eight radial glints.', '''
ellipse('ball',24,24,13)
ellipse('meridian',24,24,5,13)
line('latitude-top',(13,18),(35,18))
line('latitude-bottom',(13,30),(35,30))
for i,p in enumerate([(24,4),(24,44),(4,24),(44,24),(10,10),(38,10),(10,38),(38,38)]): self.add_dot(f'glint-{i}',p)
'''),
2: ('HRECT_L', 'The rejected face has flattened ears and a narrow vertical muzzle. Restore round ears, a broad heart-shaped face patch and rounded projecting muzzle.', 'Bilateral round ears flank a dome; a paired-lobe inner face flows into a broad muzzle.', '''
path('head',(11,28),[('A',(11,18),18,18),('A',(37,18),13,13),('A',(37,28),18,18)])
path('left-ear',(11,18),[('A',(11,30),7,6,False)])
path('right-ear',(37,18),[('A',(37,30),7,6,True)])
path('face',(24,20),[('A',(14,20),5,6,False),('A',(16,29),7,7,False),('A',(15,34),7,7,False),('A',(33,34),9,6,False),('A',(32,29),7,7,False),('A',(34,20),7,7,False),('A',(24,20),5,6,False)],True)
'''),
3: ('VRECT_L', 'The rejected hatbox resembles a squat purse, with too little cylindrical body and a large handle. Restore the shallow elliptical lid, lid band and taller cylindrical wall.', 'Elliptical lid, a shallow repeated front band, cylindrical body, centered semicircular handle.', '''
ellipse('lid',24,17,16,5)
path('body',(8,17),[('L',(8,38)),('A',(40,38),16,6,False),('L',(40,17))])
arc('lid-band',(8,24),(40,24),16,5,False)
path('handle',(18,13),[('L',(18,10)),('A',(30,10),6,6),('L',(30,13))])
'''),
4: ('HRECT_L', 'The rejected bale looks like a capsule above three floating chevrons; it lost the rolled center and continuous cut field. Restore circular roll detail, bale depth and connected field contour.', 'Circular end and offset cylindrical back share upper/lower levels; field edge supports the bale and owns stubble repeats.', '''
ellipse('bale-end',15,20,11,12)
ellipse('roll',15,20,4,5)
path('bale-depth',(15,8),[('L',(30,8)),('A',(30,32),11,12),('L',(15,32))])
path('field',(4,32),[('L',(36,32)),('A',(44,40),8,8)])
for i,x in enumerate((8,19,30)):
    poly(f'stubble-{i}',(x-2,37),(x,40),(x+2,37))
'''),
5: ('VRECT_L', 'The rejected octopus has a closed round face and four short radial stubs. The reference has a head flowing into long curled arms. Restore the open lower head silhouette and five visible curls.', 'One rounded crown transitions into mirrored side curls; three hanging lower arms curl upward.', '''
path('crown-and-side-arms',(8,25),[('L',(8,28)),('A',(16,28),4,4,False),('A',(12,17),15,15,False),('A',(36,17),12,13),('A',(32,28),15,15,False),('A',(40,28),4,4,False),('L',(40,25))])
path('left-arm',(10,36),[('L',(10,39)),('A',(20,39),5,5,False),('L',(20,32))])
path('right-arm',(28,32),[('L',(28,39)),('A',(38,39),5,5,False),('L',(38,36))])
line('central-arm',(24,34),(24,44))
self.add_dot('eye-left',(20,24)); self.add_dot('eye-right',(28,24))
'''),
6: ('VRECT_L', 'The rejected inflatable robot has a pill face and an undifferentiated body. Restore the small oval head, two linked eyes, separate soft arms and broad belly with short feet.', 'Horizontal oval face, mirrored hanging arms and a single soft body with two feet. Eyes connected by one horizontal face line.', '''
ellipse('head',24,11,9,7)
line('face-link',(21,11),(27,11))
path('body',(15,22),[('A',(12,34),20,20,False),('A',(15,40),6,6,False),('L',(15,44)),('L',(21,44)),('L',(21,40)),('L',(27,40)),('L',(27,44)),('L',(33,44)),('L',(33,40)),('A',(36,34),6,6,False),('A',(33,22),20,20,False)])
path('left-arm',(15,19),[('A',(8,32),18,18,False),('A',(12,35),4,4,False)])
path('right-arm',(33,19),[('A',(40,32),18,18),('A',(36,35),4,4)])
'''),
7: ('CIRCLE', 'The rejected owl is a shield-shaped cat face. The source is a circular Ask.fm owl badge with triangular brows and a pointed beak. Restore the round boundary, separate round eyes and paired pointed brows.', 'Circular badge contains mirrored eyes and triangular ear/brow marks; centered downward beak.', '''
ellipse('badge',24,24,20)
for side,x in enumerate((17,31)):
    ellipse(f'eye-{side}',x,25,5)
    self.add_dot(f'pupil-{side}',(x,25))
poly('left-brow',(12,16),(14,10),(20,15))
poly('right-brow',(28,15),(34,10),(36,16))
poly('beak',(20,33),(24,38),(28,33))
'''),
8: ('SQUARE', 'The rejected front bubble has no eyes and its smile reads as a handle; the rear bubble is too small and distorted. Restore a readable smiling face and a substantial overlapping reply bubble.', 'Large round smiling bubble behind a smaller lower-right reply bubble, both with distinct outward tails. Occluded rear perimeter is omitted.', '''
path('main-bubble',(23,35),[('A',(15,34),16,16),('L',(6,40)),('L',(9,29)),('A',(6,22),16,16),('A',(38,22),16,16),('L',(38,23))])
path('reply',(40,36),[('A',(42,31),9,8,False),('A',(24,31),9,8,False),('A',(33,39),9,8,False),('L',(42,42)),('L',(40,36))],True)
line('eye-left',(16,17),(16,19));line('eye-right',(27,17),(27,19))
arc('smile',(16,26),(26,26),7,5,False)
'''),
9: ('VRECT_L', 'The rejected mirror is a small ring hovering far above an oversized U-shaped support. Enlarge the circular glass and place the support around its lower half, retaining stem and base.', 'Circular glass centered on support, lower semicircular cradle, straight stem, broad foot.', '''
ellipse('glass',24,18,14)
arc('cradle',(8,21),(40,21),16,16,False)
line('stem',(24,37),(24,44))
line('base',(14,44),(34,44))
self.relate('connect','stem','base')
'''),
10: ('HRECT_L', 'The rejected teapot resembles a mug with a separate dot; its lid and long curved spout disappeared. Restore a domed lid, lid knob, rounded bowl, raised pouring spout and side handle.', 'Rounded bowl beneath domed lid, small circular knob, graceful open spout left and loop handle right.', '''
path('body',(14,19),[('A',(12,29),21,21,False),('A',(18,40),10,10,False),('L',(30,40)),('A',(36,29),10,10,False),('A',(34,19),21,21,False)],False)
path('lid',(14,19),[('A',(34,19),12,9),('L',(14,19))],True)
ellipse('knob',24,8,3)
path('spout',(12,29),[('A',(6,23),6,6),('L',(6,16)),('L',(4,13))])
path('handle',(36,20),[('A',(36,34),8,7)])
'''),
11: ('VRECT_L', 'The rejected whale reads as a broad helmet with a crossbar. Restore the near-circular body, gently smiling waterline and curved fountain instead of the flat divider.', 'Round whale body with broad smile and two lower belly seams; a mirrored two-arc fountain springs from its crown.', '''
ellipse('body',24,28,16)
arc('smile',(8,28),(40,28),24,11,False)
path('fountain-left',(24,12),[('A',(14,4),10,8,False)])
path('fountain-right',(24,12),[('A',(34,4),10,8,True)])
arc('belly-left',(18,34),(20,43),18,18,False)
arc('belly-right',(30,34),(28,43),18,18,True)
'''),
12: ('HRECT_M', 'The rejected controller has a scalloped lower edge and an undersized cross. Restore distinct sloping hand grips, a straight central recess, a clear D-pad and four buttons.', 'Lucide gamepad construction informs a rounded top with tapered grips. Reference four-button diamond and cross are retained.', '''
path('shell',(12,10),[('L',(36,10)),('A',(42,16),6),('L',(44,33)),('A',(37,38),5,5),('L',(30,30)),('L',(18,30)),('L',(11,38)),('A',(4,33),5,5),('L',(6,16)),('A',(12,10),6)],True)
poly('dpad-h',(10,21),(14,21),(18,21))
poly('dpad-v',(14,17),(14,21),(14,25))
for i,p in enumerate(((33,16),(28,21),(38,21),(33,26))):self.add_dot(f'button-{i}',p)
'''),
13: ('HRECT_M', 'The rejected strip is a thick capsule with steep bars. Restore the reference shallow rounded rectangle and lighter 45-degree diagonal divisions.', 'Shallow rounded rectangle with evenly stepped diagonal lines; deliberate short height preserves the strip concept.', '''
rounded('strip',4,16,44,32,3)
for i,(a,b) in enumerate((((4,29),(17,16)),((17,32),(33,16)),((33,32),(44,21)))):line(f'diagonal-{i}',a,b)
'''),
14: ('VRECT_L', 'The rejected profile has an exaggerated sawtooth mouth and a dot eye absent from the plain reference. Restore the smooth skull, simple nose, straight facial front and short chin-to-neck return.', 'One continuous asymmetric head silhouette, formed from circular skull arcs with a deliberate angular nose and smooth jaw.', '''
path('profile',(12,44),[('L',(12,32)),('A',(8,20),20,20),('A',(36,18),14,14),('L',(40,26)),('L',(34,26)),('L',(34,32)),('A',(30,36),4),('L',(24,36)),('L',(24,44))])
'''),
15: ('VRECT_M', 'The rejected standing body has rigid box arms and no rounded shoulder outline. Restore a round head, rounded shoulder-and-arm silhouette and two separated lower legs.', 'Outlined full-body reference is retained with mirrored shoulder radii, broad torso and rounded lower body. Human reference informs the circular head and exactly 4-unit detached head gap.', '''
ellipse('head',24,9,5)
path('body',(18,22),[('L',(30,22)),('A',(38,30),8),('L',(38,36)),('L',(32,36)),('L',(32,44)),('L',(16,44)),('L',(16,36)),('L',(10,36)),('L',(10,30)),('A',(18,22),8)],True)
line('left-arm-seam',(16,30),(16,36));line('right-arm-seam',(32,30),(32,36))
line('leg-separation',(24,36),(24,44))
'''),
16: ('SQUARE', 'The rejected RSS icon lost one of its two broadcast waves and its circular origin. Restore two concentric quarter-circle waves, circular origin and rounded square outer boundary.', 'Lucide RSS concentric arcs adapted inside the supplied rounded-square enclosure; all broadcast arcs share a center.', '''
rounded('frame',6,6,42,42,4)
ellipse('origin',15,33,3)
arc('inner-wave',(13,22),(26,35),13,13)
arc('outer-wave',(13,13),(35,35),22,22)
'''),
17: ('VRECT_L', 'The rejected tablet has a tiny central screen and no home indicator, resembling an empty nested box. Restore a larger portrait display, slimmer bezel and lower home stroke.', 'Lucide rounded tablet body with a large rectangular display and centered short home indicator.', '''
rounded('case',8,4,40,44,4)
poly('screen',(14,10),(34,10),(34,34),(14,34),closed=True)
line('home',(22,39),(26,39))
'''),
18: ('SQUARE', 'The rejected finish pose looks static with two short straight legs and a large rigid bar. Restore bent running legs, raised celebratory arms and a torn finish tape across the waist.', 'Human reference circular head and coherent stick limbs, with raised arms and angled running legs; finish tape crosses the waist. Detached head outline ends at 15, torso begins at 23: 4 ink units.', '''
ellipse('head',24,10,5)
line('torso',(24,23),(24,29))
poly('left-arm',(24,23),(15,21),(10,15),(8,6))
poly('right-arm',(24,23),(33,21),(38,15),(40,6))
poly('left-leg',(24,35),(19,42),(11,42))
poly('right-leg',(24,35),(31,39),(31,42))
poly('tape',(6,29),(42,29),(40,32),(42,35),(6,35),(8,32),closed=True)
self.mark_human_figure('runner',head='head',torso='torso',torso_junction='start')
'''),
19: ('SQUARE', 'The rejected runner has a nearly horizontal upper body and stiff angular legs. Restore the forward lean, bent pumping arms and opposing long strides of the running reference.', 'Shared human-reference circle head, torso and bent limbs. Upper torso vector (5,-12) points at the head; center-to-shoulder distance 13 minus head radius 5 leaves 8 centerline units, exactly 4 ink units.', '''
ellipse('head',29,11,5)
line('torso',(24,23),(19,35))
poly('arm-back',(24,23),(15,21),(7,29))
poly('arm-forward',(24,23),(36,23),(42,14))
poly('leg-back',(19,35),(13,41),(6,42))
poly('leg-forward',(19,35),(29,39),(29,42))
self.mark_human_figure('runner',head='head',torso='torso',torso_junction='start')
'''),
20: ('SQUARE', 'The rejected thief has an empty teardrop bag and generic running posture. Restore the tied money sack with currency mark, backward carrying arm and forward-running stride.', 'Human reference aligned detached circular head; carrying arm reaches left to tied money sack. Asymmetric arms and bent legs convey forward motion. Exact head-to-torso ink gap is 4.', '''
ellipse('head',27,11,5)
line('torso',(22,23),(17,35))
poly('forward-arm',(22,23),(34,18),(42,22))
poly('carrying-arm',(22,23),(15,27),(9,23))
poly('back-leg',(17,35),(13,40),(19,42))
poly('front-leg',(17,35),(29,31),(34,40),(42,40))
path('bag',(6,30),[('L',(10,30)),('L',(12,36)),('A',(4,36),4,5),('L',(6,30))],True)
poly('tie',(6,30),(5,26),(11,26),(10,30))
line('money-stroke',(8,34),(8,39))
self.mark_human_figure('runner',head='head',torso='torso',torso_junction='start')
'''),
}

def author(index, version='01'):
    global SOURCE_ICON_ID, SOURCE_PATH
    row=ROWS[index-1]; ref=Path(row['reference']); SOURCE_PATH=str(ref)
    SOURCE_ICON_ID=re.search(r'[0-9a-f-]{36}$',ref.stem).group()
    concept=ref.stem[:-37]
    out=ROOT/'icon_set/work/primitive-make-ray'/SOURCE_ICON_ID/f'20260929T084629Z-fix-{version}'
    out.mkdir(parents=True,exist_ok=False)
    shape, comparison, plan, body=SPECS[index]
    metadata=dict(concept=concept,source_uuid=SOURCE_ICON_ID,reference_path=SOURCE_PATH,icon_id=row['icon_id'],feedback=row['feedback'],comparison=comparison,plan=plan)
    (out/(row['icon_id']+'.metadata.json')).write_text(json.dumps(metadata,indent=2)+'\n')
    (out/'comparison.md').write_text(comparison+'\nFeedback: '+row['feedback']+'\nPlan: '+plan+'\n')
    filename=row['icon_id'].replace('-','_')+'_'+SOURCE_ICON_ID.replace('-','_')+'.py'
    source=f'''"""{plan}"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = {SOURCE_ICON_ID!r}
SOURCE_PATH = {SOURCE_PATH!r}
AUTHOR = {AUTHOR!r}

class Drawing(Solo48):
    icon_id = {row['icon_id']!r}
    keyshape = Keyshape.{shape}
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ({concept!r},)

    def build(self):
'''+HELPERS+textwrap.indent(textwrap.dedent(body).strip(),'        ')+'\n'
    (out/filename).write_text(source)
    row.update(result_dir=str(out.relative_to(ROOT)),module=str((out/filename).relative_to(ROOT)),comparison=comparison,plan=plan)
    (BATCH/'batch.json').write_text(json.dumps(ROWS,indent=2)+'\n')
    print(index,row['icon_id'],out.name)

if __name__=='__main__':
    import sys
    for number in map(int,sys.argv[1:]): author(number)
