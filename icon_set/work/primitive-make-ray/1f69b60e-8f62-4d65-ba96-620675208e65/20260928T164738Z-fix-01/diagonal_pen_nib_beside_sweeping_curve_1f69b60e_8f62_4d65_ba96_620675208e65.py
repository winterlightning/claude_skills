"""vectors pen draw.
The free stroke had abrupt bends and the nib was narrow. Restore a smooth sweeping stroke and broader pointed nib with a diagonal slit.
Lucide search radial alignment principle; original nib and free stroke.
Plan: subject-specific coherent contours; repeated members share dimensions.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '1f69b60e-8f62-4d65-ba96-620675208e65'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__diagonal-pen-nib-beside-sweeping-curve/20260928T164738Z-thuan-mac/reference/vectors pen draw_1f69b60e-8f62-4d65-ba96-620675208e65.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'diagonal-pen-nib-beside-sweeping-curve'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'design'
    aliases = ()
    keywords = ('diagonal', 'pen', 'nib', 'beside', 'sweeping', 'curve')

    def build(self):

        def path(n,start,*commands,closed=False):
            pt=start; members=[]
            for i,c in enumerate(commands):
                mid=f'{n}-{i}'
                if c[0]=='L': self.add_line(mid,pt,c[1]); end=c[1]
                elif c[0]=='A':
                    _,end,rx,ry,sweep=c
                    self.add_arc(mid,pt,end,radius_x=rx,radius_y=ry,sweep=sweep)
                elif c[0]=='C':
                    _,a,b,end=c; self.add_bezier(mid,pt,(a,b,end))
                pt=end;members.append(mid)
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x,y-r),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),('A',(x,y-r),r,r,True),closed=True)
        def box(n,l,t,r,b,rad=2):
            path(n,(l+rad,t),('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True),closed=True)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def bez(n,start,*s): self.add_bezier(n,start,*s)
        def join(a,b): self.relate('connect',a,b)
        bez('stroke',(6,6),((27,11),(2,33),(9,40)),((11,42),(14,42),(17,41)))
        poly('nib',(22,42),(28,23),(38,19),(44,25),(40,35),(22,42))
        line('slit',(22,42),(33,31));join('slit','nib')
        line('holder-a',(38,19),(42,15));line('holder-b',(44,25),(46,22));join('holder-a','nib');join('holder-b','nib')
