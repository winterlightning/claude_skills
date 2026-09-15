"""canoe-paddles: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '481229e1-4318-5a89-838e-674d0da6757e'
SOURCE_PATH = 'pictographic-primitives/outdoors/canoe paddles_481229e1-4318-5a89-838e-674d0da6757e.svg'
AUTHOR = 'gpt-6'

class CanoePaddles(Solo48):
    icon_id = 'canoe-paddles'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('canoe', 'paddles', 'outdoors', 'solo-ai-next100')

    def build(self):
        # Plan: Two broad paddle blades mirror about the central axis with a clear gap between them. Shafts meet at one central crossing.
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
        poly('blade-left',(6,14),(14,6),(20,12),(20,20),(12,20),(6,14))
        poly('blade-right',(42,14),(34,6),(28,12),(28,20),(36,20),(42,14))
        poly('shaft-left',(20,20),(24,24),(42,42));poly('shaft-right',(28,20),(24,24),(6,42))
        join('shaft-left','blade-left');join('shaft-right','blade-right');join('shaft-left','shaft-right')
