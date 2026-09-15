"""time-stopwatch-half: Regular split stopwatch; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '91cc612c-2da3-5c85-8791-ab1cd23dc432'
SOURCE_PATH = 'icons-json/interface-essential/time stopwatch half_91cc612c-2da3-5c85-8791-ab1cd23dc432.json'
AUTHOR = 'gpt-6'

class TimeStopwatchHalf(Solo48):
    icon_id = 'time-stopwatch-half'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('solo-ai-full-set', 'time-stopwatch-half')

    def build(self):
        # Plan: A true circular case is optically shifted one unit left to balance the side button. The divider and controls meet exact circle nodes.
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
        path('case',(23,14),[('A',(35,20),15,15,True),('A',(38,29),15,15,True),('A',(23,44),15,15,True),('A',(8,29),15,15,True),('A',(23,14),15,15,True)],True)
        line('divider',(23,14),(23,44));join('divider','case');line('stem',(23,4),(23,14));join('stem','case')
        path('button',(18,4),[('L',(23,4)),('L',(28,4))]);join('button','stem');line('side',(35,20),(40,15));join('side','case')
