"""Author independent SOLO48 adaptations; reference coordinates are never read."""
import ast
import hashlib
import json
import pathlib
import sys
import textwrap

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from icon_set.scripts.create_variant import prepare_variant
from icon_set.model.icons.registry import factories

AUTHOR = 'gpt-6'
WORK = pathlib.Path(__file__).parent
SCOPE = json.loads((WORK / 'scope.json').read_text())
SOURCE_ICON_ID = tuple(row['uuid'] for row in SCOPE)
SOURCE_PATH = tuple(str(ROOT/'pictographic-primitives'/row['reference_path']) for row in SCOPE)

HELPERS = '''
        # Shared shape definitions: equal corner radii and exact attachment nodes.
        nodes = {}
        def l(n, a, b):
            self.add_line(n, a, b); nodes[n] = {a, b}
        def p(n, *pts, closed=False):
            self.add_polyline(n, *pts, closed=closed); nodes[n] = set(pts)
        def a(n, start, end, r, sweep=True, ry=None):
            self.add_arc(n, start, end, radius_x=r, radius_y=ry or r, sweep=sweep)
            nodes[n] = {start, end}
        def c(n, x, y, r):
            pts = [(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
            for j in range(4):
                self.add_arc(f'{n}-{j}', pts[j], pts[(j+1)%4], radius_x=r)
            self.add_contour(n, *[f'{n}-{j}' for j in range(4)], closed=True)
            nodes[n] = set(pts)
        def rr(n, x1,y1,x2,y2,r=2, top=(),right=(),bottom=(),left=()):
            # Clockwise edges are split at real branch attachments.
            if r == 0:
                pts=[(x1,y1)]+[(x,y1) for x in sorted(top)]+[(x2,y1)]+[(x2,y) for y in sorted(right)]+[(x2,y2)]+[(x,y2) for x in sorted(bottom,reverse=True)]+[(x1,y2)]+[(x1,y) for y in sorted(left,reverse=True)]
                p(n,*pts,closed=True)
                return
            corners=[((x1+r,y1),(x2-r,y1),(x2,y1+r)),
                     ((x2,y1+r),(x2,y2-r),(x2-r,y2)),
                     ((x2-r,y2),(x1+r,y2),(x1,y2-r)),
                     ((x1,y2-r),(x1,y1+r),(x1+r,y1))]
            cuts=[[(x,y1) for x in sorted(top)],[(x2,y) for y in sorted(right)],
                  [(x,y2) for x in sorted(bottom,reverse=True)],[(x1,y) for y in sorted(left,reverse=True)]]
            members=[]; allpts=set()
            for j,(start,end,nxt) in enumerate(corners):
                pts=[start]+[q for q in cuts[j] if q not in (start,end)]+[end]
                allpts.update(pts)
                for k,(v,w) in enumerate(zip(pts,pts[1:])):
                    if v==w: continue
                    part=f'{n}-e{j}-{k}'; self.add_line(part,v,w);members.append(part)
                part=f'{n}-c{j}'; self.add_arc(part,end,nxt,radius_x=r);members.append(part)
            self.add_contour(n,*members,closed=True);nodes[n]=allpts
        def dot(n,x,y):
            self.add_dot(n,(x,y));nodes[n]={(x,y)}
'''
END = '''
        # Only exact shared nodes declare physical contact; never proximity.
        names=list(nodes)
        for i,n in enumerate(names):
            for m in names[i+1:]:
                if nodes[n] & nodes[m]: self.relate('connect',n,m)
'''

# Each entry is an independently composed subject, not a transformed SVG.
SPECS = {}
def spec(n, key, code, reduction='No defining feature omitted.', ref='panels-top-left'):
    SPECS[n]=(key,textwrap.dedent(code).strip(),reduction,ref)

spec(17,'VRECT_L','''
rr('board',8,12,40,32,2,top=(20,28),bottom=(16,24,32))
p('clip',(20,12),(20,4),(28,4),(28,12))
l('leg-left',(16,32),(12,44));l('leg-right',(32,32),(36,44));l('rear-leg',(24,32),(24,44))
''','Lower support rail merges with the board lower edge; retain clamp and three legs.','presentation')
spec(78,'VRECT_L','''
l('top',(8,4),(20,4));p('fold',(28,4),(40,16))
l('right',(40,24),(40,36));p('bottom-right',(40,44),(28,44))
l('bottom-left',(20,44),(8,44));l('left-low',(8,36),(8,24));l('left-high',(8,16),(8,12))
''',ref='files')
spec(83,'HRECT_L','''
rr('front',4,20,32,40,3)
p('rear',(12,12),(12,8),(34,8),(44,18),(44,30),(40,30))
''',ref='files')
spec(96,'HRECT_L','''
p('tab',(4,16),(4,8),(16,8),(24,16),(36,16))
l('right',(44,16),(44,28));p('bottom',(44,36),(44,40),(12,40))
l('left',(4,24),(4,36))
''',ref='folder')
spec(101,'HRECT_L','''
p('rear',(4,28),(4,8),(16,8),(24,16),(40,16))
p('front',(12,24),(20,24),(28,32),(44,32),(44,40),(12,40),closed=True)
''',ref='folder')
spec(152,'SQUARE','''
rr('frame',6,6,42,42)
for row in range(2):
 for col in range(2):
  x=14+col*12;y=14+row*12;p(f'cell-{row}-{col}',(x,y),(x+8,y),(x+8,y+8),(x,y+8),closed=True)
''',ref='panels-top-left')

def calendar(n, marks):
 spec(n,'VRECT_L',"""
rr('page',8,12,40,44,3,top=(16,32),left=(20,),right=(20,))
l('binding-left',(16,4),(16,12));l('binding-right',(32,4),(32,12))
l('header',(8,20),(40,20))
"""+marks,ref='calendar-days')
calendar(160,"for j,(x,y) in enumerate([(24,28),(32,28),(16,36),(24,36),(32,36)]): dot(f'date-{j}',x,y)")
calendar(180,"for j,x in enumerate([16,24,32]): dot(f'date-{j}',x,32)")
calendar(521,"for j,x in enumerate([19,29]): p(f'col-{j}',(x,28),(x,32),(x,36))\nfor j,y in enumerate([28,36]): p(f'row-{j}',(16,y),(19,y),(29,y),(32,y))")
calendar(524,"for j,(x,y) in enumerate([(16,28),(24,28),(32,28),(16,36),(24,36)]): p(f'date-{j}',(x-2,y-2),(x+2,y-2),(x+2,y+2),(x-2,y+2),closed=True)")
spec(161,'CIRCLE',"c('ring',24,24,20)\nc('key-head',24,20,4)\nl('slot',(24,24),(24,32))",'Keyhole lower slot becomes one open stroke to retain a readable round head.','scan')
spec(170,'HRECT_L',"rr('frame',4,8,44,40)\nrr('row',12,20,36,28,2,top=(20,28),bottom=(20,28))\nfor j,x in enumerate([20,28]): l(f'cell-{j}',(x,20),(x,28))")
spec(171,'SQUARE',"rr('frame',6,6,42,42)\nfor j,(x,y) in enumerate([(20,16),(28,32)]):\n c(f'knob-{j}',x,y,2)\n l(f'track-left-{j}',(14,y),(x-2,y));l(f'track-right-{j}',(x+2,y),(34,y))",ref='sliders-horizontal')
spec(172,'SQUARE',"rr('frame',6,6,42,42)\nfor j,y in enumerate([14,30]):\n rr(f'toggle-{j}',14,y,34,y+8,4)\n dot(f'knob-{j}',18 if j==0 else 30,y+4)",ref='toggle-left')
spec(176,'HRECT_L',"for j,pts in enumerate([[(4,16),(4,8),(12,8)],[(36,8),(44,8),(44,16)],[(44,32),(44,40),(36,40)],[(12,40),(4,40),(4,32)]]): p(f'corner-{j}',*pts)\nrr('selection',12,18,36,30,3)",ref='scan')
spec(179,'SQUARE',"rr('frame',6,6,42,42)\nc('knob',20,18,3)\nl('track-left',(14,18),(17,18));l('track-right',(23,18),(34,18))",ref='sliders-horizontal')
spec(225,'SQUARE',"rr('frame',6,6,42,42)\nc('focus',24,24,3)\np('left',(16,14),(14,18),(14,30),(16,34))\np('right',(32,14),(34,18),(34,30),(32,34))",ref='scan')
spec(248,'SQUARE',"rr('chip',14,14,34,34,2,top=(18,30),bottom=(18,30),left=(18,30),right=(18,30))\nfor j,t in enumerate([18,30]):\n l(f'top-{j}',(t,6),(t,14));l(f'bottom-{j}',(t,34),(t,42));l(f'left-{j}',(6,t),(14,t));l(f'right-{j}',(34,t),(42,t))\nc('node',24,24,2)\nl('trace-low',(18,34),(22,24));l('trace-high',(26,24),(30,20))",ref='cpu')
spec(328,'SQUARE',"p('outer',(6,6),(42,6),(42,34),(34,34),(34,42),(24,34),(6,34),closed=True)\np('inner',(15,15),(33,15),(33,25),(26,25),(26,29),(22,25),(15,25),closed=True)",ref='messages-square')
spec(432,'VRECT_L',"p('phone',(24,4),(8,4),(8,44),(24,44),(24,36))\nrr('upper',16,12,32,20,2)\nrr('lower',16,28,32,36,2)\nfor j,y in enumerate([12,24,36]): dot(f'dismiss-{j}',40,y)",ref='smartphone')
spec(436,'HRECT_L',"p('window',(4,32),(4,8),(44,8),(44,32),(4,32))\nfor j,x in enumerate([12,24,36]):\n p(f'flow-{j}',(x,40),(x,32),(x,16));p(f'arrow-{j}',(x-4,20),(x,16),(x+4,20))",'Smooth airflow simplified to three rising stems; preserve direction and rear-window enclosure.','presentation')
spec(438,'VRECT_L',"rr('phone',8,4,40,44,4)\nl('speaker',(20,12),(28,12))\nfor j,y in enumerate([20,32]):\n rr(f'card-{j}',16,y,32,y+8,2)\n l(f'text-{j}',(20,y+4),(24,y+4))",ref='smartphone')
spec(439,'SQUARE',"for j,y in enumerate([6,30]):\n rr(f'card-{j}',6,y,42,y+12,2,left=(y+8,),right=(y+8,))\n l(f'header-{j}',(6,y+8),(42,y+8))")
spec(456,'SQUARE',"rr('frame',6,6,42,42)\nfor j,y in enumerate([14,30]):\n rr(f'row-{j}',14,y,34,y+8,2,top=(20,28),bottom=(20,28))\n for k,x in enumerate([20,28]): l(f'cell-{j}-{k}',(x,y),(x,y+8))")
spec(467,'SQUARE',"rr('front',6,6,34,34,3,left=(14,),right=(14,))\nl('front-header',(6,14),(34,14))\np('rear',(42,14),(42,42),(14,42))\nl('rear-header',(34,22),(42,22))",ref='panels-top-left')
spec(470,'VRECT_L',"rr('page',8,4,40,44,3)\nrr('header',16,12,32,20,2)\nl('text-top',(16,28),(32,28));l('text-low',(16,36),(28,36))",ref='files')
spec(471,'VRECT_L',"p('page',(8,4),(28,4),(40,16),(40,44),(8,44),closed=True)\np('image',(16,12),(24,12),(24,20),(16,20),closed=True)\nfor j,y in enumerate([28,36]): l(f'text-{j}',(16,y),(32-j*4,y))",'Three text lines reduce to two to preserve the image and folded corner at 48 px.','files')
spec(485,'HRECT_L',"rr('battery',4,8,36,32,3,right=(16,24),bottom=(20,))\np('terminal',(36,16),(44,16),(44,24),(36,24))\nl('cable',(20,32),(20,40))",ref='battery')
spec(488,'HRECT_L',"rr('battery',4,8,36,40,3,right=(16,32))\np('terminal',(36,16),(44,16),(44,32),(36,32))\nrr('level',12,16,28,32,2)",ref='battery')
spec(490,'VRECT_M',"rr('battery',10,12,38,44,3,top=(18,30))\np('terminal',(18,12),(18,4),(30,4),(30,12))\np('level',(18,28),(30,28),(30,36),(18,36),closed=True)",ref='battery')
spec(491,'HRECT_L',"rr('battery',4,8,36,40,3,left=(32,),right=(24,32),bottom=(28,))\np('terminal',(36,24),(44,24),(44,32),(36,32))\np('level',(4,32),(28,32),(28,24),(36,24))",ref='battery')
spec(502,'SQUARE',"p('letter',(18,18),(18,6),(42,6),(42,42),(34,42))\nrr('card',6,26,26,42,2)\ndot('portrait-small',14,34);l('small-text',(22,34),(22,34))\ndot('portrait-large',26,14);l('letter-text',(34,14),(34,22))",ref='files')
spec(515,'SQUARE',"rr('window',6,6,42,42,2,left=(18,),right=(18,),top=(),bottom=(18,))\np('header',(6,18),(18,18),(42,18));l('sidebar',(18,18),(18,42))\nfor j,x in enumerate([14,22,30]):dot(f'header-dot-{j}',x,10)\nfor j,y in enumerate([26,34]):\n dot(f'list-{j}',10,y);rr(f'content-{j}',26,y-2,34,y+6,2)")
spec(523,'HRECT_L',"p('roof',(4,20),(24,8),(44,20),(36,20),(12,20),closed=True)\nfor j,x in enumerate([12,36]):l(f'wall-{j}',(x,20),(x,40))\np('ground',(4,40),(12,40),(36,40),(44,40))",ref='presentation')
spec(528,'SQUARE',"rr('frame',6,6,42,42,2)\np('panes',(14,14),(24,14),(34,14),(34,24),(34,34),(24,34),(14,34),(14,24),closed=True)\np('vertical',(24,14),(24,24),(24,34));p('horizontal',(14,24),(24,24),(34,24));l('handle',(34,24),(42,24))")
spec(529,'HRECT_L',"rr('frame',4,8,44,40,2)\nfor j,y in enumerate([16,32]): l(f'vertical-{j}',(24,y),(24,y+0))\nfor j,x in enumerate([12,36]):l(f'horizontal-{j}',(x,24),(x,24))\ndot('cross',24,24)")
spec(533,'HRECT_L',"rr('center',16,8,32,40,3)\np('left',(4,16),(8,16),(8,32),(4,32));p('right',(44,16),(40,16),(40,32),(44,32))",ref='files')
spec(537,'SQUARE',"rr('board',6,6,42,30,3,bottom=(16,32))\np('left-leg',(16,30),(14,38),(12,42));p('right-leg',(32,30),(34,38),(36,42));l('brace',(14,38),(34,38))",ref='presentation')
spec(540,'SQUARE',"rr('frame',6,6,42,42,2,top=(24,),bottom=(24,),left=(24,),right=(24,))\nfor j,(v,w) in enumerate([((24,6),(24,14)),((24,34),(24,42)),((6,24),(14,24)),((34,24),(42,24))]):l(f'dash-{j}',v,w)\ndot('cross',24,24)")
spec(541,'HRECT_L',"l('top-rule',(4,8),(44,8))\np('table',(4,16),(4,40),(44,40),(44,16))\nfor j,(x,y) in enumerate([(24,24),(24,32),(12,28),(36,28)]):dot(f'divider-{j}',x,y)")
spec(544,'SQUARE',"p('page',(6,6),(26,6),(26,34),(18,42),(6,42),closed=True)\np('fold',(18,42),(18,34),(26,34))\nfor j,y in enumerate([16,28]):\n p(f'check-{j}',(12,y),(15,y+3),(20,y-2))\nrr('pen',34,6,42,34,3,bottom=(38,));l('nib',(38,34),(38,42))",'Check marks carry tasks; text strokes omitted to keep paper and pen distinct.','notebook-pen')
spec(548,'SQUARE',"p('raised',(6,16),(38,6),(42,14),(10,24),closed=True)\np('board',(6,24),(18,24),(30,24),(42,24),(42,42),(6,42),closed=True)\nl('rail',(6,32),(42,32))\nl('stripe-one',(18,24),(14,32));l('stripe-two',(30,24),(26,32))",ref='clapperboard')
spec(557,'SQUARE',"rr('frame',6,6,42,42,2,top=(24,),bottom=(24,),left=(30,),right=(18,))\np('center',(24,6),(24,18),(24,30),(24,42));l('left',(6,30),(24,30));l('right',(24,18),(42,18))")
spec(559,'SQUARE',"p('rear',(18,14),(18,6),(42,6),(42,30),(38,30))\nrr('monitor',6,22,30,34,2,left=(30,),right=(30,),bottom=(18,))\nl('bezel',(6,30),(30,30));l('stand',(18,34),(18,42));p('foot',(10,42),(18,42),(26,42))",ref='presentation')
spec(575,'SQUARE',"p('rear',(22,6),(30,6),(34,14),(42,14),(42,30))\np('middle',(14,14),(22,14),(26,22),(34,22),(34,38))\np('front',(6,22),(14,22),(18,30),(26,30),(26,42),(6,42),closed=True)",ref='folder')
spec(579,'SQUARE',"rr('frame',6,6,42,42,2,left=(18,30),right=(18,30))\nfor j,y in enumerate([18,30]):p(f'row-{j}',(6,y),(24,y),(42,y))\nl('middle',(24,18),(24,30))")
spec(580,'SQUARE',"p('upper',(6,6),(42,6),(42,18),(24,18),(16,24),(16,18),(6,18),closed=True)\np('lower',(6,30),(42,30),(42,42),(34,42),(26,36),(6,36),closed=True)",ref='messages-square')
spec(591,'SQUARE',"p('front',(18,18),(32,18),(42,28),(42,42),(18,42),closed=True)\np('top-left',(6,14),(6,6),(14,6));l('top-dash',(22,6),(30,6));l('left-dash',(6,22),(6,30));l('left-bottom',(6,38),(6,42))",ref='files')
spec(595,'SQUARE',"rr('frame',6,6,42,42,2,top=(12,18,24,30,36),bottom=(12,18,24,30,36))\nfor j,x in enumerate([12,18,24,30,36]):l(f'divider-{j}',(x,6),(x,42))")
spec(597,'VRECT_M',"rr('phone',10,4,38,44,4)\np('screen',(18,12),(30,12),(30,28),(18,28),closed=True)\ndot('home',24,36)",'Home circle becomes a stroke-wide dot for clear spacing.','smartphone')
spec(598,'VRECT_L',"rr('card',8,4,40,44,6)\nrr('inset',16,12,32,36,3)",ref='files')
spec(599,'SQUARE',"p('book',(6,6),(30,6),(30,14))\np('book-bottom',(6,6),(6,42),(30,42))\nfor j,y in enumerate([14,26,38]):l(f'binding-{j}',(6,y),(10,y))\np('pen',(18,34),(22,24),(36,10),(42,16),(28,30),closed=True)\np('sketch',(14,18),(18,14),(22,18))",'Small spiral and wave details reduce to a mountain sketch; retain binding and diagonal pencil.','notebook-pen')
spec(617,'VRECT_L',"rr('reader',8,4,40,44,4)\np('screen',(16,12),(32,12),(32,28),(16,28),closed=True)\nl('home',(20,36),(28,36))",ref='smartphone')
spec(641,'SQUARE',"rr('frame',6,6,42,42,2)\np('inner',(14,14),(24,14),(34,14),(34,24),(34,34),(24,34),(14,34),(14,24),closed=True)\np('center',(20,20),(28,20),(28,28),(20,28),closed=True)\nl('top',(24,14),(24,20));l('bottom',(24,28),(24,34));l('left',(14,24),(20,24));l('right',(28,24),(34,24))")
spec(651,'VRECT_L',"p('page',(8,4),(28,4),(40,16),(40,44),(8,44),closed=True)\np('fold-inset',(28,4),(28,16),(40,16))\np('inset',(28,16),(16,16),(16,36),(28,36),(28,16))",ref='files')
spec(653,'HRECT_L',"p('tablet',(28,8),(4,8),(4,40),(44,40),(44,28))\np('screen',(24,16),(12,16),(12,32),(32,32))\nc('drawing',20,24,2)\np('stylus',(28,24),(30,16),(40,8),(44,12),(36,22),closed=True)\nl('controls',(36,32),(44,32))",ref='notebook-pen')
spec(658,'VRECT_L',"rr('frame',8,4,40,44,4)\np('opening',(16,16),(32,16),(32,32),(16,32),closed=True)",ref='files')
spec(663,'VRECT_L',"p('rail',(8,4),(24,4),(40,4))\nl('hanger',(24,4),(24,16))\nrr('sign',12,16,36,44,3,top=(24,))",ref='presentation')
spec(674,'HRECT_L',"p('folder',(4,16),(4,8),(16,8),(16,16),(40,16))\na('tr',(40,16),(44,20),4)\nl('right',(44,20),(44,36));a('br',(44,36),(40,40),4)\nl('bottom',(40,40),(8,40));a('bl',(8,40),(4,36),4);l('left',(4,36),(4,16))",ref='folder')
spec(684,'SQUARE',"rr('frame',6,6,42,42,2,top=(24,),left=(22,32),right=(22,32))\np('row-1',(6,22),(24,22),(42,22));l('row-2',(6,32),(42,32));l('top-split',(24,6),(24,22))")
spec(685,'SQUARE',"rr('frame',6,6,42,42,2,left=(18,),right=(18,),bottom=(18,))\np('header',(6,18),(18,18),(42,18));l('sidebar',(18,18),(18,42))")
spec(693,'SQUARE',"rr('frame',6,6,42,42,2,top=(18,30),bottom=(18,30),left=(24,),right=(24,))\nfor j,x in enumerate([18,30]):p(f'column-{j}',(x,6),(x,24),(x,42))\np('row',(6,24),(18,24),(30,24),(42,24))")
spec(712,'CIRCLE',"c('ring',24,24,20)\np('up',(24,4),(40,36),(8,36),closed=True)\np('down',(24,44),(8,12),(40,12),closed=True)",ref='scan')
spec(718,'SQUARE',"rr('map',6,6,42,42,2)\np('upper',(14,14),(30,14),(14,30),closed=True)\np('lower',(34,18),(34,34),(18,34),closed=True)")
spec(719,'VRECT_L',"a('top-curl',(16,20),(16,4),8);p('top',(16,4),(32,4));a('top-right',(32,4),(32,20),8);l('top-rule',(32,20),(16,20))\np('paper',(16,4),(16,36));a('lower-left',(16,36),(24,44),8,sweep=False)\nl('bottom',(24,44),(32,44));a('bottom-curl',(32,44),(32,28),8,sweep=False);l('bottom-rule',(32,28),(24,28))\nl('text',(24,24),(32,24))",ref='scroll-text')
spec(739,'HRECT_L',"rr('window',4,8,44,40,2,top=(24,34),right=(16,24))\np('split',(24,8),(24,16),(24,24),(44,24));p('small-row',(24,16),(34,16),(44,16));p('small-col',(34,8),(34,16),(34,24))")

# Hands are intrinsic to these solo subjects; thumb and card meet at shared nodes.
spec(508,'VRECT_L',"p('paper',(8,4),(32,4),(32,28),(24,28),(24,36),(8,36),closed=True)\np('hand-back',(32,20),(40,28),(40,44))\np('thumb',(32,36),(24,28),(20,32),(24,40),(28,44))",ref='hand')
spec(169,'SQUARE',"p('paper',(6,34),(6,6),(34,6),(34,14))\np('hand',(18,26),(14,22),(18,18),(26,26),(22,18),(26,14),(38,26))\na('palm',(38,26),(26,42),12);p('lower',(26,42),(14,34),(18,30))",ref='hand')
spec(505,'SQUARE',"rr('card',18,6,42,30,3,bottom=(26,))\ndot('portrait',30,14);l('text',(26,22),(34,22))\np('palm',(26,30),(26,38),(22,42),(14,42),(6,24),(10,20),(18,30))",ref='hand')
spec(506,'HRECT_L',"p('card',(20,8),(44,8),(44,32),(20,32),(20,24))\np('thumb-top',(4,20),(12,16),(24,16));a('thumb-tip',(24,16),(24,24),4);p('thumb-low',(24,24),(16,24),(12,28))\np('palm',(4,36),(12,40),(28,40),(36,32))\nfor j,y in enumerate([16,24]):l(f'text-{j}',(34,y),(36,y))",ref='hand')
spec(532,'VRECT_L',"p('front',(16,4),(32,4),(32,28),(24,28))\np('rear',(40,12),(40,36),(32,36))\np('hand',(16,12),(8,24),(12,36),(12,44),(28,44),(28,36),(24,28),(24,20),(20,20),(16,28),(16,4))\nl('cuff',(12,36),(28,36))",ref='hand')

# Repair pass: give curved pairs margin, or use round-joined rectangular walls
# when the complete content budget requires an exact straight 8-unit interval.
def replace(n, old, new):
    k,code,notes,ref=SPECS[n]
    assert old in code,(n,old)
    SPECS[n]=(k,code.replace(old,new),notes,ref)
replace(83,'(12,12)','(12,11)')
for n in [160,180,521]:replace(n,"8,12,40,44,3","8,12,40,44,0")
replace(170,"rr('frame',4,8,44,40)","rr('frame',4,8,44,40,0)")
replace(171,'[(20,16),(28,32)]','[(20,17),(28,31)]')
replace(179,'(14,18)','(15,18)')
replace(328,"(26,29)","(26,26)")
replace(432,"16,12,32,20,2","17,13,31,21,2")
replace(432,"16,28,32,36,2","17,30,31,38,2")
spec(439,'VRECT_L',"for j,y in enumerate([4,28]):\n rr(f'card-{j}',8,y,40,y+16,2,left=(y+8,),right=(y+8,))\n l(f'header-{j}',(8,y+8),(40,y+8))")
replace(470,"8,4,40,44,3","8,4,40,44,0")
replace(488,"12,16,28,32,2","13,17,27,31,2")
replace(490,"(18,28),(30,28),(30,36),(18,36)","(19,27),(29,27),(29,35),(19,35)")
replace(505,"18,6,42,30,3","18,6,42,30,0")
replace(506,"(34,y),(36,y)","(36,y),(36,y)")
replace(529,"rr('frame',4,8,44,40,2)","rr('frame',4,8,44,40,0)")
replace(532,"(40,36),(32,36)","(40,36)")
spec(559,'SQUARE',"p('rear',(18,12),(18,6),(42,6),(42,30),(39,30))\nrr('monitor',6,22,30,34,2,bottom=(18,))\nl('stand',(18,34),(18,42));p('foot',(10,42),(18,42),(26,42))",'Lower bezel merges into the monitor outline; preserve rear projection screen and front stand.','presentation')
spec(580,'VRECT_L',"p('upper',(8,4),(40,4),(40,16),(24,16),(16,22),(16,16),(8,16),closed=True)\np('lower',(8,30),(40,30),(40,38),(32,38),(32,44),(24,38),(8,38),closed=True)",ref='messages-square')
replace(597,"10,4,38,44,4","10,4,38,44,0")
replace(598,"16,12,32,36,3","17,13,31,35,3")
replace(617,"8,4,40,44,4","8,4,40,44,0")
replace(658,"(16,16),(32,16),(32,32),(16,32)","(17,16),(31,16),(31,32),(17,32)")
replace(718,"(14,14),(30,14),(14,30)","(15,15),(27,15),(15,27)")
replace(718,"(34,18),(34,34),(18,34)","(33,21),(33,33),(21,33)")
replace(83,'(40,30)','(41,30)')
replace(170,"12,20,36,28,2","12,20,36,28,0")
replace(171,'(14,y)','(15,y)');replace(171,'(34,y)','(33,y)')
replace(179,'(34,18)','(33,18)')
replace(470,"16,12,32,20,2","16,12,32,20,0")
replace(432,"17,13,31,21,2","17,12,31,20,0");replace(432,"17,30,31,38,2","17,28,31,36,0")
spec(225,'HRECT_L',"rr('frame',4,8,44,40,2)\nc('focus',24,24,2)\na('left',(16,31),(16,17),3,ry=7)\na('right',(32,17),(32,31),3,ry=7)",ref='scan')
spec(595,'HRECT_L',"rr('frame',4,8,44,40,2,top=(12,20,28,36),bottom=(12,20,28,36))\nfor j,x in enumerate([12,20,28,36]):l(f'divider-{j}',(x,8),(x,40))",'Six source strips reduce to five equal panels to retain the striped-pattern subject with clear openings.')
spec(719,'VRECT_L',"a('upper-left',(12,12),(12,4),4);p('top',(12,4),(16,4),(36,4));a('upper-right',(36,4),(36,12),4);p('top-rule',(36,12),(32,12),(16,12))\np('left-edge',(16,4),(16,12),(16,40));a('lower-left',(16,40),(20,44),4,sweep=False)\nl('bottom',(20,44),(36,44));a('lower-right',(36,44),(36,36),4,sweep=False);p('bottom-rule',(36,36),(32,36),(24,36));l('right-edge',(32,12),(32,36))\nfor j,y in enumerate([20,28]):l(f'text-{j}',(24,y),(24,y))",'Text reduces to two centered stroke-wide marks; retain opposite curled ends.','scroll-text')
spec(719,'SQUARE',"l('top',(36,6),(10,6));a('top-curl',(10,6),(6,10),4,sweep=False);p('tab',(6,10),(6,16),(14,16));l('left',(14,16),(14,36));a('foot',(14,36),(20,42),6,sweep=False);l('base',(20,42),(37,42));a('bottom-curl',(37,42),(37,32),5,sweep=False);l('bottom-top',(37,32),(26,32))\na('upper-inner',(10,6),(14,10),4);l('upper-wall',(14,10),(14,16));a('lower-inner',(26,32),(26,42),5);l('right',(36,6),(36,32));l('text-one',(23,15),(27,15));l('text-two',(23,23),(27,23))",'Mirror the existing scroll construction so the top curl is left and bottom curl right; retain both text lines.','scroll-text')
replace(506,"(24,16)","(20,16)");replace(506,"(24,24)","(20,24)");replace(506,"(36,y),(36,y)","(34,y),(36,y)")
replace(532,"(40,36)","(40,36),(32,36)");replace(532,"(28,44),(28,36)","(24,44),(24,36)");replace(532,"(12,36),(28,36)","(12,36),(24,36)")
replace(328,"(42,34),(34,34),(34,42),(24,34),(6,34)","(42,36),(34,36),(34,42),(24,36),(6,36)")
replace(328,"(33,25),(26,25),(26,26),(22,25),(15,25)","(33,23),(26,23),(26,27),(22,23),(15,23)")
replace(528,"rr('frame',6,6,42,42,2)","rr('frame',6,6,42,42,2,right=(24,))")
replace(248,"14,14,34,34,2","12,12,36,36,2")
replace(248,"(t,14)","(t,12)");replace(248,"(t,34)","(t,36)");replace(248,"(14,t)","(12,t)");replace(248,"(34,t)","(36,t)")
replace(248,"24,24,2","24,24,3");replace(248,"(18,34),(22,24)","(18,36),(24,27)");replace(248,"(26,24),(30,20)","(27,24),(32,20)")

spec(502,'SQUARE',"p('letter',(18,18),(18,6),(42,6),(42,42))\nrr('card',6,26,34,42,0)\ndot('portrait-small',14,34);l('small-text',(22,34),(26,34))\ndot('portrait-large',26,14);dot('letter-text',34,14)",'Circular identity marks reduce to dots; one short text mark per item remains.','files')
spec(544,'HRECT_L',"rr('page',4,8,28,40,0)\nfor j,y in enumerate([18,30]):p(f'check-{j}',(12,y),(14,y+2),(18,y-2))\nrr('pen',36,8,44,32,3,bottom=(40,));l('nib',(40,32),(40,40))",'Remove folded corner, pen clip, and task text to retain two legible check marks and the full pen silhouette.','notebook-pen')
spec(599,'SQUARE',"p('book',(30,6),(6,6),(6,14),(6,26),(6,34),(6,42),(14,42))\nfor j,y in enumerate([14,26,34]):l(f'binding-{j}',(6,y),(10,y))\np('pen',(22,40),(26,30),(36,20),(42,26),(32,36),closed=True)\np('sketch',(18,18),(22,14),(26,18))",'Retain one mountain sketch, three binding marks and diagonal pencil; omit the tiny curl and wave.','notebook-pen')
spec(169,'SQUARE',"p('paper',(6,34),(6,6),(34,6))\np('fingers',(22,30),(14,22),(20,16),(26,22),(30,16),(42,28))\na('palm',(42,28),(28,42),14)\np('lower',(28,42),(18,38),(14,34),(18,30))",'Reduce individual finger creases to two broad knuckles and a curved palm; keep the grip at lower right.','hand')

replace(169,"(30,16)","(32,14)")
spec(529,'HRECT_L',"rr('frame',4,8,44,40,2,top=(24,),bottom=(24,),left=(24,),right=(24,))\nfor j,(v,w) in enumerate([((24,8),(24,12)),((24,36),(24,40)),((4,24),(12,24)),((36,24),(44,24))]):l(f'dash-{j}',v,w)\np('cross-h',(20,24),(24,24),(28,24));p('cross-v',(24,20),(24,24),(24,28))")
replace(540,"dot('cross',24,24)","p('cross-h',(22,24),(24,24),(26,24));p('cross-v',(24,22),(24,24),(24,26))")
spec(541,'HRECT_L',"l('top-rule',(4,8),(44,8))\nrr('table',4,16,44,40,0,top=(24,),bottom=(24,),left=(28,),right=(28,))\nfor j,(v,w) in enumerate([((24,16),(24,20)),((24,36),(24,40)),((4,28),(12,28)),((36,28),(44,28))]):l(f'dash-{j}',v,w)\np('cross',(20,28),(24,28),(28,28))")

spec(505,'SQUARE',"rr('card',18,6,42,30,0,bottom=(26,))\ndot('portrait',30,14);l('text',(26,22),(34,22))\np('thumb',(18,30),(10,22),(6,26),(6,34));a('palm-left',(6,34),(14,42),8,sweep=False);l('palm-base',(14,42),(18,42));a('palm-right',(18,42),(26,34),8,sweep=False);l('support',(26,34),(26,30))",'Keep the upward palm and portrait mark; simplify the identity mark to a dot.','hand')
spec(508,'VRECT_L',"p('paper',(12,36),(8,36),(8,4),(32,4),(32,20),(32,24))\np('hand-back',(32,20),(40,28),(40,44))\nl('thumb-upper',(32,36),(24,28));a('thumb-tip',(24,28),(20,32),4,sweep=False);p('thumb-lower',(20,32),(24,40),(28,44))",'The document outline stops beneath the gripping hand to avoid doubled ink.','hand')
spec(532,'VRECT_L',"p('front',(16,20),(16,4),(32,4),(32,28),(24,28))\np('rear',(40,12),(40,36),(32,36))\np('hand',(8,20),(8,28),(8,36),(12,44),(24,44),(24,36),(24,28),(24,20))\na('thumb-tip',(24,20),(16,20),4,sweep=False);p('thumb-inner',(16,20),(16,28),(8,28));l('cuff',(8,36),(24,36))",'Keep two staggered cards and a cuffed gripping hand; omit individual finger creases.','hand')
spec(719,'VRECT_L',"a('upper-left',(12,12),(12,4),4);p('top',(12,4),(14,4),(36,4));a('upper-right',(36,4),(36,12),4);p('top-rule',(36,12),(34,12),(14,12))\np('left-edge',(14,4),(14,12),(14,40));a('lower-left',(14,40),(18,44),4,sweep=False)\nl('bottom',(18,44),(36,44));a('lower-right',(36,44),(36,36),4,sweep=False);p('bottom-rule',(36,36),(34,36),(22,36));l('right-edge',(34,12),(34,36))\nfor j,y in enumerate([20,28]):l(f'text-{j}',(22,y),(26,y))",'Rolls become open curled ends without a second overlapping seam; preserve two text lines.','scroll-text')

spec(508,'VRECT_L',"p('paper',(8,36),(8,4),(32,4),(32,20),(32,24))\np('hand-back',(32,20),(40,28),(40,44))\nl('thumb-upper',(33,36),(25,28));a('thumb-tip',(25,28),(19,36),5,sweep=False);l('thumb-lower',(19,36),(25,44))",'Document lower edge is occluded; thumb uses a broad semicircular fingertip with integer centre (22,32).','hand')
spec(719,'SQUARE',"l('top',(36,6),(10,6));a('top-curl',(10,6),(6,10),4,sweep=False);p('tab',(6,10),(6,16),(14,16));l('left',(14,16),(14,36));a('foot',(14,36),(20,42),6,sweep=False);p('base',(20,42),(26,42),(37,42));a('bottom-curl',(37,42),(37,32),5,sweep=False);l('bottom-top',(37,32),(26,32))\na('upper-inner',(10,6),(14,10),4);l('upper-wall',(14,10),(14,16));a('lower-inner',(26,32),(26,42),5);l('right',(36,6),(36,32));l('text-one',(23,15),(27,15));l('text-two',(23,23),(27,23))",'Mirror the existing scroll construction and explicitly split the lower roll at its seam attachment; retain both text lines.','scroll-text')

replace(508,"(33,36)","(32,36)")
spec(172,'VRECT_L',"rr('frame',8,4,40,44,0)\nrr('toggle-top',16,12,32,20,4);a('top-knob',(20,12),(20,20),4)\nrr('toggle-bottom',16,28,32,36,4);a('bottom-knob',(28,28),(28,36),4,sweep=False)",'Toggle knobs share their outer semicircle with the pill outline; retain the enclosing panel.','toggle-left')
spec(456,'SQUARE',"rr('frame',6,6,42,42,2)\nfor j,y in enumerate([12,28]):\n rr(f'row-{j}',12,y,36,y+8,0,top=(20,28),bottom=(20,28))\n for k,x in enumerate([20,28]):l(f'cell-{j}-{k}',(x,y),(x,y+8))",'Keep the six cells and enclosing frame; the tiny clipped internal corner is omitted.')

replace(508,"(32,24)","(32,23)")

def main():
    out=WORK/'candidates';out.mkdir(exist_ok=True)
    existing=factories();manifest=[]
    for row in SCOPE:
        n=row['number']
        if n!=row['canonical_source_number']:continue
        key,code,reduction,ref=SPECS[n]
        plan=row['authoring_plan']; ident=plan['subject']['icon_id']
        if ident in existing:ident += '-adapted-'+plan['source_uuid'][:8]
        parent=plan['existing_target']
        parent_family=existing[parent].family
        if existing[parent].keyshape.name != 'FREE':
            _,_,scaffold=prepare_variant(parent,parent_family,row['name'])
            ast.parse(scaffold)
        # A legacy FREE parent cannot transfer its per-ID exception. These
        # candidates use freshly authored standard keyshapes and no exception.
        desc=plan['subject']['description']
        header=f'''"""{desc}"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = {plan['source_uuid']!r}
SOURCE_PATH = {plan['reference_path']!r}
AUTHOR = {AUTHOR!r}
ADAPTED_FROM = {parent!r}
DESIGN_NOTES = {reduction!r}
CONSTRUCTION_REFERENCE = {'Lucide '+ref+' original and atomic-debug; coherent contours and shared attachment nodes.'!r}

class Drawing(Solo48):
    icon_id = {ident!r}
    variant_of = {parent if parent_family=='solo' else None!r}
    variant_label = {row['name']!r}
    keyshape = Keyshape.{key}
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = {row['category']!r}
    aliases = ()
    keywords = {tuple(plan['subject']['tags'])!r}
    def build(self):
        # Plan: {desc}
        # {key}: exact SOLO48 envelope; repeated parts share coordinates.
        # Reduction: {reduction}
'''
        source=header+HELPERS+'\n'+textwrap.indent(code,'        ')+'\n'+END
        filename=ident.replace('-','_')+'_'+plan['source_uuid'].replace('-','_')+'.py'
        path=out/filename;path.write_text(source)
        manifest.append({'number':n,'source_numbers':plan['source_numbers'],'icon_id':ident,'parent':parent,'parent_module':row['parent_module'],'parent_sha256':hashlib.sha256(pathlib.Path(row['parent_module']).read_bytes()).hexdigest(),'candidate':str(path.resolve()),'keyshape':key,'reduction':reduction,'lucide_reference':ref})
    (WORK/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(f'{len(manifest)} independent candidate modules authored.')

if __name__=='__main__':main()
