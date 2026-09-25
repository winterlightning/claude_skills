"""A horizontal battery has a rounded rectangular case and a small terminal on its right end. A long inset charge gauge spans most of the case and is divided into four adjacent compartments."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '33faddf4-6c93-4508-bf49-bd5a27dd53af'
SOURCE_PATH = 'pictographic-primitives/mobile/charging battery full_33faddf4-6c93-4508-bf49-bd5a27dd53af.svg'
AUTHOR = 'gpt-6'

class MobileIcon(Solo48):
    icon_id = 'full-battery-segmented'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "mobile"
    aliases = ()
    keywords = ('battery', 'charge', 'full', 'power', 'energy', 'gauge', 'indicator')

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
        self.add_polyline('case', (4,8),(36,8),(36,40),(4,40), closed=True)
        self.add_line('terminal', (44,20), (44,28))
        for i, x in enumerate((12,20,28)):
            self.add_line(f'charge-{i}', (x,17), (x,31))
