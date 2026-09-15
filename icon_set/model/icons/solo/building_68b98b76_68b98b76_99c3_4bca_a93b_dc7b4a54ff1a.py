"""building-68b98b76: next fifty AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '68b98b76-99c3-4bca-a93b-dc7b4a54ff1a'
SOURCE_PATH = 'pictographic-primitives/building/building_68b98b76-99c3-4bca-a93b-dc7b4a54ff1a.svg'
AUTHOR = 'gpt-6'

class Building68b98b76(Solo48):
    icon_id = 'building-68b98b76'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    aliases = ()
    keywords = ('building', 'solo-ai-next50')

    def build(self):
        # Plan: A tall sloped tower stands beside a short annex, with a simple entrance between their shared baseline nodes. Keep the stepped silhouette and remove tiny junction kinks.
        # Reference: Lucide building-2 original and atomic-debug construction.

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
        poly('tower',(24,44),(24,14),(40,4),(40,44),(24,44))
        poly('annex',(24,24),(8,24),(8,44),(24,44));join('annex','tower')
