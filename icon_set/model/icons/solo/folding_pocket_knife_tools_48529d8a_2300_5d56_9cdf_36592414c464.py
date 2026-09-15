"""folding-pocket-knife-tools: Smooth folded pocket knife; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '48529d8a-2300-5d56-9cdf-36592414c464'
SOURCE_PATH = 'icons-json/tools/folding pocket knife_48529d8a-2300-5d56-9cdf-36592414c464.json'
AUTHOR = 'gpt-6'

class FoldingPocketKnifeTools(Solo48):
    icon_id = 'folding-pocket-knife-tools'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'tools'
    aliases = ()
    keywords = ('solo-ai-full-set', 'folding-pocket-knife-tools')

    def build(self):
        # Plan: Preserve the open blade and curved handle; broaden the handle heel without changing the V arrangement.
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
        path('blade',(31,29),[('C',(10,6),(19,23),(11,15)),('C',(36,24),(21,8),(31,17)),('L',(31,29))],True)
        path('handle',(36,24),[('C',(42,30),(40,23),(42,26)),('C',(12,42),(39,37),(20,42)),('C',(6,37),(8,42),(6,41)),('C',(12,33),(6,34),(8,33)),('C',(31,29),(20,33),(27,31)),('L',(36,24))],True);join('blade','handle')
