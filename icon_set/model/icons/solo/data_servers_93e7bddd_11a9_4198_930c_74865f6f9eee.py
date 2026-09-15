"""data-servers: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '93e7bddd-11a9-4198-930c-74865f6f9eee'
SOURCE_PATH = 'pictographic-primitives/servers/data_93e7bddd-11a9-4198-930c-74865f6f9eee.svg'
AUTHOR = 'gpt-6'

class DataServers(Solo48):
    icon_id = 'data-servers'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'servers'
    aliases = ()
    keywords = ('data', 'servers', 'solo-ai-next100')

    def build(self):
        # Plan: Retain the original broad cylindrical database proportions. True elliptical rims and evenly spaced levels replace the irregular tracing.
        # Reference: Lucide database original and atomic-debug construction.

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
        path('top',(6,11),[('A',(42,11),18,5,True),('A',(6,11),18,5,True)],True)
        path('body',(6,11),[('L',(6,37)),('A',(42,37),18,5,False),('L',(42,11))]);join('body','top')
        path('ring',(6,24),[('A',(42,24),18,5,False)]);join('ring','body')
