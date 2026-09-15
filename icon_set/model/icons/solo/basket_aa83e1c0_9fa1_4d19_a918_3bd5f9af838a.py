"""basket: AI stroke review; parent retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'aa83e1c0-9fa1-4d19-a918-3bd5f9af838a'
SOURCE_PATH = 'pictographic-primitives/symbol/basket_aa83e1c0-9fa1-4d19-a918-3bd5f9af838a.svg'
AUTHOR = 'gpt-6'

class Basket(Solo48):
    icon_id = 'basket'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('basket', 'symbol', 'solo-ai-first50')

    def build(self):
        # Plan: A symmetric basket has one tapered bowl and paired outward handle strokes, all on shared attachment nodes.
        # Reference: Lucide original/shopping-basket.svg and atomic-debug/shopping-basket.svg.

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
        poly('basket',(4,20),(12,20),(36,20),(44,20),(38,40),(10,40),closed=True)
        for side in (-1,1):
         x=lambda d:24+side*d
         line(f'handle-{side}',(x(12),20),(x(6),8));join(f'handle-{side}','basket')

