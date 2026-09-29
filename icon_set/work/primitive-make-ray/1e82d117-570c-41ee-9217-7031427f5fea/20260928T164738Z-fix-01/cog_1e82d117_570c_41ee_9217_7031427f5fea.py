"""cog.
The gear had uneven valleys and a stray center dot absent from the original. Make six balanced teeth and remove that dot.
Original six-tooth outline; shared mirrored parameters.
Plan: subject-specific coherent contours; repeated members share dimensions.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '1e82d117-570c-41ee-9217-7031427f5fea'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cog/20260928T164738Z-thuan-mac/reference/cog_1e82d117-570c-41ee-9217-7031427f5fea.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cog'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'interface-essential'
    aliases = ()
    keywords = ('cog',)

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
        # Top and bottom teeth, with two teeth on each side. Mirror about both axes.
        upper=[(20,6),(28,6),(30,14),(38,12),(42,20),(36,24)]
        lower=[(x,48-y) for x,y in reversed(upper[:-1])]
        left=[(48-x,y) for x,y in reversed(upper[2:]+lower[:-2])]
        poly('gear',(20,6),(28,6),(30,14),(38,12),(42,20),(36,24),(42,28),(38,36),(30,34),(28,42),(20,42),(18,34),(10,36),(6,28),(12,24),(6,20),(10,12),(18,14),closed=True)
