"""synchronize-arrow: Smooth refresh curve with center; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '185b4c70-8b6e-44d8-a39b-cf7d4767f520'
SOURCE_PATH = 'icons-json/interface-essential/synchronize arrow_185b4c70-8b6e-44d8-a39b-cf7d4767f520.json'
AUTHOR = 'gpt-6'

class SynchronizeArrow(Solo48):
    icon_id = 'synchronize-arrow'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('solo-ai-full-set', 'synchronize-arrow')

    def build(self):
        # Plan: Keep the inset center ellipse and rotation direction; replace segmented perimeter with coherent arcs.
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
        path('curve',(8,24),[('A',(26,8),18,16,True),('A',(44,24),18,16,True),('A',(26,40),18,16,True)])
        path('head',(4,19),[('L',(8,24)),('L',(13,19))]);join('head','curve')
        self.add_arc('center-top',(22,24),(32,24),radius_x=5,radius_y=4)
        self.add_arc('center-bottom',(32,24),(22,24),radius_x=5,radius_y=4)
        self.add_contour('center','center-top','center-bottom',closed=True)
