"""A large numeral five stands beside a capital G with a short inward horizontal arm. A smaller capital E sits at the lower right, aligned with the baseline of the larger characters."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4d3f552b-975a-5213-8db2-f60c0d18a007'
SOURCE_PATH = 'pictographic-primitives/mobile/5ge_4d3f552b-975a-5213-8db2-f60c0d18a007.svg'
AUTHOR = 'gpt-6'

class MobileIcon(Solo48):
    icon_id = 'text-5ge-text'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "mobile"
    aliases = ()
    keywords = ('5ge', 'network', 'text', 'cellular', 'mobile', 'letters', 'connection')

    def build(self):
        # Typed paths keep continuous joins; dimensions belong to each symbol.
        def path(name, start, commands, closed=False):
            members, here = [], start
            for i, (kind, end, *args) in enumerate(commands):
                ident = f"{name}-{i}"
                if kind == "L":
                    self.add_line(ident, here, end)
                else:
                    rx, ry, sweep = args
                    self.add_arc(ident, here, end, radius_x=rx, radius_y=ry, sweep=sweep)
                members.append(ident)
                here = end
            self.add_contour(name, *members, closed=closed)
        def rounded(name, x0, y0, x1, y1, r):
            path(name, (x0+r,y0), [
                ('L',(x1-r,y0)), ('A',(x1,y0+r),r,r,True),
                ('L',(x1,y1-r)), ('A',(x1-r,y1),r,r,True),
                ('L',(x0+r,y1)), ('A',(x0,y1-r),r,r,True),
                ('L',(x0,y0+r)), ('A',(x0+r,y0),r,r,True)], True)
        # Plan: three spaced monoline characters; E is half-height on the baseline.
        # HRECT_L extremes (4,8)-(44,40). No useful local Lucide lettering match.
        path('five',(12,8), [('L',(4,8)),('L',(4,24)),('L',(8,24)),('A',(12,28),4,4,True),('L',(12,36)),('A',(8,40),4,4,True),('L',(4,40))])
        path('g',(28,8), [('L',(24,8)),('A',(20,12),4,4,False),('L',(20,36)),('A',(24,40),4,4,False),('L',(28,40)),('L',(28,24)),('L',(24,24))])
        self.add_polyline('e', (44,24),(36,24),(36,32),(36,40),(44,40))
        self.add_line('e-arm',(36,32),(44,32))
        self.relate('connect','e','e-arm')
