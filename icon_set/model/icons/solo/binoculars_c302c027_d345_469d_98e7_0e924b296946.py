"""binoculars: Tapered barrels; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c302c027-d345-469d-98e7-0e924b296946'
SOURCE_PATH = 'icons-json/outdoors/binoculars_c302c027-d345-469d-98e7-0e924b296946.json'
AUTHOR = 'gpt-6'

class Binoculars(Solo48):
    icon_id = 'binoculars'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('solo-ai-next50-refine', 'solo-ai-next50', 'binoculars')

    def build(self):
        # Plan: Mirrored broad eyepieces taper out to round objectives. Shared lens radii and an upper bridge preserve the original binocular proportions.
        # Reference: Lucide binoculars: original and atomic-debug geometry.

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
        for side in (-1,1):
         x=lambda d:24+side*d
         circle(f'lens-{side}',x(12),32,8)
         path(f'barrel-{side}',(x(20),32),[('C',(x(16),14),(x(20),26),(x(16),20)),('C',(x(10),8),(x(16),10),(x(14),8)),('C',(x(4),14),(x(6),8),(x(4),10)),('L',(x(4),18)),('L',(x(4),32))])
         join(f'barrel-{side}',f'lens-{side}')
        line('bridge',(20,18),(28,18))
        join('bridge','barrel--1');join('bridge','barrel-1')
