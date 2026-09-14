"""A low semicircular arc rests on a straight horizon, interrupted near its upper-left side by a small circular sun. Short rays surround the sun, with a taller upright mark above the arc.

Dropped minor rays; preserved the sun on its respective side of the daylight arc.
Construction reference: Lucide sun: centered circle; daylight arc deliberately interrupted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3b91179d-54d6-411e-a6dd-c91c93c5edd3'
SOURCE_PATH = 'pictographic-primitives/weather/day afternoon_3b91179d-54d6-411e-a6dd-c91c93c5edd3.svg'
AUTHOR = 'gpt-6'

class AfternoonSun(Solo48):
    icon_id = 'afternoon-sun'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/weather"
    aliases = ()
    keywords = ('afternoon', 'sun', 'daylight', 'horizon', 'sky', 'weather')

    def build(self) -> None:
        # Envelope repair: shared boundary nodes and cardinal curve extrema;
        # retain the subject, grid, stroke, and declared physical joins.
        # Live HRECT_XL visible bounds: (2, 6, 46, 42).
        self.add_arc('sun-top', (4, 16), (20, 16), radius_x=8, radius_y=8, sweep=True, large_arc=False)
        self.add_arc('sun-bottom', (20, 16), (4, 16), radius_x=8, radius_y=8, sweep=True, large_arc=False)
        self.add_contour('sun', 'sun-top', 'sun-bottom', closed=True)
        self.add_arc('day-arc', (30, 22), (44, 40), radius_x=14, radius_y=18, sweep=True, large_arc=False)
        self.add_line('horizon', (4, 40), (44, 40))
        self.relate("connect", 'day-arc', 'horizon')
