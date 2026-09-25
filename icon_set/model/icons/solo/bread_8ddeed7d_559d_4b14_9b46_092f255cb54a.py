"""bread: Broad bread slice; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8ddeed7d-559d-4b14-9b46-092f255cb54a'
SOURCE_PATH = 'pictographic-primitives/symbol/bread_8ddeed7d-559d-4b14-9b46-092f255cb54a.svg'
AUTHOR = 'gpt-6'

class Bread(Solo48):
    icon_id = 'bread'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol',)
    aliases = ()
    keywords = ('solo-ai-next50-refine', 'solo-ai-next50', 'bread')

    def build(self):
        # Plan: A wide slice body retains the original proportion. A low softly domed crown has shallow shoulders, with matching sides and softly rounded bottom corners; no decorative crumbs.
        # Reference: Original football; exact mirrored panel construction.

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
        # Shared axis owns the left and right sides of the slice.
        right=[('C',(42,14),(38,6),(42,10)),('C',(39,20),(42,17),(40,19)),('L',(39,39)),('A',(36,42),3,3,True),('L',(24,42))]
        path('slice',(24,6),right+[('L',(12,42)),('A',(9,39),3,3,True),('L',(9,20)),('C',(6,14),(8,19),(6,17)),('C',(24,6),(6,10),(10,6))],True)
