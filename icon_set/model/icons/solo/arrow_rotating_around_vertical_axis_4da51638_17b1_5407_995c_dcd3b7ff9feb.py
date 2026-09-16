"""Arrow Rotating around Vertical Axis.

Symbol plan: A broad elliptical return curves around the vertical axis, ending in mirrored inward-pointing arrowheads. Shared cubic tangents keep the upper turns smooth; the crossing uses an explicit axis junction.
Lucide: rotate-3d; original and atomic-debug geometry inspected.
Keyshape: VRECT_L; centerline (8,4)-(40,44); ink (6,2)-(42,46).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4da51638-17b1-5407-995c-dcd3b7ff9feb'
SOURCE_PATH = 'pictographic-primitives/arrows/d rotation y axis_4da51638-17b1-5407-995c-dcd3b7ff9feb.svg'
AUTHOR = 'gpt-6'


class ArrowRotatingAroundVerticalAxis(Solo48):
    icon_id = 'arrow-rotating-around-vertical-axis'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'direction', 'navigation', 'pointer', 'movement', 'route', 'flow', 'orientation')

    def build(self):
        self.path('axis',(24,4),(24,32),(24,44))
        self.path('rotation',(16,14),(8,24,12,16,8,18),(24,32,16,8,False),(40,24,16,8,False),(32,14,40,18,36,16))
        self.relate('connect','axis','rotation')
        for n,mirror in [('left',False),('right',True)]:
            def p(x,y):return (48-x if mirror else x,y)
            self.path(n+'-head',p(8,10),p(16,14),p(16,22));self.relate('connect',n+'-head','rotation')

    def path(self, name, start, *steps, closed=False):
        members=[]
        point=start
        for index, step in enumerate(steps):
            member=f"{name}-{index+1}"
            if len(step)==2:
                self.add_line(member,point,step)
                point=step
            elif len(step)==5:
                x,y,rx,ry,sweep=step
                self.add_arc(member,point,(x,y),radius_x=rx,radius_y=ry,sweep=sweep)
                point=(x,y)
            else:
                x,y,cx1,cy1,cx2,cy2=step
                self.add_bezier(member,point,((cx1,cy1),(cx2,cy2),(x,y)))
                point=(x,y)
            members.append(member)
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,x,y,r):
        self.path(name,(x,y-r),(x+r,y,r,r,True),(x,y+r,r,r,True),
                  (x-r,y,r,r,True),(x,y-r,r,r,True),closed=True)

    def rect(self,name,x,y,w,h,r=2):
        self.path(name,(x+r,y),(x+w-r,y),(x+w,y+r,r,r,True),
                  (x+w,y+h-r),(x+w-r,y+h,r,r,True),(x+r,y+h),
                  (x,y+h-r,r,r,True),(x,y+r),(x+r,y,r,r,True),closed=True)
