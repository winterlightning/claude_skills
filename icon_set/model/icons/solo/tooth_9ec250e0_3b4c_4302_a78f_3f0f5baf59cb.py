"""tooth: Smooth tooth crown and roots; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9ec250e0-3b4c-4302-a78f-3f0f5baf59cb'
SOURCE_PATH = 'pictographic-primitives/health/tooth_9ec250e0-3b4c-4302-a78f-3f0f5baf59cb.svg'
AUTHOR = 'gpt-6'

class Tooth(Solo48):
    icon_id = 'tooth'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('solo-ai-full-set', 'tooth')

    def build(self):
        # Plan: Keep the broad crown and two roots; replace angular bulges with smooth paired curves and an open root valley.
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
        path('tooth',(24,7),[('C',(33,4),(28,6),(30,4)),('C',(40,14),(38,4),(40,8)),('C',(36,27),(40,20),(36,22)),('C',(32,44),(36,35),(37,44)),('C',(24,30),(27,44),(29,30)),('C',(16,44),(19,30),(21,44)),('C',(12,27),(11,44),(12,35)),('C',(8,14),(12,22),(8,20)),('C',(15,4),(8,8),(10,4)),('C',(24,7),(18,4),(20,6))],True)
