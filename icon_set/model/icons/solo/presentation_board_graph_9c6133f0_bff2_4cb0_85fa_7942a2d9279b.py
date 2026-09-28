"""presentation-board-graph: Clear presentation graph; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9c6133f0-bff2-4cb0-85fa-7942a2d9279b'
SOURCE_PATH = 'pictographic-primitives/office/presentation board graph_9c6133f0-bff2-4cb0-85fa-7942a2d9279b.svg'
AUTHOR = 'gpt-6'

class PresentationBoardGraph(Solo48):
    icon_id = 'presentation-board-graph'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    categories = ('office', 'primitives')
    aliases = ()
    keywords = ('solo-ai-full-set', 'presentation-board-graph')

    def build(self):
        # Plan: Preserve a rectangular display, compact line chart and tripod. Share the chart attachment with the frame.
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
        path('board',(6,6),[('L',(42,6)),('L',(42,30)),('L',(24,30)),('L',(6,30)),('L',(6,20)),('L',(6,6))],True)
        path('chart',(6,20),[('L',(17,20)),('L',(21,15)),('L',(28,22)),('L',(33,14))]);join('chart','board')
        path('stem',(24,30),[('L',(24,34)),('L',(24,42))]);poly('legs',(16,42),(24,34),(32,42));join('legs','stem');join('stem','board')
