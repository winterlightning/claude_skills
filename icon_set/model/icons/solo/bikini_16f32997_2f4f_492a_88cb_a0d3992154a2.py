"""bikini: AI stroke review; parent retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '16f32997-2f4f-492a-88cb-a0d3992154a2'
SOURCE_PATH = 'icons-json/symbol/bikini_16f32997-2f4f-492a-88cb-a0d3992154a2.json'
AUTHOR = 'gpt-6'

class Bikini(Solo48):
    icon_id = 'bikini'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('bikini', 'symbol', 'solo-ai-first50')

    def build(self):
        # Plan: Two mirrored smooth cups have a clear center bridge and crossed shoulder ties. Rebalanced the cups to remove the pinched central opening.
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
        for side in (-1,1):
         x=lambda d:24+side*d
         path(f'cup-{side}',(x(14),20), [('C',(x(4),32),(x(8),24),(x(4),27)),('C',(x(12),40),(x(4),38),(x(7),40)),('C',(x(20),32),(x(17),40),(x(20),38)),('C',(x(14),20),(x(20),27),(x(17),22))],True)
         poly(f'tie-{side}',(x(14),20),(24,8),(x(-6),8));join(f'tie-{side}',f'cup-{side}')
        line('bridge',(20,32),(28,32));join('bridge','cup--1');join('bridge','cup-1');join('tie--1','tie-1')

