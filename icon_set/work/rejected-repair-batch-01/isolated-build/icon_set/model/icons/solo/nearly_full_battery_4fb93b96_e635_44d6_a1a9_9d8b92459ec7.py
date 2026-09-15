"""A horizontal battery has a rounded rectangular body and a short terminal projecting from its right end. Five evenly spaced vertical charge marks occupy most of the body, leaving a small blank area beside the terminal."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4fb93b96-e635-44d6-a1a9-9d8b92459ec7'
SOURCE_PATH = 'pictographic-primitives/mobile/charging battery almost full_4fb93b96-e635-44d6-a1a9-9d8b92459ec7.svg'
AUTHOR = 'gpt-6'

class MobileIcon(Solo48):
    icon_id = 'nearly-full-battery'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/mobile"
    aliases = ()
    keywords = ('battery', 'charge', 'level', 'nearly-full', 'power', 'energy', 'indicator')

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
            self.add_line(f'charge-{i}', (x,24 if i == 2 else 17), (x,31))
