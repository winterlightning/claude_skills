"""User-requested review revisions, preserving the previous candidates."""
from pathlib import Path
import sys,json,ast,textwrap
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.scripts.create_variant import prepare_variant
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/holes-review/mapping.json'
AUTHOR='gpt-6'
W=Path(__file__).parent
names=['leaning-tower-of-pisa','paw-print-v2','tuk-tuk-side-view','crawling-baby','curled-raccoon','pelican-on-water-v2','castle-tower-with-pennant-v2','sheep-jumping-fence','sea-lion']
mp=json.loads((W/'mapping.json').read_text())
state=W/'revision-2-mapping.json'
if not state.exists():
 out=[]
 for m in mp:
  if m['original'] in names:
   p,newid,s=prepare_variant(m['candidate'],'solo','Review revision: clear geometry and spacing')
   p.write_text(s);out.append({**m,'previous_candidate':m['candidate'],'previous_file':m['file'],'candidate':newid,'file':str(p.relative_to(ROOT))})
 state.write_text(json.dumps(out,indent=2))
revs=json.loads(state.read_text());codes={};notes={};keys={}
def put(n,key,note,code):keys[n]=key;notes[n]=note;codes[n]=textwrap.dedent(code)
put('leaning-tower-of-pisa','SQUARE','Straightened the leaning side walls, evenly spaced the sloping floors, and fitted the square envelope.', '''
# One constant lean controls both walls; every floor follows the same slope.
top_y,bottom_y=6,42
left_top,right_top=22,38
left=lambda y:left_top-(y-top_y)//3
right=lambda y:right_top-(y-top_y)//3
floor_ys=(15,24,33)
left_nodes=[(left(y),y) for y in floor_ys]
right_nodes=[(right(y+3),y+3) for y in floor_ys]
self.add_polyline('shaft',(left(bottom_y),bottom_y),*reversed(left_nodes),(left_top,top_y),(right_top,top_y),*right_nodes,(right(bottom_y),bottom_y),closed=True)
for i,(a,b) in enumerate(zip(left_nodes,right_nodes)):
    self.add_line(f'floor-{i}',a,b)
    self.relate('connect',f'floor-{i}','shaft')
self.add_polyline('ground',(6,42),(left(bottom_y),bottom_y),(right(bottom_y),bottom_y),(42,42))
self.relate('connect','ground','shaft')
''')
put('paw-print-v2','SQUARE','Balanced four circular toes with wider spacing and a smooth central pad; corrected the top and bottom bounds.', '''
# Mirrored toes share dimensions; the lower pad owns its paired corner arcs.
for name,cx,cy,radius in (('inner-left',15,10,4),('inner-right',33,10,4),('outer-left',9,24,3),('outer-right',39,24,3)):
    self.add_arc(name+'-top',(cx-radius,cy),(cx+radius,cy),radius_x=radius)
    self.add_arc(name+'-bottom',(cx+radius,cy),(cx-radius,cy),radius_x=radius)
    self.add_contour(name,name+'-top',name+'-bottom',closed=True)
self.add_arc('pad-crown',(16,38),(32,38),radius_x=8,radius_y=10)
self.add_arc('pad-right',(32,38),(28,42),radius_x=4)
self.add_line('pad-notch-right',(28,42),(24,40))
self.add_line('pad-notch-left',(24,40),(20,42))
self.add_arc('pad-left',(20,42),(16,38),radius_x=4)
self.add_contour('pad','pad-crown','pad-right','pad-notch-right','pad-notch-left','pad-left',closed=True)
''')
put('tuk-tuk-side-view','HRECT_L','Made the front wheel exactly circular and aligned both wheels on one baseline; fitted the full horizontal envelope.', '''
# Cabin owns its shared post nodes; the fork ends at the front wheel rim.
self.add_polyline('roof',(4,8),(22,8),(28,8))
self.add_polyline('rear-post',(4,8),(4,24),(4,36))
self.add_polyline('front-post',(22,8),(22,24),(22,36))
self.add_line('seat',(4,24),(22,24))
self.add_polyline('floor',(12,36),(22,36),(32,34))
self.add_polyline('front-frame',(28,8),(34,18),(38,28))
self.add_line('handlebar',(34,18),(40,18))
for name,cx,cy,r in (('rear-wheel',8,36,4),('front-wheel',38,34,6)):
    points=((cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r))
    for i,(a,b) in enumerate(zip(points,points[1:])):
        self.add_arc(f'{name}-{i}',a,b,radius_x=r)
    self.add_contour(name,*[f'{name}-{i}' for i in range(4)],closed=True)
for i,a in enumerate(self.primitives):
    for b in self.primitives[i+1:]:
        if a.start in (b.start,b.end) or a.end in (b.start,b.end):
            self.relate('connect',a.element_id,b.element_id)
''')
put('crawling-baby','SQUARE','Rebuilt the folded leg and foot as one roomy contour, retained the round head, and corrected all outer bounds.', '''
# Side-view crawling pose: circular head, rounded back, bent arm and folded leg.
self.add_arc('head-top',(6,12),(18,12),radius_x=6)
self.add_arc('head-bottom',(18,12),(6,12),radius_x=6)
self.add_contour('head','head-top','head-bottom',closed=True)
self.add_line('back',(20,24),(32,24))
self.add_arc('hip',(32,24),(42,34),radius_x=10)
self.add_line('leg-outer',(42,34),(42,38))
self.add_arc('foot-round',(42,38),(38,42),radius_x=4)
self.add_line('sole',(38,42),(30,42))
self.add_line('leg-inner',(30,42),(30,34))
self.add_line('belly',(30,34),(22,34))
self.add_line('arm-inner',(22,34),(14,42))
self.add_arc('hand',(14,42),(6,36),radius_x=8,radius_y=6)
self.add_line('arm-outer',(6,36),(14,26))
self.add_arc('shoulder',(14,26),(20,24),radius_x=6)
self.add_contour('body','back','hip','leg-outer','foot-round','sole','leg-inner','belly','arm-inner','hand','arm-outer','shoulder',closed=True)
''')
put('curled-raccoon','SQUARE','Smoothed the outer body and striped tail, enlarged the muzzle space around the eye, and removed the crowded inner cheek hook.', '''
# Curled body and two tail stripes; asymmetry preserves the left-facing muzzle.
self.add_line('nose-top',(6,14),(10,14))
self.add_arc('forehead',(10,14),(24,6),radius_x=14,radius_y=8)
self.add_arc('back',(24,6),(42,24),radius_x=18)
self.add_arc('tail-outer',(42,24),(24,42),radius_x=18)
self.add_line('tail-base',(24,42),(14,42))
self.add_arc('tail-round',(14,42),(6,34),radius_x=8)
self.add_line('tail-tip-rise',(6,34),(6,28))
self.add_line('tail-tip',(6,28),(10,28))
self.add_line('tail-inner-left',(10,28),(16,32))
self.add_line('tail-inner-mid',(16,32),(24,34))
self.add_arc('tail-inner-turn',(24,34),(34,24),radius_x=10,sweep=False)
self.add_contour('outline','nose-top','forehead','back','tail-outer','tail-base','tail-round','tail-tip-rise','tail-tip','tail-inner-left','tail-inner-mid','tail-inner-turn')
self.add_line('nose-front',(6,14),(6,19))
self.add_arc('muzzle',(6,19),(12,25),radius_x=6,sweep=False)
self.add_line('cheek',(12,25),(22,25))
self.add_contour('face','nose-front','muzzle','cheek')
self.relate('connect','face','outline')
self.add_line('ear',(24,6),(24,10))
self.relate('connect','ear','outline')
self.add_line('stripe-one',(14,42),(16,32))
self.add_line('stripe-two',(24,42),(24,34))
self.relate('connect','stripe-one','outline')
self.relate('connect','stripe-two','outline')
self.add_dot('eye',(18,16))
''')
put('pelican-on-water-v2','SQUARE','Rounded the head, smoothed the neck and wing, and replaced the joined scallops with a continuous gentle wave.', '''
# Circular head flows into a bent neck; two opposite half-ellipses form one wave.
self.add_arc('head-left',(20,14),(28,6),radius_x=8)
self.add_arc('head-right',(28,6),(36,14),radius_x=8)
self.add_arc('neck-back',(36,14),(30,24),radius_x=12)
self.add_line('wing-root',(30,24),(26,26))
self.add_arc('wing-upper',(26,26),(42,22),radius_x=16,radius_y=4,sweep=False)
self.add_arc('wing-lower',(42,22),(32,32),radius_x=10)
self.add_contour('outline','head-left','head-right','neck-back','wing-root','wing-upper','wing-lower')
self.add_line('bill-top',(6,14),(20,14))
self.add_arc('bill-pouch',(20,14),(6,14),radius_x=7,radius_y=6)
self.add_contour('pouch','bill-top','bill-pouch',closed=True)
self.add_line('neck-front',(20,14),(15,26))
self.add_arc('breast',(15,26),(17,32),radius_x=6,sweep=False)
self.add_contour('neck','neck-front','breast')
self.relate('connect','outline','pouch')
self.relate('connect','outline','neck')
self.relate('connect','pouch','neck')
self.add_arc('wave-up',(6,41),(24,41),radius_x=9,radius_y=1)
self.add_arc('wave-down',(24,41),(42,41),radius_x=9,radius_y=1,sweep=False)
self.add_contour('water','wave-up','wave-down')
''')
put('castle-tower-with-pennant-v2','VRECT_L','Rebuilt two equally wide battlements with eight-unit clearances; a taller layout gives the flag and arched doorway room.', '''
# Two equal battlements, a centred door, and an intrinsic flag on a shared pole.
left,right,inner_left,inner_right=8,40,16,32
self.add_polyline('outline',(left,44),(left,20),(inner_left,20),(inner_left,28),(24,28),(inner_right,28),(inner_right,20),(right,20),(right,44),(inner_right,44),(inner_left,44),closed=True)
self.add_polyline('flag',(24,28),(24,12),(24,4),(40,4),(36,8),(40,12),(24,12))
self.relate('connect','flag','outline')
self.add_arc('door',(inner_left,44),(inner_right,44),radius_x=8)
self.relate('connect','door','outline')
''')
put('sheep-jumping-fence','SQUARE','Rebuilt the fence as two upright posts and one level rail, with clear air beneath the jumping sheep.', '''
# Fleece lobes share clean joins; the separate fence owns two equal posts and one rail.
self.add_arc('wool-top',(16,12),(28,12),radius_x=6)
self.add_arc('wool-shoulder',(28,12),(40,16),radius_x=8)
self.add_arc('wool-rump',(40,16),(34,22),radius_x=6)
self.add_arc('wool-base',(34,22),(22,22),radius_x=6,radius_y=3)
self.add_arc('wool-left',(22,22),(14,22),radius_x=4,radius_y=3)
self.add_line('wool-neck',(14,22),(16,12))
self.add_contour('fleece','wool-top','wool-shoulder','wool-rump','wool-base','wool-left','wool-neck',closed=True)
self.add_line('head-top',(16,12),(12,12))
self.add_arc('muzzle',(12,12),(12,22),radius_x=6,radius_y=5,sweep=False)
self.add_line('jaw',(12,22),(14,22))
self.add_contour('head','head-top','muzzle','jaw')
self.add_line('front-hoof',(14,22),(8,28))
self.add_line('rear-hoof',(34,22),(40,28))
self.relate('connect','head','fleece')
self.relate('connect','head','front-hoof')
self.relate('connect','fleece','front-hoof')
self.relate('connect','fleece','rear-hoof')
for name,x in (('post-left',16),('post-right',32)):
    self.add_polyline(name,(x,34),(x,38),(x,42))
    self.relate('connect',name,'rail')
self.add_polyline('rail',(6,38),(16,38),(32,38),(42,38))
''')
put('sea-lion','SQUARE','Rebuilt the muzzle with a clear mouth notch and room around the eye, while smoothing the head and rear flipper.', '''
# Left-facing head with a deliberate mouth notch; body and flippers form one contour.
self.add_arc('head-back',(16,6),(28,16),radius_x=12,radius_y=10)
self.add_line('neck-back',(28,16),(28,22))
self.add_line('back-start',(28,22),(30,22))
self.add_arc('back',(30,22),(42,34),radius_x=12)
self.add_line('rear-edge',(42,34),(42,38))
self.add_arc('rear-tip',(42,38),(38,42),radius_x=4)
self.add_line('rear-base',(38,42),(34,42))
self.add_line('rear-inner',(34,42),(36,34))
self.add_line('rear-join',(36,34),(30,32))
self.add_arc('belly',(30,32),(24,34),radius_x=12,radius_y=6)
self.add_line('front-flipper',(24,34),(28,42))
self.add_arc('front-flipper-base',(28,42),(16,38),radius_x=12,radius_y=4)
self.add_line('chest-base',(16,38),(10,40))
self.add_line('front-foot',(10,40),(6,38))
self.add_line('chest-lower',(6,38),(10,30))
self.add_arc('chest-upper',(10,30),(8,24),radius_x=14)
self.add_line('jaw',(8,24),(6,18))
self.add_line('mouth-lower',(6,18),(10,16))
self.add_line('mouth-upper',(10,16),(6,14))
self.add_arc('forehead',(6,14),(16,6),radius_x=10,radius_y=8)
self.add_contour('body','head-back','neck-back','back-start','back','rear-edge','rear-tip','rear-base','rear-inner','rear-join','belly','front-flipper','front-flipper-base','chest-base','front-foot','chest-lower','chest-upper','jaw','mouth-lower','mouth-upper','forehead',closed=True)
self.add_line('flipper-mark',(16,30),(16,38))
self.relate('connect','flipper-mark','body')
self.add_dot('eye',(19,15))
''')
# Keep the Pisa geometry exactly as reviewed; only its keyshape assignment was wrong.
pisa=next(m for m in revs if m['original']=='leaning-tower-of-pisa')
pisa_tree=ast.parse((ROOT/pisa['previous_file']).read_text())
pisa_build=next(x for x in ast.walk(pisa_tree) if isinstance(x,ast.FunctionDef) and x.name=='build')
codes['leaning-tower-of-pisa']='\n'.join(ast.unparse(x) for x in pisa_build.body)
notes['leaning-tower-of-pisa']='Kept the reviewed drawing unchanged and selected the square keyshape matching its actual bounds.'
codes['paw-print-v2']=codes['paw-print-v2'].replace("self.add_line('pad-notch-right',(28,42),(24,40))", "self.add_arc('pad-notch-right',(28,42),(24,42),radius_x=6,sweep=False)").replace("self.add_line('pad-notch-left',(24,40),(20,42))", "self.add_arc('pad-notch-left',(24,42),(20,42),radius_x=6,sweep=False)")
codes['crawling-baby']=codes['crawling-baby'].replace("(6,12),(18,12),radius_x=6", "(7,11),(17,11),radius_x=5").replace("(18,12),(6,12),radius_x=6", "(17,11),(7,11),radius_x=5")
for m in revs:
 p=ROOT/m['file'];t=ast.parse(p.read_text());c=next(x for x in t.body if isinstance(x,ast.ClassDef))
 for x in c.body:
  if isinstance(x,ast.FunctionDef) and x.name=='build':x.body=ast.parse(codes[m['original']]).body
  if isinstance(x,ast.Assign) and any(isinstance(a,ast.Name) and a.id=='keyshape' for a in x.targets):x.value=ast.parse('Keyshape.'+keys[m['original']],mode='eval').body
 ast.fix_missing_locations(t);p.write_text('# Review revision; previous candidates preserved.\n'+ast.unparse(t)+'\n')
(W/'revision-2-notes.json').write_text(json.dumps(notes,indent=2))
print('Wrote',len(revs),'review revisions')
