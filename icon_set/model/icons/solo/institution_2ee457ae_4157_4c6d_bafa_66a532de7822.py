"""institution: Balanced flag-topped building; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2ee457ae-4157-4c6d-bafa-66a532de7822'
SOURCE_PATH = 'icons-json/symbol/institution_2ee457ae-4157-4c6d-bafa-66a532de7822.json'
AUTHOR = 'gpt-6'

class Institution(Solo48):
    icon_id = 'institution'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('solo-ai-full-set', 'institution')

    def build(self):
        # Plan: Preserve the dome and building; a broad rectangular pennant keeps the small flag opening readable.
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
        path('roof',(8,33),[('A',(24,20),16,13,True),('A',(40,33),16,13,True),('L',(36,33)),('L',(12,33)),('L',(8,33))],True)
        path('building',(12,33),[('L',(12,44)),('L',(36,44)),('L',(36,33))]);join('building','roof')
        path('flag',(24,4),[('L',(36,4)),('L',(36,12)),('L',(24,12)),('L',(24,4))],True)
        line('pole',(24,12),(24,20));join('pole','roof');join('pole','flag')
