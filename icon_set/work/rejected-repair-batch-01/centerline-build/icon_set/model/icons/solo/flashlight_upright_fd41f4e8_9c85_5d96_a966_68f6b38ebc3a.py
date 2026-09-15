"""flashlight-upright: Upright flashlight with broad lens, tapered collar, rounded handle and a switch stroke. Shared axis and matching corner radii preserve symmetry."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fd41f4e8-9c85-5d96-a966-68f6b38ebc3a'
SOURCE_PATH = 'pictographic-primitives/outdoors/outdoors flashlight_fd41f4e8-9c85-5d96-a966-68f6b38ebc3a.svg'
AUTHOR = 'gpt-6'


class FlashlightUpright(Solo48):
    icon_id = 'flashlight-upright'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('flashlight', 'torch', 'light', 'camping', 'battery', 'outdoors', 'lamp', 'outdoors-batch-02')

    def build(self):
        # Plan: Upright flashlight with broad lens, tapered collar, rounded handle and a switch stroke. Shared axis and matching corner radii preserve symmetry.
        # Lucide flashlight original and atomic-debug inspected for construction.
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
        path('flashlight',(8,4),[('L',(40,4)),('L',(40,12)),('L',(33,20)),('L',(33,35)),('A',(15,35),9,9,True),('L',(15,20)),('L',(8,12)),('L',(8,4))],True)
        line('lens',(8,12),(40,12));join('lens','flashlight')
        line('switch',(24,28),(24,32))
