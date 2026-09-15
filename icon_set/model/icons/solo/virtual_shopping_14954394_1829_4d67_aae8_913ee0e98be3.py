"""virtual-shopping: Balanced shopping carrier; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '14954394-1829-4d67-aae8-913ee0e98be3'
SOURCE_PATH = 'pictographic-primitives/shopping/virtual shopping_14954394-1829-4d67-aae8-913ee0e98be3.svg'
AUTHOR = 'gpt-6'

class VirtualShopping(Solo48):
    icon_id = 'virtual-shopping'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('solo-ai-full-set', 'virtual-shopping')

    def build(self):
        # Plan: Preserve the tapered carrier and long inset handle; keep equal clear space beside both handle ends.
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
        path('bag',(10,17),[('L',(19,17)),('L',(29,17)),('L',(38,17)),('L',(40,44)),('L',(8,44)),('L',(10,17))],True)
        path('handle',(19,23),[('L',(19,17)),('L',(19,9)),('A',(29,9),5,5,True),('L',(29,17)),('L',(29,23))]);join('handle','bag')
