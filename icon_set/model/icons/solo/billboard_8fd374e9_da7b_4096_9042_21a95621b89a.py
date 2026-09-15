"""billboard: Even freestanding board; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8fd374e9-da7b-4096-9042-21a95621b89a'
SOURCE_PATH = 'pictographic-primitives/business/billboard_8fd374e9-da7b-4096-9042-21a95621b89a.svg'
AUTHOR = 'gpt-6'

class Billboard(Solo48):
    icon_id = 'billboard'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('solo-ai-full-set', 'billboard')

    def build(self):
        # Plan: A clean rectangular board owns two equally spaced feet with exact attachment nodes.
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
        path('board',(6,6),[('L',(42,6)),('L',(42,34)),('L',(36,34)),('L',(12,34)),('L',(6,34)),('L',(6,6))],True)
        for x in [12,36]:
         line(f'leg-{x}',(x,34),(x,42));path(f'foot-{x}',(x-4,42),[('L',(x,42)),('L',(x+4,42))]);join(f'leg-{x}','board');join(f'leg-{x}',f'foot-{x}')
