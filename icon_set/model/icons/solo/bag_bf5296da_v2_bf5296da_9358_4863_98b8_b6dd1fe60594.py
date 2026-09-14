"""bag-bf5296da: AI stroke review; parent retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bf5296da-9358-4863-98b8-b6dd1fe60594'
SOURCE_PATH = 'icons-json/photography/bag_bf5296da-9358-4863-98b8-b6dd1fe60594.json'
AUTHOR = 'gpt-6'

class BagBf5296daVariant2(Solo48):
    icon_id = 'bag-bf5296da-v2'
    variant_of = 'bag-bf5296da'
    variant_label = 'AI stroke review · first 50'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'photography'
    aliases = ()
    keywords = ('bag', 'photography', 'solo-ai-first50')

    def build(self):
        # Plan: A symmetric shopping bag uses one smooth arched handle and a tapered body; the handle meets shared rim nodes. Removed conversion dents and inconsistent corners.
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
        axis, half_handle = 24, 8
        path('handle',(axis-half_handle,16), [('L',(16,12)),('A',(32,12),8,8,True),('L',(axis+half_handle,16))])
        path('bag',(12,16), [('L',(16,16)),('L',(32,16)),('L',(36,16)),('L',(40,38)),('C',(34,44),(40,42),(38,44)),('L',(14,44)),('C',(8,38),(10,44),(8,42)),('L',(12,16))],True)
        join('bag','handle')

