"""dragon-fruit: Crowned fruit — local spacing refinement; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a2765449-859e-4487-b952-c495c743933d'
SOURCE_PATH = 'icons-json/food/dragon fruit_a2765449-859e-4487-b952-c495c743933d.json'
AUTHOR = 'gpt-6'

class DragonFruit(Solo48):
    icon_id = 'dragon-fruit'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('solo-ai-full-set', 'dragon-fruit')

    def build(self):
        # Plan: Original five-point crown and rounded fruit restored. Moved the two side tips and inner notches slightly.
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
        path('fruit',(8,20),[('L',(12,22)),('L',(11,10)),('L',(19,18)),('L',(24,4)),('L',(29,18)),('L',(37,10)),('L',(36,22)),('L',(40,20)),('C',(24,44),(39,36),(35,44)),('C',(8,20),(13,44),(9,36))],True)
