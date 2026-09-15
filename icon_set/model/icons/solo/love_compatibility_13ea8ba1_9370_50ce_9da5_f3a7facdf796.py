"""love-compatibility: Smooth overlapping hearts; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '13ea8ba1-9370-50ce-9da5-f3a7facdf796'
SOURCE_PATH = 'pictographic-primitives/romance/love compatibility_13ea8ba1-9370-50ce-9da5-f3a7facdf796.svg'
AUTHOR = 'gpt-6'

class LoveCompatibility(Solo48):
    icon_id = 'love-compatibility'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'romance'
    aliases = ()
    keywords = ('solo-ai-full-set', 'love-compatibility')

    def build(self):
        # Plan: Preserve two overlapping hearts at different depths. Keep the rear outline open only where the front heart occludes it.
        # Reference: Lucide heart-crack: original and atomic-debug geometry.

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
        path('front',(31,22),[('C',(38,18),(33,19),(36,18)),('C',(44,25),(42,18),(44,21)),('C',(31,40),(44,31),(36,36)),('C',(18,25),(26,36),(18,31)),('C',(24,18),(18,21),(20,18)),('C',(31,22),(26,18),(29,19))],True)
        path('rear',(21,34),[('L',(16,40)),('C',(4,20),(10,34),(4,27)),('C',(13,8),(4,12),(8,8)),('C',(21,12),(16,8),(19,10)),('C',(29,8),(23,10),(26,8)),('C',(38,18),(34,8),(38,12))]);join('rear','front')
