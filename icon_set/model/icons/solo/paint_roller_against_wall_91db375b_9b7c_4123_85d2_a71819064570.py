"""Paint Roller against Wall.

Symbol plan: A wall corner above a rectangular roller with a tangent bent axle. The wall is partial and the grip becomes one stroke to preserve clear space.
Lucide construction: paint-roller; original and atomic-debug inspected.
Keyshape: SQUARE; centerline (6,6)-(42,42); ink (4,4)-(44,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '91db375b-9b7c-4123-85d2-a71819064570'
SOURCE_PATH = 'pictographic-primitives/construction/construction paint_91db375b-9b7c-4123-85d2-a71819064570.svg'
AUTHOR = 'gpt-6'


class PaintRollerAgainstWall(Solo48):
    icon_id = 'paint-roller-against-wall'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'construction'
    categories = ('construction', 'primitives')
    aliases = ()
    keywords = ('paint', 'roller', 'against', 'wall')

    def build(self):
        self.path('wall',(6,10),(6,6),(42,6),(42,14))
        self.path('roller',(8,18),(24,18),(26,20,2,2,True),(26,24),(26,28),(24,30,2,2,True),(8,30),(6,28,2,2,True),(6,20),(8,18,2,2,True),closed=True)
        self.path('axle',(26,24),(34,24),(38,28,4,4,True),(38,34),(34,38,4,4,True),(22,38),(18,42,4,4,False))
        self.relate('connect','roller','axle')

    def path(self, name, start, *steps, closed=False):
        members=[]
        point=start
        for i, step in enumerate(steps):
            member=f"{name}-{i+1}"
            if len(step)==2:
                self.add_line(member, point, step)
                point=step
            else:
                x,y,rx,ry,sweep=step
                self.add_arc(member, point, (x,y), radius_x=rx, radius_y=ry, sweep=sweep)
                point=(x,y)
            members.append(member)
        self.add_contour(name,*members,closed=closed)

    def circle(self, name, x, y, r):
        self.path(name,(x-r,y),(x+r,y,r,r,True),(x-r,y,r,r,True),closed=True)

    def rect(self, name, x, y, w, h, r=2):
        self.path(name,(x+r,y),(x+w-r,y),(x+w,y+r,r,r,True),
                  (x+w,y+h-r),(x+w-r,y+h,r,r,True),(x+r,y+h),
                  (x,y+h-r,r,r,True),(x,y+r),(x+r,y,r,r,True),closed=True)
