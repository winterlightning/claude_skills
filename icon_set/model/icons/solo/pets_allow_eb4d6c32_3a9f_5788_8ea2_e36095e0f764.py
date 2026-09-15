"""pets-allow: Coherent dog silhouette; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'eb4d6c32-3a9f-5788-8ea2-e36095e0f764'
SOURCE_PATH = 'pictographic-primitives/wayfinding/pets allow_eb4d6c32-3a9f-5788-8ea2-e36095e0f764.svg'
AUTHOR = 'gpt-6'

class PetsAllow(Solo48):
    icon_id = 'pets-allow'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    aliases = ()
    keywords = ('solo-ai-full-set', 'pets-allow')

    def build(self):
        # Plan: Preserve the side-view dog; broaden the legs and muzzle opening while retaining the raised tail.
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
        path('dog',(8,40),[('L',(8,24)),('C',(4,18),(5,23),(4,21)),('C',(12,23),(6,21),(8,23)),('L',(21,23)),('C',(27,12),(24,23),(24,14)),('L',(32,8)),('L',(32,14)),('L',(44,18)),('L',(42,26)),('L',(36,26)),('L',(36,40)),('L',(28,40)),('L',(26,31)),('L',(18,31)),('L',(16,40)),('L',(8,40))],True)
