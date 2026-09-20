SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/side-final-eight/batch.json'
AUTHOR='gpt-6'
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'side-repair-50-priority-10'))
from glyph_fit import fit
D={};GLYPHS={};TEXT={};TALL={1,4}
def plan(n,shape,parts,body):D[n]=(shape,parts,'source composition; shared small-size character construction',body)
def dollar(y):
 return f"""
self.add_line('dollar-top',(17,{y}),(16,{y}))
self.add_arc('dollar-upper',(16,{y}),(16,{y+4}),radius_x=4,radius_y=2,sweep=False)
self.add_arc('dollar-lower',(16,{y+4}),(16,{y+8}),radius_x=4,radius_y=2,sweep=True)
self.add_line('dollar-bottom',(16,{y+8}),(15,{y+8}));self.add_contour('dollar','dollar-top','dollar-upper','dollar-lower','dollar-bottom')
self.add_line('tick-top',(16,{y-2}),(16,{y}));self.add_line('tick-bottom',(16,{y+8}),(16,{y+9}))
self.relate('connect','tick-top','dollar');self.relate('connect','tick-bottom','dollar')
"""
plan(1,'SQUARE','Bitcoin chat bubble with two clear B counters, paired currency ticks and a lower-left tail.',"""
self.add_polyline('bubble',(2,2),(30,2),(30,40),(16,40),(6,46),(6,40),(2,40),(2,2))
self.add_polyline('upper',(10,30),(10,14),(18,14))
self.add_arc('bowl-top',(18,14),(18,22),radius_x=4)
self.add_line('middle',(18,22),(10,22));self.relate('connect','upper','bowl-top');self.relate('connect','middle','upper');self.relate('connect','middle','bowl-top')
self.add_arc('bowl-bottom',(18,22),(18,30),radius_x=4)
self.add_line('bottom',(18,30),(10,30));self.add_contour('lower','bowl-bottom','bottom');self.relate('connect','lower','upper');self.relate('connect','lower','middle')
for name,a,b in [('tick-tl',(12,10),(12,14)),('tick-tr',(20,10),(20,16)),('tick-bl',(12,30),(12,34)),('tick-br',(20,28),(20,34))]:
 self.add_line(name,a,b)
 self.relate('connect',name,'upper' if name=='tick-tl' else 'bowl-top' if name=='tick-tr' else 'lower')
""")
plan(2,'SQUARE','Money chat bubble retaining its tail and the approved light dollar mark.',"self.add_polyline('bubble',(2,2),(30,2),(30,26),(16,26),(8,30),(8,26),(2,26),(2,2))\n"+dollar(10))
plan(3,'SQUARE','Shield with a genuine five-point outlined star; upper frame opens around the star.',"""
self.add_polyline('star',(16,2),(20,8),(26,8),(21,13),(23,20),(16,16),(9,20),(11,13),(6,8),(12,8),(16,2))
self.add_line('left',(2,14),(2,19));self.add_bezier('shield-left',(2,19),((2,24),(10,28),(16,30)))
self.add_bezier('shield-right',(16,30),((22,28),(30,24),(30,19)));self.add_line('right',(30,19),(30,14));self.add_contour('shield','left','shield-left','shield-right','right')
""")
body,_=fit('symbol-pound',18,16,16,'pound')
shift="""
class Offset:
 def add_line(_,n,a,b):return self.add_line(n,(a[0],a[1]+10),(b[0],b[1]+10))
 def add_bezier(_,n,a,ps):return self.add_bezier(n,(a[0],a[1]+10),tuple((x,y+10) for x,y in ps))
 def __getattr__(_,n):return getattr(self,n)
g=Offset()
"""
plan(4,'SQUARE','Tall clipped-corner invoice with the shared pound glyph.',"self.add_polyline('page',(2,2),(20,2),(30,12),(30,46),(2,46),(2,2))\n"+shift+body.replace('self.','g.'));GLYPHS[4]=('symbol-pound',)
plan(5,'SQUARE','Clipped-corner dollar document retaining the earlier light-dollar appearance.',"self.add_polyline('page',(2,2),(20,2),(30,12),(30,30),(2,30),(2,2))\n"+dollar(14))
plan(6,'CIRCLE','Registered mark retaining the complete circle and a compact R with an open bowl.',"""
circle(self,'ring',16,16,14)
self.add_polyline('r-stem',(12,22),(12,10),(16,10))
self.add_bezier('r-bowl',(16,10),((22,10),(22,18),(16,18)))
self.add_line('r-middle',(16,18),(12,18));self.relate('connect','r-stem','r-bowl');self.relate('connect','r-middle','r-stem');self.relate('connect','r-middle','r-bowl')
self.add_line('r-leg',(16,18),(20,22));self.relate('connect','r-leg','r-bowl');self.relate('connect','r-leg','r-middle')
""")
plan(7,'SQUARE','Hryvnia: reverse-S with two crossbars and a smooth diagonal middle.',"""
self.add_bezier('top',(8,2),((22,2),(30,2),(22,10)))
self.add_line('middle',(22,10),(10,22))
self.add_bezier('bottom',(10,22),((2,30),(10,30),(24,30)))
self.add_contour('reverse-s','top','middle','bottom')
self.add_line('upper-bar',(2,10),(30,10));self.add_line('lower-bar',(2,22),(30,22))
self.relate('connect','upper-bar','reverse-s');self.relate('connect','lower-bar','reverse-s')
""")
plan(8,'SQUARE','Monitor with the lighter dollar and a simple central stand.',"box(self,'screen',2,2,30,26,3)\nself.add_line('stand',(16,26),(16,30));self.relate('connect','stand','screen')\n"+dollar(10))
D[3]=(*D[3][:3],D[3][3].replace('((2,24),(10,28),(16,30))','((2,26),(10,28),(16,30))').replace('((22,28),(30,24),(30,19))','((22,28),(30,26),(30,19))'))
D[8]=(*D[8][:3],D[8][3].replace('(16,8),(16,10)','(16,9),(16,10)'))

# Shared optical forms own the character geometry, independently of each frame.
for n,fn in [(1,'draw_bitcoin'),(6,'draw_registered_r')]:
 D[n]=(*D[n][:3],D[n][3].strip().split('\n',1)[0]+f"\nfrom icon_set.typeface.sub32 import {fn}\n{fn}(self)")
D[7]=(*D[7][:3],"from icon_set.typeface.sub32 import draw_hryvnia\ndraw_hryvnia(self)")
for n,y,stub in [(2,10,2),(5,14,2),(8,10,1)]:
 frame=D[n][3].split("self.add_line('dollar-top'")[0]
 D[n]=(*D[n][:3],frame+f"from icon_set.typeface.sub32 import draw_dollar\ndraw_dollar(self,{y},{stub})")
GLYPHS.update({1:('symbol-bitcoin',),2:('symbol-dollar',),5:('symbol-dollar',),6:('letter-r-uppercase',),7:('symbol-hryvnia',),8:('symbol-dollar',)})
