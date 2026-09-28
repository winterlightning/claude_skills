"""seasoning-chilli: Smooth curved chilli; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '41f0de58-c686-4c1c-bb67-50e2eae2c9b5'
SOURCE_PATH = 'pictographic-primitives/food/seasoning chilli_41f0de58-c686-4c1c-bb67-50e2eae2c9b5.svg'
AUTHOR = 'gpt-6'

class SeasoningChilli(Solo48):
    icon_id = 'seasoning-chilli'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('solo-ai-full-set', 'seasoning-chilli')

    def build(self):
        # Plan: Preserve the curved pepper, cap and rising stem. Exact curve extrema and cap nodes keep the tapered silhouette coherent.
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
        path('pepper',(30,17),[('C',(36,12),(30,14),(32,12)),('C',(40,20),(39,12),(40,15)),('C',(23,42),(40,33),(33,42)),('C',(6,32),(15,42),(9,38)),('C',(28,27),(15,34),(26,30)),('L',(30,17))],True)
        path('cap',(30,17),[('C',(40,20),(32,23),(37,25))]);join('cap','pepper')
        path('stem',(36,12),[('C',(42,6),(36,8),(39,6))]);join('stem','pepper')
