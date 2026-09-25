"""shopping-bag-1b586bc1: Balanced tapered shopping bag; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1b586bc1-bc24-4649-9d1f-2c9c15a8444b'
SOURCE_PATH = 'pictographic-primitives/shopping/shopping bag_1b586bc1-bc24-4649-9d1f-2c9c15a8444b.svg'
AUTHOR = 'gpt-6'

class ShoppingBag(Solo48):
    icon_id = 'shopping-bag-1b586bc1'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    categories = ('shopping', 'state')
    aliases = ()
    keywords = ('solo-ai-full-set', 'shopping-bag-1b586bc1')

    def build(self):
        # Plan: Preserve hanging handle ends; widen the shoulders and move the hanging ends inward to maintain clear space.
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
        path('bag',(8,44),[('L',(8,17)),('L',(17,17)),('L',(31,17)),('L',(40,17)),('L',(40,44)),('L',(8,44))],True)
        path('handle',(17,23),[('L',(17,17)),('L',(17,11)),('A',(31,11),7,7,True),('L',(31,17)),('L',(31,23))]);join('handle','bag')
