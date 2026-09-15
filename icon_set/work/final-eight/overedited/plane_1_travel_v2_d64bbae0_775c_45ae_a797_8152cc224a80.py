"""plane-1-travel: Side-view plane — clear spacing; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd64bbae0-775c-45ae-a797-8152cc224a80'
SOURCE_PATH = 'icons-json/travel/plane 1_d64bbae0-775c-45ae-a797-8152cc224a80.json'
AUTHOR = 'gpt-6'

class Plane1TravelVariant2(Solo48):
    icon_id = 'plane-1-travel-v2'
    variant_of = 'plane-1-travel'
    variant_label = 'Side-view plane — clear spacing'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'travel'
    aliases = ()
    keywords = ('solo-ai-full-set', 'plane-1-travel')

    def build(self):
        # Plan: Widened both mirrored wings and preserved the rounded nose.
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
        path('plane',(4,14),[('L',(16,20)),('L',(20,20)),('L',(14,8)),('L',(25,8)),('L',(31,20)),('L',(39,20)),('C',(44,24),(42,20),(44,22)),('C',(39,28),(44,26),(42,28)),('L',(31,28)),('L',(25,40)),('L',(14,40)),('L',(20,28)),('L',(16,28)),('L',(4,34)),('L',(8,24)),('L',(4,14))],True)
