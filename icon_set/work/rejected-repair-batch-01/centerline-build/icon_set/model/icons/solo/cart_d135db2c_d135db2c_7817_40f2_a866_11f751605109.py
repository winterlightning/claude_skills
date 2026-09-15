"""cart-d135db2c: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd135db2c-7817-40f2-a866-11f751605109'
SOURCE_PATH = 'pictographic-primitives/shopping/cart_d135db2c-7817-40f2-a866-11f751605109.svg'
AUTHOR = 'gpt-6'

class CartD135db2c(Solo48):
    icon_id = 'cart-d135db2c'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('cart', 'shopping', 'solo-ai-next100')

    def build(self):
        # Plan: Retain the wheeled shopping cart, its handle direction and a broad basket. Round wheel dots match and remain clear of the basket.
        # Reference: Lucide shopping-cart original and atomic-debug construction.

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
        poly('basket',(4,16),(40,16),(32,30),(12,30),(4,16))
        poly('handle',(40,16),(44,8));join('handle','basket')
        self.add_dot('wheel-left',(16,40));self.add_dot('wheel-right',(30,40))
