"""A tall crescent moon has a broad rounded outer curve on the left and a deeply concave inner edge on the right. Its upper and lower tips taper to pointed ends.

Preserved the crescent visible in the source despite its gibbous label; deliberate right-facing opening.
Construction reference: Lucide moon: large outer arc and concave inner arc.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ab11dce4-bd70-5a18-b77d-6f0e04cf719c'
SOURCE_PATH = 'pictographic-primitives/weather/night moon gibbous_ab11dce4-bd70-5a18-b77d-6f0e04cf719c.svg'
AUTHOR = 'gpt-6'

class TallCrescentMoon(Solo48):
    icon_id = 'tall-crescent-moon'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/weather"
    aliases = ()
    keywords = ('moon', 'crescent', 'night', 'lunar', 'sky', 'astronomy')

    def build(self) -> None:
        # Live VRECT_XL visible bounds: (6, 2, 42, 46).
        self.add_arc('outer', (40, 6), (40, 42), radius_x=32, radius_y=20, sweep=False, large_arc=False)
        self.add_arc('inner', (40, 42), (40, 6), radius_x=15, radius_y=20, sweep=True, large_arc=False)
        self.add_contour('moon', 'outer', 'inner', closed=True)
