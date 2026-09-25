"""inflatable-raft-and-paddle: Top-view capsule raft with two transverse seats and a single-bladed paddle. Tube represented by the outer stroke; nested inner tube omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '92104123-8895-5407-a206-a94ae12de98d'
SOURCE_PATH = 'pictographic-primitives/outdoors/sport rafting equipment_92104123-8895-5407-a206-a94ae12de98d.svg'
AUTHOR = 'gpt-6'

class InflatableRaftAndPaddle(Solo48):
    icon_id = 'inflatable-raft-and-paddle'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    categories = ('outdoors', 'primitives')
    aliases = ()
    keywords = ('raft', 'rafting', 'paddle', 'inflatable', 'boat', 'whitewater', 'sport', 'outdoors-batch-03')

    def build(self):
        # Plan: Top-view capsule raft with two transverse seats and a single-bladed paddle. Tube represented by the outer stroke; nested inner tube omitted.
        # Lucide construction reference: sailboat; original and atomic-debug inspected where named.
        # Human scenes use icon_set/references/human_ref/full_body_ref.png.
        # Centerline envelope: (4, 8, 44, 40).
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
        path('raft',(4,20),[('A',(28,20),12,12,True),('L',(28,28)),('A',(4,28),12,12,True),('L',(4,20))],True)
        for i,y in enumerate((20,28)):
            line(f'seat-{i}',(4,y),(28,y));join(f'seat-{i}','raft')
        path('blade',(36,8),[('L',(44,8)),('L',(44,20)),('A',(40,24),4,4,True),('A',(36,20),4,4,True),('L',(36,8))],True)
        line('shaft',(40,24),(40,40));join('shaft','blade')
