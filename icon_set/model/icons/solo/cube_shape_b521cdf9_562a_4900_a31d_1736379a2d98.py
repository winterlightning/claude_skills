"""cube-shape: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b521cdf9-562a-4900-a31d-1736379a2d98'
SOURCE_PATH = 'pictographic-primitives/design/cube shape_b521cdf9-562a-4900-a31d-1736379a2d98.svg'
AUTHOR = 'gpt-6'

class CubeShape(Solo48):
    icon_id = 'cube-shape'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('cube', 'shape', 'design', 'solo-ai-next100')

    def build(self):
        # Plan: Preserve the isometric box as three broad faces with a shared center junction. Top-face depth differentiates the original variant.
        # Reference: Lucide box original and atomic-debug construction.

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
        poly('box',(24,6),(42,18),(42,32),(24,42),(6,32),(6,18),closed=True)
        poly('seams',(6,18),(24,28),(42,18));line('vertical',(24,28),(24,42));join('seams','box');join('vertical','seams');join('vertical','box')
