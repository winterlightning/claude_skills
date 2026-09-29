from pathlib import Path
from datetime import datetime,timezone
import json,textwrap,sys,cairosvg
from icon_set.scripts.primitive_fix import load_icon,render_previews
ROOT=Path(__file__).parent
AUTHOR='gpt-6'
rows=json.loads((ROOT/('runs.json' if (ROOT/'runs.json').exists() else 'inputs.json')).read_text())
notes=[
('The rejected judge has a short helmet-like hair arch and a generic V shirt; the original has long parted hair and a robe collar.','Restore long outward-turning hair, a parted hairline, circular jaw and judicial robe collar.'),
('The rejected judge has a short helmet-like hair arch and a generic V shirt; the original has long parted hair and a robe collar.','Restore long outward-turning hair, a parted hairline, circular jaw and judicial robe collar.'),
('The laptop base has a raised hump and the tablet/phone shapes lack the original distinction.','Restore two upright devices, the phone control, a partially occluded laptop screen and a downward notch in its base.'),
('Two vertical outlined squares became two horizontally arranged dots.','Restore two small outlined squares in a vertical column inside a clear laptop screen.'),
('The short device rectangles and shallow base lose the tall source arrangement.','Restore two tall rounded screens above a linked laptop body and curved lower base.'),
('The rejected drawing loses the bowl hull, one signal arc and the distinct rim.','Restore a deep curved hull, rim, three signal arcs and water beneath.'),
('A lard portion on a rectangular tray became a dome on a semicircular dish.','Restore the rounded rectangular tray and low oblong lard portion with a curled end.'),
('The laurel crown became a straight helmet band with dangling bars.','Restore a sloping laurel twig with paired leaf strokes and a smooth right-facing head profile.'),
('The rejected face has a closed smile and two tiny external strokes instead of large tears.','Restore an open laughing mouth, closed happy eyes and two large teardrops overlapping the lower cheeks.'),
('The mower hood disappeared, leaving a steering rod and two wheels.','Restore the rounded engine hood, seat/back outline, steering stem and unequal wheels.'),
('The pump jack lost the lattice braces and right-hand counterweight.','Restore the slanted beam, curved horsehead, triangular lattice support, hanging rod and counterweight.'),
('The croissant became a hollow crescent with almost no rolled layers.','Restore the plump diagonal pastry, curled tapered ends and curved seams dividing the rolled sections.'),
('The pinecone became a leaf with straight chevron stripes.','Restore overlapping pointed scales, rounded lower lobes and the short stem.'),
('The delivery truck lost its canopy and stacked package arrangement; wheels hang below a detached chassis.','Restore the left-facing cab, windshield, canopy, large front wheel and stacked boxes on the flatbed.'),
('The hen has a rectangular comb, pointed triangular tail and overly flat body.','Restore the split rounded comb, plump curved body, two-lobed tail, beak and bent feet.'),
('The sneezing face became a jagged zigzag and the sneeze rays became dots.','Restore a smooth left-facing anatomical profile, closed eye, open lips, sloping neck and three outward sneeze rays.'),
('The pointing hand lost a folded-finger step and its thumb reads as a squared bump.','Restore the long left-pointing index finger, rounded thumb/palm and three folded fingers.'),
('The sheep became a smooth boxy animal with a circular head and no wool or ear.','Restore a woolly scalloped outline, long left-facing head, drooping ear and short legs.'),
('The leggings have a low crotch and broad angular legs, reading as ordinary trousers.','Restore the high crotch, long narrow tapered legs and smooth waist-to-ankle contour.'),
('The lifeguard has no convincing seat or bent leg; the ladder and two water rows are missing.','Restore an elevated ladder chair, seated figure with bent leg and two rows of water waves.'),
]
helpers='''
    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def rect(self,n,x,y,w,h,r=0):
        if not r:
            self.add_polyline(n,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
            return
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        for j in range(8):
            if j%2:self.add_arc(n+str(j),pts[j],pts[(j+1)%8],radius_x=r)
            else:self.add_line(n+str(j),pts[j],pts[(j+1)%8])
        self.add_contour(n,*(n+str(j) for j in range(8)),closed=True)
    def curve(self,n,start,*segments):
        self.add_bezier(n,start,*segments)
'''
designs=[]
def add(k,c,ref='Original reference; no useful exact Lucide match. Smooth curves and shared geometric proportions are authored on SOLO48.'):
 designs.append((k,textwrap.dedent(c).strip(),ref))
for i in range(2):
 add('VRECT_L','''
# Portrait: circular r9 jaw, shoulders at y30 touch the jaw ink at y28.
self.add_arc('jaw',(15,17),(33,17),radius_x=9,sweep=False)
self.curve('parted-hairline',(33,17),((29,17),(26,13),(24,11)),((22,14),(18,17),(15,17)))
self.add_contour('face','jaw','parted-hairline',closed=True)
self.curve('hair',(12,33),((10,32),(8,31),(6,30)),((10,24),(9,21),(9,16)),((9,0),(39,0),(39,16)),((39,21),(38,24),(42,30)),((40,31),(38,32),(36,33)))
self.curve('shoulders',(6,44),((8,33),(14,30),(24,30)),((34,30),(40,33),(42,44)))
self.add_polyline('collar',(18,31),(24,38),(30,31))
self.add_line('robe-front',(24,38),(24,44))
self.relate('connect','face','shoulders')
self.relate('connect','collar','robe-front')
''','human_ref/user.svg and human-reference.md: circular jaw, broad shoulders and touching-ink portrait construction; source owns long parted hair and collar.')
add('SQUARE','''
self.rect('tablet',13,4,13,25,3)
self.rect('phone',33,4,12,25,3)
self.add_dot('phone-control',(39,24))
self.curve('laptop-left',(9,22),((6,22),(6,24),(6,27)),((6,27),(6,39),(6,39)))
self.add_line('laptop-right',(41,33),(41,39))
self.curve('base',(4,39),((4,44),(8,44),(12,44)),((12,44),(36,44),(36,44)),((40,44),(44,44),(44,39)))
self.add_polyline('deck-left',(4,39),(18,39))
self.curve('notch',(18,39),((18,43),(29,43),(29,39)))
self.add_line('deck-right',(29,39),(44,39))
self.relate('connect','base','deck-left');self.relate('connect','base','deck-right')
self.relate('connect','notch','deck-left');self.relate('connect','notch','deck-right')
''','Lucide laptop: rounded upright screen and lower deck; source owns the two foreground devices and occlusion.')
add('SQUARE','''
self.rect('screen',8,6,32,28,3)
for y in (13,24):self.rect('tile-'+str(y),15,y,6,6)
self.add_polyline('base',(8,34),(6,42),(42,42),(40,34))
self.relate('connect','screen','base')
''','Lucide laptop: screen with consistent rounded corners and a broad lower deck.')
add('SQUARE','''
for x in (4,30):self.rect('upright-'+str(x),x,4,14,27,3)
self.add_line('screen-bridge',(18,18),(30,18))
self.add_line('body-left',(11,31),(11,39))
self.add_line('body-right',(37,31),(37,39))
self.add_line('deck',(5,39),(43,39))
self.curve('base',(5,39),((5,44),(9,44),(13,44)),((13,44),(35,44),(35,44)),((39,44),(43,44),(43,39)))
self.relate('connect','deck','base')
''','Lucide laptop and smartphone: consistent screen radii; source owns the two tall panels and lower connecting body.')
add('SQUARE','''
# Three nested signal arcs, a bowl-shaped hull and one continuous water stroke.
for n,y,w,h in [('outer',8,10,6),('middle',13,6,4),('inner',18,2,2)]:
 self.curve('signal-'+n,(24-w,y),((24-w//2,y-h),(24+w//2,y-h),(24+w,y)))
self.curve('back-left',(4,23),((5,20),(9,20),(13,19)))
self.curve('back-right',(35,19),((39,20),(43,20),(44,23)))
self.curve('rim',(4,23),((12,28),(36,28),(44,23)))
self.curve('hull',(44,23),((42,40),(6,40),(4,23)))
self.add_contour('vessel','rim','hull',closed=True)
self.curve('water',(4,43),((8,43),(10,42),(12,40)),((17,44),(21,44),(24,40)),((29,44),(33,44),(36,40)),((39,42),(41,43),(44,43)))
''')
add('HRECT_L','''
self.rect('tray',4,8,40,32,6)
self.curve('lard',(13,26),((10,19),(17,16),(24,16)),((36,15),(38,20),(35,27)),((33,32),(18,32),(15,29)),((14,28),(13,27),(13,26)))
self.curve('curled-end',(27,30),((27,24),(31,23),(35,26)))
''')
add('VRECT_L','''
self.curve('head-back',(10,44),((10,44),(10,35),(10,35)),((0,27),(4,11),(13,6)),((21,1),(33,4),(36,11)))
self.add_polyline('forehead-nose',(38,20),(42,28),(36,28),(36,34))
self.curve('chin',(36,34),((36,39),(31,38),(28,38)))
self.add_line('neck',(28,38),(28,44))
self.curve('laurel-stem',(4,22),((16,22),(28,16),(41,11)))
for n,p,a,b in [('left',(13,21),(14,14),(18,24)),('middle',(23,18),(25,11),(28,21)),('right',(33,14),(35,7),(38,17))]:
 self.add_polyline('leaf-pair-'+n,a,p,b)
self.relate('connect','chin','neck')
''')
add('CIRCLE','''
self.curve('head-top',(6,32),((0,16),(10,4),(24,4)),((38,4),(48,16),(42,32)))
self.curve('chin',(12,39),((18,47),(30,47),(36,39)))
for n,x in [('left',16),('right',32)]:
 self.curve('eye-'+n,(x-4,18),((x-2,13),(x+2,13),(x+4,18)))
self.add_line('mouth-top',(14,28),(34,28))
self.curve('mouth-bottom',(34,28),((31,39),(17,39),(14,28)))
self.add_contour('mouth','mouth-top','mouth-bottom',closed=True)
self.curve('tear-left',(9,26),((9,32),(15,39),(8,39)),((0,39),(4,32),(9,26)))
self.curve('tear-right',(39,26),((39,32),(33,39),(40,39)),((48,39),(44,32),(39,26)))
''')
add('SQUARE','''
self.circle('front-wheel',13,36,8)
self.circle('rear-wheel',39,38,6)
self.curve('hood',(5,29),((5,24),(7,21),(12,21)),((12,21),(26,21),(26,21)),((31,21),(33,24),(33,29)))
self.add_polyline('hood-end',(33,29),(33,33))
self.add_line('chassis',(21,36),(33,36))
self.curve('seat',(26,20),((26,20),(26,16),(29,16)),((29,16),(40,15),(40,22)),((40,22),(40,32),(40,32)))
self.add_polyline('steering',(4,4),(10,4),(16,21))
self.relate('connect','hood','hood-end')
''','Lucide tractor: unequal round wheels and a separate engine silhouette; source owns lawn-mower proportions and steering stem.')
add('SQUARE','''
self.curve('horsehead',(15,4),((8,3),(3,20),(6,23)),((10,25),(19,7),(15,4)))
self.add_polyline('beam',(14,12),(43,23),(41,28),(12,17))
self.add_polyline('tower',(17,44),(26,18),(35,44))
self.add_line('brace-a',(21,29),(32,39))
self.add_line('brace-b',(31,29),(20,39))
self.add_line('pump-rod',(7,23),(7,44))
self.add_line('counterweight-rod',(40,28),(40,35))
self.rect('counterweight',37,35,6,9)
self.add_line('ground',(4,44),(44,44))
''')
add('SQUARE','''
self.curve('pastry',(12,27),((6,21),(2,23),(4,29)),((6,34),(11,39),(22,41)),((29,43),(36,37),(40,31)),((45,25),(46,13),(40,5)),((37,1),(36,8),(35,12)),((33,12),(31,13),(31,16)),((24,12),(15,17),(17,21)),((15,22),(13,23),(12,27)))
self.curve('left-tip-seam',(12,27),((10,32),(11,36),(14,39)))
self.curve('left-roll',(17,21),((17,29),(19,35),(22,41)))
self.curve('right-roll',(31,16),((36,20),(39,25),(40,31)))
self.curve('right-tip-seam',(35,12),((40,11),(43,15),(44,20)))
''','Lucide croissant: plump rolled central body and rounded tapered ends; source owns the diagonal direction and full pastry mass.')
add('VRECT_L','''
self.curve('top-scale',(15,13),((17,9),(20,6),(24,4)),((28,6),(31,9),(33,13)))
self.curve('middle-left',(10,23),((10,19),(10,15),(15,11)),((20,13),(22,16),(24,19)))
self.curve('middle-right',(38,23),((38,19),(38,15),(33,11)),((28,13),(26,16),(24,19)))
self.add_polyline('center-scale',(17,26),(24,19),(31,26))
self.curve('lower-left',(7,22),((7,35),(12,40),(24,40)),((24,40),(24,33),(24,33)),((20,28),(12,23),(7,22)))
self.curve('lower-right',(41,22),((41,35),(36,40),(24,40)),((24,40),(24,33),(24,33)),((28,28),(36,23),(41,22)))
self.add_line('stem',(24,40),(24,44))
''')
add('SQUARE','''
self.circle('front-wheel',12,38,6)
self.add_polyline('cab',(14,10),(8,23),(4,27),(4,36),(6,36))
self.add_line('canopy',(14,10),(44,10))
self.add_line('cab-back',(21,10),(21,36))
self.add_line('windshield-bottom',(8,23),(21,23))
self.add_line('flatbed',(18,36),(44,36))
self.rect('lower-packages',27,25,17,11)
self.add_line('package-division',(36,25),(36,36))
self.rect('upper-package',31,16,9,9)
self.relate('connect','canopy','cab')
''','Lucide truck: coherent cabin/chassis and circular wheels; source owns the open canopy and stacked cargo, with one visible front wheel.')
add('SQUARE','''
self.curve('body',(9,13),((12,8),(17,11),(20,18)),((24,28),(31,27),(36,20)),((40,16),(41,12),(44,15)),((47,18),(43,22),(42,23)),((47,26),(43,29),(41,30)),((39,43),(14,43),(9,33)),((6,28),(10,22),(8,18)))
self.add_polyline('beak',(8,18),(4,15),(9,13))
self.curve('comb',(10,11),((5,2),(12,2),(14,5)),((20,1),(22,7),(18,11)))
self.add_polyline('foot-left',(18,40),(16,45),(13,45))
self.add_polyline('foot-right',(27,40),(26,45),(23,45))
self.relate('connect','body','beak')
''','Lucide bird: flowing curved body and small attached feet; source owns split comb and two-lobed tail.')
add('SQUARE','''
self.curve('head-neck',(15,23),((11,23),(12,20),(14,17)),((15,14),(13,9),(20,5)),((31,0),(43,10),(39,22)),((37,27),(34,30),(35,34)),((36,39),(40,43),(43,46)))
self.add_polyline('nose',(15,23),(11,25),(16,26),(16,29))
self.curve('lips-chin',(16,29),((22,28),(23,31),(18,32)),((18,37),(22,35),(25,35)))
self.add_polyline('neck-front',(25,35),(27,41),(24,45))
self.add_line('closed-eye',(19,17),(22,18))
for n,a,b in [('upper',(4,29),(10,31)),('middle',(3,36),(10,35)),('lower',(5,43),(11,39))]:self.add_line('sneeze-'+n,a,b)
self.relate('connect','head-neck','nose');self.relate('connect','nose','lips-chin');self.relate('connect','lips-chin','neck-front')
''','Human reference: preserve coherent continuous head/neck anatomy rather than a detached stick-figure construction; original owns profile and sneeze rays.')
add('HRECT_L','''
self.curve('hand',(22,16),((22,16),(8,16),(8,16)),((1,16),(1,24),(8,24)),((8,24),(20,24),(20,24)),((15,24),(15,31),(21,31)),((17,31),(17,37),(23,37)),((20,37),(20,42),(25,42)),((25,42),(34,42),(34,42)),((42,42),(44,35),(44,28)),((44,28),(44,22),(44,22)),((44,13),(35,6),(29,6)),((24,6),(22,10),(22,16)))
self.add_line('middle-finger-crease',(21,31),(25,31))
self.add_line('ring-finger-crease',(23,37),(26,37))
self.relate('connect','hand','middle-finger-crease');self.relate('connect','hand','ring-finger-crease')
''','Lucide hand: rounded finger ends and a continuous palm contour; source owns the pointing direction and folded finger count.')
add('SQUARE','''
self.curve('woolly-body',(8,14),((10,4),(20,4),(22,12)),((28,12),(30,19),(24,19)),((20,19),(19,16),(18,15)))
self.curve('back',(28,15),((32,11),(35,13),(36,15)),((45,13),(45,23),(43,26)),((45,29),(43,34),(41,35)))
self.add_polyline('rear-leg',(41,35),(42,44),(36,44),(35,37))
self.curve('belly',(35,37),((32,40),(26,38),(24,36)),((21,39),(19,38),(17,38)))
self.add_polyline('front-leg',(17,38),(16,44),(11,44),(11,36))
self.curve('chest-face',(11,36),((6,33),(6,28),(7,24)),((0,25),(1,17),(8,14)))
self.relate('connect','back','rear-leg');self.relate('connect','rear-leg','belly');self.relate('connect','belly','front-leg');self.relate('connect','front-leg','chest-face');self.relate('connect','chest-face','woolly-body')
''')
add('VRECT_M','''
self.add_line('waist',(14,4),(34,4))
self.curve('right-leg',(34,4),((36,15),(34,31),(34,44)))
self.add_polyline('inner-legs',(34,44),(28,44),(24,15),(20,44),(14,44))
self.curve('left-leg',(14,44),((14,31),(12,15),(14,4)))
self.relate('connect','waist','right-leg');self.relate('connect','right-leg','inner-legs');self.relate('connect','inner-legs','left-leg');self.relate('connect','left-leg','waist')
''')
add('SQUARE','''
# Stick figure: r4 at (14,8), torso starts (14,20), so head/body ink gap is exactly 4.
self.circle('head',14,8,4)
self.add_line('torso',(14,20),(14,26))
self.add_polyline('seated-leg',(14,26),(22,26),(28,34))
self.add_polyline('chair',(6,20),(8,28),(21,28))
self.add_line('left-chair-leg',(8,28),(4,44))
self.add_line('right-chair-leg',(21,28),(24,44))
self.add_line('rung-upper',(7,34),(22,34))
self.add_line('rung-lower',(5,40),(23,40))
for y in (39,45):
 self.curve('water-'+str(y),(28,y),((31,y),(33,y-2),(34,y-3)),((37,y),(41,y),(44,y-3)))
self.mark_human_figure('lifeguard',head='head',torso='torso',torso_junction='start')
self.relate('connect','torso','seated-leg')
''','human_ref/full_body_ref.png: outlined round head, coherent seated torso and bent leg; source owns the tall chair and two water rows.')

def revise(i,code):
 old=designs[i-1];designs[i-1]=(old[0],textwrap.dedent(code).strip(),old[2])
revise(4,designs[3][1].replace('(13,24)','(12,23)'))
revise(11,"""
self.curve('horsehead',(15,4),((8,3),(3,20),(6,23)),((10,25),(19,7),(15,4)))
self.add_line('beam',(12,14),(43,25))
self.add_polyline('tower',(16,44),(26,21),(36,44))
self.add_line('brace-a',(21,32),(32,43))
self.add_line('brace-b',(31,32),(20,43))
self.add_line('pump-rod',(7,23),(7,44))
self.add_line('counterweight-rod',(40,24),(40,34))
self.rect('counterweight',36,34,8,10)
self.add_line('ground',(4,44),(44,44))
""")
revise(13,"""
self.curve('top-scale',(15,13),((17,9),(20,6),(24,4)),((28,6),(31,9),(33,13)))
self.curve('middle-left',(10,23),((10,19),(10,15),(15,11)),((20,13),(22,16),(24,19)))
self.curve('middle-right',(38,23),((38,19),(38,15),(33,11)),((28,13),(26,16),(24,19)))
self.add_polyline('center-scale',(17,26),(24,19),(31,26))
self.curve('lower-outline',(7,22),((7,35),(12,40),(24,40)),((36,40),(41,35),(41,22)))
self.curve('lower-scale-top',(7,22),((12,23),(20,28),(24,33)),((28,28),(36,23),(41,22)))
self.add_line('stem',(24,33),(24,44))
self.relate('connect','lower-outline','lower-scale-top');self.relate('connect','lower-scale-top','stem')
""")
revise(16,"""
self.curve('head-neck',(15,23),((11,23),(12,20),(14,17)),((15,14),(13,9),(20,5)),((31,0),(43,10),(39,22)),((37,27),(34,30),(35,34)),((36,39),(40,43),(43,46)))
self.add_polyline('nose-upper-lip',(15,23),(11,25),(17,27))
self.curve('lower-lip-chin',(17,33),((17,38),(22,36),(25,35)))
self.add_polyline('neck-front',(25,35),(27,41),(24,45))
self.add_line('closed-eye',(19,17),(22,18))
for n,a,b in [('upper',(4,28),(10,30)),('middle',(3,35),(10,35)),('lower',(5,42),(11,39))]:self.add_line('sneeze-'+n,a,b)
self.relate('connect','head-neck','nose-upper-lip');self.relate('connect','lower-lip-chin','neck-front')
""")

if __name__=='__main__':
 selected=list(map(int,sys.argv[1:])) or list(range(1,21))
 for index in selected:
  row=rows[index-1];keyshape,code,refs=designs[index-1]
  reference=Path(row['reference']);SOURCE_ICON_ID=reference.stem[-36:];SOURCE_PATH=str(reference);concept=reference.stem[:-37]
  stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
  run=Path('icon_set/work/primitive-make-ray')/SOURCE_ICON_ID/(stamp+'-meaning-fix');run.mkdir(parents=True)
  meta={'concept':concept,'source_uuid':SOURCE_ICON_ID,'reference_path':SOURCE_PATH}
  (run/(row['id']+'.metadata.json')).write_text(json.dumps(meta,indent=2))
  (run/'review-before.md').write_text(f'Subject: {concept}.\n\nOriginal/current: {notes[index-1][0]}\n\nFeedback: {row["feedback"]}\n\nRevision: {notes[index-1][1]}\n\nReferences: {refs}\n')
  module=run/(row['id'].replace('-','_')+'_'+SOURCE_ICON_ID.replace('-','_')+'.py')
  extra='    human_construction = "bust"\n' if index in (1,2) else ''
  source=f'''from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = {SOURCE_ICON_ID!r}
SOURCE_PATH = {SOURCE_PATH!r}
AUTHOR = {AUTHOR!r}
# Symbol plan: {notes[index-1][1]}
# Construction references: {refs}
class Drawing(Solo48):
    icon_id = {row['id']!r}
    keyshape = Keyshape.{keyshape}
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = {row['category']!r}
    aliases = ()
    keywords = ({concept!r},)
{extra}{helpers}
    def build(self):
{textwrap.indent(code,'        ')}
'''
  module.write_text(source)
  try:
   icon=load_icon(module);report=icon.validate_icon();svg=icon.to_svg()
   (run/(row['id']+'.svg')).write_text(svg);(run/'validation.txt').write_text(report.describe());render_previews(svg,row['id'],48,run)
   for label,p in [('reference',reference),('before',Path(row['before']))]:cairosvg.svg2png(url=str(p),write_to=str(run/(label+'.png')),output_width=192,output_height=192)
   row.update({'run':str(run),'module':str(module),'svg':str(run/(row['id']+'.svg')),'comparison':notes[index-1][0],'change':notes[index-1][1],'references':refs})
   print(index,row['id'],report.status,len(report.errors),len(report.warnings),flush=True)
  except Exception as error:
   (run/'attempt-error.txt').write_text(str(error));print(index,'AUTHORING ERROR',repr(error),flush=True)
  (ROOT/'runs.json').write_text(json.dumps(rows,indent=2))
