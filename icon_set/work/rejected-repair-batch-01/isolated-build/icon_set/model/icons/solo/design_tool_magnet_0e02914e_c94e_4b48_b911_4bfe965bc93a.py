"""design-tool-magnet: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0e02914e-c94e-4b48-b911-4bfe965bc93a'
SOURCE_PATH = 'pictographic-primitives/design/design tool magnet_0e02914e-c94e-4b48-b911-4bfe965bc93a.svg'
AUTHOR = 'gpt-6'

class DesignToolMagnet(Solo48):
    icon_id = 'design-tool-magnet'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('design', 'tool', 'magnet', 'solo-ai-next100')

    def build(self):
        # Plan: Keep a broad horseshoe magnet with two equal pole bands. Concentric semicircles and shared verticals repair uneven inner walls.
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
        path('magnet',(6,6),[('L',(16,6)),('L',(16,24)),('A',(32,24),8,8,False),('L',(32,6)),('L',(42,6)),('L',(42,24)),('A',(6,24),18,18,True),('L',(6,6))],True)
        for x in (6,32):line(f'pole-{x}',(x,16),(x+10,16));join(f'pole-{x}','magnet')
