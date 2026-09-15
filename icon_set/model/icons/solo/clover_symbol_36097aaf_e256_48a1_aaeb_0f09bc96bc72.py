"""clover-symbol: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '36097aaf-e256-48a1-aaeb-0f09bc96bc72'
SOURCE_PATH = 'icons-json/symbol/clover_36097aaf-e256-48a1-aaeb-0f09bc96bc72.json'
AUTHOR = 'gpt-6'

class CloverSymbol(Solo48):
    icon_id = 'clover-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('clover', 'symbol', 'solo-ai-next100')

    def build(self):
        # Plan: Four heart-shaped leaves meet at the center, preserving the original diagonal leaf divisions. One rotated leaf definition owns all lobes and spacing.
        # Reference: Lucide clover original and atomic-debug construction.

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
        leaf=[('L',(14,14)),('C',(19,6),(14,8),(15,6)),('C',(24,11),(22,6),(23,11)),('C',(29,6),(25,11),(26,6)),('C',(34,14),(33,6),(34,8)),('L',(24,24))]
        turn=lambda p,n:p if n==0 else turn((48-p[1],p[0]),n-1)
        for n in range(4):
         path(f'leaf-{n}',(24,24),[(k,turn(e,n),*[turn(p,n) for p in controls]) for k,e,*controls in leaf],True)
         for m in range(n):join(f'leaf-{n}',f'leaf-{m}')
