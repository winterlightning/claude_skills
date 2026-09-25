"""condom: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '56cbe40d-c073-46c1-98ab-44e9f8ae8fb5'
SOURCE_PATH = 'pictographic-primitives/money/condom_56cbe40d-c073-46c1-98ab-44e9f8ae8fb5.svg'
AUTHOR = 'gpt-6'

class Condom(Solo48):
    icon_id = 'condom'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    categories = ('primitives', 'money')
    aliases = ()
    keywords = ('condom', 'money', 'solo-ai-next100')

    def build(self):
        # Plan: Keep the packet with regular sealed teeth at the top and bottom; the central packet remains spacious.
        # Reference: No useful exact Lucide match; supplied original silhouette.

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
        points=[(8,4),(12,8),(16,4),(20,8),(24,4),(28,8),(32,4),(36,8),(40,4),(40,44),(36,40),(32,44),(28,40),(24,44),(20,40),(16,44),(12,40),(8,44)]
        poly('packet',*points,closed=True)
