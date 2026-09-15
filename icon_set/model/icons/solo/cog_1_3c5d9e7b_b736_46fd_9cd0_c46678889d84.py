"""cog-1: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3c5d9e7b-b736-46fd-9cd0-c46678889d84'
SOURCE_PATH = 'pictographic-primitives/interface-essential/cog 1_3c5d9e7b-b736-46fd-9cd0-c46678889d84.svg'
AUTHOR = 'gpt-6'

class Cog1(Solo48):
    icon_id = 'cog-1'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('cog', 'interface-essential', 'solo-ai-next100')

    def build(self):
        # Plan: Eight evenly repeated gear teeth retain the original cog silhouette. Paired cardinal and diagonal teeth follow one mirrored quadrant.
        # Reference: Lucide cog original and atomic-debug construction.

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
        quadrant=[(24, 6), (28, 6), (30, 11), (34, 10), (38, 14), (37, 18), (42, 20), (42, 24)]
        turn=lambda p,n:p if n==0 else turn((48-p[1],p[0]),n-1)
        points=[]
        for n in range(4):points.extend(turn(p,n) for p in quadrant[:-1])
        poly('gear',*points,closed=True)
