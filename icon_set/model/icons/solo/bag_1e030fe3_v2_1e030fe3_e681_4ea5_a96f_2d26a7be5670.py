"""bag-1e030fe3: AI stroke review; parent retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1e030fe3-e681-4ea5-a96f-2d26a7be5670'
SOURCE_PATH = 'icons-json/shopping/bag_1e030fe3-e681-4ea5-a96f-2d26a7be5670.json'
AUTHOR = 'gpt-6'

class Bag1e030fe3Variant2(Solo48):
    icon_id = 'bag-1e030fe3-v2'
    variant_of = 'bag-1e030fe3'
    variant_label = 'AI stroke review · first 50'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('bag', 'shopping', 'solo-ai-first50')

    def build(self):
        # Plan: A structured shopping bag retains its straight-sided base; paired tapered walls and a semicircular handle use shared rim nodes. Removed the faceted handle.
        # Reference: Lucide original/shopping-bag.svg and atomic-debug/shopping-bag.svg.

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
        path('handle',(16,16), [('L',(16,12)),('A',(32,12),8,8,True),('L',(32,16))])
        poly('bag',(12,16),(16,16),(32,16),(36,16),(40,44),(8,44),closed=True);join('handle','bag')

