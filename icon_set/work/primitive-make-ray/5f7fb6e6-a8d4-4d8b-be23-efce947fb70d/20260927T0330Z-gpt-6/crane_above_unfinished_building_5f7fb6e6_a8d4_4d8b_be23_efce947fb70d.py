"""Crane above Unfinished Building.

Symbol plan: A mast, braced boom and hanging hook rise over a stepped unfinished wall. Dense paired supports and latticework are reduced to one mast.
Lucide construction: construction; original and atomic-debug inspected.
Keyshape: SQUARE; centerline (6,6)-(42,42); ink (4,4)-(44,44).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '5f7fb6e6-a8d4-4d8b-be23-efce947fb70d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__crane-above-unfinished-building/20260927T032242Z-thuan-mac-1/reference/construction building_5f7fb6e6-a8d4-4d8b-be23-efce947fb70d.svg'
AUTHOR = "gpt-6"


class CraneAboveUnfinishedBuilding(Solo48):
    icon_id = 'crane-above-unfinished-building'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'construction'
    categories = ('construction', 'primitives')
    aliases = ()
    keywords = ('crane', 'above', 'unfinished', 'building')

    def build(self):
        self.path('building',(6,42),(6,32),(24,32),(24,26),(32,26),(32,34),(42,34),(42,42),(6,42),closed=True)
        self.path('mast',(14,18),(14,32));self.relate('connect','mast','building')
        self.path('roof',(6,18),(18,6),(42,18),(6,18),closed=True);self.relate('connect','roof','mast')
        
        self.path('hook',(42,18),(42,26),(40,28,2,2,True));self.relate('connect','hook','roof')

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
