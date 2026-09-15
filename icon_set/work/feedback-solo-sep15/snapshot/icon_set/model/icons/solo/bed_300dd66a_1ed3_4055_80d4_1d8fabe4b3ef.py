"""bed: AI stroke review; parent retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '300dd66a-1ed3-4055-80d4-1d8fabe4b3ef'
SOURCE_PATH = 'pictographic-primitives/state/bed_300dd66a-1ed3-4055-80d4-1d8fabe4b3ef.svg'
AUTHOR = 'gpt-6'

class Bed(Solo48):
    icon_id = 'bed'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('bed', 'state', 'solo-ai-first50')

    def build(self):
        # Plan: A clear bed frame has a tall head post, a broad mattress band and two legs. Both horizontal rails meet split post nodes.
        # Reference: Lucide original/bed.svg and atomic-debug/bed.svg.

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
        poly('head',(4,8),(4,24),(4,32),(4,40))
        poly('foot',(44,24),(44,32),(44,40))
        line('top',(4,24),(44,24));line('bottom',(4,32),(44,32))
        for n in ('top','bottom'):join(n,'head');join(n,'foot')

