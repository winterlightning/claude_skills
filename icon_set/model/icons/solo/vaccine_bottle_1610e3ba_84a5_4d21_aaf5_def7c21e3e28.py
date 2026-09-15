"""vaccine-bottle: Smooth vaccine vial; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1610e3ba-84a5-4d21-aaf5-def7c21e3e28'
SOURCE_PATH = 'icons-json/health/vaccine bottle_1610e3ba-84a5-4d21-aaf5-def7c21e3e28.json'
AUTHOR = 'gpt-6'

class VaccineBottle(Solo48):
    icon_id = 'vaccine-bottle'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('solo-ai-full-set', 'vaccine-bottle')

    def build(self):
        # Plan: Preserve the neck, broad bottle and liquid surface; use matching shoulders and a coherent waterline.
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
        path('bottle',(18,4),[('L',(18,13)),('C',(8,18),(12,15),(8,16)),('L',(8,29)),('L',(8,40)),('A',(12,44),4,4,False),('L',(36,44)),('A',(40,40),4,4,False),('L',(40,29)),('L',(40,18)),('C',(30,13),(40,16),(36,15)),('L',(30,4))])
        path('cap',(14,4),[('L',(18,4)),('L',(30,4)),('L',(34,4))]);join('cap','bottle')
        path('liquid',(8,29),[('C',(24,29),(14,26),(18,26)),('C',(40,29),(30,32),(34,32))]);join('liquid','bottle')
