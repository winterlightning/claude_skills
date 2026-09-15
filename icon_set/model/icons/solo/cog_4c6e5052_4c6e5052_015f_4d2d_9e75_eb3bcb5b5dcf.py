"""cog-4c6e5052: Eight-tooth gear; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4c6e5052-015f-4d2d-9e75-eb3bcb5b5dcf'
SOURCE_PATH = 'icons-json/interface-essential/cog_4c6e5052-015f-4d2d-9e75-eb3bcb5b5dcf.json'
AUTHOR = 'gpt-6'

class Cog4c6e5052(Solo48):
    icon_id = 'cog-4c6e5052'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('solo-ai-shapes-refine', 'solo-ai-next100', 'cog-4c6e5052')

    def build(self):
        # Plan: Restore eight distinct teeth around the gear rather than the four-armed shape. One repeated quadrant owns all tooth widths and root transitions.
        # Reference: Lucide cog: original and atomic-debug geometry.

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
        quarter=[(24,6),(28,6),(28,12),(30,12),(34,8),(40,14),(36,18),(36,20),(42,20),(42,24)]
        turn=lambda p,n:p if n==0 else turn((48-p[1],p[0]),n-1)
        poly('gear',*[turn(p,n) for n in range(4) for p in quarter[:-1]],closed=True)
