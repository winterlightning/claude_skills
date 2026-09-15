"""A wide horizontal battery has a short terminal projecting from its right end. A small charge gauge near the left edge is divided into two adjoining rectangular compartments, with empty space extending to the right."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0c8f7f81-3b5e-4964-a6bc-5955f81d4007'
SOURCE_PATH = 'pictographic-primitives/mobile/charging battery two bars_0c8f7f81-3b5e-4964-a6bc-5955f81d4007.svg'
AUTHOR = 'gpt-6'

class MobileIcon(Solo48):
    icon_id = 'two-bar-battery'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/mobile"
    aliases = ()
    keywords = ('battery', 'two-bars', 'charge', 'power', 'energy', 'level', 'indicator')

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
        for i, x in enumerate((13,21)):
            self.add_line(f'charge-{i}', (x,17), (x,31))
