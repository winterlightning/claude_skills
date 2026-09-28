"""sailboat-triangle-sail: Symmetric triangular sail separated from a broad flat-deck hull. Water row omitted to preserve sail/hull clearance."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6920feca-ba55-4c5c-8e6c-032c49ca2982'
SOURCE_PATH = 'pictographic-primitives/outdoors/sailing boat_6920feca-ba55-4c5c-8e6c-032c49ca2982.svg'
AUTHOR = 'gpt-6'

class SailboatTriangleSail(Solo48):
    icon_id = 'sailboat-triangle-sail'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    categories = ('outdoors', 'state')
    aliases = ()
    keywords = ('sailboat', 'sail', 'boat', 'sailing', 'sea', 'water', 'yacht', 'outdoors-batch-03')

    def build(self):
        # Plan: Symmetric triangular sail separated from a broad flat-deck hull. Water row omitted to preserve sail/hull clearance.
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
        poly('sail',(12,24),(24,8),(36,24),closed=True)
        poly('hull',(4,32),(44,32),(36,40),(12,40),closed=True)
