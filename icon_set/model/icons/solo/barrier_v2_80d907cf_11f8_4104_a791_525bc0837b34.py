"""barrier: AI stroke review; parent retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '80d907cf-11f8-4104-a791-525bc0837b34'
SOURCE_PATH = 'icons-json/symbol/barrier_80d907cf-11f8-4104-a791-525bc0837b34.json'
AUTHOR = 'gpt-6'

class BarrierVariant2(Solo48):
    icon_id = 'barrier-v2'
    variant_of = 'barrier'
    variant_label = 'AI stroke review · first 50'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('barrier', 'symbol', 'solo-ai-first50')

    def build(self):
        # Plan: A broad striped road barrier with paired legs. Reduced the stripes to two spacious diagonals and removed floating top dots.
        # Reference: Lucide original/construction.svg and atomic-debug/construction.svg.

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
        poly('board',(4,8),(20,8),(36,8),(44,8),(44,24),(36,24),(20,24),(12,24),(4,24),closed=True)
        line('stripe-1',(4,24),(20,8));line('stripe-2',(20,24),(36,8))
        for n in ('stripe-1','stripe-2'):join(n,'board')
        for x in (12,36):
         line(f'leg-{x}',(x,24),(x,40));join(f'leg-{x}','board')

