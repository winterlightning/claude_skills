"""flip: Clean calendar corner; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd3a329c3-d291-512e-bc93-90a8d0c4c1fc'
SOURCE_PATH = 'pictographic-primitives/content/flip_d3a329c3-d291-512e-bc93-90a8d0c4c1fc.svg'
AUTHOR = 'gpt-6'

class Flip(Solo48):
    icon_id = 'flip'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    categories = ('primitives', 'content')
    aliases = ()
    keywords = ('solo-ai-full-set', 'flip')

    def build(self):
        # Plan: Keep three equal binding marks and the lifted lower corner; every attachment is explicit.
        # Reference: Original subject; preserve the distinctive silhouette and proportions.

        # Typed path helpers preserve each continuous stroke and its round joins.
        def path(name, start, commands, closed=False):
            members = []
            here = start
            for index, command in enumerate(commands):
                ident = f"{name}-{index}"
                kind, end, *args = command
                if kind == "L" and tuple(end) == tuple(here):
                    continue
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
        path('page',(6,10),[('L',(14,10)),('L',(24,10)),('L',(34,10)),('L',(42,10)),('L',(42,30)),('L',(30,42)),('L',(6,42)),('L',(6,10))],True)
        path('fold',(42,30),[('L',(30,30)),('L',(30,42))]);join('fold','page')
        for x in [14,24,34]:path(f'ring-{x}',(x,6),[('L',(x,10)),('L',(x,15))]);join(f'ring-{x}','page')
