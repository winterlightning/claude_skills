"""canoe: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2f08daf6-071b-5ac7-9717-2239ffbb2925'
SOURCE_PATH = 'pictographic-primitives/outdoors/canoe_2f08daf6-071b-5ac7-9717-2239ffbb2925.svg'
AUTHOR = 'gpt-6'

class Canoe(Solo48):
    icon_id = 'canoe'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('canoe', 'outdoors', 'solo-ai-next100')

    def build(self):
        # Plan: Preserve the broad canoe with raised ends and a scooped gunwale; both ends share curvature and the hull stays low.
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
        path('hull',(4,8),[('C',(24,21),(8,17),(16,21)),('C',(44,8),(32,21),(40,17)),('L',(44,18)),('C',(24,40),(44,36),(38,40)),('C',(4,18),(10,40),(4,36)),('L',(4,8))],True)
