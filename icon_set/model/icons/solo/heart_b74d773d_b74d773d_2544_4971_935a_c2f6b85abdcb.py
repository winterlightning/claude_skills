"""heart-b74d773d: Balanced flowing heart; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b74d773d-2544-4971-935a-c2f6b85abdcb'
SOURCE_PATH = 'icons-json/romance/heart_b74d773d-2544-4971-935a-c2f6b85abdcb.json'
AUTHOR = 'gpt-6'

class HeartB74d773d(Solo48):
    icon_id = 'heart-b74d773d'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'romance'
    aliases = ()
    keywords = ('solo-ai-full-set', 'heart-b74d773d')

    def build(self):
        # Plan: Matched lobes around the shared center; retain the broad heart and pointed bottom.
        # Reference: Lucide heart: original and atomic-debug geometry.

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
        path('heart',(24,13),[('C',(34,8),(27,10),(29,8)),('C',(44,18),(40,8),(44,12)),('C',(39,27),(44,22),(42,24)),('L',(24,40)),('L',(9,27)),('C',(4,18),(6,24),(4,22)),('C',(14,8),(4,12),(8,8)),('C',(24,13),(19,8),(21,10))],True)
