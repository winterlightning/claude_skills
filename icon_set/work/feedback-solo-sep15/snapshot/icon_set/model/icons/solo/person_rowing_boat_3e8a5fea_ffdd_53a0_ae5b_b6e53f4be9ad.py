"""person-rowing-boat: Seated rower with bent arms, boat and an oar. Shared full_body_ref.png: head center (24,11), radius 3 and shoulder y22 give exactly 4 units of ink clearance. Water omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3e8a5fea-ffdd-53a0-ae5b-b6e53f4be9ad'
SOURCE_PATH = 'pictographic-primitives/outdoors/canoe person_3e8a5fea-ffdd-53a0-ae5b-b6e53f4be9ad.svg'
AUTHOR = 'gpt-6'


class PersonRowingBoat(Solo48):
    icon_id = 'person-rowing-boat'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('rowing', 'boat', 'canoe', 'person', 'paddle', 'water', 'sport', 'outdoors', 'outdoors-batch-01')

    def build(self):
        # Plan: Seated rower with bent arms, boat and an oar. Shared full_body_ref.png: head center (24,11), radius 3 and shoulder y22 give exactly 4 units of ink clearance. Water omitted.
        # Lucide sailboat: original and atomic-debug inspected for contour construction.
        # Keyshape centerline extremes: (4, 8, 44, 40).

        def path(name, start, commands, closed=False):
            members, here = [], start
            for i, (kind, end, *args) in enumerate(commands):
                part = f"{name}-{i}"
                if kind == 'L':
                    self.add_line(part, here, end)
                else:
                    rx, ry, sweep = args
                    self.add_arc(part, here, end, radius_x=rx, radius_y=ry, sweep=sweep)
                members.append(part)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, cx, cy, r):
            path(name, (cx-r,cy), [('A',(cx+r,cy),r,r,True),('A',(cx-r,cy),r,r,True)], True)
        def rounded(name, x0, y0, x1, y1, r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line, poly = self.add_line, self.add_polyline
        join = lambda a,b: self.relate('connect',a,b)
        circle('head',24,11,3)
        poly('body',(14,30),(20,22),(30,22))
        poly('oar',(30,22),(30,30),(44,36));join('body','oar')
        path('hull',(4,30),[('L',(14,30)),('L',(30,30)),('L',(24,40)),('L',(14,40)),('L',(4,30))],True)
        join('body','hull');join('oar','hull')
