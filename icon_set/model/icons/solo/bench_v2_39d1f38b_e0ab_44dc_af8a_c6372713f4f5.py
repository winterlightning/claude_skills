"""bench: AI stroke review; parent retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '39d1f38b-e0ab-44dc-af8a-c6372713f4f5'
SOURCE_PATH = 'icons-json/furnitures/bench_39d1f38b-e0ab-44dc-af8a-c6372713f4f5.json'
AUTHOR = 'gpt-6'

class BenchVariant2(Solo48):
    icon_id = 'bench-v2'
    variant_of = 'bench'
    variant_label = 'AI stroke review · first 50'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    aliases = ()
    keywords = ('bench', 'furnitures', 'solo-ai-first50')

    def build(self):
        # Plan: A picnic bench keeps two sloping trestle legs and two level planks. All four plank-leg junctions are exact shared nodes.
        # Reference: No useful exact Lucide match; geometric construction from the supplied subject.

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
        poly('top',(8,8),(16,8),(32,8),(40,8))
        poly('seat',(4,24),(12,24),(36,24),(44,24))
        poly('left-leg',(16,8),(12,24),(8,40))
        poly('right-leg',(32,8),(36,24),(40,40))
        for n in ('left-leg','right-leg'):join(n,'top');join(n,'seat')

