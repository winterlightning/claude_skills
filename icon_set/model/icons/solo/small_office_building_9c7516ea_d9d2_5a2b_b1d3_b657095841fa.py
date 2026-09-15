"""small-office-building: Balanced office entrance; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9c7516ea-d9d2-5a2b-b1d3-b657095841fa'
SOURCE_PATH = 'pictographic-primitives/office/small office building_9c7516ea-d9d2-5a2b-b1d3-b657095841fa.svg'
AUTHOR = 'gpt-6'

class SmallOfficeBuilding(Solo48):
    icon_id = 'small-office-building'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('solo-ai-full-set', 'small-office-building')

    def build(self):
        # Plan: Preserve the roof and arched doorway with a clear band above the arch and exact shared wall nodes.
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
        path('roof',(4,8),[('L',(44,8)),('L',(44,18)),('L',(40,18)),('L',(8,18)),('L',(4,18)),('L',(4,8))],True)
        path('base',(4,40),[('L',(8,40)),('L',(18,40)),('L',(30,40)),('L',(40,40)),('L',(44,40))])
        for x in [8,40]:line(f'wall-{x}',(x,18),(x,40));join(f'wall-{x}','roof');join(f'wall-{x}','base')
        path('door',(18,40),[('L',(18,33)),('A',(30,33),6,6,True),('L',(30,40))]);join('door','base')
