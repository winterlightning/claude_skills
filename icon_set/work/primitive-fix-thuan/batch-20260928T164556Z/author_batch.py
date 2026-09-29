from pathlib import Path
import json, re, textwrap, shutil
ROOT=Path(__file__).resolve().parent
rows=json.loads((ROOT/'batch.json').read_text())
HELPERS='''
        def path(name, start, steps, closed=False):
            here=start; members=[]
            for i,step in enumerate(steps):
                ident=f'{name}-{i}'
                if len(step)==2:
                    self.add_line(ident,here,step); end=step
                elif step[0]=='C':
                    _,end,c1,c2=step
                    self.add_bezier(ident,here,(c1,c2,end))
                else:
                    end,rx,ry,sweep=step
                    self.add_arc(ident,here,end,radius_x=rx,radius_y=ry,sweep=sweep)
                here=end;members.append(ident)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)
        def rounded(name,l,t,r,b,k):
            path(name,(l+k,t),[(r-k,t),((r,t+k),k,k,True),(r,b-k),((r-k,b),k,k,True),(l+k,b),((l,b-k),k,k,True),(l,t+k),((l+k,t),k,k,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
'''
plans={}
def plan(i,key,wrong,change,ref,code):
    plans[i]=(key,wrong,change,ref,textwrap.dedent(code))
for i in range(3):
    mirrored=i==0
    plan(i,'HRECT_L','The plus is undersized relative to the head, as the reviewer explicitly noted.',
         'Enlarged plus arms by 50 percent, enlarged the circular head and rebalanced the shoulders; retained the exact 4-unit detached head gap.',
         'human_ref/user.svg: circular head and smooth shoulders; Lucide user-round-plus original and atoms: orthogonal plus and shared shoulder arc.',f'''
def pt(x,y): return (48-x,y) if {mirrored!r} else (x,y)
cx=16 if not {mirrored!r} else 32
circle('head',cx,15,7)
path('shoulders',pt(4,40),[(pt(16,30),12,10,True),(pt(28,40),12,10,True)])
poly('plus-h',pt(32,15),pt(38,15),pt(44,15))
poly('plus-v',pt(38,9),pt(38,15),pt(38,21))
join('plus-h','plus-v')
''')
plan(3,'VRECT_L','The can was squat and the spray marks were uneven, unlike the tall reference can.',
     'Lengthened the can, rounded its shoulder and nozzle, and made two balanced outward spray rays.', 'Lucide spray-can: distinct nozzle, body and spray hierarchy.', '''
rounded('can',8,14,28,44,5)
path('nozzle',(14,14),[(14,6),((16,4),2,2,True),(20,4),((22,6),2,2,True),(22,14)])
join('can','nozzle')
line('spray-upper',(32,9),(40,5))
line('spray-lower',(32,17),(40,21))
''')
plan(4,'SQUARE','The upright trapezoid cup and angular grip lost the tilted paint reservoir and natural airbrush profile.',
     'Restored the tilted rounded paint cup, tapered nozzle, rounded grip and curved trigger.', 'No useful exact Lucide match; source supplies the tilted cup and grip.', '''
path('body',(6,27),[(12,23),(37,23),((42,28),5,5,True),(39,31),(42,39),((38,42),4,4,True),(34,42),(29,31),(12,31),(6,27)],True)
path('cup',(23,6),[(33,12),((34,16),3,3,True),(30,22),((26,23),3,3,True),(18,18),((17,14),3,3,True),(21,7),((23,6),2,2,True)],True)
line('neck',(22,21),(20,23));join('neck','body');join('neck','cup')
path('trigger',(25,31),[((19,39),8,8,True),(16,38)])
join('trigger','body')
''')
plan(5,'HRECT_L','The wings were blocky and the tail/nose proportion made the aircraft resemble a generic arrow.',
     'Rebuilt slimmer swept wings, a longer fuselage and a rounded nose, preserving both wings and the rightward heading.', 'Lucide plane: coherent aircraft outline with swept wings.', '''
path('plane',(4,18),[(7,18),(11,23),(20,23),(14,8),(18,8),(31,23),(39,23),((44,27),5,4,True),((39,31),5,4,True),(31,31),(18,40),(14,40),(20,31),(4,31),(6,25),(4,18)],True)
''')
plan(6,'SQUARE','The plane looked like a crown and the crops were short chevrons with no ground or stems.',
     'Restored a curved side-view fuselage, one swept wing, visible spray strokes and three taller sprouts on a shared ground line.', 'Lucide plane: simplified aircraft silhouette; original controls side-view arrangement.', '''
path('plane',(6,6),[('C',(15,14),(9,6),(10,14)),(23,14),(29,6),(32,14),(36,14),((42,19),6,5,True),((36,24),6,5,True),(22,24),(8,20),((6,17),3,3,True),(6,6)],True)
line('spray-left',(20,29),(18,31));line('spray-right',(30,29),(28,31))
for j,x in enumerate((10,24,38)):
    poly(f'crop-{j}',(x-4,36),(x,42),(x+4,36))
    join(f'crop-{j}','ground')
poly('ground',(6,42),(10,42),(24,42),(38,42),(42,42))
''')
plan(7,'CIRCLE','The rejected clock omitted all four hour markers and used an overly short hand pair.',
     'Restored four cardinal hour markers and a clear 10:08 hand pair inside a circular face.', 'Lucide clock: concentric face and joined hand pair.', '''
circle('face',24,24,20)
for name,a,b in [('north',(24,10),(24,12)),('east',(36,24),(38,24)),('south',(24,36),(24,38)),('west',(10,24),(12,24))]:line(name,a,b)
poly('hands',(17,19),(24,24),(32,16))
''')
plan(8,'VRECT_L','The squat dome, short torso and cramped leg gap made the mascot heavier than the original.',
     'Raised the dome, lengthened the blank torso and widened the separation of the rounded legs while retaining the reference’s armless blank face.', 'Lucide bot: clear head/body hierarchy; reference owns mascot silhouette.', '''
path('outline',(8,20),[((24,8),16,12,True),((40,20),16,12,True),(40,32),((36,36),4,4,True),(35,36),(35,40),((27,40),4,4,True),(27,36),(21,36),(21,40),((13,40),4,4,True),(13,36),(12,36),((8,32),4,4,True),(8,20)],True)
line('seam',(8,20),(40,20));join('outline','seam')
line('antenna-left',(14,10),(10,4));line('antenna-right',(34,10),(38,4))
join('antenna-left','outline');join('antenna-right','outline')
''')
plan(9,'SQUARE','The shallow opening and very short vertical legs read more like a horseshoe than a doorway.',
     'Extended the straight jambs and rebuilt concentric semicircular arches with uniform masonry thickness.', 'No useful direct Lucide archway match; concentric circular construction from source.', '''
path('arch',(6,42),[(6,24),((42,24),18,18,True),(42,42),(34,42),(34,24),((14,24),10,10,False),(14,42),(6,42)],True)
''')
plan(10,'VRECT_L','The open single-stroke back and short seat lost the upholstered shell and armrest of the reference.',
     'Restored an outlined swept back and rounded seat, a separate armrest, and slim splayed legs.', 'Lucide armchair: rounded upholstery and leg hierarchy; source controls side view.', '''
path('shell',(8,7),[((14,6),4,4,True),(21,29),((25,32),4,4,False),(36,32),((40,36),4,4,True),((36,40),4,4,True),(22,40),((14,33),9,9,True),(8,7)],True)
path('arm',(18,21),[(29,21),((35,27),6,6,True),(36,32)]);join('arm','shell')
line('leg-front',(22,40),(20,44));line('leg-rear',(35,40),(37,44))
join('leg-front','shell');join('leg-rear','shell')
''')
plan(11,'SQUARE','The thin open back and arm stub removed the broad padded side profile of the original.',
     'Reconstructed the high upholstered back, rounded arm and seat silhouette, with two splayed legs.', 'Lucide armchair: coherent padded outline and shared corner radii.', '''
path('shell',(8,34),[(10,24),((15,20),5,5,True),(25,20),((30,16),5,5,False),(34,8),((37,6),3,3,True),(42,6),(37,30),((32,34),5,5,True),(8,34)],True)
line('front-leg',(14,34),(10,42));line('rear-leg',(31,34),(37,42));join('front-leg','shell');join('rear-leg','shell')
path('front-cushion',(10,26),[(8,26),((6,28),2,2,False),(6,32),((8,34),2,2,False)]);join('front-cushion','shell')
''')
plan(12,'SQUARE','The terminal arrowhead was cramped and the dash rhythm was irregular, making the route hard to follow.',
     'Rebuilt regular dash gaps, rounded elbows and a longer final descending arrow with a clear open head.', 'Lucide arrow-right and move-up: shaft-to-tip junction and open arrowhead.', '''
line('start',(6,6),(6,12))
path('first-elbow',(6,20),[((10,24),4,4,False),(14,24)])
line('middle',(22,24),(26,24))
path('second-elbow',(34,24),[((38,28),4,4,True)])
line('last-dash',(38,36),(38,42))
poly('head',(32,36),(38,42),(44,36));join('head','last-dash')
''')
plan(13,'HRECT_L','The central arrow was too short with a tiny head, and broad flattened U shapes dominated the data rows.',
     'Lengthened the arrow, opened its head and narrowed the U interruptions; retained repeated ticks in both rows.', 'Lucide arrow-right: long shaft and open equal-arm head.', '''
for side in (-1,1):
    y=lambda d:24+side*d
    prefix='top' if side<0 else 'bottom'
    for j,x in enumerate((4,12,20)):
        line(f'{prefix}-tick-{j}',(x,y(16)),(x,y(11)))
    path(prefix+'-u',(32,y(16)),[(32,y(10)),((44,y(10)),6,5,side>0),(44,y(16))])
line('shaft',(4,24),(34,24));poly('head',(28,18),(34,24),(28,30));join('shaft','head')
''')
plan(14,'SQUARE','The inner arrowhead tips nearly touched, collapsing the gap between the paired upward arrows.',
     'Separated the heads, lengthened both shafts and widened the smooth semicircular U while preserving symmetry.', 'Lucide move-up: equal open arrowheads and centered shafts.', '''
path('u',(12,6),[(12,30),((36,30),12,12,False),(36,6)])
poly('left',(6,12),(12,6),(18,12));poly('right',(30,12),(36,6),(42,12));join('u','left');join('u','right')
''')
plan(15,'VRECT_L','The crescent was an elongated D with flattened tips, unlike the round lunar outline.',
     'Replaced the elliptical-looking outline with a circular outer lunar arc and a smooth concave inner arc.', 'Lucide moon: coherent circular crescent contours; retained source direction.', '''
self.add_arc('outer',(8,8),(8,40),radius_x=20,radius_y=20,large_arc=True,sweep=True)
self.add_arc('inner',(8,40),(8,8),radius_x=16,radius_y=16,sweep=False)
self.add_contour('moon','outer','inner',closed=True)
''')
plan(16,'VRECT_L','The cap bisected a circular face, the hair became ears and the bowtie dominated the portrait.',
     'Lengthened the blank face below the cap brim, restored scalloped side hair, and reduced the bowtie around a distinct round knot.', 'human_ref/user.svg: circular jaw vocabulary; no useful exact Lucide clown match.', '''
path('face',(16,18),[(16,24),((32,24),8,8,False),(32,18)],False)
path('cap',(16,18),[((24,10),8,8,True),((32,18),8,8,True),(16,18)],True);join('face','cap')
circle('pompom',24,6,2);line('hat-tip',(24,8),(24,10));join('hat-tip','pompom');join('hat-tip','cap')
path('hair-left',(16,18),[((10,19),4,4,False),((10,26),4,4,False),((16,27),4,4,False)])
path('hair-right',(32,18),[((38,19),4,4,True),((38,26),4,4,True),((32,27),4,4,True)])
join('hair-left','face');join('hair-left','cap');join('hair-right','face');join('hair-right','cap')
circle('knot',24,40,2)
path('bow-left',(22,39),[(13,36),(13,44),(22,41)]);path('bow-right',(26,39),[(35,36),(35,44),(26,41)])
join('knot','bow-left');join('knot','bow-right')
''')
plan(17,'HRECT_L','The head sat too high and the neck ribbons were detached blobs instead of flowing strands.',
     'Enlarged the round blank face, refined the three-lobed side hair and attached two smooth curling ribbons to the jaw.', 'human_ref/user.svg: circular head; source supplies side hair and ribbon curls.', '''
circle('head',24,20,12)
path('hair-left',(14,13),[((8,15),4,4,False),((8,25),5,5,False),((14,27),4,4,False)])
path('hair-right',(34,13),[((40,15),4,4,True),((40,25),5,5,True),((34,27),4,4,True)])
join('hair-left','head');join('hair-right','head')
path('ribbon-left',(17,30),[((16,35),4,4,False),((17,40),4,4,True)])
path('ribbon-right',(31,30),[((32,35),4,4,True),((31,40),4,4,False)])
join('ribbon-left','head');join('ribbon-right','head')
''')
plan(18,'VRECT_L','The bowl and straw were heavy and the stem too short compared with the tall reference glass.',
     'Extended the stem, widened the bowl and rebuilt a single straight straw with one top bend.', 'Lucide martini: stem centered on bowl and equal base arms; source retains rounded bowl.', '''
path('bowl',(8,15),[(40,15),((24,31),16,16,True),((8,15),16,16,True)],True)
poly('stem',(24,31),(24,44));poly('base',(16,44),(24,44),(32,44));join('stem','bowl');join('stem','base')
poly('straw',(24,24),(34,6),(40,4));join('straw','bowl')
''')
plan(19,'VRECT_L','The leaf was squat and the vein arms met at almost the same height rather than alternating.',
     'Rebuilt a taller gently lobed leaf with staggered left/right veins and a clear lower stem.', 'Lucide leaf: one coherent blade and sparse branching vein structure.', '''
path('leaf',(24,4),[('C',(33,10),(29,4),(29,8)),('C',(38,19),(38,11),(39,14)),('C',(39,27),(37,23),(40,23)),('C',(30,37),(39,31),(34,34)),('C',(24,40),(28,39),(27,40)),('C',(18,37),(21,40),(20,39)),('C',(9,27),(14,34),(9,31)),('C',(10,19),(8,23),(11,23)),('C',(15,10),(9,14),(10,11)),('C',(24,4),(19,8),(19,4))],True)
poly('stem',(24,12),(24,22),(24,30),(24,40),(24,44));join('stem','leaf')
line('left-vein',(17,16),(24,22));line('right-vein',(24,30),(31,24));join('left-vein','stem');join('right-vein','stem')
''')

def generate(indices=None,attempt='01'):
    for i,r in enumerate(rows):
        if indices is not None and i not in indices:continue
        key,wrong,change,ref,code=plans[i]
        source=Path(r['ref']);uuid=re.search(r'[a-f0-9-]{36}$',source.stem).group();concept=source.stem[:-37]
        run=Path('icon_set/work/primitive-make-ray')/uuid/('20260928T164556Z-fix-gpt-6-'+attempt)
        run.mkdir(exist_ok=False,parents=True)
        metadata={'concept':concept,'source_uuid':uuid,'reference_path':r['ref']}
        (run/(r['icon_id']+'.metadata.json')).write_text(json.dumps(metadata,indent=2))
        module=run/(r['icon_id'].replace('-','_')+'_'+uuid.replace('-','_')+'.py')
        header=f'''"""{concept}.
Before review: {wrong}
Feedback: {r['feedback']}
Revision: {change}
Construction: {ref}
Plan: coherent named contours; shared dimensions for mirrored or repeated parts.
SOLO48 {key}; 4px stroke. Native visual review required before acceptance.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = {uuid!r}
SOURCE_PATH = {r['ref']!r}
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = {r['icon_id']!r}
    keyshape = Keyshape.{key}
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = {tuple(concept.split())!r}
    def build(self):
'''
        module.write_text(header+HELPERS+textwrap.indent(code,'        '))
        shutil.copy(Path(r['fix_dir'])/'reference.png',run/'reference.png')
        shutil.copy(Path(r['fix_dir'])/'before.png',run/'before.png')
        r.update(run=str(run),module=str(module),source_uuid=uuid,concept=concept,wrong=wrong,change=change,construction=ref,keyshape=key)
    (ROOT/'batch.json').write_text(json.dumps(rows,indent=2))

if __name__=='__main__':generate()
