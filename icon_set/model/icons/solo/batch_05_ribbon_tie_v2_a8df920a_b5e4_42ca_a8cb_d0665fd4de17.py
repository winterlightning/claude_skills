"""batch-05-ribbon-tie: AI stroke review; parent retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a8df920a-b5e4-42ca-a8cb-d0665fd4de17'
SOURCE_PATH = 'icons-json/accessories/batch-05/ribbon tie_a8df920a-b5e4-42ca-a8cb-d0665fd4de17.json'
AUTHOR = 'gpt-6'

class Batch05RibbonTieVariant2(Solo48):
    icon_id = 'batch-05-ribbon-tie-v2'
    variant_of = 'batch-05-ribbon-tie'
    variant_label = 'AI stroke review · first 50'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'ribbon', 'tie', 'accessories', 'solo-ai-first50')

    def build(self):
        # Plan: A centered bow-tie knot controls two mirrored fabric wings; omitted the crowded interior creases.
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
        poly('knot',(19,16),(29,16),(29,32),(19,32),closed=True)
        poly('left',(19,16),(4,8),(4,40),(19,32))
        poly('right',(29,16),(44,8),(44,40),(29,32))
        join('left','knot');join('right','knot')

