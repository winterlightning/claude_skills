"""chip-symbol: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd0dd0f52-f552-4b31-8bb1-bed37c84eff0'
SOURCE_PATH = 'pictographic-primitives/symbol/chip_d0dd0f52-f552-4b31-8bb1-bed37c84eff0.svg'
AUTHOR = 'gpt-6'

class ChipSymbol(Solo48):
    icon_id = 'chip-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol',)
    aliases = ()
    keywords = ('chip', 'symbol', 'solo-ai-next100')

    def build(self):
        # Plan: Preserve the square chip with paired leads; each axis uses shared pin spacing and exact body contacts. Corner radius retains this variant identity.
        # Reference: Lucide microchip original and atomic-debug construction.

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
        rounded('body',14,14,34,34,5)

        for p in (20,28):
         for k,a,b in [('t',(p,6),(p,14)),('b',(p,34),(p,42)),('l',(6,p),(14,p)),('r',(34,p),(42,p))]:
          line(f'{k}-{p}',a,b);join(f'{k}-{p}','body')
