"""blood-bag: next fifty AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ddd5c887-7f6f-4c09-900f-c7b0eb9b5ada'
SOURCE_PATH = 'pictographic-primitives/health/blood bag_ddd5c887-7f6f-4c09-900f-c7b0eb9b5ada.svg'
AUTHOR = 'gpt-6'

class BloodBag(Solo48):
    icon_id = 'blood-bag'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    categories = ('health', 'primitives')
    aliases = ()
    keywords = ('blood', 'bag', 'health', 'solo-ai-next50')

    def build(self):
        # Plan: A smooth IV blood bag has four matching body corners and a broad centered outlet. The empty reservoir preserves the source rather than adding a medical modifier.
        # Reference: Lucide droplet original and atomic-debug construction.

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
        path('bag',(18,36),[('L',(16,36)),('A',(8,28),8,8,True),('L',(8,12)),('A',(16,4),8,8,True),('L',(32,4)),('A',(40,12),8,8,True),('L',(40,28)),('A',(32,36),8,8,True),('L',(30,36)),('L',(30,44)),('L',(18,44)),('L',(18,36))],True)
