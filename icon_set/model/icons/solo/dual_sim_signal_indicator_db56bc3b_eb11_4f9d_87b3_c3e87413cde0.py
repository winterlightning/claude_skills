"""Three hollow rounded signal bars increase in height from left to right. A separate lower row of three short horizontal marks aligns beneath them, forming a two-row cellular signal display."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'db56bc3b-eb11-4f9d-87b3-c3e87413cde0'
SOURCE_PATH = 'pictographic-primitives/mobile/dual sim signal full_db56bc3b-eb11-4f9d-87b3-c3e87413cde0.svg'
AUTHOR = 'gpt-6'

class MobileIcon(Solo48):
    icon_id = 'dual-sim-signal-indicator'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "mobile"
    aliases = ()
    keywords = ('dual-sim', 'signal', 'bars', 'cellular', 'network', 'reception', 'indicator')

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
        # Plan: three repeated hollow columns, rising tops, aligned second row.
        # HRECT_L extremes (4,8)-(44,40). Lucide signal: common baseline and progression.
        for i, (x, top) in enumerate(((4,24),(20,16),(36,8))):
            self.add_polyline(f'bar-{i}', (x,top),(x+8,top),(x+8,32),(x,32), closed=True)
            self.add_line(f'second-sim-{i}', (x,40),(x+8,40))
