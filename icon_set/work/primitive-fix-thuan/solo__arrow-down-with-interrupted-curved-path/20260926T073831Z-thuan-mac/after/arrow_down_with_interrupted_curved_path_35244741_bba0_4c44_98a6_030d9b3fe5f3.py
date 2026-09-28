"""Arrow Down with Interrupted Curved Path.

Symbol plan: Three separated runs form a downward winding arrow. Tangent quarter-circle turns preserve the interrupted path without tiny dashes.
Lucide: corner-down-right; original and atomic-debug geometry inspected.
Keyshape: SQUARE; centerline (6,6)-(42,42); ink (4,4)-(44,44).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '35244741-bba0-4c44-98a6-030d9b3fe5f3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__arrow-down-with-interrupted-curved-path/20260926T073831Z-thuan-mac/reference/dash down fast large head_35244741-bba0-4c44-98a6-030d9b3fe5f3.svg'
AUTHOR = 'claude-opus-5-5'


class ArrowDownWithInterruptedCurvedPath(Solo48):
    icon_id = 'arrow-down-with-interrupted-curved-path'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('arrow', 'direction', 'navigation', 'pointer', 'movement', 'route', 'flow', 'orientation')

    def build(self):
        # Revision per review: a straight vertical shaft now rises above the arrowhead. The two
        # interrupted curved runs are tighter so the gaps (9 each) and the shaft fit: run 1 drops
        # from (6, 6) and turns right on an r6 quarter arc to (12, 16); run 2 goes right from
        # (21, 16) and turns down on an r6 quarter arc to (36, 22); the shaft falls from (36, 31)
        # to the tip (36, 42), 5 above the 45-degree arrowhead arms (30, 36)/(42, 36).
        self.path('first-run', (6, 6), (6, 10), (12, 16, 6, 6, False))
        self.path('second-run', (21, 16), (30, 16), (36, 22, 6, 6, True))
        self.add_line('shaft', (36, 31), (36, 42))
        self.path('arrowhead', (30, 36), (36, 42), (42, 36)); self.relate('connect', 'shaft', 'arrowhead')

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
