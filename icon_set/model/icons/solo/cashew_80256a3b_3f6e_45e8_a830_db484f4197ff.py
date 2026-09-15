"""cashew: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '80256a3b-3f6e-45e8-a830-db484f4197ff'
SOURCE_PATH = 'icons-json/_uncategorized_10/cashew_80256a3b-3f6e-45e8-a830-db484f4197ff.json'
AUTHOR = 'gpt-6'

class Cashew(Solo48):
    icon_id = 'cashew'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized'
    aliases = ()
    keywords = ('cashew', '_uncategorized', 'solo-ai-next100')

    def build(self):
        # Plan: A smooth crescent cashew retains broad rounded tips, a full outer belly and one scooped inner curve.
        # Reference: No useful exact Lucide match; supplied original silhouette.

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
        path('nut',(29,6),[('C',(42,20),(38,6),(42,10)),('C',(19,42),(42,34),(33,42)),('C',(6,30),(10,42),(6,37)),('C',(15,25),(6,24),(10,23)),('C',(25,20),(23,29),(28,24)),('C',(23,12),(23,17),(22,15)),('C',(29,6),(23,8),(25,6))],True)
