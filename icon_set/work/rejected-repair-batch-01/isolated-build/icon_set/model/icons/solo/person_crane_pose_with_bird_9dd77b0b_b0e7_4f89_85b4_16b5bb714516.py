"""person-crane-pose-with-bird: One-legged balancing person with raised knee, spread arms and a small flying bird. Head center (32,11), radius 3; shoulder y22 gives exact 4-unit ink gap. Ground line omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9dd77b0b-b0e7-4f89-85b4-16b5bb714516'
SOURCE_PATH = 'pictographic-primitives/outdoors/takengei person_9dd77b0b-b0e7-4f89-85b4-16b5bb714516.svg'
AUTHOR = 'gpt-6'

class PersonCranePoseWithBird(Solo48):
    icon_id = 'person-crane-pose-with-bird'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('balance', 'pose', 'person', 'martial-arts', 'crane', 'beach', 'bird', 'exercise', 'outdoors-batch-03')

    def build(self):
        # Plan: One-legged balancing person with raised knee, spread arms and a small flying bird. Head center (32,11), radius 3; shoulder y22 gives exact 4-unit ink gap. Ground line omitted.
        # Lucide construction reference: none; original and atomic-debug inspected where named.
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
        circle('head',32,11,3)
        poly('arms',(12,22),(32,22),(44,22))
        poly('body',(32,22),(32,30),(32,40));join('body','arms')
        poly('raised-leg',(32,30),(20,30),(24,36));join('raised-leg','body')
        poly('bird',(4,8),(10,12),(16,8))
