"""Arrow Down with Broad Triangular Head.

Symbol plan: A broad triangular arrowhead and a short capsule-ended shaft. Shared shoulders and a rounded shaft cap preserve the source; all directions derive from one integer construction.
Lucide: arrow-big-down; original and atomic-debug geometry inspected.
Keyshape: VRECT_L; centerline (8,4)-(40,44); ink (6,2)-(42,46).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ccdf4288-9efa-52e7-84f7-316367905bed'
SOURCE_PATH = 'pictographic-primitives/arrows/end point triangle arrow bottom_ccdf4288-9efa-52e7-84f7-316367905bed.svg'
AUTHOR = 'gpt-6'

class ArrowDownWithBroadTriangularHead(Solo48):
    icon_id = 'arrow-down-with-broad-triangular-head'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'direction', 'navigation', 'pointer', 'movement', 'route', 'flow', 'orientation')

    def build(self):
        direction='down'
        def p(x,y):
            if direction=='down':return (x,y)
            if direction=='up':return (48-x,48-y)
            if direction=='left':return (48-y,x)
            return (y,48-x)
        self.path('arrow',p(20,24),p(20,8),(*p(24,4),*p(20,6),*p(22,4)),(*p(28,8),*p(26,4),*p(28,6)),p(28,24),p(40,24),p(24,44),p(8,24),p(20,24),closed=True)

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
