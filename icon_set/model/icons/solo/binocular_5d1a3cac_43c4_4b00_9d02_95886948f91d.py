"""binocular: AI stroke review; parent retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5d1a3cac-43c4-4b00-9d02-95886948f91d'
SOURCE_PATH = 'pictographic-primitives/outdoors/binocular_5d1a3cac-43c4-4b00-9d02-95886948f91d.svg'
AUTHOR = 'gpt-6'

class Binocular(Solo48):
    icon_id = 'binocular'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('binocular', 'outdoors', 'solo-ai-first50')

    def build(self):
        # Plan: Two equal objective lenses have four units of ink clearance. Tapered barrels and a short bridge use exact shared endpoints; removed the crowded center overlap.
        # Reference: Lucide original/binoculars.svg and atomic-debug/binoculars.svg.

        # Typed path helpers preserve each continuous stroke and its round joins.
        def path(name, start, commands, closed=False):
            members = []
            here = start
            for index, command in enumerate(commands):
                ident = f"{name}-{index}"
                kind, end, *args = command
                if kind == "L":
                    self.add_line(ident, here, end)
                elif kind == "A":
                    rx, ry, sweep = args
                    self.add_arc(ident, here, end, radius_x=rx, radius_y=ry, sweep=sweep)
                elif kind == "C":
                    c1, c2 = args
                    self.add_bezier(ident, here, (c1, c2, end))
                members.append(ident)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, cx, cy, r):
            path(name, (cx-r,cy), [("A",(cx+r,cy),r,r,True), ("A",(cx-r,cy),r,r,True)], True)
        def rounded(name, x0, y0, x1, y1, r):
            path(name, (x0+r,y0), [
                ("L",(x1-r,y0)), ("A",(x1,y0+r),r,r,True),
                ("L",(x1,y1-r)), ("A",(x1-r,y1),r,r,True),
                ("L",(x0+r,y1)), ("A",(x0,y1-r),r,r,True),
                ("L",(x0,y0+r)), ("A",(x0+r,y0),r,r,True)], True)
        line = self.add_line
        poly = self.add_polyline
        join = lambda a,b: self.relate("connect",a,b)
        for side in (-1,1):
         x=lambda d:24+side*d
         cx=x(12)
         circle(f'lens-{side}',cx,32,8)
         path(f'barrel-{side}',(x(20),32), [('L',(x(16),8)),('L',(x(8),8)),('L',(x(4),20)),('L',(x(4),32))])
         join(f'barrel-{side}',f'lens-{side}')
        line('bridge',(20,20),(28,20));join('bridge','barrel--1');join('bridge','barrel-1')

