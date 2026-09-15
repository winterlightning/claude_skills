"""pearl: Smooth pearl shell; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3e6bf106-b5c7-4e50-a890-c966c81a9369'
SOURCE_PATH = 'icons-json/products/pearl_3e6bf106-b5c7-4e50-a890-c966c81a9369.json'
AUTHOR = 'gpt-6'

class Pearl(Solo48):
    icon_id = 'pearl'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'products'
    aliases = ()
    keywords = ('solo-ai-full-set', 'pearl')

    def build(self):
        # Plan: Preserve the open scalloped lid, round pearl and cupped shell. The bowl meets the pearl at exact side nodes.
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
        path('lid',(10,19),[('C',(6,16),(7,19),(6,18)),('C',(12,10),(6,12),(9,10)),('C',(24,6),(16,10),(17,6)),('C',(36,10),(31,6),(32,10)),('C',(42,16),(39,10),(42,12)),('C',(38,19),(42,18),(41,19))])
        path('pearl',(19,28),[('A',(24,23),5,5,True),('A',(29,28),5,5,True),('A',(24,33),5,5,True),('A',(19,28),5,5,True)],True)
        path('bowl',(19,28),[('C',(6,32),(14,28),(9,29)),('C',(24,42),(9,40),(17,42)),('C',(42,32),(31,42),(39,40)),('C',(29,28),(39,29),(34,28))]);join('bowl','pearl')
