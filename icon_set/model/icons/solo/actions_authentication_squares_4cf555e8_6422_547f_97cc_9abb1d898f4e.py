"""actions-authentication-squares: Clean routed connection; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4cf555e8-6422-547f-97cc-9abb1d898f4e'
SOURCE_PATH = 'pictographic-primitives/programing/actions authentication squares_4cf555e8-6422-547f-97cc-9abb1d898f4e.svg'
AUTHOR = 'gpt-6'

class ActionsAuthenticationSquares(Solo48):
    icon_id = 'actions-authentication-squares'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('solo-ai-full-set', 'actions-authentication-squares')

    def build(self):
        # Plan: Preserve the two endpoint types and S-shaped route; use coherent semicircular turns and clear node spacing.
        # Reference: Original subject; preserve the distinctive silhouette and proportions.

        # Typed path helpers preserve each continuous stroke and its round joins.
        def path(name, start, commands, closed=False):
            members = []
            here = start
            for index, command in enumerate(commands):
                ident = f"{name}-{index}"
                kind, end, *args = command
                if kind == "L" and tuple(end) == tuple(here):
                    continue
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
        if False:circle('start',12,12,6)
        else:path('start',(6,6),[('L',(18,6)),('L',(18,12)),('L',(18,18)),('L',(6,18)),('L',(6,6))],True)
        path('end',(32,32),[('L',(42,32)),('L',(42,42)),('L',(32,42)),('L',(32,36)),('L',(32,32))],True)
        path('route',(18,12),[('L',(32,12)),('A',(32,24),6,6,True),('L',(26,24)),('A',(26,36),6,6,False),('L',(32,36))]);join('route','start');join('route','end')
