"""archway: AI stroke review; parent retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '726d709a-1fc5-42e8-b357-8d83c0bb1293'
SOURCE_PATH = 'icons-json/_uncategorized_04/archway_726d709a-1fc5-42e8-b357-8d83c0bb1293.json'
AUTHOR = 'gpt-6'

class ArchwayVariant2(Solo48):
    icon_id = 'archway-v2'
    variant_of = 'archway'
    variant_label = 'AI stroke review · first 50'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_04'
    aliases = ()
    keywords = ('archway', '_uncategorized_04', 'solo-ai-first50')

    def build(self):
        # Plan: Concentric tangent arches form one continuous architectural outline. A shared center and radii keep the passage equally wide.
        # Reference: No useful exact Lucide match; geometric construction from the supplied subject.

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
        path('arch',(4,40), [('L',(4,28)),('A',(44,28),20,20,True),('L',(44,40)),('L',(36,40)),('L',(36,28)),('A',(12,28),12,12,False),('L',(12,40)),('L',(4,40))],True)

