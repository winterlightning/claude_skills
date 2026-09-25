"""slalom-kayaker: Kayaker leaning back in a sharply tilted hull with a diagonal paddle. Head center (32,7), radius 3; shoulder y18 gives exact 4-unit ink clearance. A single torso/grip stroke replaces overlapping arms; blade outlines and water omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '477bc7e3-a160-4d87-a147-7a6a34928430'
SOURCE_PATH = 'pictographic-primitives/outdoors/sport kayaking_477bc7e3-a160-4d87-a147-7a6a34928430.svg'
AUTHOR = 'gpt-6'

class SlalomKayaker(Solo48):
    icon_id = 'slalom-kayaker'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    categories = ('outdoors', 'primitives')
    aliases = ()
    keywords = ('kayaking', 'kayak', 'paddle', 'whitewater', 'sport', 'water', 'slalom', 'outdoors-batch-03')

    def build(self):
        # Plan: Kayaker leaning back in a sharply tilted hull with a diagonal paddle. Head center (32,7), radius 3; shoulder y18 gives exact 4-unit ink clearance. A single torso/grip stroke replaces overlapping arms; blade outlines and water omitted.
        # Lucide construction reference: sailboat; original and atomic-debug inspected where named.
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
        circle('head',32,7,3)
        line('body',(32,18),(24,30))
        poly('paddle',(16,16),(24,30),(32,44));join('paddle','body')
        poly('kayak',(8,36),(24,30),(40,24),(32,44),(16,44),closed=True)
        join('kayak','body');join('kayak','paddle')
