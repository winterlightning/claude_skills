"""casino-chip-1: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c7cef94c-7b9b-4df7-b935-546150f20188'
SOURCE_PATH = 'icons-json/symbol/casino chip 1_c7cef94c-7b9b-4df7-b935-546150f20188.json'
AUTHOR = 'gpt-6'

class CasinoChip1(Solo48):
    icon_id = 'casino-chip-1'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('casino', 'chip', 'symbol', 'solo-ai-next100')

    def build(self):
        # Plan: A circular chip with a centered ring and four diagonal radial sectors; matched sectors keep rotational balance.
        # Reference: Lucide disc original and atomic-debug construction.

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
        circle('rim',24,24,20);circle('core',24,24,10)
        for i,(a,b) in enumerate([((10,10),(17,17)),((38,10),(31,17)),((38,38),(31,31)),((10,38),(17,31))]):
         line(f'sector-{i}',a,b);join(f'sector-{i}','rim');join(f'sector-{i}','core')
