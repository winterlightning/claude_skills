"""airplane-other: Airliner · top view; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4a625cc1-8989-433b-89db-ddf1b6a98ffe'
SOURCE_PATH = 'icons-json/other/airplane_4a625cc1-8989-433b-89db-ddf1b6a98ffe.json'
AUTHOR = 'gpt-6'

class AirplaneOther(Solo48):
    icon_id = 'airplane-other'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('solo-ai-refine', 'solo-ai-first50', 'airplane-other')

    def build(self):
        # Plan: A front-to-back axis owns a round nose, broad swept wings, and a distinct tailplane. Mirrored coordinates make a second airplane design; deliberate upright orientation.
        # Reference: Lucide plane: original and atomic-debug geometry.

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
        right=[(28,10),(28,18),(42,28),(42,36),(28,28),(28,35),(34,39),(34,42),(24,40)]
        mirror=lambda p:(48-p[0],p[1])
        commands=[('L',p) for p in right[1:]]+[('L',mirror(p)) for p in reversed(right[:-1])]+[('A',(28,10),4,4,True)]
        path('airframe',right[0],commands,True)
