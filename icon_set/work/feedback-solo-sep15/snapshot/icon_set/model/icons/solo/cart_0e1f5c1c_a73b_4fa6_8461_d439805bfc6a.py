"""cart: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0e1f5c1c-a73b-4fa6-8461-d439805bfc6a'
SOURCE_PATH = 'pictographic-primitives/shopping/cart_0e1f5c1c-a73b-4fa6-8461-d439805bfc6a.svg'
AUTHOR = 'gpt-6'

class Cart(Solo48):
    icon_id = 'cart'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('cart', 'shopping', 'solo-ai-next100')

    def build(self):
        # Plan: Keep the source hand basket; paired handles share endpoints with its rim. Each basket retains a different taper or handle construction.
        # Reference: Lucide shopping-basket original and atomic-debug construction.

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
        poly('basket',(4,20),(44,20),(36,40),(12,40),(4,20))
        poly('handle-left',(12,20),(20,8));poly('handle-right',(28,8),(36,20));join('handle-left','basket');join('handle-right','basket')
