"""Two diagonal, nested L-shaped outlined bands, each with shared cap and corner radii.
Keyshape: SQUARE. Uniform 4px SOLO48 stroke.
Construction: No useful exact Lucide brand match; shared geometric construction.
Revision: Widened the bands, regularized rounded ends and elbows, and restored the diagonal nesting.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e542d314-5b0f-4e8e-928d-604b7d3d4044'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__google-optimize-logo/20260928T173050Z-thuan-mac/reference/google optimize logo_e542d314-5b0f-4e8e-928d-604b7d3d4044.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'google-optimize-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('google', 'optimize', 'logo')

    def build(self):
        for name,x,y,w,h in [('upper',21,6,21,20),('lower',11,25,15,17)]:
            r=5;right=x+w
            self.path(name,(x,y),(right-r,y),(right,y+r,r,r,True),(right,y+h-r),
                      (right-10,y+h-r,5,5,True),(right-10,y+10),(x,y+10),
                      (x,y,5,5,True),closed=True)

    def path(self, name, start, *steps, closed=False):
        members=[]; here=start
        for j,step in enumerate(steps):
            member=f'{name}-{j}'
            if len(step)==2:
                self.add_line(member,here,step); end=step
            elif len(step)==5:
                x,y,rx,ry,sweep=step;end=(x,y)
                self.add_arc(member,here,end,radius_x=rx,radius_y=ry,sweep=sweep)
            else:
                x,y,c1x,c1y,c2x,c2y=step;end=(x,y)
                self.add_bezier(member,here,((c1x,c1y),(c2x,c2y),end))
            members.append(member);here=end
        self.add_contour(name,*members,closed=closed)

    def ring(self,name,x,y,rx,ry=None):
        ry=rx if ry is None else ry
        self.path(name,(x-rx,y),(x,y-ry,rx,ry,True),(x+rx,y,rx,ry,True),
                  (x,y+ry,rx,ry,True),(x-rx,y,rx,ry,True),closed=True)

    def rect(self,name,x,y,w,h,r=3):
        self.path(name,(x+r,y),(x+w-r,y),(x+w,y+r,r,r,True),(x+w,y+h-r),
                  (x+w-r,y+h,r,r,True),(x+r,y+h),(x,y+h-r,r,r,True),
                  (x,y+r),(x+r,y,r,r,True),closed=True)


    def cups(self,top=24,bottom=44):
        for side,s in [('left',1),('right',-1)]:
            def p(x,y):return (24+s*(x-24),y)
            def c(x,y,a,b,d,e):return (*p(x,y),*p(a,b),*p(d,e))
            self.path(side+'-hand',p(11,bottom),c(4,top+9,11,bottom-4,4,top+14),p(4,top),
                      (*p(10,top),3,3,s==1),p(10,top+7),
                      c(14,top+5,10,top+4,12,top+3),p(18,top+10),
                      c(20,top+14,19,top+11,20,top+12),p(20,bottom))
            self.add_line(side+'-thumb-crease',p(10,top+7),p(14,top+12))
            self.relate('connect',side+'-hand',side+'-thumb-crease')
