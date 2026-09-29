from pathlib import Path
import json,sys,textwrap
ROOT=Path(__file__).resolve().parent;xs=json.loads((ROOT/'items.json').read_text())
SOURCE_ICON_ID=[x['source_uuid'] for x in xs]
SOURCE_PATH=[x['reference'] for x in xs]
AUTHOR='gpt-6'
helper='''
    def circle(self,n,x,y,r,ry=None):
        ry=r if ry is None else ry
        self.add_arc(n+'a',(x-r,y),(x+r,y),radius_x=r,radius_y=ry)
        self.add_arc(n+'b',(x+r,y),(x-r,y),radius_x=r,radius_y=ry)
        self.add_contour(n,n+'a',n+'b',closed=True)
    def rect(self,n,x,y,w,h,r=3):
        self.add_line(n+'t',(x+r,y),(x+w-r,y))
        self.add_arc(n+'tr',(x+w-r,y),(x+w,y+r),radius_x=r)
        self.add_line(n+'r',(x+w,y+r),(x+w,y+h-r))
        self.add_arc(n+'br',(x+w,y+h-r),(x+w-r,y+h),radius_x=r)
        self.add_line(n+'b',(x+w-r,y+h),(x+r,y+h))
        self.add_arc(n+'bl',(x+r,y+h),(x,y+h-r),radius_x=r)
        self.add_line(n+'l',(x,y+h-r),(x,y+r))
        self.add_arc(n+'tl',(x,y+r),(x+r,y),radius_x=r)
        self.add_contour(n,*[n+s for s in ['t','tr','r','br','b','bl','l','tl']],closed=True)
'''
ds=[]
def add(k,wrong,change,ref,body):ds.append(dict(keyshape=k,wrong=wrong,change=change,lucide=ref,body=textwrap.dedent(body)))
add('SQUARE','The emblem was reduced to two disconnected thin hooks, losing the broad intertwined ribbon silhouette.','Restored broad diagonal S ribbons with rounded returns and overlapping offset ends.','No useful exact Lucide logo match; coherent tangent curves and shared diagonal offsets.', '''
self.add_bezier('upper-ribbon',(33,9),((28,4),(23,4),(19,8)),((15,12),(10,17),(7,20)),((0,28),(10,38),(18,31)),((23,26),(29,20),(33,17)),((40,11),(48,21),(41,28)))
self.add_bezier('lower-ribbon',(41,28),((36,33),(31,38),(28,41)),((23,46),(18,44),(15,41)))
self.add_bezier('inner-return',(15,41),((20,36),(28,28),(33,23)),((36,20),(39,24),(36,27)),((32,31),(27,36),(24,38)))
self.add_bezier('upper-return',(24,38),((20,42),(14,39),(12,38)))
self.add_line('upper-inner',(12,26),(29,9))
self.relate('connect','upper-ribbon','lower-ribbon');self.relate('connect','lower-ribbon','inner-return');self.relate('connect','inner-return','upper-return')
''')
add('CIRCLE','A scalloped ring with a tiny center replaced the recognizable eight separate flower petals.','Restored eight individual elongated petals around a larger open center, with a regular radial arrangement.','flower: central disc and radial petal structure; eight-petal count comes from original.', '''
self.circle('center',24,24,5)
# The cardinal and diagonal petals share a quarter-turn repeat definition.
for i in range(4):
 def p(x,y):
  x,y=x-24,y-24
  for _ in range(i):x,y=-y,x
  return (24+x,24+y)
 self.add_bezier('cardinal'+str(i),p(21,18),(p(18,9),p(18,4),p(24,4)),(p(30,4),p(30,9),p(27,18)))
 self.add_bezier('diagonal'+str(i),p(27,18),(p(31,9),p(36,7),p(40,11)),(p(44,15),p(39,19),p(31,22)))
''')
add('SQUARE','The rounded rectangular bubble and tiny arrow-like house lost the broad oval housing and house proportions.','Restored an oval speech bubble with a clear tail and a wider house with an open wall contour and pitched roof.','message-circle: smooth bubble and distinct tail; original controls house arrangement.', '''
self.add_bezier('bubble',(10,33),((0,24),(3,7),(18,5)),((33,1),(44,10),(44,21)),((44,33),(32,39),(18,36)))
self.add_polyline('tail',(18,36),(5,43),(10,33));self.relate('connect','tail','bubble')
self.add_polyline('roof',(13,22),(24,12),(35,22))
self.add_polyline('walls',(17,19),(17,30),(31,30),(31,19))
self.relate('connect','walls','roof')
''')
add('SQUARE','The information glyph resembled a short stem on a broad blob, and the bubble tail was too curved.','Restored a serif lowercase i, with a separate dot, upper flag and baseline, inside a square message bubble with an angular tail.','message-square: rounded box and intentional angular tail.', '''
self.add_polyline('bottom-tail',(42,30),(42,34),(23,34),(14,43),(14,34),(9,34))
self.add_arc('bl',(9,34),(5,30),radius_x=4)
self.add_line('left',(5,30),(5,9));self.add_arc('tl',(5,9),(9,5),radius_x=4)
self.add_line('top',(9,5),(38,5));self.add_arc('tr',(38,5),(42,9),radius_x=4)
self.add_line('right',(42,9),(42,30));self.add_contour('bubble','bottom-tail','bl','left','tl','top','tr','right',closed=True)
self.add_dot('dot',(24,13))
self.add_polyline('info',(20,21),(24,21),(24,29));self.add_line('serif',(19,29),(29,29));self.relate('connect','info','serif')
''')
add('HRECT_M','The two source circles became narrow vertical ellipses, so the Venn intersection proportions were wrong.','Restored two equal true circles with a balanced central intersection lens.','No extra symbol added: the original shows only two circles; shared radius and baseline.', '''
for n,x in [('left',18),('right',30)]:self.circle(n,x,24,14)
self.relate('connect','left','right')
''')
add('SQUARE','The envelope became a rectangular document with a V band; the open side flaps and lower envelope flap disappeared.','Rebuilt the open envelope around a projecting invoice, with side flaps, lower flap, two item lines and a dollar mark.','mail-open: diagonal side folds and open envelope silhouette.', '''
self.add_polyline('paper',(10,26),(10,4),(38,4),(38,26))
self.add_polyline('envelope',(10,17),(4,22),(4,41),(44,41),(44,22),(38,17))
self.add_polyline('flap',(4,41),(20,29),(28,29),(44,41))
self.add_line('fold-left',(4,22),(15,30));self.add_line('fold-right',(44,22),(33,30))
self.relate('connect','envelope','flap');self.relate('connect','fold-left','envelope');self.relate('connect','fold-right','envelope')
for y in [12,20]:self.add_line('item'+str(y),(16,y),(20,y))
self.add_bezier('dollar',(32,11),((26,9),(24,14),(29,15)),((35,16),(32,22),(26,20)))
self.add_line('currency-top',(29,7),(29,10));self.add_line('currency-bottom',(29,21),(29,24))
''')
infinity='''
self.add_bezier('cross-down',(14,14),((20,14),(28,34),(34,34)))
self.add_arc('right-loop',(34,34),(34,14),radius_x=10,sweep=False)
self.add_bezier('cross-up',(34,14),((28,14),(20,34),(14,34)))
self.add_arc('left-loop',(14,34),(14,14),radius_x=10,sweep=True)
self.add_contour('infinity','cross-down','right-loop','cross-up','left-loop',closed=True)
'''
add('HRECT_M','The horizontal infinity sign was stretched into two upright oval loops.','Restored wide rounded infinity lobes and a smooth diagonal crossing, matching the horizontal source proportions.','infinity: tangent semicircular ends joined by smooth crossing curves.',infinity)
add('SQUARE','The four-snake pinwheel became a two-headed DNA-like pair with round heads.','Restored four pointed snake heads around a rotationally repeated curved interweave.','No useful exact snake match; four quarter-turn instances share smooth S-body geometry.', '''
for i in range(4):
 def p(x,y):
  x,y=x-24,y-24
  for _ in range(i):x,y=-y,x
  return (24+x,24+y)
 self.add_bezier('snake-body'+str(i),p(14,12),(p(4,15),p(3,24),p(10,28)),(p(17,32),p(23,26),p(25,22)))
 self.add_bezier('snake-head'+str(i),p(14,12),(p(12,8),p(16,6),p(19,7)),(p(21,7),p(21,5),p(22,4)),(p(24,10),p(19,14),p(14,12)))
 self.relate('connect','snake-body'+str(i),'snake-head'+str(i))
''')
add('VRECT_L','Three diamond map bases became horizontal bars and the large top node was reduced to another small circle.','Restored a prominent upper node, a vertical link, and three small circular markers on diamond bases.','network: shared linked-node construction; original diamond map bases retained.', '''
self.circle('hub',24,11,8)
self.add_line('link',(24,19),(24,31));self.relate('connect','hub','link')
for i,(x,y) in enumerate([(8,28),(24,34),(40,28)]):
 self.circle('marker'+str(i),x,y,3)
 self.add_polyline('base'+str(i),(x,y+3),(x+6,y+7),(x,y+11),(x-6,y+7),closed=True)
 self.relate('connect','marker'+str(i),'base'+str(i))
self.relate('connect','link','marker1')
''')
add('HRECT_M','The loop was too tall, producing a bow-tie silhouette rather than a broad infinity symbol.','Rebalanced the loop to two wide equal lobes with smooth tangent joins and a centered crossing.','infinity: coherent crossing curves and circular end lobes.',infinity)
add('VRECT_L','The raft lost its inflatable rim and read as an oval sign with a bar.','Restored the surrounding air tube, recessed cockpit and a seat, beside a separate paddle with a wide blade and end grip.','sailboat: coherent vessel contours; the raft structure comes from the original.', '''
self.add_arc('raft-top',(4,16),(28,16),radius_x=12)
self.add_line('raft-right',(28,16),(28,32));self.add_arc('raft-bottom',(28,32),(4,32),radius_x=12)
self.add_line('raft-left',(4,32),(4,16));self.add_contour('raft','raft-top','raft-right','raft-bottom','raft-left',closed=True)
self.rect('cockpit',10,12,12,24,6)
self.add_line('seat',(10,24),(22,24));self.relate('connect','seat','cockpit')
self.rect('blade',35,4,9,14,3)
self.add_line('shaft',(40,18),(40,44));self.add_line('grip',(36,44),(44,44));self.relate('connect','shaft','blade');self.relate('connect','shaft','grip')
''')
hijab='''
self.add_arc('hood-top',(12,16),(36,16),radius_x=12)
self.add_bezier('left',(12,16),((12,24),(13,28),(10,33)),((6,38),(6,40),(6,44)))
self.add_bezier('right',(36,16),((36,24),(35,28),(38,33)),((42,38),(42,40),(42,44)))
self.add_contour('outer','left',closed=False)
self.relate('connect','hood-top','left');self.relate('connect','hood-top','right')
self.circle('face',24,19,7)
self.add_bezier('scarf-fold',(10,33),((18,32),(24,43),(37,31)))
self.add_bezier('lower-fold',(24,43),((29,41),(36,38),(40,36)))
'''
add('VRECT_L','The scarf was a narrow arch with vertical sides; its shoulders and wrap folds were missing.','Restored a rounded hood, circular face opening, sloping shoulders and overlapping scarf folds.','human_ref/user.svg: circular face and rounded shoulder construction; asymmetry follows the scarf wrap.',hijab)
add('VRECT_L','The torso and scarf wrap were reduced to a flat arc under an oval opening.','Rebuilt the complete hijab bust with broad shoulders and two sweeping wrap folds around a circular face.','human_ref/user.svg: head proportions and soft shoulder construction; source controls head covering.',hijab)
japanese='''
self.add_bezier('hair-left',(14,29),((9,29),(6,28),(6,23)),((6,11),(15,4),(26,4)))
self.add_bezier('hair-right',(42,23),((42,29),(38,29),(33,29)))
self.add_arc('jaw',(32,20),(16,20),radius_x=8)
self.add_bezier('fringe',(16,20),((15,17),(16,14),(18,12)),((21,17),(26,19),(32,20)))
self.add_contour('face','jaw','fringe',closed=True)
self.add_bezier('flower',(36,6),((39,3),(42,7),(40,10)),((45,9),(46,14),(41,15)),((44,20),(39,22),(36,18)),((32,22),(28,19),(31,15)),((26,14),(28,9),(33,10)),((32,5),(35,3),(36,6)))
self.add_arc('shoulders',(6,44),(42,44),radius_x=18,radius_y=12)
self.add_line('collar-main',(33,34),(21,44));self.add_line('collar-cross',(16,34),(25,41))
self.relate('connect','collar-main','collar-cross')
self.relate('connect','face','shoulders')
'''
add('VRECT_L','The flower ornament disappeared and the kimono collar became one unrelated diagonal.','Restored the flower hair ornament, swept fringe, rounded bob and crossed kimono collar.','human_ref/user.svg and user: circular jaw with rounded shoulders; flower: smooth petal lobes.',japanese)
add('VRECT_L','The two distinct loop arrows became one S-shaped line and the upper arrowhead disappeared.','Restored two circular iteration sweeps with separate arrowheads over a rightward baseline arrow.','No useful exact workflow match; coherent circular sweeps and open arrowheads.', '''
self.add_line('baseline',(4,42),(44,42));self.add_polyline('baseline-arrow',(39,37),(44,42),(39,47));self.relate('connect','baseline','baseline-arrow')
self.add_bezier('lower-loop',(23,42),((38,34),(29,17),(17,21)),((9,23),(6,28),(7,33)))
self.add_polyline('lower-arrow',(6,27),(7,33),(12,29));self.relate('connect','lower-loop','lower-arrow');self.relate('connect','lower-loop','baseline')
self.add_bezier('upper-loop',(18,21),((5,13),(17,0),(27,5)),((33,7),(35,11),(34,16)))
self.add_polyline('upper-arrow',(29,11),(34,16),(39,11));self.relate('connect','upper-loop','upper-arrow')
''')
add('SQUARE','The linked hexagonal endpoints became dots and the central cube was skewed.','Restored a symmetric three-face cube with three explicit hexagonal nodes and straight radial connectors.','network: repeated node ownership; the original isometric cube and hexagons define the geometry.', '''
self.add_polyline('cube',(24,18),(33,23),(33,33),(24,38),(15,33),(15,23),closed=True)
self.add_polyline('seams',(15,23),(24,28),(33,23));self.add_line('vertical',(24,28),(24,38));self.relate('connect','seams','cube');self.relate('connect','vertical','cube');self.relate('connect','vertical','seams')
for n,x,y in [('top',24,7),('left',7,39),('right',41,39)]:
 self.add_polyline(n,(x,y-5),(x+4,y-3),(x+4,y+3),(x,y+5),(x-4,y+3),(x-4,y-3),closed=True)
self.add_line('top-link',(24,12),(24,18));self.add_line('left-link',(15,33),(11,36));self.add_line('right-link',(33,33),(37,36))
for n in ['top','left','right']:
 self.relate('connect',n+'-link',n);self.relate('connect',n+'-link','cube')
''')
add('VRECT_L','The characteristic flower and crossed garment lapels were absent.','Restored the flower ornament, swept fringe, bob silhouette and two crossing kimono lapels.','human_ref/user.svg and user: circular jaw and shoulders; flower: rounded petal construction.',japanese)
add('VRECT_L','The exaggerated pinched hips and short crotch made the jeans look like flared shorts.','Restored straight long trouser legs, a higher crotch, front pocket curves and a short central fly.','shirt: coherent garment outline and connected seams; trouser proportions follow the reference.', '''
self.add_polyline('jeans',(12,4),(36,4),(40,44),(28,44),(24,23),(20,44),(8,44),closed=True)
self.add_bezier('pocket-left',(20,4),((20,10),(17,13),(11,13)))
self.add_bezier('pocket-right',(28,4),((28,10),(31,13),(37,13)))
self.add_line('fly',(24,4),(24,13))
for n in ['pocket-left','pocket-right','fly']:self.relate('connect',n,'jeans')
''')
add('SQUARE','The crossed straight legs and raised free arm did not convey a javelin throwing stance.','Restored a bent rear throwing arm gripping the inclined javelin, a compact forward arm, torso and bent running legs.','human_ref/full_body_ref.png and person-standing: outlined circular head, coherent limb strokes.', '''
self.add_line('javelin',(4,12),(44,2))
self.circle('head',24,18,4)
self.add_line('torso',(24,30),(26,36))
self.add_polyline('throwing-arm',(24,30),(16,27),(12,10));self.relate('connect','throwing-arm','torso');self.relate('connect','throwing-arm','javelin')
self.add_polyline('front-arm',(24,30),(32,30),(34,27));self.relate('connect','front-arm','torso')
self.add_polyline('rear-leg',(26,36),(21,39),(15,44));self.add_polyline('front-leg',(26,36),(35,35),(40,44));self.relate('connect','rear-leg','torso');self.relate('connect','front-leg','torso')
self.mark_human_figure('thrower',head='head',torso='torso',torso_junction='start')
''')
add('SQUARE','The judge robe was missing and the gavel was a filled square on a diagonal stick.','Restored a full judicial robe with a V collar and central seam, plus a diagonal rectangular gavel head and handle.','human_ref/user.svg and user: circular head and rounded bust; garment contour from original.', '''
self.circle('head',21,12,8)
self.add_bezier('robe',(5,44),((5,36),(6,29),(15,28)))
self.add_polyline('collar',(15,28),(21,35),(27,28))
self.add_bezier('robe-right',(27,28),((30,29),(32,30),(34,32)),((36,35),(37,39),(37,44)))
self.add_line('hem',(5,44),(37,44));self.add_line('seam',(21,35),(21,44))
for n in ['robe','robe-right','hem','seam']:self.relate('connect',n,'collar') if n in ['robe','robe-right','seam'] else None
self.relate('connect','hem','robe');self.relate('connect','hem','robe-right');self.relate('connect','seam','hem')
self.add_polyline('gavel',(34,16),(44,23),(39,30),(29,23),closed=True)
self.add_line('handle',(34,27),(27,37));self.relate('connect','handle','gavel')
''')
assert len(ds)==20
for x,d in zip(xs,ds):
 run=Path('icon_set/work/primitive-make-ray')/x['source_uuid']/f"20260929T033633Z-fix-{x['n']:02}-r1";run.mkdir(parents=True,exist_ok=False)
 x.update({k:v for k,v in d.items() if k!='body'});x['run']=str(run)
 (run/(x['icon_id']+'.metadata.json')).write_text(json.dumps({'concept':x['concept'],'source_uuid':x['source_uuid'],'reference_path':x['reference'],'feedback':x['feedback']},indent=2))
 (run/'comparison.md').write_text(f"Original and rejected images inspected before authoring.\n\nRejected: {d['wrong']}\n\nFeedback: {x['feedback']}\n\nRevision: {d['change']}\n\nConstruction: {d['lucide']}\n")
 p=run/(x['icon_id'].replace('-','_')+'_'+x['source_uuid'].replace('-','_')+'.py')
 head=f'''"""{x['concept']}.\nPlan: {d['change']}\nConstruction: {d['lucide']}\nKeyshape: {d['keyshape']}; preserve the original's recognizable proportions.\n"""\nfrom icon_set.model.icons.solo._base import Solo48\nfrom icon_set.model.keyshapes import Keyshape\nSOURCE_ICON_ID = {x['source_uuid']!r}\nSOURCE_PATH = {x['reference']!r}\nAUTHOR = 'gpt-6'\nclass Drawing(Solo48):\n    icon_id = {x['icon_id']!r}\n    keyshape = Keyshape.{d['keyshape']}\n    semantic_role = 'MAIN'\n    semantic_kind = 'noun'\n    category = 'objects'\n    aliases = ()\n    keywords = {tuple(x['concept'].split())!r}\n'''
 p.write_text(head+helper+'\n    def build(self):\n'+textwrap.indent(d['body'],'        '));x['module']=str(p)
(ROOT/'authored.json').write_text(json.dumps(xs,indent=2));print('Authored 20 fresh runs')
