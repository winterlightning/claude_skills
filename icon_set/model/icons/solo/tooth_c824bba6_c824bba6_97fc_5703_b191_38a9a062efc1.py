"""tooth-c824bba6: Smooth rooted tooth; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c824bba6-97fc-5703-b191-38a9a062efc1'
SOURCE_PATH = 'pictographic-primitives/health/tooth_c824bba6-97fc-5703-b191-38a9a062efc1.svg'
AUTHOR = 'gpt-6'

class ToothC824bba6(Solo48):
    icon_id = 'tooth-c824bba6'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('solo-ai-full-set', 'tooth-c824bba6')

    def build(self):
        # Plan: Preserve two roots and a gently notched crown. Broaden the inner root channel while keeping the natural asymmetric crown.
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
        path('tooth',(24,7),[('C',(14,4),(20,6),(18,4)),('C',(8,15),(10,4),(8,9)),('C',(12,32),(8,21),(11,27)),('C',(17,44),(13,40),(14,44)),('C',(24,28),(21,44),(18,28)),('C',(31,44),(30,28),(27,44)),('C',(36,32),(34,44),(35,40)),('C',(40,15),(37,27),(40,21)),('C',(34,4),(40,9),(38,4)),('C',(24,7),(30,4),(28,6))],True)
