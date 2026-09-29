"""A wide horizontal battery case has a short projecting terminal at its right edge. Two upright charge marks sit together near the left end, leaving the rest of the interior empty."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '49b6bd6a-0b34-4b3d-ac40-03cf5a529dc8'
SOURCE_PATH = 'pictographic-primitives/mobile/charging battery low_49b6bd6a-0b34-4b3d-ac40-03cf5a529dc8.svg'
AUTHOR = 'gpt-6'

class MobileIcon(Solo48):
    icon_id = 'low-battery'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "mobile"
    categories = ("mobile", "primitives")
    aliases = ()
    keywords = ('battery', 'low', 'charge', 'power', 'energy', 'level', 'indicator')

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
        # HRECT_L extremes (4,8)-(44,40). Rounded cell and detached terminal.
        # Lucide battery-full: equal corner radii and an evenly spaced charge series.
        rounded('case', 4, 8, 36, 40, 4)
        self.add_line('terminal', (44,20), (44,28))
        self.add_line('charge', (13,17), (13,31))
