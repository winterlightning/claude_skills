"""sailboat-curved-sail: Tall sail with straight mast edge and a quarter-ellipse belly above a broad hull. Water row omitted; curved sail is intentionally asymmetric."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '74c318d1-397c-4a33-9a8b-1a68e1da926e'
SOURCE_PATH = 'pictographic-primitives/outdoors/sailing boat_74c318d1-397c-4a33-9a8b-1a68e1da926e.svg'
AUTHOR = 'gpt-6'

class SailboatCurvedSail(Solo48):
    icon_id = 'sailboat-curved-sail'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('sailboat', 'sail', 'boat', 'sailing', 'regatta', 'sea', 'water', 'outdoors-batch-03')

    def build(self):
        # Plan: Tall sail with straight mast edge and a quarter-ellipse belly above a broad hull. Water row omitted; curved sail is intentionally asymmetric.
        # Lucide construction reference: sailboat; original and atomic-debug inspected where named.
        # Human scenes use icon_set/references/human_ref/full_body_ref.png.
        # Centerline envelope: (6, 6, 42, 42).
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
        path('sail',(14,6),[('A',(36,25),22,19,True),('L',(14,25)),('L',(14,6))],True)
        poly('hull',(6,34),(42,34),(34,42),(14,42),closed=True)
