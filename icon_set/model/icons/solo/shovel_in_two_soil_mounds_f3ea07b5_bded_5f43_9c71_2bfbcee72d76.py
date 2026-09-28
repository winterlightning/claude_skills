"""Shovel in Two Soil Mounds.

Symbol plan: A diagonal T-grip shovel enters two soil mounds. The buried lower blade and soil baseline are omitted; the visible blade joins the taller mound.
Lucide construction: shovel; original and atomic-debug inspected.
Keyshape: SQUARE; centerline (6,6)-(42,42); ink (4,4)-(44,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f3ea07b5-bded-5f43-9c71-2bfbcee72d76'
SOURCE_PATH = 'pictographic-primitives/construction/construction shovel_f3ea07b5-bded-5f43-9c71-2bfbcee72d76.svg'
AUTHOR = 'gpt-6'


class ShovelInTwoSoilMounds(Solo48):
    icon_id = 'shovel-in-two-soil-mounds'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'construction'
    categories = ('construction', 'primitives')
    aliases = ()
    keywords = ('shovel', 'in', 'two', 'soil', 'mounds')

    def build(self):
        self.path('grip',(6,14),(10,10),(14,6))
        self.add_line('shaft',(10,10),(24,24));self.relate('connect','shaft','grip')
        self.path('blade',(24,24),(30,18),(36,24),(32,32))
        self.relate('connect','shaft','blade')
        self.path('soil',(6,42),(14,34,8,8,True),(22,42,8,8,True),(32,32,10,10,True),(42,42,10,10,True))
        self.relate('connect','blade','soil')

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
