"""plane: Swept-wing plane — local spacing refinement; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '39150a1e-77de-4299-ad47-aea402520e87'
SOURCE_PATH = 'pictographic-primitives/travel/plane_39150a1e-77de-4299-ad47-aea402520e87.svg'
AUTHOR = 'gpt-6'

class Plane(Solo48):
    icon_id = 'plane'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'travel'
    aliases = ()
    keywords = ('solo-ai-full-set', 'plane')

    def build(self):
        # Plan: Original outlined tail and both swept wings restored. Adjusted nearby tips and junctions to open the gaps.
        # Reference: Lucide plane: original and atomic-debug geometry.

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
        path('plane',(4,29),[('L',(14,34)),('L',(23,28)),('L',(20,40)),('L',(31,36)),('L',(33,24)),('L',(40,20)),('C',(44,14),(43,18),(44,16)),('C',(37,11),(44,10),(40,9)),('L',(32,12)),('L',(19,8)),('C',(14,15),(16,8),(12,12)),('L',(22,19)),('L',(14,24)),('L',(6,21)),('L',(4,29))],True)
