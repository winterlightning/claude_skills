"""beaker: AI stroke review; parent retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f1cab2ea-f7f8-47a0-972d-7983402b29a8'
SOURCE_PATH = 'pictographic-primitives/symbol/beaker_f1cab2ea-f7f8-47a0-972d-7983402b29a8.svg'
AUTHOR = 'gpt-6'

class Beaker(Solo48):
    icon_id = 'beaker'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('beaker', 'symbol', 'solo-ai-first50')

    def build(self):
        # Plan: A round flask flows tangentially into its narrow neck. The neck and lip share nodes; omitted extra liquid decoration absent from the source.
        # Reference: Lucide original/flask-round.svg and atomic-debug/flask-round.svg.

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
        path('flask',(19,4), [('L',(19,12)),('C',(8,28),(19,18),(8,18)),('A',(40,28),16,16,False),('C',(29,12),(40,18),(29,18)),('L',(29,4))])
        poly('lip',(15,4),(19,4),(29,4),(33,4));join('lip','flask')

