"""graph-line-spline: Smooth two-series graph; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8f4acbb4-799c-5a89-97d6-f6dbcb05930f'
SOURCE_PATH = 'icons-json/business/graph line spline_8f4acbb4-799c-5a89-97d6-f6dbcb05930f.json'
AUTHOR = 'gpt-6'

class GraphLineSpline(Solo48):
    icon_id = 'graph-line-spline'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('solo-ai-full-set', 'graph-line-spline')

    def build(self):
        # Plan: Preserve both chart series and axes. Repeat a shallow coherent wave at a twelve-unit offset and start clear of the vertical axis.
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
        poly('axis',(4,8),(4,40),(44,40))
        path('upper',(13,16),[('C',(28,12),(19,8),(22,12)),('C',(44,8),(34,14),(39,13))])
        path('lower',(13,28),[('C',(28,24),(19,20),(22,24)),('C',(44,20),(34,26),(39,25))])
