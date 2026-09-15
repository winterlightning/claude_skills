"""shop-4c6a59d7: Regular shop awning; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4c6a59d7-f0de-4dca-8f97-74c02d16025e'
SOURCE_PATH = 'icons-json/shopping/shop_4c6a59d7-f0de-4dca-8f97-74c02d16025e.json'
AUTHOR = 'gpt-6'

class Shop4c6a59d7(Solo48):
    icon_id = 'shop-4c6a59d7'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('solo-ai-full-set', 'shop-4c6a59d7')

    def build(self):
        # Plan: Four equal elliptical scallops and a centered doorway preserve the storefront with clear headroom.
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
        path('awning',(4,18),[('L',(8,8)),('L',(40,8)),('L',(44,18)),('A',(39,22),5,4,True),('A',(34,18),5,4,True),('A',(24,18),5,4,True),('A',(14,18),5,4,True),('A',(9,22),5,4,True),('A',(4,18),5,4,True)],True)
        path('walls',(9,22),[('L',(9,40)),('L',(19,40)),('L',(29,40)),('L',(39,40)),('L',(39,22))]);join('walls','awning')
        path('door',(19,40),[('L',(19,31)),('L',(29,31)),('L',(29,40))]);join('door','walls')
