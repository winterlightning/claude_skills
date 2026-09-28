"""House with Stacked Bricks.

Symbol plan: A house silhouette behind two staggered masonry courses. Perspective lines and door are omitted for the brick stack.
Lucide construction: house; original and atomic-debug inspected.
Keyshape: SQUARE; centerline (6,6)-(42,42); ink (4,4)-(44,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2ba11ba8-365c-41f5-be66-b10c2e064768'
SOURCE_PATH = 'pictographic-primitives/construction/construction house_2ba11ba8-365c-41f5-be66-b10c2e064768.svg'
AUTHOR = 'gpt-6'


class HouseWithStackedBricks(Solo48):
    icon_id = 'house-with-stacked-bricks'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'construction'
    categories = ('construction', 'primitives')
    aliases = ()
    keywords = ('house', 'with', 'stacked', 'bricks')

    def build(self):
        self.path('house',(6,24),(6,20),(24,6),(42,20),(42,42),(30,42))
        self.path('bricks',(6,42),(6,34),(14,34),(14,26),(30,26),(30,34),(22,34),(22,42),(6,42),closed=True)
        self.add_line('course',(14,34),(22,34));self.relate('connect','course','bricks')
        self.add_line('ground',(22,42),(30,42));self.relate('connect','ground','bricks');self.relate('connect','ground','house')

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
