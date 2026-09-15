"""plane-1: Ascending plane — clear spacing; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '18f96efa-93ca-4c4e-9556-e131c14f8073'
SOURCE_PATH = 'icons-json/travel/plane 1_18f96efa-93ca-4c4e-9556-e131c14f8073.json'
AUTHOR = 'gpt-6'

class Plane1Variant2(Solo48):
    icon_id = 'plane-1-v2'
    variant_of = 'plane-1'
    variant_label = 'Ascending plane — clear spacing'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'travel'
    aliases = ()
    keywords = ('solo-ai-full-set', 'plane-1')

    def build(self):
        # Plan: Opened the angled fuselage and wing; simplified the narrow tail into a clear stabilizer stroke.
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
        path('plane',(10,34),[('L',(17,40)),('L',(40,20)),('C',(44,13),(42,18),(44,16)),('C',(39,8),(44,10),(42,8)),('L',(29,16)),('L',(16,8)),('L',(6,16)),('L',(23,24)),('L',(10,34))],True)
        line('tail-fin',(4,24),(10,34));join('tail-fin','plane')
