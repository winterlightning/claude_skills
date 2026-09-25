"""bone-1: next fifty AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a601a97f-bd18-4fca-a87b-a7ca04a43188'
SOURCE_PATH = 'pictographic-primitives/symbol/bone 1_a601a97f-bd18-4fca-a87b-a7ca04a43188.svg'
AUTHOR = 'gpt-6'

class Bone1(Solo48):
    icon_id = 'bone-1'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('bone', 'symbol', 'solo-ai-next50')

    def build(self):
        # Plan: A diagonal bone uses four equal semicircular end lobes and a broad diagonal shaft. Shared lobe radius and half-turn symmetry replace the lumpy traced ends.
        # Reference: Lucide bone original and atomic-debug construction.

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
        path('bone',(24,12),[('A',(36,12),6,6,True),('A',(36,24),6,6,True),('L',(32,24)),('L',(24,32)),('L',(24,36)),('A',(12,36),6,6,True),('A',(12,24),6,6,True),('L',(16,24)),('L',(24,16)),('L',(24,12))],True)
