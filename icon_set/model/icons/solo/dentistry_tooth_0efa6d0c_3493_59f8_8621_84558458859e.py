"""dentistry-tooth: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0efa6d0c-3493-59f8-8621-84558458859e'
SOURCE_PATH = 'icons-json/health/dentistry tooth_0efa6d0c-3493-59f8-8621-84558458859e.json'
AUTHOR = 'gpt-6'

class DentistryTooth(Solo48):
    icon_id = 'dentistry-tooth'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('dentistry', 'tooth', 'health', 'solo-ai-next100')

    def build(self):
        # Plan: Keep the broad crown and two long rounded roots. Shared root proportions preserve the tooth identity. Both sides mirror smoothly.
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
        path('tooth',(24,6),[('C',(34,4),(28,6),(30,4)),('C',(40,13),(39,4),(40,7)),
        ('C',(36,27),(40,18),(36,22)),
        ('C',(30,44),(35,34),(35,44)),('C',(24,28),(29,44),(31,28)),('C',(18,44),(17,28),(19,44)),('C',(12,27),(13,44),(13,34)),('C',(8,13),(12,22),(8,18)),('C',(14,4),(8,7),(9,4)),('C',(24,6),(18,4),(20,6))],True)
