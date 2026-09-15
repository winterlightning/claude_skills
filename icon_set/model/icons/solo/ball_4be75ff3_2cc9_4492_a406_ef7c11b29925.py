"""ball: AI stroke review; parent retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4be75ff3-2cc9-4492-a406-ef7c11b29925'
SOURCE_PATH = 'pictographic-primitives/sports/ball_4be75ff3-2cc9-4492-a406-ef7c11b29925.svg'
AUTHOR = 'gpt-6'

class Ball(Solo48):
    icon_id = 'ball'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    aliases = ()
    keywords = ('ball', 'sports', 'solo-ai-first50')

    def build(self):
        # Plan: A true circular ball with two smooth sweeping seams. Seams meet the perimeter at exact cardinal nodes; no faceted conversion curves.
        # Reference: Lucide original/volleyball.svg and atomic-debug/volleyball.svg.

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
        path('outline',(4,24), [('A',(24,4),20,20,True),('A',(44,24),20,20,True),('A',(24,44),20,20,True),('A',(4,24),20,20,True)],True)
        path('seam-top',(24,4), [('C',(44,24),(24,15),(33,24))])
        path('seam-bottom',(4,24), [('C',(24,44),(15,24),(24,33))])
        join('seam-top','outline');join('seam-bottom','outline')

