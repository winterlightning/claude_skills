"""Complete-source repairs, with explicit compact curves and shared text."""
from glyph_native import fit
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/sub-fidelity-repair-32/batch.json'
AUTHOR='gpt-6'
D={};DIMS={};GLYPHS={}
def plan(n,w,h,parts,body):
 D[n]=('SQUARE',parts,'Complete original',body);DIMS[n]=(w,h)
def ring(s):return f"circle(self,'frame',{s//2},{s//2},{s//2-2})\n"
def glyph(g,h,x,y,p='glyph',w=64):return fit(g,h,x,y,p,width=w)[0]+'\n'
def bubble(w,h):
 return f"""self.add_line('top',(6,2),({w-6},2))
self.add_arc('tr',({w-6},2),({w-2},6),radius_x=4)
self.add_line('right',({w-2},6),({w-2},{h-14}))
self.add_arc('br',({w-2},{h-14}),({w-6},{h-10}),radius_x=4)
self.add_polyline('tail',({w-6},{h-10}),(20,{h-10}),(10,{h-2}),(10,{h-10}),(6,{h-10}))
self.add_arc('bl',(6,{h-10}),(2,{h-14}),radius_x=4)
self.add_line('left',(2,{h-14}),(2,6))
self.add_arc('tl',(2,6),(6,2),radius_x=4)
self.add_contour('frame','top','tr','right','br','tail','bl','left','tl',closed=True)
"""
def oval_bubble(s):
 return f"""self.add_bezier('bubble-a',({s//4},{s-10}),(({-s//6},{s//2}),(2,2),({s//2},2)))
self.add_bezier('bubble-b',({s//2},2),(({s+8},2),({s+8},{s-8}),({s//3},{s-10})))
self.add_polyline('tail',({s//3},{s-10}),(4,{s-2}),({s//4},{s-10}))
self.add_contour('frame','bubble-a','bubble-b','tail',closed=True)
"""
plan(1,48,48,'Outer face circle, two sloping eyebrows, two eyes, and the open downturned mouth.',ring(48)+"""
self.add_line('brow-left',(12,15),(19,19));self.add_line('brow-right',(29,19),(36,15))
self.add_dot('eye-left',(17,25));self.add_dot('eye-right',(31,25))
self.add_bezier('frown',(16,36),((21,30),(27,30),(32,36)))
""")
plan(2,32,32,'Inner asymmetric bowl connected to the right return; complete open outer sweep.',"""
self.add_bezier('bowl-top',(22,17),((25,5),(9,7),(10,17)))
self.add_bezier('bowl-bottom',(10,17),((10,25),(18,24),(22,20)))
self.add_line('bowl-join',(22,20),(22,17))
self.add_contour('bowl','bowl-top','bowl-bottom','bowl-join',closed=True)
self.add_bezier('return',(22,20),((25,26),(30,23),(30,16)))
self.add_bezier('outer-top',(30,16),((30,-3),(2,-3),(2,16)))
self.add_bezier('outer-bottom',(2,16),((2,30),(13,32),(22,29)))
self.add_contour('outer','return','outer-top','outer-bottom')
self.relate('connect','bowl','outer')
""")
plan(3,64,64,'Speech bubble and tail enclosing the shared two-bar bitcoin glyph.',oval_bubble(64)+glyph('symbol-bitcoin',28,32,29));GLYPHS[3]=('symbol-bitcoin',)
plan(4,32,32,'Two circular bubbles with the original unequal sizes and diagonal tangency.',"""
circle(self,'large',13,19,11);circle(self,'small',26,6,4)
""")
plan(5,48,48,'Magnifying glass enclosing the complete three-face cube.',"""
circle(self,'glass',21,21,19)
self.add_line('handle',(35,35),(46,46));self.relate('connect','glass','handle')
self.add_polyline('cube',(12,16),(21,12),(30,16),(30,28),(21,32),(12,28),(12,16),closed=True)
self.add_polyline('faces',(12,16),(21,20),(30,16));self.add_line('vertical',(21,20),(21,32))
self.relate('connect','cube','faces');self.relate('connect','cube','vertical');self.relate('connect','faces','vertical')
""")
plan(6,48,48,'Interrupted document, all three original internal marks and rising diagonal slash.',"""
self.add_line('slash',(8,46),(40,2))
self.add_line('left',(12,40),(12,10));self.add_arc('tl',(12,10),(16,6),radius_x=4)
self.add_line('top',(16,6),(37,6));self.add_contour('upper','left','tl','top')
self.add_line('right',(40,14),(40,38));self.add_arc('br',(40,38),(36,42),radius_x=4)
self.add_line('bottom',(36,42),(18,42));self.add_contour('lower','right','br','bottom')
self.add_dot('dot',(19,12));self.add_line('mark',(34,24),(40,24));self.relate('connect','mark','lower')
self.add_line('short',(28,34),(33,34));self.relate('connect','slash','upper')
""")
plan(7,32,32,'Broken heart outline behind the original descending diagonal slash.',"""
self.add_line('slash',(2,2),(30,30))
self.add_bezier('heart-top',(5,5),((10,1),(12,5),(16,9)))
self.add_bezier('heart-right',(16,9),((26,-3),(39,12),(23,23)))
self.add_contour('heart-upper','heart-top','heart-right')
self.add_bezier('heart-left',(3,13),((3,17),(9,24),(16,29)))
self.add_line('end',(16,29),(17,28));self.add_contour('heart-lower','heart-left','end')
self.relate('connect','heart-upper','slash')
""")
plan(8,32,32,'SIM-card outline with clipped upper-right corner and divided inner capsule.',"""
self.add_polyline('edge',(8,2),(22,2),(28,8),(28,26))
self.add_arc('br',(28,26),(24,30),radius_x=4)
self.add_line('bottom',(24,30),(8,30));self.add_arc('bl',(8,30),(4,26),radius_x=4)
self.add_line('left',(4,26),(4,6));self.add_arc('tl',(4,6),(8,2),radius_x=4)
self.add_contour('frame','edge','br','bottom','bl','left','tl',closed=True)
box(self,'chip',11,10,21,23,2)
self.add_line('division',(11,17),(21,17));self.relate('connect','chip','division')
""")
for n in [9,10]:
 plan(n,32,32,'Original single crossbar, rounded open euro contour and flat central spine.',"""
self.add_bezier('upper',(26,4),((16,-2),(7,3),(6,13)))
self.add_line('spine',(6,13),(6,19))
self.add_bezier('lower',(6,19),((7,29),(17,34),(26,28)))
self.add_contour('curve','upper','spine','lower')
self.add_line('bar',(2,16),(19,16));self.relate('connect','curve','bar')
""")
plan(11,56,56,'Speech bubble with tail and uppercase HI using shared glyphs.',oval_bubble(56)+glyph('letter-h-uppercase',18,22,25,'h')+"self.add_line('i',(36,16),(36,34))\n");GLYPHS[11]=('letter-h-uppercase','letter-i-uppercase')
plan(12,48,40,'Rounded panel, two tracks and two offset circular knobs.',"""
box(self,'frame',2,2,46,38,4)
circle(self,'knob-top',18,12,4);circle(self,'knob-bottom',30,28,4)
self.add_line('tl',(8,12),(14,12));self.add_line('tr',(22,12),(40,12))
self.add_line('bl',(8,28),(26,28));self.add_line('br',(34,28),(40,28))
for p in ['tl','tr']:self.relate('connect',p,'knob-top')
for p in ['bl','br']:self.relate('connect',p,'knob-bottom')
""")
plan(13,48,32,'Rounded card containing horizontal key with two downward teeth.',"""
box(self,'frame',2,2,46,30,3);circle(self,'bow',33,16,6)
self.add_line('shaft',(10,16),(27,16));self.relate('connect','shaft','bow')
for i,x in enumerate([12,18]):
 self.add_line('tooth'+str(i),(x,16),(x,20));self.relate('connect','tooth'+str(i),'shaft')
""")
plan(14,32,32,'Wavy image border, detached dot and original asymmetric mountain.',"""
self.add_bezier('top',(3,3),((7,-1),(8,5),(12,3)))
self.add_bezier('top2',(12,3),((16,0),(17,5),(21,3)))
self.add_bezier('tr',(21,3),((30,-2),(33,4),(29,11)))
self.add_bezier('right',(29,11),((27,15),(33,17),(29,23)))
self.add_bezier('br',(29,23),((33,32),(26,32),(22,29)))
self.add_bezier('bottom',(22,29),((17,26),(17,33),(12,29)))
self.add_bezier('bl',(12,29),((5,33),(-1,30),(3,23)))
self.add_bezier('left',(3,23),((6,17),(0,18),(3,12)))
self.add_bezier('tl',(3,12),((6,8),(-1,7),(3,3)))
self.add_contour('frame','top','top2','tr','right','br','bottom','bl','left','tl',closed=True)
self.add_dot('sun',(10,11));self.add_polyline('mountain',(12,23),(21,13),(25,19))
""")
plan(15,48,48,'Circle, six-sided nanobot with central dot and two curved appendages.',ring(48)+"""
self.add_polyline('body',(16,15),(24,10),(32,15),(32,27),(24,32),(16,27),closed=True)
self.add_dot('core',(24,21))
self.add_bezier('leg-left',(16,27),((12,32),(14,35),(16,37)))
self.add_bezier('leg-right',(32,27),((36,32),(34,35),(32,37)))
self.relate('connect','body','leg-left');self.relate('connect','body','leg-right')
""")
for n,left in [(16,False),(22,True)]:
 b="self.add_polyline('triangle',(13,15),(25,24),(13,33),closed=True)\nself.add_polyline('chevron',(29,15),(39,24),(29,33))\n"
 if left:b="self.add_polyline('triangle',(35,15),(23,24),(35,33),closed=True)\nself.add_polyline('chevron',(19,15),(9,24),(19,33))\n"
 plan(n,48,48,'Circle enclosing a complete playback triangle and separate directional chevron.',ring(48)+b)
plan(17,56,56,'Circular outline around uppercase O and the lowered smaller 2.',ring(56)+glyph('letter-o-uppercase',18,21,25,'o')+glyph('digit-2',14,39,33,'two'));GLYPHS[17]=('letter-o-uppercase','digit-2')
plan(18,48,48,'Rectangular speech bubble with tail, lock body, shackle and keyhole dot.',bubble(48,48)+"""
box(self,'lock',16,18,32,30,2)
self.add_line('sl',(19,18),(19,13));self.add_arc('shackle',(19,13),(29,13),radius_x=5)
self.add_line('sr',(29,13),(29,18));self.add_contour('arch','sl','shackle','sr')
self.relate('connect','arch','lock');self.add_dot('hole',(24,24))
""")
plan(19,64,32,'Long rounded password field enclosing two crosses and a lower underscore.',"""
box(self,'frame',2,4,62,28,7)
for i,x in enumerate([14,32]):
 self.add_line('a'+str(i),(x-4,12),(x+4,20));self.add_line('b'+str(i),(x+4,12),(x-4,20));self.relate('connect','a'+str(i),'b'+str(i))
self.add_line('underscore',(46,21),(54,21))
""")
plan(20,32,32,'Tall rounded device with two short vertical marks and lower horizontal divider.',"""
box(self,'frame',7,2,25,30,4)
self.add_line('divider',(7,24),(25,24));self.relate('connect','divider','frame')
self.add_line('left-mark',(13,9),(13,17));self.add_line('right-mark',(19,9),(19,17))
""")
plan(21,48,48,'Complete circle enclosing the shared pound glyph.',ring(48)+glyph('symbol-pound',24,24,24));GLYPHS[21]=('symbol-pound',)
plan(23,48,48,'Circle, detached left chevron, second arrowhead and curved return shaft.',ring(48)+"""
self.add_polyline('first',(16,15),(10,21),(16,27))
self.add_polyline('second',(27,15),(21,21),(27,27))
self.add_bezier('shaft',(21,21),((33,21),(37,25),(37,34)))
self.relate('connect','second','shaft')
""")
plan(24,48,48,'Circle, diagonal prohibition segments, organic tilted sperm head and flowing tail.',ring(48)+"""
self.add_line('slash-top',(34,14),(40,8));self.add_line('slash-bottom',(8,40),(19,29))
self.relate('connect','frame','slash-top');self.relate('connect','frame','slash-bottom')
self.add_bezier('head-a',(14,9),((8,7),(13,22),(18,19)))
self.add_bezier('head-b',(18,19),((26,14),(21,10),(14,9)))
self.add_contour('head','head-a','head-b',closed=True)
self.add_bezier('tail-a',(20,18),((31,25),(30,29),(26,32)))
self.add_bezier('tail-b',(26,32),((20,37),(25,41),(32,40)))
self.add_contour('tail','tail-a','tail-b');self.relate('connect','head','tail')
""")
plan(25,32,32,'Complete speech bubble with lower-right tail and two unequal text lines.',"""
self.add_line('top',(6,3),(26,3));self.add_arc('tr',(26,3),(30,7),radius_x=4)
self.add_line('right',(30,7),(30,20));self.add_arc('br',(30,20),(26,24),radius_x=4)
self.add_polyline('tail',(26,24),(23,24),(23,30),(15,24),(6,24))
self.add_arc('bl',(6,24),(2,20),radius_x=4);self.add_line('left',(2,20),(2,7));self.add_arc('tl',(2,7),(6,3),radius_x=4)
self.add_contour('frame','top','tr','right','br','tail','bl','left','tl',closed=True)
self.add_line('long',(10,10),(22,10));self.add_line('short',(10,17),(18,17))
""")
plan(26,32,32,'Three heart-shaped leaves joined at a common centre and a curved lower stem.',"""
self.add_bezier('top-left',(16,16),((8,8),(5,2),(10,2)))
self.add_bezier('notch-left',(10,2),((13,1),(15,4),(16,5)))
self.add_bezier('notch-right',(16,5),((18,1),(21,1),(23,3)))
self.add_bezier('top-right',(23,3),((27,7),(21,11),(16,16)))
self.add_contour('top','top-left','notch-left','notch-right','top-right',closed=True)
self.add_bezier('left-top',(16,16),((5,7),(-2,6),(3,14)))
self.add_line('left-notch',(3,14),(5,16))
self.add_bezier('left-bottom',(5,16),((-4,22),(4,29),(16,16)))
self.add_contour('left','left-top','left-notch','left-bottom',closed=True)
self.add_bezier('right-top',(16,16),((27,7),(34,7),(29,14)))
self.add_line('right-notch',(29,14),(27,16))
self.add_bezier('right-bottom',(27,16),((36,22),(29,29),(16,16)))
self.add_contour('right','right-top','right-notch','right-bottom',closed=True)
self.add_bezier('stem',(16,16),((16,24),(16,27),(13,30)))
for a,b in [('top','left'),('top','right'),('left','right'),('stem','top'),('stem','left'),('stem','right')]:self.relate('connect',a,b)
""")
plan(27,64,64,'Circle enclosing uppercase T and M using the shared typeface.',ring(64)+glyph('letter-t-uppercase',22,22,32,'t')+glyph('letter-m-uppercase',22,44,32,'m'));GLYPHS[27]=('letter-t-uppercase','letter-m-uppercase')
plan(28,32,32,'Magnifying glass enclosing two unequal vertical marks.',"""
circle(self,'glass',13,13,11)
self.add_line('handle',(21,21),(30,30));self.relate('connect','glass','handle')
self.add_line('short',(10,8),(10,13));self.add_line('long',(16,8),(16,18))
""")
plan(29,48,48,'Circle, outlined head, smooth open shoulders and separate right-hand minus.',ring(48)+"""
circle(self,'head',19,17,6)
self.add_bezier('shoulders',(10,37),((13,29),(25,29),(28,37)))
self.add_line('minus',(33,26),(39,26))
""")
plan(30,56,56,'Circle enclosing uppercase U and V in source order with shared glyphs.',ring(56)+glyph('letter-u-uppercase',20,19,28,'u')+glyph('letter-v-uppercase',20,37,28,'v'));GLYPHS[30]=('letter-u-uppercase','letter-v-uppercase')
plan(31,32,40,'Two wireless arcs above a rounded card with a small lower-right mark.',"""
self.add_bezier('outer',(5,6),((12,0),(20,0),(27,6)))
self.add_bezier('inner',(10,12),((14,9),(18,9),(22,12)))
box(self,'card',2,20,30,38,3);self.add_line('mark',(20,32),(22,32))
""")
plan(32,32,32,'Circle enclosing a single-bar yuan sign, preserving the original one-bar form.',ring(32)+glyph('symbol-yuan-one-bar',14,16,16));GLYPHS[32]=('symbol-yuan-one-bar',)
# Refine compact trial geometry from measured clearances.
def replace(n,a,b):
 shape,parts,ref,body=D[n];D[n]=(shape,parts,ref,body.replace(a,b))
plan(2,32,32,D[2][1],"""
self.add_bezier('bowl-top',(22,17),((25,5),(9,7),(10,17)))
self.add_bezier('bowl-bottom',(10,17),((10,25),(18,24),(22,20)))
self.add_line('bowl-join',(22,20),(22,17));self.add_contour('bowl','bowl-top','bowl-bottom','bowl-join',closed=True)
self.add_bezier('return',(22,20),((25,26),(30,23),(30,16)))
self.add_bezier('outer-tr',(30,16),((30,8),(24,2),(16,2)))
self.add_bezier('outer-tl',(16,2),((8,2),(2,8),(2,16)))
self.add_bezier('outer-bl',(2,16),((2,24),(8,30),(16,30)))
self.add_bezier('outer-end',(16,30),((18,30),(20,30),(22,29)))
self.add_contour('outer','return','outer-tr','outer-tl','outer-bl','outer-end');self.relate('connect','bowl','outer')
""")
# Source bubbles meet: use a shared tangent point, not a false exemption between separated circles.
plan(4,32,32,D[4][1],"""
circle(self,'large',12,20,10);circle(self,'small',26,6,4)
""")
replace(5,'(12,16),(21,12),(30,16)','(11,15),(21,10),(31,15)');replace(5,'(30,28),(21,32),(12,28),(12,16)','(31,27),(21,33),(11,27),(11,15)');replace(5,'(12,16),(21,20),(30,16)','(11,15),(21,21),(31,15)');replace(5,'(21,20),(21,32)','(21,21),(21,33)')
# Keep a proportionate portrait canvas rather than artificial empty side margins.
replace(6,'(18,42)','(20,42)');replace(6,'(19,12)','(20,13)')
# Shift the document drawing six units left, giving an exact 36px envelope.
import ast

def translate(n,dx,dy,w,h):
 sh,parts,ref,body=D[n];tree=ast.parse(body)
 class T(ast.NodeTransformer):
  def visit_Tuple(self,node):
   node=self.generic_visit(node)
   if len(node.elts)==2 and all(isinstance(x,ast.Constant) and isinstance(x.value,(int,float)) for x in node.elts):node.elts=[ast.Constant(node.elts[0].value+dx),ast.Constant(node.elts[1].value+dy)]
   return node
 D[n]=(sh,parts,ref,ast.unparse(T().visit(tree)));DIMS[n]=(w,h)
translate(6,-6,0,36,48)
replace(7,'(5,5),((10,1),(12,5),(16,9))','(5,5),((9,1),(12,5),(16,9))')
replace(7,'((26,-3),(39,12),(23,23))','((26,-3),(37,12),(23,23))')
# 32px euro envelope with deliberately placed cardinal extrema.
for n in [9,10]:
 plan(n,32,32,D[n][1],"""
self.add_bezier('upper-tip',(30,5),((27,3),(23,2),(20,2)))
self.add_bezier('upper',(20,2),((12,2),(6,7),(6,13)))
self.add_line('spine',(6,13),(6,19))
self.add_bezier('lower',(6,19),((6,25),(12,30),(20,30)))
self.add_bezier('lower-tip',(20,30),((23,30),(27,29),(30,27)))
self.add_contour('curve','upper-tip','upper','spine','lower','lower-tip')
self.add_line('bar',(2,16),(20,16));self.relate('connect','curve','bar')
""")
replace(12,"2,2,46,38,4","2,2,46,40,4");replace(12,"18,12,4","18,13,4");replace(12,'(8,12),(14,12)','(8,13),(14,13)');replace(12,'(22,12),(40,12)','(22,13),(40,13)');DIMS[12]=(48,42)
replace(13,'[12,18]','[10,18]')
replace(17,"(44, 40)","(43, 39)")
replace(19,"2,4,62,28,7","2,2,62,30,7")
plan(20,32,48,D[20][1],"""
box(self,'frame',2,2,30,46,6)
self.add_line('divider',(2,36),(30,36));self.relate('connect','divider','frame')
self.add_line('left-mark',(12,13),(12,25));self.add_line('right-mark',(20,13),(20,25))
""")
replace(23,'(16,15),(10,21),(16,27)','(15,15),(9,21),(15,27)');replace(23,'(37,25),(37,34)','(36,25),(36,32)')
replace(24,'(14,9),((8,7),(13,22),(18,19))','(17,11),((12,10),(15,24),(20,21))');replace(24,'(18,19),((26,14),(21,10),(14,9))','(20,21),((28,16),(24,12),(17,11))');replace(24,'(20,18),((31,25),(30,29),(26,32))','(22,20),((31,25),(30,29),(26,32))');replace(24,'((20,37),(25,41),(32,40))','((22,35),(25,39),(30,38))')
replace(27,glyph('letter-t-uppercase',22,22,32,'t'),glyph('letter-t-uppercase',18,20,32,'t'));replace(27,glyph('letter-m-uppercase',22,44,32,'m'),glyph('letter-m-uppercase',18,43,32,'m'))
plan(28,40,40,D[28][1],"""
circle(self,'glass',16,16,14)
self.add_line('handle',(26,26),(38,38));self.relate('connect','glass','handle')
self.add_line('short',(12,10),(12,16));self.add_line('long',(20,10),(20,23))
""")
replace(29,"(10,37),((13,29),(25,29),(28,37))","(12,35),((15,29),(25,29),(28,35))")
replace(30,glyph('letter-u-uppercase',20,19,28,'u'),glyph('letter-u-uppercase',18,18,28,'u'));replace(30,glyph('letter-v-uppercase',20,37,28,'v'),glyph('letter-v-uppercase',18,38,28,'v'))
replace(31,"(5,6),((12,0),(20,0),(27,6))","(5,5),((12,1),(20,1),(27,5))");replace(31,'(20,32),(22,32)','(19,30),(22,30)')
replace(32,glyph('symbol-yuan-one-bar',14,16,16),glyph('symbol-yuan-one-bar',12,16,16))
# Final source-shaped curves use explicit extrema and smooth shared tangents.
def oval_bubble(s):
 c=s//2;y=c-4
 return f"""self.add_bezier('ul',({c},2),((8,2),(2,10),(2,{y})))
self.add_bezier('ll',(2,{y}),((2,{y+8}),(7,{s-16}),({s//4},{s-12})))
self.add_polyline('tail',({s//4},{s-12}),(4,{s-2}),({s//3},{s-10}))
self.add_bezier('lr',({s//3},{s-10}),(({s-12},{s-3}),({s-2},{y+12}),({s-2},{y})))
self.add_bezier('ur',({s-2},{y}),(({s-2},10),({s-8},2),({c},2)))
self.add_contour('frame','ul','ll','tail','lr','ur',closed=True)
"""
plan(3,64,64,D[3][1],oval_bubble(64)+glyph('symbol-bitcoin',28,32,29))
plan(11,56,56,D[11][1],oval_bubble(56)+glyph('letter-h-uppercase',18,22,25,'h')+glyph('letter-i-uppercase',18,36,25,'i'))
plan(4,36,40,D[4][1],"""
circle(self,'large',17,23,15);circle(self,'small',29,7,5)
self.relate('connect','large','small')
""")
# More decisive departure angle at the real heart/slash intersection avoids a thick sliver.
replace(7,"(5,5),((9,1),(12,5),(16,9))","(5,5),((9,-1),(13,5),(16,9))")
plan(8,40,48,D[8][1],"""
self.add_polyline('edge',(6,2),(28,2),(38,12),(38,42))
self.add_arc('br',(38,42),(34,46),radius_x=4)
self.add_line('bottom',(34,46),(6,46));self.add_arc('bl',(6,46),(2,42),radius_x=4)
self.add_line('left',(2,42),(2,6));self.add_arc('tl',(2,6),(6,2),radius_x=4)
self.add_contour('frame','edge','br','bottom','bl','left','tl',closed=True)
box(self,'chip',12,14,28,36,3)
self.add_line('division',(12,25),(28,25));self.relate('connect','chip','division')
""")
replace(12,'(8,13)','(9,13)');replace(12,'(8,28)','(9,28)')
# Wavy frame, four rounded corners and repeated shallow undulations.
b="""self.add_bezier('corner-tr',(26,2),((29,2),(30,3),(30,6)))
self.add_bezier('corner-br',(30,26),((30,29),(29,30),(26,30)))
self.add_bezier('corner-bl',(6,30),((3,30),(2,29),(2,26)))
self.add_bezier('corner-tl',(2,6),((2,3),(3,2),(6,2)))
"""
# Endpoints at wave extrema; horizontal/vertical tangents retain smooth joins.
wave=[(6,2),(11,4),(16,2),(21,4),(26,2)]
for side in range(4):
 def rot(p):
  x,y=p
  for _ in range(side):x,y=32-y,x
  return x,y
 for i in range(4):
  x,y=wave[i];u,v=wave[i+1];a=rot((x,y));c1=rot((x+2,y));c2=rot((u-2,v));e=rot((u,v))
  b+=f"self.add_bezier('s{side}-{i}',{a!r},{(c1,c2,e)!r})\n"
names=[]
for side,corner in enumerate(['corner-tr','corner-br','corner-bl','corner-tl']):names += [f's{side}-{i}' for i in range(4)]+[corner]
b+="self.add_contour('frame',"+','.join(repr(x) for x in names)+",closed=True)\nself.add_dot('sun',(10,11))\nself.add_polyline('mountain',(12,22),(19,12),(23,18))\n"
plan(14,32,32,D[14][1],b)
plan(17,64,64,D[17][1],ring(64)+glyph('letter-o-uppercase',20,23,28,'o')+glyph('digit-2',18,45,36,'two'))
plan(18,48,52,D[18][1],bubble(48,52)+"""
box(self,'lock',15,20,33,34,2)
self.add_line('sl',(19,20),(19,14));self.add_arc('shackle',(19,14),(29,14),radius_x=5)
self.add_line('sr',(29,14),(29,20));self.add_contour('arch','sl','shackle','sr')
self.relate('connect','arch','lock');self.add_dot('hole',(24,27))
""")
# Source tail and text need 3 separate 8-unit intervals vertically.
replace(25,'(6,3),(26,3)','(6,2),(26,2)');replace(25,'(26,3),(30,7)','(26,2),(30,6)');replace(25,'(30,7),(30,20)','(30,6),(30,22)');replace(25,'(30,20),(26,24)','(30,22),(26,26)');replace(25,'(26,24),(23,24),(23,30),(15,24),(6,24)','(26,26),(23,26),(23,32),(15,26),(6,26)');replace(25,'(6,24),(2,20)','(6,26),(2,22)');replace(25,'(2,20),(2,7)','(2,22),(2,6)');replace(25,'(2,7),(6,3)','(2,6),(6,2)');replace(25,'(10,17),(18,17)','(10,18),(18,18)');DIMS[25]=(32,34)
plan(26,32,32,D[26][1],"""
self.add_bezier('tl',(16,16),((12,12),(5,2),(9,2)))
self.add_bezier('tnl',(9,2),((12,2),(14,4),(16,6)))
self.add_bezier('tnr',(16,6),((18,4),(20,2),(23,2)))
self.add_bezier('tr',(23,2),((27,2),(20,12),(16,16)))
self.add_contour('top','tl','tnl','tnr','tr',closed=True)
self.add_bezier('lt',(16,16),((9,12),(2,5),(2,10)))
self.add_bezier('ln',(2,10),((2,13),(4,15),(6,16)))
self.add_bezier('lb',(6,16),((4,17),(2,19),(2,22)))
self.add_bezier('le',(2,22),((2,28),(10,22),(16,16)))
self.add_contour('left','lt','ln','lb','le',closed=True)
self.add_bezier('rt',(16,16),((23,12),(30,5),(30,10)))
self.add_bezier('rn',(30,10),((30,13),(28,15),(26,16)))
self.add_bezier('rb',(26,16),((28,17),(30,19),(30,22)))
self.add_bezier('re',(30,22),((30,28),(22,22),(16,16)))
self.add_contour('right','rt','rn','rb','re',closed=True)
self.add_bezier('stem',(16,16),((16,24),(16,27),(13,30)))
for a,b in [('top','left'),('top','right'),('left','right'),('stem','top'),('stem','left'),('stem','right')]:self.relate('connect',a,b)
""")
replace(28,'(20,23)','(20,22)')
replace(29,'(12,35),((15,29),(25,29),(28,35))','(13,35),((16,29),(25,29),(28,35))')
# Place real shared junctions at primitive endpoints, preserving both tangent circles.
plan(4,36,40,D[4][1],"""
self.add_arc('large-a',(26,11),(8,35),radius_x=15)
self.add_arc('large-b',(8,35),(26,11),radius_x=15)
self.add_contour('large','large-a','large-b',closed=True)
self.add_arc('small-a',(26,11),(32,3),radius_x=5)
self.add_arc('small-b',(32,3),(26,11),radius_x=5)
self.add_contour('small','small-a','small-b',closed=True)
self.relate('connect','large','small')
""")
replace(7,"self.add_line('slash',(2,2),(30,30))","self.add_polyline('slash',(2,2),(5,5),(23,23),(30,30))")
replace(12,'(40,13)','(39,13)');replace(12,'(40,28)','(39,28)')
replace(14,"(10,11)","(11,11)");replace(14,"(23,18)","(22,18)")
def oval_bubble(s):
 c=s//2;y=c-3;bottom=s-8
 return f"""self.add_bezier('ul',({c},2),(({round(c*.45)},2),(2,{round(y*.45)}),(2,{y})))
self.add_bezier('ll',(2,{y}),((2,{y+8}),(7,{s-17}),({s//4},{s-13})))
self.add_polyline('tail',({s//4},{s-13}),(4,{s-2}),({s//3},{s-10}))
self.add_bezier('base',({s//3},{s-10}),(({c-5},{bottom}),({c-2},{bottom}),({c},{bottom})))
self.add_bezier('lr',({c},{bottom}),(({round(s-c*.45)},{bottom}),({s-2},{y+12}),({s-2},{y})))
self.add_bezier('ur',({s-2},{y}),(({s-2},{round(y*.45)}),({round(s-c*.45)},2),({c},2)))
self.add_contour('frame','ul','ll','tail','base','lr','ur',closed=True)
"""
plan(3,64,64,D[3][1],oval_bubble(64)+glyph('symbol-bitcoin',28,32,29))
plan(11,56,56,D[11][1],oval_bubble(56)+glyph('letter-h-uppercase',18,22,25,'h')+"from icon_set.typeface.source_composition_forms import draw_plain_i\ndraw_plain_i(self)\n")
plan(17,64,64,D[17][1],ring(64)+"from icon_set.typeface.source_composition_forms import draw_oxygen\ndraw_oxygen(self)\n")
plan(27,64,64,D[27][1],ring(64)+glyph('letter-t-uppercase',18,20,32,'t')+"from icon_set.typeface.source_composition_forms import draw_sloping_m\ndraw_sloping_m(self)\n")
# Exactly four units of visible clearance between detached head and shoulders.
replace(29,'(13,35),((16,29),(25,29),(28,35))','(13,35),((16,29.666666666666668),(25,29.666666666666668),(28,35))')
# Round the clover lobes; preserve three heart-shaped leaves rather than pointed petals.
replace(26,"self.add_bezier('tl',(16,16),((12,12),(5,2),(9,2)))","self.add_bezier('tl',(16,16),((12,12),(8,10),(8,8)))\nself.add_bezier('tla',(8,8),((6,4),(8,2),(12,2)))")
replace(26,"self.add_bezier('tnl',(9,2),((12,2),(14,4),(16,6)))","self.add_bezier('tnl',(12,2),((14,2),(15,4),(16,6)))")
replace(26,"self.add_bezier('tnr',(16,6),((18,4),(20,2),(23,2)))","self.add_bezier('tnr',(16,6),((17,4),(18,2),(20,2)))")
replace(26,"self.add_bezier('tr',(23,2),((27,2),(20,12),(16,16)))","self.add_bezier('tra',(20,2),((24,2),(26,4),(24,8)))\nself.add_bezier('tr',(24,8),((24,10),(20,12),(16,16)))")
replace(26,"'tl','tnl','tnr','tr'","'tl','tla','tnl','tnr','tra','tr'")
plan(25,40,36,D[25][1],"""
self.add_line('top',(6,2),(34,2));self.add_arc('tr',(34,2),(38,6),radius_x=4)
self.add_line('right',(38,6),(38,22));self.add_arc('br',(38,22),(34,26),radius_x=4)
self.add_polyline('tail',(34,26),(30,26),(30,34),(20,26),(6,26))
self.add_arc('bl',(6,26),(2,22),radius_x=4);self.add_line('left',(2,22),(2,6));self.add_arc('tl',(2,6),(6,2),radius_x=4)
self.add_contour('frame','top','tr','right','br','tail','bl','left','tl',closed=True)
self.add_line('long',(12,10),(28,10));self.add_line('short',(12,18),(22,18))
""")
D[3]=(*D[3][:3],D[3][3]+"from icon_set.typeface.source_composition_forms import draw_bitcoin_serifs\ndraw_bitcoin_serifs(self)\n")
