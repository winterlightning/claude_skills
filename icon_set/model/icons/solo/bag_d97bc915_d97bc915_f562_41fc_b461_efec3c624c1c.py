"""bag-d97bc915: Structured gusset tote; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd97bc915-f562-41fc-b461-efec3c624c1c'
SOURCE_PATH = 'pictographic-primitives/shopping/bag_d97bc915-f562-41fc-b461-efec3c624c1c.svg'
AUTHOR = 'gpt-6'

class BagD97bc915(Solo48):
    icon_id = 'bag-d97bc915'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    categories = ('shopping', 'primitives')
    aliases = ()
    keywords = ('solo-ai-refine', 'solo-ai-first50', 'bag-d97bc915')

    def build(self):
        # Plan: A tall box-shaped tote has an angular handle and one functional side gusset. The side panel is intentionally asymmetric, eight units wide, rather than decorative variation.
        # Reference: Lucide paper-bag: original and atomic-debug geometry.

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
        poly('handle',(16,16),(16,4),(28,4),(28,16))
        poly('body',(8,16),(16,16),(28,16),(32,16),(40,24),(40,44),(32,44),(8,44),closed=True)
        line('gusset',(32,16),(32,44));join('gusset','body');join('handle','body')
