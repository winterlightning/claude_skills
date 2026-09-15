"""spa-lotus: Smooth layered lotus; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e8702a12-17ed-5a47-8c95-0f49c17db245'
SOURCE_PATH = 'icons-json/spas/spa lotus_e8702a12-17ed-5a47-8c95-0f49c17db245.json'
AUTHOR = 'gpt-6'

class SpaLotus(Solo48):
    icon_id = 'spa-lotus'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'spas'
    aliases = ()
    keywords = ('solo-ai-full-set', 'spa-lotus')

    def build(self):
        # Plan: Preserve the layered open flower with broad central and side petals. Omit the two crowded basal curls while retaining the lotus silhouette.
        # Reference: Lucide flower-2: original and atomic-debug geometry.

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
        path('center',(24,40),[('C',(24,8),(12,30),(14,18)),('C',(24,40),(34,18),(36,30))],True)
        path('left',(24,40),[('C',(4,20),(9,40),(4,31)),('C',(16,24),(9,20),(13,22))]);join('left','center')
        path('right',(24,40),[('C',(44,20),(39,40),(44,31)),('C',(32,24),(39,20),(35,22))]);join('right','center');join('left','right')
