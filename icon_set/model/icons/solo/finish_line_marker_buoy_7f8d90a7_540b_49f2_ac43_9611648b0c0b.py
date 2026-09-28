"""finish-line-marker-buoy: Pennant on a pole over the visible dome of a buoy, meeting a single water row. Submerged lower arc omitted; middle waves share their radii."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7f8d90a7-540b-49f2-ac43-9611648b0c0b'
SOURCE_PATH = 'pictographic-primitives/outdoors/sailing finish line_7f8d90a7-540b-49f2-ac43-9611648b0c0b.svg'
AUTHOR = 'gpt-6'

class FinishLineMarkerBuoy(Solo48):
    icon_id = 'finish-line-marker-buoy'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    categories = ('outdoors', 'primitives')
    aliases = ()
    keywords = ('buoy', 'finish-line', 'sailing', 'regatta', 'flag', 'marker', 'water', 'race', 'outdoors-batch-03')

    def build(self):
        # Plan: Pennant on a pole over the visible dome of a buoy, meeting a single water row. Submerged lower arc omitted; middle waves share their radii.
        # Lucide construction reference: flag-triangle-right; original and atomic-debug inspected where named.
        # Human scenes use icon_set/references/human_ref/full_body_ref.png.
        # Centerline envelope: (8, 4, 40, 44).
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
        poly('flag',(24,28),(24,16),(24,4),(40,10),(24,16))
        path('buoy',(12,40),[('A',(24,28),12,12,True),('A',(36,40),12,12,True)]);join('flag','buoy')
        path('water',(8,40),[('A',(12,40),2,2,False),('A',(24,40),6,4,True),('A',(36,40),6,4,False),('A',(40,40),2,2,True)]);join('water','buoy')
