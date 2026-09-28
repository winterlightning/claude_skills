"""box-25bec113: next fifty AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '25bec113-9501-56df-8f1c-88dce76cb03d'
SOURCE_PATH = 'pictographic-primitives/shipping/box_25bec113-9501-56df-8f1c-88dce76cb03d.svg'
AUTHOR = 'gpt-6'

class Box25bec113(Solo48):
    icon_id = 'box-25bec113'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shipping'
    categories = ('primitives', 'shipping')
    aliases = ()
    keywords = ('box', 'shipping', 'solo-ai-next50')

    def build(self):
        # Plan: A rounded tuck-top carton has a broad central closing tab. Matching radii soften the package without copying a flat frame.
        # Reference: Lucide package original and atomic-debug construction.

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
        path('carton',(12,6),[('L',(18,6)),('L',(18,18)),('L',(30,18)),('L',(30,6)),('L',(36,6)),('A',(42,12),6,6,True),('L',(42,36)),('A',(36,42),6,6,True),('L',(12,42)),('A',(6,36),6,6,True),('L',(6,12)),('A',(12,6),6,6,True)],True)
