"""A car emits jagged noise marks beneath a lightning bolt.
Plan: complete reference composition, coherent strokes and parameterized repeat definitions.
SOLO48 SQUARE; omissions: Fine body rounding and window divider omitted; wheels and sound marks retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='0cd83d52-cde5-4493-95b0-2a1a4f137c27'
SOURCE_PATH='icon_set/work/todo-references/noise pollution car_0cd83d52-cde5-4493-95b0-2a1a4f137c27.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='noise-pollution-car'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('noise', 'pollution', 'car')

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self,n,x,y,w,h,r=2):
        p=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        ids=[]
        for i in range(8):
            k=n+'-'+str(i);ids.append(k)
            if i%2:self.add_arc(k,p[i],p[(i+1)%8],radius_x=r)
            else:self.add_line(k,p[i],p[(i+1)%8])
        self.add_contour(n,*ids,closed=True)

    def build(self):

        self.add_polyline('bolt',(26,6),(20,14),(26,14),(24,20),(32,12),(26,12),closed=True)
        self.add_polyline('noise-left',(6,18),(9,21),(10,19),(12,22))
        self.add_polyline('noise-right',(42,14),(40,18),(42,20),(40,24))
        self.circle('wheel-left',14,39,3);self.circle('wheel-right',34,39,3)
        self.add_bezier('front',(11,39),((6,39),(6,34),(14,32)))
        self.add_polyline('roof',(14,32),(18,28),(30,28),(34,32))
        self.add_bezier('rear',(34,32),((42,32),(42,39),(37,39)))
        self.add_line('chassis',(17,39),(31,39))
        self.relate('connect','front','wheel-left');self.relate('connect','front','roof');self.relate('connect','roof','rear');self.relate('connect','rear','wheel-right')
        self.relate('connect','chassis','wheel-left');self.relate('connect','chassis','wheel-right')

# Final visible bounds: (4, 4, 44, 44)
# Construction: Paired equal-radius wheels, coherent body contours and a sloped roof.
# Final reductions: Fine body rounding and window divider omitted; wheels and sound marks retained.
# Visual review: Car, wheels, lightning and both jagged noise marks remain clear. Lightning is compact and bold; window divider and fine body details omitted.
