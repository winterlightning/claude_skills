from pathlib import Path
import json,sys,textwrap
ROOT=Path(__file__).resolve().parent
REPO=Path.cwd();sys.path.insert(0,str(REPO))
items=json.loads((ROOT/'items.json').read_text())
# Every source identity is preserved in the per-icon module and metadata before drawing.
SOURCE_ICON_ID=[x['source_uuid'] for x in items]
SOURCE_PATH=[x['reference'] for x in items]
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
# Each definition is a fresh visual reconstruction, not traced source coordinates.
designs=[]
def add(key,wrong,change,ref,body):designs.append(dict(keyshape=key,wrong=wrong,change=change,lucide=ref,body=textwrap.dedent(body)))
add('SQUARE','The straight roadside strokes lost the intersection corners, and the car was too small.','Restored branching intersection edges, paired sensor waves, and a larger rounded car.','car-front: rounded front body and tapered windscreen.', '''
self.rect('body',14,27,20,11,3)
self.add_polyline('roof',(16,27),(19,19),(29,19),(32,27))
self.relate('connect','roof','body')
for x in [18,30]:
 self.add_line('tire'+str(x),(x,38),(x,41));self.relate('connect','tire'+str(x),'body')
for side in [-1,1]:
 def p(x,y):return (24+side*x,y)
 s=str(side)
 self.add_polyline('road'+s,p(18,42),p(14,23),p(18,23))
 self.add_bezier('wave-in'+s,p(7,8),(p(10,9),p(12,11),p(12,14)))
 self.add_bezier('wave-out'+s,p(9,2),(p(16,3),p(20,8),p(20,14)))
''')
add('SQUARE','The incline disappeared and the angular vehicle read as a tilted block.','Added an explicit sloped road beneath a recognizable side-view car with two round wheels.','car: coherent roof, hood, wheel arrangement.', '''
self.add_polyline('ramp',(4,44),(44,24))
self.add_bezier('body',(9,31),((4,32),(3,29),(4,25)),((5,23),(7,22),(9,21)))
self.add_polyline('roof',(9,21),(10,13),(24,6),(32,11))
self.add_bezier('hood',(32,11),((36,8),(40,9),(42,13)),((44,17),(42,19),(39,20)))
self.add_line('sill',(17,27),(29,21))
self.circle('rear-wheel',13,29,4)
self.circle('front-wheel',34,19,4)
self.add_line('window-base',(9,21),(32,11))
self.relate('connect','body','roof');self.relate('connect','roof','hood');self.relate('connect','roof','window-base')
''')
add('VRECT_L','Road markings became a dot and short diagonal fragments; the car had no lamps.','Restored converging road edges, a dashed center line, and a rounded front car with lamps.','car-front: rounded bumper and windscreen.', '''
self.rect('body',8,16,32,14,3)
self.add_polyline('roof',(11,16),(16,4),(32,4),(37,16));self.relate('connect','roof','body')
for x in [14,34]:
 self.add_dot('lamp'+str(x),(x,23));self.add_line('tire'+str(x),(x,30),(x,34));self.relate('connect','tire'+str(x),'body')
self.add_line('road-left',(13,37),(8,44));self.add_line('road-right',(35,37),(40,44))
self.add_line('dash1',(24,36),(24,38));self.add_line('dash2',(24,43),(24,44))
''')
add('HRECT_L','The frame was compressed into a scooter-like shape and cargo dominated the bicycle.','Restored full-size wheels and a triangular bicycle frame beneath a compact rear cargo box.','bike: equal circular wheels; car: open connected silhouette.', '''
self.circle('rear',12,32,8);self.circle('front',36,32,8)
self.rect('cargo',4,8,16,12,2)
self.add_polyline('frame',(12,32),(24,32),(32,20),(18,20),(12,32))
self.add_polyline('fork',(36,32),(29,8),(25,8))
self.add_line('seat-post',(24,32),(20,20))
self.relate('connect','frame','rear');self.relate('connect','fork','front');self.relate('connect','frame','cargo');self.relate('connect','seat-post','frame')
''')
add('SQUARE','Two bare dots did not identify seated occupants.','Restored two outlined heads and paired shoulder curves behind the windscreen, plus lamps and tires.','car-front and human_ref/user.svg: rounded body and small repeated busts.', '''
self.rect('body',6,27,36,12,3)
self.add_polyline('roof',(9,27),(14,6),(34,6),(39,27));self.relate('connect','roof','body')
for x in [18,30]:
 self.circle('head'+str(x),x,15,3)
 self.add_bezier('shoulders'+str(x),(x-5,26),((x-5,23),(x+5,23),(x+5,26)))
 self.add_dot('lamp'+str(x),(x-5 if x==18 else x+5,33))
for x in [12,36]:
 self.add_line('tire'+str(x),(x,39),(x,42));self.relate('connect','tire'+str(x),'body')
''')
add('SQUARE','The requested wash strokes were present in the displayed version, but the solid-looking bumper weakened the car.','Kept exactly three diagonal wash strokes and rebuilt the car with an open bumper and distinct lamps.','car-front: balanced front-view enclosure.', '''
for i in range(3):self.add_line('wash'+str(i),(13+10*i,6),(10+10*i,12))
self.rect('body',6,28,36,11,3)
self.add_polyline('roof',(10,28),(15,20),(33,20),(38,28));self.relate('connect','roof','body')
for x in [13,35]:
 self.add_dot('lamp'+str(x),(x,33));self.add_line('tire'+str(x),(x,39),(x,42));self.relate('connect','tire'+str(x),'body')
''')
add('SQUARE','The band looked like a ball with two dots rather than a wearable display.','Reconstructed the closed perspective strap, front display edges, and two short horizontal display marks.','watch: distinguish strap from watch face with coherent contours.', '''
self.circle('band',24,24,18)
self.add_bezier('front-edge',(29,6),((17,12),(17,36),(29,42)))
self.add_bezier('inner-edge',(25,10),((37,19),(37,29),(25,38)))
self.add_line('display-top',(8,16),(21,16));self.add_line('display-bottom',(8,32),(21,32))
self.add_line('mark1',(12,22),(15,22));self.add_line('mark2',(12,27),(15,27))
''')
add('VRECT_M','The heavy U-shaped body and oversized triangular bell obscured the saxophone.','Slimmed the long body and retained a curved lower bow, flared upward bell, mouthpiece, and two keys.','No direct useful saxophone match; smooth arc and tangent principles used.', '''
self.add_polyline('mouthpiece',(10,4),(16,4))
self.add_bezier('outer',(16,4),((23,4),(25,9),(25,17)))
self.add_line('inner-shaft',(16,4),(16,31))
self.add_bezier('bow-outer',(16,31),((16,48),(35,48),(35,31)))
self.add_polyline('bell',(35,31),(38,25),(29,17),(29,30))
self.add_bezier('bow-inner',(29,30),((29,36),(25,36),(25,30)))
self.add_line('shaft',(25,30),(25,17))
for y in [17,24]:self.add_line('key'+str(y),(22,y),(27,y))
self.relate('connect','outer','mouthpiece');self.relate('connect','outer','inner-shaft');self.relate('connect','inner-shaft','bow-outer');self.relate('connect','bow-outer','bell');self.relate('connect','bell','bow-inner');self.relate('connect','bow-inner','shaft');self.relate('connect','shaft','outer')
''')
add('HRECT_M','The large square case and two enclosed cells no longer read as a full horizontal battery.','Made the case horizontal with three evenly spaced full-charge bars and a clear right terminal.','battery-full: rounded horizontal housing and repeated vertical charge bars.', '''
self.rect('case',4,10,32,28,3)
for i in range(3):self.add_line('charge'+str(i),(12+i*8,18),(12+i*8,30))
self.add_line('terminal',(44,20),(44,28))
''')
add('CIRCLE','The fork had only two very short tines and read as a Y.','Restored a three-tine fork and a separate curved knife inside the circular dining symbol.','utensils: three parallel tines, rounded bowl, long stems.', '''
self.circle('ring',24,24,20)
self.add_bezier('fork',(11,14),((11,14),(11,22),(11,22)),((11,28),(23,28),(23,22)),((23,22),(23,14),(23,14)))
self.add_line('stem',(17,14),(17,35))
self.add_line('knife-back',(31,13),(31,35))
self.add_bezier('blade',(31,13),((36,17),(37,22),(36,26)))
self.add_line('blade-base',(36,26),(31,26))
self.relate('connect','fork','stem');self.relate('connect','blade','knife-back');self.relate('connect','blade','blade-base');self.relate('connect','blade-base','knife-back')
''')
add('VRECT_L','The angular crown merged with the head and the face lacked recognizable elephant features.','Restored broad elephant ears, rounded forehead lobes, separate crown, eyes, and a curved long trunk.','No useful deity match; paired geometry and smooth contour principles.', '''
self.add_bezier('crown',(15,14),((13,10),(18,5),(24,4)),((30,5),(35,10),(33,14)))
self.add_bezier('face',(21,29),((12,27),(12,13),(19,13)),((22,13),(23,15),(24,15)),((25,15),(26,13),(29,13)),((37,13),(35,27),(30,29)),((27,31),(27,35),(28,36)),((30,37),(36,34),(36,38)),((36,42),(22,48),(21,39)),((21,36),(21,32),(21,29)))
for side in [-1,1]:
 def p(x,y):return (24+side*x,y)
 self.add_bezier('ear'+str(side),p(10,15),(p(22,8),p(19,22),p(17,26)),(p(15,29),p(12,30),p(8,30)))
self.add_dot('eye-left',(20,22));self.add_dot('eye-right',(28,22))
''')
add('CIRCLE','The earth looked like an abstract swirl and the outer ring overwhelmed the small globe.','Enlarged the earth and node while keeping a clean open surrounding ring and readable continent strokes.','globe: circular global silhouette; source continent arrangement preserved.', '''
self.add_bezier('orbit',(9,38),((0,29),(3,8),(17,5)),((32,0),(44,12),(44,24)),((44,30),(42,35),(39,38)))
self.circle('earth',24,20,11)
self.add_bezier('land-upper',(25,9),((18,17),(28,14),(27,21)),((27,26),(31,21),(35,20)))
self.add_bezier('land-lower',(13,20),((21,18),(18,27),(23,31)))
self.circle('node',24,39,5)
''')
# Hand construction uses coherent rounded finger/palm silhouettes, with open wrists.
add('SQUARE','The square merged into a P-shaped hand and had only one pin.','Separated a four-sided chip with multiple pins from a recognizable index-thumb pinch and open wrist.','hand-grab: rounded finger turns and coherent palm; human_ref/user.svg reviewed.', '''
self.rect('chip',6,13,11,11,2)
for i in range(2):
 t=9+i*5
 for n,a,b in [('t',(t,10),(t,13)),('b',(t,24),(t,27)),('l',(3,16+i*5),(6,16+i*5)),('r',(17,16+i*5),(20,16+i*5))]:self.add_line(n+str(i),a,b)
self.add_bezier('hand',(42,42),((42,34),(42,26),(40,22)),((36,17),(29,8),(24,6)),((22,5),(20,6),(20,8)),((20,11),(27,10),(30,14)),((35,19),(34,25),(31,27)),((26,32),(22,26),(20,24)),((17,21),(14,23),(16,27)),((20,33),(28,36),(28,42)))
''')
add('SQUARE','The hand had become a hook detached from a generic gem.','Restored the rounded index finger and thumb pinch, open wrist, and flat-topped diamond with a facet line.','hand-grab and gem: rounded finger return and flat-topped jewel.', '''
self.add_polyline('gem',(4,13),(8,6),(18,6),(23,13),(13,24),(4,13))
self.add_line('facet',(4,13),(23,13));self.relate('connect','facet','gem')
self.add_bezier('hand',(42,42),((42,34),(43,20),(38,13)),((35,9),(31,8),(28,8)),((24,8),(24,13),(28,13)),((34,13),(36,19),(34,24)),((32,31),(26,32),(22,27)),((18,21),(13,25),(17,30)),((21,35),(25,37),(25,42)))
''')
add('SQUARE','The lower foot looked like a shoe or tray and the hand was a floating curved bar.','Restored the ankle, heel, instep and toes below a coherent extended finger and thumb.','hand-helping: finger and palm silhouette; no useful foot match.', '''
self.add_polyline('ankle',(6,29),(6,39))
self.add_bezier('foot',(6,39),((6,42),(8,42),(12,42)),((19,42),(27,42),(33,42)),((38,42),(38,38),(33,36)),((24,32),(18,31),(18,27)))
self.add_polyline('ankle-top',(18,27),(18,23),(6,23),(6,29));self.relate('connect','ankle','foot');self.relate('connect','foot','ankle-top');self.relate('connect','ankle','ankle-top')
self.add_bezier('hand',(42,6),((34,6),(29,5),(27,7)),((23,10),(19,13),(17,15)),((13,18),(15,22),(19,20)),((23,18),(26,16),(29,15)))
self.add_bezier('thumb',(25,17),((27,22),(34,22),(42,15)))
''')
add('SQUARE','The capsule and two hands were reduced to unrelated loops and strokes.','Added a capsule dividing seam and two recognizable opposing hands with a visible passing gesture.','hand-helping: open palm and distinct thumb.', '''
self.rect('pill',9,17,23,11,5)
self.add_line('seam',(20,17),(20,28));self.relate('connect','seam','pill')
self.add_polyline('upper-back',(42,6),(34,10),(25,10),(19,16))
self.add_bezier('upper-thumb',(42,17),((39,19),(36,22),(33,22)),((30,26),(28,27),(27,25)),((25,24),(28,20),(30,18)))
self.add_bezier('palm',(6,34),((12,34),(17,33),(20,37)),((25,37),(31,36),(33,38)),((35,39),(36,42),(36,42)))
self.add_line('palm-base',(6,42),(36,42));self.relate('connect','palm','palm-base')
''')
add('SQUARE','The finger was horizontal and merged into the bell knob, losing the pressing action.','Redrew a downward pointing bent finger over a separate plunger and domed service bell.','hand-grab: smooth fingertip; source downward pressing gesture retained.', '''
self.add_bezier('finger',(19,6),((21,9),(24,12),(25,14)),((23,17),(20,21),(20,22)),((19,26),(23,27),(25,24)),((29,20),(32,16),(34,13)),((34,17),(34,19),(37,19)),((40,19),(39,12),(40,6)))
self.add_line('button',(21,29),(29,29));self.add_line('plunger',(25,29),(25,33));self.relate('connect','button','plunger')
self.add_bezier('dome',(6,42),((6,30),(42,30),(42,42)))
self.add_line('base',(6,42),(42,42));self.relate('connect','base','dome')
''')
add('HRECT_L','The hand was angular and the evenly aligned seeds read like motion marks.','Restored a rounded releasing hand with cuff and staggered falling seeds beneath the fingertips.','hand-helping: smooth finger, thumb and wrist transitions.', '''
self.add_bezier('hand',(36,12),((30,11),(25,8),(22,8)),((19,8),(11,13),(6,16)),((2,18),(5,22),(8,21)),((12,19),(17,16),(21,16)),((16,20),(14,22),(17,24)),((20,26),(26,21),(29,22)),((32,23),(34,23),(36,23)))
self.add_polyline('cuff',(36,8),(44,8),(44,27),(36,27),(36,8))
self.add_line('seed1',(9,29),(9,32));self.add_line('seed2',(23,32),(25,35));self.add_line('seed3',(35,31),(34,34));self.add_line('seed4',(14,39),(17,40))
''')
add('SQUARE','Only two small holes remained, and the hand no longer visibly removed a pill from a multi-cell sheet.','Restored a blister sheet with five large circular cells and a thumb lifting the lower-right pill.','hand-grab: rounded fingertip; source repeated cell structure retained.', '''
self.add_bezier('tray',(13,33),((9,33),(6,34),(6,29)),((6,22),(6,13),(6,10)),((6,6),(8,6),(12,6)),((20,6),(31,6),(36,6)),((41,6),(42,8),(42,12)),((42,18),(42,25),(42,29)),((42,33),(39,33),(36,33)))
for x,y in [(14,15),(24,15),(34,15),(14,25),(24,25)]:self.circle('cell'+str(x)+'-'+str(y),x,y,3)
self.add_bezier('thumb',(22,35),((26,31),(29,27),(31,26)),((35,22),(39,27),(36,31)),((34,35),(31,39),(30,42)))
self.add_line('wrist',(18,33),(18,42))
''')
add('SQUARE','The tablet became a small square and the hand obscured the phone, losing the three-device composition.','Restored a tall tablet, separate phone, central screen corners and an upright tapping index finger.','hand-grab: rounded upright finger; watch: device enclosure separation.', '''
self.add_bezier('tablet',(15,39),((10,39),(6,40),(6,35)),((6,27),(6,15),(6,10)),((6,6),(8,6),(12,6)),((16,6),(21,6),(24,6)),((27,6),(27,8),(27,11)),((27,14),(27,16),(27,19)))
self.add_line('tablet-top',(6,13),(27,13))
self.rect('phone',34,6,10,17,2)
self.add_line('phone-bottom',(34,18),(44,18));self.relate('connect','phone','phone-bottom')
self.add_polyline('screen',(17,36),(17,24),(25,24))
self.add_bezier('touch',(26,42),((23,39),(20,36),(21,34)),((23,31),(26,36),(28,37)),((28,32),(28,29),(28,28)),((28,24),(34,24),(34,28)),((34,31),(34,33),(34,33)),((37,34),(42,35),(42,37)),((42,39),(41,41),(41,42)))
''')
assert len(designs)==20
for d,x in zip(designs,items):
 n=x['n'];run=Path('icon_set/work/primitive-make-ray')/x['source_uuid']/f'20260928T180129Z-fix-{n:02}-r1';run.mkdir(parents=True,exist_ok=False)
 x.update({k:v for k,v in d.items() if k!='body'});x['run']=str(run)
 (run/(x['icon_id']+'.metadata.json')).write_text(json.dumps({k:x[k] for k in ['concept','source_uuid','reference','feedback']},indent=2))
 (run/'comparison.md').write_text(f"Original and current compared before drawing.\n\nRejected: {d['wrong']}\n\nFeedback: {x['feedback']}\n\nRevision: {d['change']}\n\nConstruction: {d['lucide']}\n")
 module=run/(x['icon_id'].replace('-','_')+'_'+x['source_uuid'].replace('-','_')+'.py')
 head=f'''"""{x['concept']}.\nPlan: {d['change']}\nConstruction: {d['lucide']}\nKeyshape: {d['keyshape']}; semantic arrangement prioritized within 48px.\n"""\nfrom icon_set.model.icons.solo._base import Solo48\nfrom icon_set.model.keyshapes import Keyshape\nSOURCE_ICON_ID = {x['source_uuid']!r}\nSOURCE_PATH = {x['reference']!r}\nAUTHOR = "gpt-6"\n\nclass Drawing(Solo48):\n    icon_id = {x['icon_id']!r}\n    keyshape = Keyshape.{d['keyshape']}\n    semantic_role = "MAIN"\n    semantic_kind = "noun"\n    category = "objects"\n    aliases = ()\n    keywords = {tuple(x['concept'].split())!r}\n'''
 module.write_text(head+helper+'\n    def build(self):\n'+textwrap.indent(d['body'],'        '))
 x['module']=str(module)
(ROOT/'authored.json').write_text(json.dumps(items,indent=2))
print('Authored',len(items),'fresh runs')
