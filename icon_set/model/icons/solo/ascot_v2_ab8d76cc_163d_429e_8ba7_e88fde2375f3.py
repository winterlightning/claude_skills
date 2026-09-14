"""ascot: AI stroke review; parent retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ab8d76cc-163d-429e-8ba7-e88fde2375f3'
SOURCE_PATH = 'icons-json/_uncategorized_04/ascot_ab8d76cc-163d-429e-8ba7-e88fde2375f3.json'
AUTHOR = 'gpt-6'

class AscotVariant2(Solo48):
    icon_id = 'ascot-v2'
    variant_of = 'ascot'
    variant_label = 'AI stroke review · first 50'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_04'
    aliases = ()
    keywords = ('ascot', '_uncategorized_04', 'solo-ai-first50')

    def build(self):
        # Plan: A symmetric broad neckband joins one tapered fabric blade. Kept angular fabric corners and removed conversion bumps.
        # Reference: Lucide original/shirt.svg and atomic-debug/shirt.svg.

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
        poly('band',(8,4),(40,4),(32,14),(16,14),closed=True)
        poly('blade',(16,14),(8,36),(24,44),(40,36),(32,14))
        join('band','blade')

