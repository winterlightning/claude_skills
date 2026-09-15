"""shopping-basket-shopping: Clean basket rim; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b8307606-fc5e-5c79-9f79-07ac43dd5ed8'
SOURCE_PATH = 'pictographic-primitives/shopping/shopping basket_b8307606-fc5e-5c79-9f79-07ac43dd5ed8.svg'
AUTHOR = 'gpt-6'

class ShoppingBasketShopping(Solo48):
    icon_id = 'shopping-basket-shopping'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('solo-ai-full-set', 'shopping-basket-shopping')

    def build(self):
        # Plan: Preserve the basket and two raised handles; remove the retraced rim and use shared attachment points.
        # Reference: Lucide shopping-basket: original and atomic-debug geometry.

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
        path('basket',(4,17),[('L',(12,17)),('L',(36,17)),('L',(44,17)),('L',(38,40)),('L',(10,40)),('L',(4,17))],True)
        line('left',(12,17),(19,8));line('right',(36,17),(29,8));join('left','basket');join('right','basket')
