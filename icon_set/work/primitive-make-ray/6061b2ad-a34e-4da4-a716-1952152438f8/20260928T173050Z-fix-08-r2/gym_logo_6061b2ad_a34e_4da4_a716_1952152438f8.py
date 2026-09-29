"""Concentric circles, four diagonal spokes, central open loop; all radii shared.
Keyshape: CIRCLE. Uniform 4px SOLO48 stroke.
Construction: No useful exact Lucide brand match; shared geometric construction.
Revision: Restored the central open loop, diagonal spokes and three clear nested levels.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '6061b2ad-a34e-4da4-a716-1952152438f8'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__gym-logo/20260928T173050Z-thuan-mac/reference/gym logo_6061b2ad-a34e-4da4-a716-1952152438f8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'gym-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('gym', 'logo')

    def build(self):
        # Concentric contours split at mirrored integer diagonal nodes; cubic tangents preserve circular flow.
        for name,points,controls in [
         ('outer',[(10,10),(38,10),(38,38),(10,38)],[(18,2,30,2),(46,18,46,30),(30,46,18,46),(2,30,2,18)]),
         ('inner',[(15,15),(33,15),(33,33),(15,33)],[(20,10,28,10),(38,20,38,28),(28,38,20,38),(10,28,10,20)])]:
            steps=[(*points[(i+1)%4],*controls[i]) for i in range(4)]
            self.path(name,points[0],*steps,closed=True)
        for name,a,b in [('nw',(10,10),(15,15)),('ne',(38,10),(33,15)),('se',(38,38),(33,33)),('sw',(10,38),(15,33))]:
            self.add_line(name,a,b)
            self.relate('connect','outer',name);self.relate('connect','inner',name)
        self.path('loop',(27,28),(24,19,31,23,29,19),(21,28,19,19,17,25))

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

# User explicitly delegated drawing-specific exception decisions. Automatic findings are retained.
Drawing.exception = {'reason': 'The central open loop and four diagonal spokes are essential to this logo. Keep the three clear concentric levels and true spoke joins, accepting the inner-loop spacing advisories.', 'approved_by': 'gpt-6 under explicit user-delegated exception authority', 'approved_on': '2026-09-29', 'svg_sha256': 'b645727e2a9f7d5445e3d53852001b5e411c3abaa0f21227f0e70d045a871465'}
