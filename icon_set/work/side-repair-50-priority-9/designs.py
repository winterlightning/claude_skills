SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/side-repair-50-priority-9/batch.json'
AUTHOR='gpt-6'
D={};GLYPHS={};TEXT={}
def plan(n,shape,parts,ref,body):D[n]=(shape,parts,ref,body)
plan(11,'SQUARE','Open chicken head, closed arched comb, two eye dots and a closed diamond beak.','egg / original source: smooth bilateral head and closed comb opening',"""
self.add_line('head-left',(2,30),(2,24))
self.add_bezier('head-tl',(2,24),((2,16),(6,8),(12,8)))
self.add_line('head-top',(12,8),(20,8))
self.add_bezier('head-tr',(20,8),((26,8),(30,16),(30,24)))
self.add_line('head-right',(30,24),(30,30))
self.add_contour('head','head-left','head-tl','head-top','head-tr','head-right')
self.add_arc('comb',(12,8),(20,8),radius_x=4,radius_y=6);self.relate('connect','comb','head')
self.add_line('eye-left',(11,16),(11,16));self.add_line('eye-right',(21,16),(21,16))
self.add_polyline('beak',(16,20),(23,25),(16,30),(9,25),(16,20))
""")
plan(1,'SQUARE','Closed document frame and all three horizontal content lines.','file-text: rounded enclosing page',"""
box(self,'page',2,2,30,30,2)
for i,(y,end) in enumerate(((9,23),(16,17),(23,21))):self.add_line(f'text-{i}',(9,y),(end,y))
""")
for n,xs in [(3,(8,13,19,24)),(47,(8,12,16,20,24))]:
 plan(n,'SQUARE',f'Rounded enclosing square with all {len(xs)} vertical barcode bars.','scan-barcode: closed frame and repeated vertical strokes',f"box(self,'frame',2,2,30,30,4)\nfor i,x in enumerate({xs!r}):self.add_line(f'bar-{{i}}',(x,9),(x,23))")
plan(6,'SQUARE','Rounded bound notebook, vertical binding and all three binding marks.','notebook: binding and closed page',"""
box(self,'book',6,2,30,30,3)
for i,y in enumerate((8,16,24)):
 self.add_line(f'binding-{i}',(2,y),(12,y));self.relate('connect',f'binding-{i}','book')
""")
plan(7,'VRECT_XL','Calculator frame, separate closed display and four horizontal keys in two rows.','calculator: display and repeated key grid',"""
box(self,'body',4,2,28,30,4);box(self,'display',10,8,22,14,1)
for row,y in enumerate((21,25)):
 for col,x in enumerate((11,21)):self.add_line(f'key-{row}-{col}',(x-1,y),(x+1,y))
""")
plan(10,'SQUARE','Checklist document with two separate square checkboxes and two horizontal content lines.','list-check: paired rows, complete source boxes',"""
box(self,'page',2,2,30,30,3)
for i,y in enumerate((8,20)):
 box(self,f'checkbox-{i}',8,y,16,y+6,0)
 self.add_line(f'text-{i}',(22,y+3),(24,y+3))
""")
plan(24,'SQUARE','Square root node, connected branching stem and two square child nodes.','network: connected node hierarchy',"""
box(self,'root',12,2,20,10,0);box(self,'left',2,22,10,30,0);box(self,'right',22,22,30,30,0)
self.add_line('stem',(16,10),(16,16));self.relate('connect','stem','root')
self.add_polyline('branch',(6,22),(6,16),(26,16),(26,22));self.relate('connect','branch','stem');self.relate('connect','branch','left');self.relate('connect','branch','right')
""")
plan(34,'VRECT_XL','Clipped-corner page with closed picture panel and both horizontal text lines.','file-image: closed picture panel',"""
self.add_polyline('page',(4,30),(4,2),(21,2),(28,9),(28,30),(4,30))
box(self,'panel',10,8,22,16,0)
self.add_line('text-long',(10,22),(22,22));self.add_line('text-short',(10,26),(15,26))
""")
plan(42,'VRECT_XL','Clipped-corner page enclosing a separate rounded rectangular panel divided into two cells.','file-spreadsheet: nested panel and horizontal divider',"""
self.add_polyline('page',(4,30),(4,2),(21,2),(28,9),(28,30),(4,30))
box(self,'panel',10,8,22,24,2)
self.add_line('divider',(10,16),(22,16));self.relate('connect','divider','panel')
""")
plan(39,'SQUARE','Three ascending closed candlestick bodies, each retaining an upper and lower wick.','chart-candlestick: repeated rounded bodies and paired stems',"""
for i,(x,top) in enumerate(((2,19),(12,12),(22,5))):
 box(self,f'body-{i}',x,top,x+8,top+8,2)
 self.add_line(f'wick-top-{i}',(x+4,top-3),(x+4,top));self.relate('connect',f'wick-top-{i}',f'body-{i}')
 self.add_line(f'wick-bottom-{i}',(x+4,top+8),(x+4,top+11));self.relate('connect',f'wick-bottom-{i}',f'body-{i}')
""")
plan(38,'HRECT_M','Three concentric open rainbow semicircles, all retaining open undersides.','rainbow: shared center and three arc radii',"""
for i,r in enumerate((14,8,2)):self.add_arc(f'arc-{i}',(16-r,24),(16+r,24),radius_x=r)
""")
plan(12,'CIRCLE','Circular frame, separate closed right-pointing triangle and vertical stop bar.','circle-skip-forward: full frame and two distinct controls',"""
circle(self,'frame',16,16,14)
self.add_polyline('triangle',(8,10),(17,16),(8,22),(8,10))
self.add_line('stop',(24,10),(24,22))
""")
plan(30,'VRECT_XL','Closed phone frame, separate closed play triangle and footer divider.','smartphone: closed rounded enclosure and footer',"""
box(self,'phone',4,2,28,30,4)
self.add_polyline('play',(12,8),(22,13),(12,18),(12,8))
self.add_line('footer',(4,24),(28,24));self.relate('connect','footer','phone')
""")
# User-authorized careful simplifications, retaining each concept at 32px/4px.
SIMPLIFICATIONS={}
def revise(n,note,body,shape=None):
 old=D[n];D[n]=(shape or old[0],old[1]+' Small-size treatment: '+note,old[2],body);SIMPLIFICATIONS[n]=note
revise(1,'Reduced three content lines to two.',"box(self,'page',2,2,30,30,3)\nself.add_line('line-1',(10,11),(22,11))\nself.add_line('line-2',(10,21),(18,21))")
for n in (3,47):
 revise(n,'Reduced the barcode to three bars and opened the enclosure into four scan corners.',"""
for name,pts in [('tl',((2,6),(2,2),(6,2))),('tr',((26,2),(30,2),(30,6))),('bl',((2,26),(2,30),(6,30))),('br',((26,30),(30,30),(30,26)))]:self.add_polyline(name,*pts)
for i,(x,top,bottom) in enumerate(((8,10,22),(16,8,24),(24,10,22))):self.add_line(f'bar-{i}',(x,top),(x,bottom))
""")
revise(6,'Reduced three binding marks to two.',"""
box(self,'book',6,2,30,30,3)
for i,y in enumerate((11,21)):
 self.add_line(f'binding-{i}',(2,y),(12,y));self.relate('connect',f'binding-{i}','book')
""")
revise(7,'Simplified the display to a horizontal indicator and retained all four keys as round marks.',"""
box(self,'body',4,2,28,30,4)
self.add_line('display',(11,10),(21,10))
for i,(x,y) in enumerate(((11,17),(21,17),(11,23),(21,23))):self.add_line(f'key-{i}',(x,y),(x,y))
""")
revise(10,'Replaced small empty checkbox outlines with readable check strokes; kept two rows and their text marks.',"""
box(self,'page',2,2,30,30,3)
for i,y in enumerate((11,21)):
 self.add_polyline(f'check-{i}',(9,y),(11,y+2),(14,y-2))
 self.add_line(f'text-{i}',(21,y),(23,y))
""")
revise(11,'Merged the comb into the outer head outline, removing only the tiny dividing line; kept both eyes and the closed diamond beak.',"""
self.add_line('head-left',(2,30),(2,24))
self.add_bezier('head-tl',(2,24),((2,16),(6,8),(12,8)))
self.add_arc('comb',(12,8),(20,8),radius_x=4,radius_y=6)
self.add_bezier('head-tr',(20,8),((26,8),(30,16),(30,24)))
self.add_line('head-right',(30,24),(30,30))
self.add_contour('head','head-left','head-tl','comb','head-tr','head-right')
self.add_line('eye-left',(11,16),(11,16));self.add_line('eye-right',(21,16),(21,16))
self.add_polyline('beak',(16,20),(23,25),(16,30),(9,25),(16,20))
""")
revise(12,'Removed the circular enclosure; retained the closed play triangle and separate stop bar.',"""
self.add_polyline('triangle',(2,2),(22,16),(2,30),(2,2));self.add_line('stop',(30,2),(30,30))
""",'SQUARE')
revise(24,'Simplified the stepped branch routing to two direct links, retaining all three square nodes.',"""
box(self,'root',12,2,20,10,0);box(self,'left',2,22,10,30,0);box(self,'right',22,22,30,30,0)
for name,x in [('left',6),('right',26)]:
 self.add_line(name+'-link',(16,10),(x,22));self.relate('connect',name+'-link','root');self.relate('connect',name+'-link',name)
self.relate('connect','left-link','right-link')
""")
revise(30,'Removed the footer divider to give the closed play triangle a clear opening.',"""
box(self,'phone',4,2,28,30,4)
self.add_polyline('play',(12,9),(21,16),(12,23),(12,9))
""")
revise(34,'Combined the picture area into a page header and reduced the body text to one line.',"""
box(self,'page',4,2,28,30,3)
self.add_line('header',(4,12),(28,12));self.relate('connect','header','page')
self.add_line('body-text',(12,22),(20,22))
""")
revise(38,'Reduced three rainbow bands to two clear open arcs.',"""
self.add_arc('outer',(2,22),(30,22),radius_x=14,radius_y=12)
self.add_arc('inner',(10,22),(22,22),radius_x=6,radius_y=5)
""",'HRECT_S')
revise(39,'Reduced three candlesticks to two while retaining their ascending placement and all four wicks.',"""
for i,(x,top) in enumerate(((2,19),(22,5))):
 box(self,f'body-{i}',x,top,x+8,top+8,2)
 self.add_line(f'wick-top-{i}',(x+4,top-3),(x+4,top));self.relate('connect',f'wick-top-{i}',f'body-{i}')
 self.add_line(f'wick-bottom-{i}',(x+4,top+8),(x+4,top+11));self.relate('connect',f'wick-bottom-{i}',f'body-{i}')
""")
revise(42,'Merged the nested panel into the page frame while retaining its two-cell division.',"""
self.add_polyline('page',(4,30),(4,2),(21,2),(28,9),(28,30),(4,30))
self.add_line('divider',(4,16),(28,16));self.relate('connect','divider','page')
""")
plan(2,'SQUARE','Baby with round head, hair tuft, two ears, shoulders and diagonal swaddle.','human_ref/user.svg: round head and exact detached head gap',"""
circle(self,'head',16,10,6)
for n,a,b in [('hair',(16,2),(16,4)),('ear-left',(8,10),(10,10)),('ear-right',(22,10),(24,10))]:self.add_line(n,a,b);self.relate('connect',n,'head')
self.add_bezier('body-left',(2,30),((4,26),(10,24),(16,24)))
self.add_bezier('body-right-a',(16,24),((20,24),(23,25),(25,26)))
self.add_bezier('body-right-b',(25,26),((27,27),(29,29),(30,30)))
self.add_contour('body','body-left','body-right-a','body-right-b')
self.add_line('wrap',(10,30),(25,26));self.relate('connect','wrap','body')
""")
SIMPLIFICATIONS[2]='Simplified the hair curl and ear contours to short strokes; retained the head, both ears, body and swaddle.'
plan(16,'SQUARE','Delivery-worker cap with emblem, two eyes and open curved cheeks.','human_ref/user.svg: circular cheek arcs; source cap retained',"""
self.add_polyline('cap',(6,16),(8,4),(16,2),(24,4),(26,16))
self.add_line('brim',(2,16),(30,16));self.relate('connect','cap','brim')
self.add_line('emblem',(16,9),(16,9))
for name,x,end in [('left',4,(10,30)),('right',28,(22,30))]:
 self.add_line(name+'-side',(x,16),(x,20))
 self.add_arc(name+'-cheek',(x,20),end,radius_x=12,sweep=name=='left')
 self.add_contour(name,name+'-side',name+'-cheek');self.relate('connect',name,'brim')
for n,x in [('left',12),('right',20)]:self.add_line(n+'-eye',(x,23),(x,23))
""")
SIMPLIFICATIONS[16]='Rendered the small cap emblem as a dot and flattened the brim; retained both eyes and cheeks.'
plan(22,'SQUARE','Graduate mortarboard above a circular jaw and open shoulder bust.','human_ref/user.svg: circular jaw and exact four-unit detached gap',"""
self.add_polyline('cap',(2,6),(16,2),(30,6),(16,10),(2,6))
self.add_arc('jaw',(9,8),(23,8),radius_x=7,sweep=False);self.relate('connect','jaw','cap')
self.add_bezier('shoulder-left',(4,30),((4,26),(9,23),(16,23)))
self.add_bezier('shoulder-right',(16,23),((23,23),(28,26),(28,30)));self.add_contour('shoulders','shoulder-left','shoulder-right')
""")
SIMPLIFICATIONS[22]='Removed the narrow cap band and opened the shoulder base; kept the mortarboard, circular jaw and bust.'
plan(36,'VRECT_XL','Portrait with a center-parted hair silhouette, circular jaw and open shoulders.','human_ref/user.svg: circular jaw and four-unit detached gap',"""
self.add_bezier('hair-l',(9,9),((9,5),(9,2),(12,2)))
self.add_bezier('part-l',(12,2),((14,2),(16,3),(16,5)))
self.add_bezier('part-r',(16,5),((16,3),(18,2),(20,2)))
self.add_bezier('hair-r',(20,2),((23,2),(23,5),(23,9)))
self.add_arc('jaw',(23,9),(9,9),radius_x=7)
self.add_contour('head','hair-l','part-l','part-r','hair-r','jaw',closed=True)
self.add_bezier('shoulder-l',(4,30),((4,27),(10,24),(16,24)))
self.add_bezier('shoulder-r',(16,24),((22,24),(28,27),(28,30)));self.add_contour('body','shoulder-l','shoulder-r')
""")
SIMPLIFICATIONS[36]='Moved the center part into the hair silhouette, omitted the tiny side hair tips, and opened the shoulder base.'
plan(23,'SQUARE','Perspective cube above a small upward-pointing hand.','box and human_ref/full_body_ref.png: geometric cube and simplified gesture',"""
self.add_polyline('cube-top',(12,7),(21,2),(30,7),(21,12),(12,7))
self.add_polyline('cube-front',(21,12),(21,23),(30,18),(30,7));self.relate('connect','cube-front','cube-top')
self.add_line('cube-open-edge',(12,7),(12,15));self.relate('connect','cube-open-edge','cube-top')
self.add_polyline('hand',(4,20),(4,28),(10,28),(10,30))
self.add_line('thumb',(2,26),(4,28));self.relate('connect','thumb','hand')
""")
SIMPLIFICATIONS[23]='Reduced the small hand to an index stroke, palm and thumb, retaining the complete perspective cube.'
plan(28,'HRECT_XL','Open-wrist robotic hand with raised finger and a single joint seam.','hand: broad open palm and rounded finger tip',"""
self.add_line('upper',(2,4),(12,8))
self.add_bezier('knuckle',(12,8),((18,8),(20,8),(20,12)))
self.add_line('notch',(20,12),(20,16));self.add_line('finger-up',(20,16),(26,10))
self.add_bezier('tip',(26,10),((28,8),(30,10),(30,12)))
self.add_line('finger-side',(30,12),(30,18));self.add_line('finger-bottom',(30,18),(22,26))
self.add_bezier('palm',(22,26),((20,28),(18,28),(16,28)))
self.add_line('wrist-base',(16,28),(2,24))
self.add_contour('hand','upper','knuckle','notch','finger-up','tip','finger-side','finger-bottom','palm','wrist-base')
self.add_line('joint',(12,8),(12,18));self.relate('connect','joint','hand')
""")
SIMPLIFICATIONS[28]='Reduced the wrist and finger seams to one clear joint mark; retained the open wrist and pointing hand silhouette.'
plan(35,'SQUARE','Open-palm hand gesture with four raised finger strokes and a separate thumb branch.','human_ref/full_body_ref.png: simplified human gesture strokes',"""
self.add_line('outer-left',(6,8),(6,22))
self.add_bezier('palm-left',(6,22),((6,28),(12,30),(18,30)))
self.add_bezier('palm-right',(18,30),((26,30),(30,26),(30,22)))
self.add_line('outer-right',(30,22),(30,10));self.add_contour('palm','outer-left','palm-left','palm-right','outer-right')
self.add_line('finger-middle',(14,2),(14,18));self.add_line('finger-ring',(22,4),(22,18))
self.add_line('thumb',(2,20),(6,22));self.relate('connect','thumb','palm')
""")
SIMPLIFICATIONS[35]='Rendered the four fingers as single gesture strokes rather than narrow doubled outlines; retained all four fingers and the thumb.'
# Second geometry pass after examining the native-size drafts.
D[2]=(D[2][0],D[2][1],D[2][2],"""
circle(self,'head',16,8,4)
for n,a,b in [('hair',(16,2),(16,4)),('ear-left',(10,8),(12,8)),('ear-right',(20,8),(22,8))]:self.add_line(n,a,b);self.relate('connect',n,'head')
self.add_bezier('body-left',(2,30),((2,25),(9,20),(16,20)))
self.add_bezier('body-right-a',(16,20),((21,20),(24,22),(26,25)))
self.add_bezier('body-right-b',(26,25),((28,27),(29,29),(30,30)))
self.add_contour('body','body-left','body-right-a','body-right-b')
self.add_line('wrap',(10,30),(26,25));self.relate('connect','wrap','body')
""")
D[16]=(D[16][0],D[16][1],D[16][2],D[16][3].replace("sweep=name=='left'","sweep=name=='right'"))
D[22]=(D[22][0],D[22][1],D[22][2],"""
self.add_polyline('cap-top',(9,11),(2,8),(16,2),(30,8),(23,11))
self.add_arc('jaw',(23,11),(9,11),radius_x=7)
self.relate('connect','cap-top','jaw')
self.add_bezier('shoulder-left',(4,30),((4,28),(9,26),(16,26)))
self.add_bezier('shoulder-right',(16,26),((23,26),(28,28),(28,30)));self.add_contour('shoulders','shoulder-left','shoulder-right')
""")
SIMPLIFICATIONS[22]='Merged the cap front and band into the head outline and opened the shoulder base; preserved the mortarboard silhouette and circular jaw.'
plan(4,'SQUARE','Upright battery with raised terminal and a clear internal lightning bolt.','battery-charging: open outline around the modifier',"""
self.add_line('left-bottom',(8,30),(6,30));self.add_arc('bl',(6,30),(2,26),radius_x=4)
self.add_line('left',(2,26),(2,14));self.add_arc('tl',(2,14),(6,10),radius_x=4)
self.add_polyline('terminal',(6,10),(10,10),(10,2),(22,2),(22,10),(26,10))
self.add_arc('tr',(26,10),(30,14),radius_x=4);self.add_line('right',(30,14),(30,26));self.add_arc('br',(30,26),(26,30),radius_x=4);self.add_line('right-bottom',(26,30),(24,30))
self.add_contour('left-frame','left-bottom','bl','left','tl');self.relate('connect','left-frame','terminal')
self.add_contour('right-frame','tr','right','br','right-bottom');self.relate('connect','right-frame','terminal')
self.add_polyline('bolt',(18,16),(10,24),(22,24),(16,30))
""")
SIMPLIFICATIONS[4]='Opened the lower shell around the bolt and merged the terminal divider into the outline.'
rotation="""
class Rotated:
 def add_line(_,n,a,b):return self.add_line(n,(32-a[1],a[0]),(32-b[1],b[0]))
 def add_arc(_,n,a,b,**kw):
  rx=kw.pop('radius_x');ry=kw.pop('radius_y',rx)
  return self.add_arc(n,(32-a[1],a[0]),(32-b[1],b[0]),radius_x=ry,radius_y=rx,**kw)
 def add_polyline(_,n,*pts):return self.add_polyline(n,*[(32-y,x) for x,y in pts])
 def __getattr__(_,n):return getattr(self,n)
r=Rotated()
"""
plan(9,'SQUARE','Side-terminal battery with a clear lightning mark.','battery-charging: open modifier clearance',rotation+D[4][3].replace('self.','r.'))
SIMPLIFICATIONS[9]='Opened the shell around the bolt and merged the terminal divider; retained the side-terminal orientation.'
plan(8,'VRECT_M','Tapered carrot with two upright leaf strokes and one short texture mark.','carrot: tapered body and upright leaves',"""
self.add_arc('shoulder',(8,14),(24,14),radius_x=8,radius_y=5)
self.add_line('right',(24,14),(20,28));self.add_bezier('tip-right',(20,28),((18,30),(18,30),(16,30)))
self.add_bezier('tip-left',(16,30),((14,30),(14,30),(12,28)));self.add_line('left',(12,28),(8,14))
self.add_contour('carrot','shoulder','right','tip-right','tip-left','left',closed=True)
self.add_polyline('leaves',(10,2),(16,9),(22,2));self.relate('connect','leaves','carrot')
self.add_line('mark',(10,21),(15,21));self.relate('connect','mark','carrot')
""")
SIMPLIFICATIONS[8]='Rendered the two leaves as upright strokes and reduced two texture marks to one.'
plan(13,'SQUARE','Three equal open circles in a triangular cluster.','circle: equal radii and shared triangular layout',"""
for name,x,y in [('top',16,7),('left',7,25),('right',25,25)]:circle(self,name,x,y,5)
""")
SIMPLIFICATIONS[13]='Separated the tangent circles to preserve three equal, clear rings on the integer grid.'
plan(15,'CIRCLE','Two concentric coin outlines.','circle: consistent circular centerlines',"circle(self,'outer',16,16,14)\ncircle(self,'inner',16,16,7)")
SIMPLIFICATIONS[15]='Removed the tiny central stamp stroke, retaining the double-ring coin.'
cutlery="""
self.add_line('fork-left',(2,2),(2,14));self.add_arc('fork-bowl',(2,14),(10,14),radius_x=4,sweep=False);self.add_line('fork-right',(10,14),(10,2));self.add_contour('fork','fork-left','fork-bowl','fork-right')
self.add_line('fork-stem',(6,18),(6,30));self.relate('connect','fork-stem','fork')
self.add_line('knife-stem',(22,2),(22,30));self.add_bezier('knife-curve',(22,2),((30,4),(30,10),(30,20)));self.add_line('knife-base',(30,20),(22,20));self.add_contour('blade','knife-curve','knife-base');self.relate('connect','blade','knife-stem')
"""
for n in (18,19):
 plan(n,'SQUARE','Fork with two clear tines beside a closed curved knife blade.','utensils: broad bowl and open blade counter',cutlery)
 SIMPLIFICATIONS[n]=('Removed the enclosing circle and ' if n==18 else '')+'reduced the fork to two tines while retaining its bowl, handle and the knife blade.'
plan(20,'SQUARE','Crossed two-tine fork and round spoon with clear handles.','utensils-crossed: crossed handles and rounded bowl',"""
self.add_line('fork-left',(2,8),(10,16));self.add_bezier('bowl-left',(10,16),((14,20),(16,20),(18,18)))
self.add_bezier('bowl-right',(18,18),((20,16),(20,14),(16,10)));self.add_line('fork-right',(16,10),(8,2));self.add_contour('fork','fork-left','bowl-left','bowl-right','fork-right')
self.add_line('fork-handle',(18,18),(30,30));self.relate('connect','fork-handle','fork')
circle(self,'spoon',25,7,5)
self.add_line('spoon-handle',(22,11),(14,25));self.relate('connect','spoon-handle','spoon');self.relate('connect','spoon-handle','fork-handle');self.relate('connect','spoon-handle','fork')
""")
SIMPLIFICATIONS[20]='Reduced the fork to two tines and made the spoon bowl circular; retained crossed handles and an open spoon interior.'
plan(21,'SQUARE','Separate circle, square and triangle.','shapes: three distinct geometric forms',"""
circle(self,'circle',9,8,6);box(self,'square',2,22,10,30,0)
self.add_polyline('triangle',(18,30),(24,18),(30,30),(18,30))
""")
SIMPLIFICATIONS[21]='Removed the outer enclosure; retained all three separate shapes.'
measurement="""
self.add_line('top',(6,2),(30,2));self.add_arc('top-round',(6,10),(6,2),radius_x=4)
self.add_polyline('top-jaw',(6,10),(10,10),(14,2))
for a,b in [('top','top-round'),('top','top-jaw'),('top-round','top-jaw')]:self.relate('connect',a,b)
self.add_line('guide',(22,18),(30,18))
self.add_arc('bottom-round',(6,26),(6,18),radius_x=4)
self.add_polyline('bottom-jaw',(6,18),(10,18),(14,26))
self.add_polyline('bottom',(6,26),(30,26),(30,30))
for a,b in [('bottom','bottom-round'),('bottom','bottom-jaw'),('bottom-round','bottom-jaw')]:self.relate('connect',a,b)
"""
for n in (25,27):
 plan(n,'SQUARE','Two rounded measurement jaws, separate middle guide and lower-right extension.','ruler: rounded measurement construction',measurement)
 SIMPLIFICATIONS[n]='Removed the tiny end tick; retained both jaws, middle guide and the vertical extension.'
plan(26,'SQUARE','Two diagonal open chain links and a short connecting stroke.','link: opposing rounded C links',"""
self.add_arc('lower',(6,12),(20,26),radius_x=10,large_arc=True,sweep=False)
self.add_arc('upper',(12,6),(26,20),radius_x=10,large_arc=True,sweep=True)
self.add_line('join',(12,20),(20,12))
""")
SIMPLIFICATIONS[26]='Simplified the inward-bent tips into two clear open links and a central joining stroke.'
plan(40,'SQUARE','Pointed rocket body with integrated fins, cockpit mark and exhaust stem.','rocket: pointed nose and broad integrated fins',"""
self.add_bezier('nose-right',(16,2),((20,4),(26,8),(26,13)))
self.add_polyline('lower',(26,13),(26,17),(30,26),(2,26),(6,17),(6,13))
self.add_bezier('nose-left',(6,13),((6,8),(12,4),(16,2)));self.relate('connect','nose-right','lower');self.relate('connect','nose-left','lower');self.relate('connect','nose-left','nose-right')
self.add_line('cockpit',(16,12),(16,12));self.add_line('exhaust',(16,26),(16,30));self.relate('connect','exhaust','lower')
""")
SIMPLIFICATIONS[40]='Merged the fin seams into the body outline and simplified the cockpit to a round window mark.'
plan(41,'VRECT_XL','Eight-lobed rosette with a center mark and notched ribbon.','award: scalloped seal and attached ribbon',"""
pts=[(13,5),(19,5),(24,7),(24,15),(19,17),(13,17),(8,15),(8,7),(13,5)]
for i,(a,b,r) in enumerate(zip(pts,pts[1:],(3,4,4,4,3,4,4,4))):self.add_arc(f'lobe-{i}',a,b,radius_x=r)
self.add_contour('seal',*[f'lobe-{i}' for i in range(8)],closed=True)
self.add_line('center',(16,11),(16,11))
self.add_polyline('ribbon',(8,15),(8,30),(16,27),(24,30),(24,15));self.relate('connect','ribbon','seal')
""")
SIMPLIFICATIONS[41]='Rendered the small central ring as a round mark and made the ribbon notch shallower; retained the scalloped seal.'
plan(43,'SQUARE','Seated scooter with two open wheels, seat, chassis and upright handle.','bike: external wheel connections and coherent frame',"""
circle(self,'rear',7,25,5);circle(self,'front',25,25,5)
self.add_line('deck',(7,20),(11,20));self.add_bezier('rise',(11,20),((14,20),(15,17),(16,15)))
self.add_line('upper-frame',(16,15),(22,10));self.add_contour('frame','deck','rise','upper-frame');self.relate('connect','frame','rear')
self.add_polyline('steering',(16,2),(20,2),(22,10),(25,20));self.relate('connect','steering','frame');self.relate('connect','steering','front')
self.add_line('seat-post',(12,8),(16,15));self.relate('connect','seat-post','frame')
self.add_line('seat',(8,8),(16,8));self.relate('connect','seat','seat-post')
""")
SIMPLIFICATIONS[43]='Moved axle connections to the tyre boundaries so both wheel openings stay clear; simplified the chassis curve.'
plan(44,'SQUARE','Rounded shield containing a five-ray star mark.','shield-star: open shield silhouette and central five-point symbol',"""
self.add_bezier('roof-left',(2,6),((6,3),(12,2),(16,2)))
self.add_bezier('roof-right',(16,2),((20,2),(26,3),(30,6)))
self.add_line('right',(30,6),(30,15));self.add_bezier('base-right',(30,15),((30,22),(23,28),(16,30)))
self.add_bezier('base-left',(16,30),((9,28),(2,22),(2,15)));self.add_line('left',(2,15),(2,6));self.add_contour('shield','roof-left','roof-right','right','base-right','base-left','left',closed=True)
for i,p in enumerate(((16,9),(22,13),(20,20),(12,20),(10,13))):
 self.add_line(f'ray-{i}',(16,15),p)
 for j in range(i):self.relate('connect',f'ray-{i}',f'ray-{j}')
""")
SIMPLIFICATIONS[44]='Simplified the small outlined star to a five-ray mark, preserving the shield and five-point meaning.'
plan(46,'SQUARE','Connected car with wireless arc, windshield silhouette and two wheel stems.','car / wifi: one clear wireless arc above the car',"""
self.add_arc('wireless',(8,6),(24,6),radius_x=8,radius_y=4)
self.add_polyline('car',(2,26),(2,20),(6,20),(10,12),(22,12),(26,20),(30,20),(30,26),(2,26))
for n,x in [('left',6),('right',26)]:self.add_line(n+'-wheel',(x,26),(x,30));self.relate('connect',n+'-wheel','car')
""")
SIMPLIFICATIONS[46]='Reduced two wireless arcs to one and removed the bumper divider; kept both wheel stems.'
plan(50,'SQUARE','Diagonal syringe with rounded barrel, needle, plunger shaft and cap.','syringe: rounded barrel and separate plunger',"""
self.add_polyline('barrel',(6,18),(16,8),(24,16),(14,26))
self.add_bezier('nose-l',(14,26),((11,29),(9,29),(6,26)))
self.add_bezier('nose-r',(6,26),((3,23),(3,21),(6,18)));self.add_contour('nose','nose-l','nose-r');self.relate('connect','nose','barrel')
self.add_line('needle',(6,26),(2,30));self.relate('connect','needle','nose')
self.add_line('plunger',(20,12),(27,5));self.relate('connect','plunger','barrel')
self.add_line('cap',(24,2),(30,8));self.relate('connect','cap','plunger')
""")
SIMPLIFICATIONS[50]='Removed the two graduation ticks while retaining all functional syringe parts.'

# Review-driven spacing corrections, preserving all remaining major parts.
D[4]=(*D[4][:3],D[4][3].replace("(30,26)","(30,24)").replace("(26,30)","(26,28)").replace("(24,30)","(26,28)"))
D[9]=(*D[9][:3],rotation+D[4][3].replace('self.','r.'))
D[46]=(*D[46][:3],D[46][3].replace('(2,20),(6,20)','(2,18),(7,18)').replace('(26,20),(30,20)','(25,18),(30,18)'))
D[43]=(*D[43][:3],D[43][3].replace("self.add_line('deck',(7,20),(11,20));self.add_bezier('rise',(11,20),((14,20),(15,17),(16,15)))","self.add_line('deck',(7,20),(7,16));self.add_bezier('rise',(7,16),((7,12),(13,12),(16,15)))"))
# Fresh attempts for the remaining complete source compositions.
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'side-repair-50-priority-10'))
from glyph_fit import fit,text
plan(5,'SQUARE','Bicycle with two open tyres, raised saddle, handlebar and connecting frame.','bike: circular wheels and external frame joins',"""
circle(self,'rear',7,25,5);circle(self,'front',25,25,5)
self.add_polyline('frame',(7,20),(12,10),(23,10),(25,20));self.relate('connect','frame','rear');self.relate('connect','frame','front')
self.add_line('seat-post',(12,10),(10,4));self.relate('connect','seat-post','frame')
self.add_line('seat',(6,4),(14,4));self.relate('connect','seat','seat-post')
self.add_polyline('handle',(23,10),(25,2),(30,2));self.relate('connect','handle','frame')
""")
SIMPLIFICATIONS[5]='Removed internal spokes and the small pedal triangle; retained two wheels, saddle, handlebar and frame.'
for n,gid in [(14,'symbol-question'),(48,'symbol-equals'),(49,'letter-r-uppercase')]:
 body,_=fit(gid,13,16,16,f'char{n}');plan(n,'CIRCLE','Original circular enclosure and shared '+gid,'shared typeface',"circle(self,'frame',16,16,14)\n"+body);GLYPHS[n]=(gid,)
 SIMPLIFICATIONS[n]='No parts removed in this fresh framed-glyph attempt.'
body,_=fit('symbol-plus',6,16,12,'plus')
plan(37,'CIRCLE','Circular plus and minus sign.','shared plus glyph and horizontal minus',"circle(self,'frame',16,16,14)\n"+body+"\nself.add_line('minus',(13,21),(19,21))")
GLYPHS[37]=('symbol-plus','symbol-hyphen');SIMPLIFICATIONS[37]='Removed the diagonal separator; retained both arithmetic signs and the circle.'
TEXT[45]=text(('digit-0','symbol-percent'));GLYPHS[45]=TEXT[45]['glyphs'];plan(45,'SQUARE','Zero percent from the existing shared glyphs.','shared typeface',TEXT[45]['body']);SIMPLIFICATIONS[45]='Uniform natural-width shared-glyph layout with integer grid fitting.'
for n in (17,29,31,32,33):
 body,_=fit('symbol-dollar',16,16,16,f'char{n}')
 if n==17:frame="box(self,'page',2,2,30,30,3)\n";shape='SQUARE';parts='Financial document with shared dollar sign.'
 elif n==29:frame="box(self,'phone',4,10,28,30,3)\nself.add_arc('wireless',(8,6),(24,6),radius_x=8,radius_y=4)\n";shape='VRECT_XL';parts='Wireless-payment phone and shared dollar sign.'
 elif n==31:frame="self.add_polyline('bag-top',(10,8),(6,2),(26,2),(22,8))\nself.add_bezier('bag-right',(22,8),((30,16),(30,22),(30,25)))\nself.add_bezier('bag-bottom',(30,25),((30,30),(2,30),(2,25)))\nself.add_bezier('bag-left',(2,25),((2,22),(2,16),(10,8)))\nself.add_line('tie',(10,8),(22,8))\nself.add_contour('bag','bag-right','bag-bottom','bag-left');self.relate('connect','bag-top','bag');self.relate('connect','tie','bag');self.relate('connect','tie','bag-top')\n";shape='SQUARE';parts='Money bag with gathered neck and shared dollar sign.'
 elif n==32:frame="self.add_polyline('bubble',(2,2),(30,2),(30,24),(14,24),(6,30),(6,24),(2,24),(2,2))\n";shape='SQUARE';parts='Money speech bubble with shared dollar sign.'
 else:frame="box(self,'screen',2,2,30,22,2)\nself.add_line('stand',(16,22),(16,30));self.relate('connect','stand','screen')\nself.add_line('foot',(10,30),(22,30));self.relate('connect','foot','stand')\n";shape='SQUARE';parts='Financial monitor with stand and shared dollar sign.'
 plan(n,shape,parts,'shared typeface and original frame',frame+body);GLYPHS[n]=('symbol-dollar',);SIMPLIFICATIONS[n]='Removed minor divider marks; retained the subject enclosure and currency character.'
D[4]=(*D[4][:3],D[4][3].replace("self.add_arc('br',(30,24),(26,28),radius_x=4)","self.add_arc('br',(30,24),(28,26),radius_x=2)").replace("self.add_line('right-bottom',(26,28),(26,28))","self.add_line('right-bottom',(28,26),(28,26))"))
D[9]=(*D[9][:3],rotation+D[4][3].replace('self.','r.'))
D[5]=(*D[5][:3],D[5][3].replace('(12,10)','(12,12)').replace('(23,10)','(23,12)'))
D[43]=(*D[43][:3],D[43][3].replace("(12,8)","(12,4)").replace("(8,8),(16,8)","(8,4),(16,4)"))
# Move ribbon attachments to the actual lower boundary of the seal.
D[41]=(*D[41][:3],D[41][3].replace("(8,15),(8,30),(16,27),(24,30),(24,15)","(8,15),(4,30),(16,27),(28,30),(24,15)"))
D[41]=('SQUARE',*D[41][1:])
# Keep the fork bowl clear of the crossing: handles intersect below both utensils.
D[20]=(*D[20][:3],"""
self.add_polyline('fork',(2,6),(8,12),(14,6),(8,2))
self.add_line('fork-handle',(8,12),(26,30));self.relate('connect','fork-handle','fork')
circle(self,'spoon',25,7,5)
self.add_line('spoon-handle',(22,11),(10,29));self.relate('connect','spoon-handle','spoon');self.relate('connect','spoon-handle','fork-handle')
""")
# Open the nonsemantic outer help frame to give the shared question mark its natural height.
TEXT[14]=text(('symbol-question',));GLYPHS[14]=TEXT[14]['glyphs'];D[14]=('SQUARE','Shared question mark at natural proportions.','shared typeface',TEXT[14]['body']);SIMPLIFICATIONS[14]='Removed the surrounding circle; retained the complete shared question character.'
# Bare equality retains the mathematical meaning while avoiding a crowded enclosure.
body,_=fit('symbol-equals',12,16,16,'equal')
D[48]=('HRECT_S','Two equal shared horizontal equality strokes.','shared typeface',body)
SIMPLIFICATIONS[48]='Removed the enclosing circle; retained the shared equality glyph and its proportions.'

D[41]=('VRECT_XL',*D[41][1:])
TEXT[48]=text(('symbol-equals',));D[48]=('SQUARE',D[48][1],D[48][2],TEXT[48]['body'])

SIMPLIFICATIONS[45]='Shared zero and percent glyphs; percent counters each shifted outward by one grid unit to clear the slash, without changing their shapes.'
