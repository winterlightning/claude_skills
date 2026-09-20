SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/side-repair-50-priority-10/batch.json'
AUTHOR='gpt-6'
from glyph_fit import fit,text
D={};TEXT={};GLYPHS={};SIMPLIFICATIONS={}
def plan(n,shape,parts,body):D[n]=(shape,parts,'shared typeface / geometric source construction',body)
for n,ids in [(2,('letter-d-uppercase','letter-w-uppercase','letter-g-uppercase')),(3,('letter-w-uppercase','letter-a-uppercase','letter-v-uppercase')),(10,('symbol-hryvnia',)),(11,('symbol-kip',)),(12,('symbol-lira-two-bar',)),(14,('symbol-pound',)),(15,('symbol-prescription',)),(16,('symbol-rupee',)),(18,('symbol-won-one-bar',))]:
 TEXT[n]=text(ids);plan(n,'SQUARE','Shared glyphs '+', '.join(ids)+' at 32px ink height and natural width.',TEXT[n]['body']);GLYPHS[n]=ids
 SIMPLIFICATIONS[n]='Shared glyph reuse with integer-grid fitting; tiny W turns use one consistent round-join hint.' if n in (2,3,18) else 'No character substitution; uses the newly added shared glyph.'
plan(1,'SQUARE','Tactical diagram retaining both X marks, the circle and curved upward arrow.',"""
circle(self,'start',7,25,5)
for name,x,y,r in [('upper',7,6,3),('lower',27,27,3)]:
 self.add_line(name+'-a',(x-r,y-r),(x+r,y+r));self.add_line(name+'-b',(x-r,y+r),(x+r,y-r));self.relate('connect',name+'-a',name+'-b')
self.add_bezier('route',(7,20),((7,14),(24,20),(24,12)))
self.add_line('up',(24,12),(24,2));self.add_contour('arrow','route','up');self.relate('connect','arrow','start')
self.add_polyline('tip',(18,8),(24,2),(30,8));self.relate('connect','tip','arrow')
""")
SIMPLIFICATIONS[1]='Removed the surrounding board frame; retained every tactical mark and the arrow.'
plan(4,'VRECT_L','Single strong lightning bolt representing the repeated lightning state.',"self.add_polyline('bolt',(26,2),(6,18),(22,18),(10,30))")
SIMPLIFICATIONS[4]='Reduced the three repeated bolts to one clear bolt.'
plan(5,'SQUARE','Open circular profile with a complete selection pointer and diagonal tail.',"""
self.add_arc('profile',(20,6),(6,20),radius_x=10,large_arc=True,sweep=False)
self.add_polyline('pointer',(13,13),(30,20),(23,23),(20,30),(13,13))
self.add_line('tail',(23,23),(30,30));self.relate('connect','tail','pointer')
""")
SIMPLIFICATIONS[5]='Removed the internal hair part and cropped the head behind the pointer; retained the cursor and its tail.'
# Try shared characters inside the original concept frames before reducing them.
for n,gid in [(6,'symbol-bitcoin'),(9,'symbol-yuan-one-bar'),(17,'symbol-pound')]:
 body,_=fit(gid,13,16,16,f'char{n}');plan(n,'CIRCLE','Circular currency badge with shared '+gid,"circle(self,'frame',16,16,14)\n"+body);GLYPHS[n]=(gid,)
for n,gid in [(7,'symbol-bitcoin'),(8,'symbol-pound'),(13,'symbol-pound')]:
 body,_=fit(gid,15,16,16,f'char{n}')
 if n==7:
  frame="self.add_polyline('bubble',(2,2),(30,2),(30,24),(14,24),(6,30),(6,24),(2,24),(2,2))\n";shape='SQUARE';parts='Currency speech bubble retaining the shared Bitcoin sign and tail.'
 elif n==8:
  frame="box(self,'page',2,2,30,30,3)\n";shape='SQUARE';parts='Invoice page with a shared pound sign.';SIMPLIFICATIONS[n]='Removed the two small invoice text lines.'
 else:
  frame="box(self,'phone',4,10,28,30,3)\nself.add_arc('wireless',(8,5),(24,5),radius_x=10,radius_y=3)\n";shape='VRECT_XL';parts='Wireless-payment phone retaining shared pound character.';SIMPLIFICATIONS[n]='Reduced two wireless arcs to one and removed the phone footer.'
 plan(n,shape,parts,frame+body);GLYPHS[n]=(gid,)
# Currency badges use the full shared character when the enclosing coin ring
# would close its counters at a 4px stroke; the currency identity is retained.
for n,gid in [(6,'symbol-bitcoin'),(17,'symbol-pound')]:
 TEXT[n]=text((gid,));GLYPHS[n]=(gid,);plan(n,'SQUARE','Shared '+gid+' at natural width and full 32px ink height.',TEXT[n]['body'])
 SIMPLIFICATIONS[n]='Removed the surrounding coin ring; preserved the complete currency character and its shared proportions.'
body,_=fit('symbol-yuan-one-bar',12,16,16,'char9')
D[9]=('CIRCLE','Circular yuan badge with the shared one-bar yuan.','shared typeface',"circle(self,'frame',16,16,14)\n"+body)
