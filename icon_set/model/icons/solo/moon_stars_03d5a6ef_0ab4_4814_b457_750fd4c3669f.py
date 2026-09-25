"""A large crescent moon opens toward the upper right. Two four-pointed stars of unequal size occupy the space beside its concave inner edge, forming a clear night-sky group.

Reduced the second star to a dot; retained the right-facing crescent and main star.
Construction reference: Lucide moon: coherent outer and concave inner arcs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '03d5a6ef-0ab4-4814-b457-750fd4c3669f'
SOURCE_PATH = 'pictographic-primitives/weather/weather night clear_03d5a6ef-0ab4-4814-b457-750fd4c3669f.svg'
AUTHOR = 'gpt-6'

class MoonStars(Solo48):
    icon_id = 'moon-stars'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "weather"
    aliases = ()
    keywords = ('moon', 'star', 'night', 'sky', 'crescent', 'astronomy')

    def build(self) -> None:
        # Live HRECT_XL visible bounds: (2, 6, 46, 42).
        self.add_arc('moon-outer', (24, 8), (24, 40), radius_x=20, radius_y=16, sweep=False, large_arc=False)
        self.add_arc('moon-inner', (24, 40), (24, 8), radius_x=10, radius_y=16, sweep=True, large_arc=False)
        self.add_contour('moon', 'moon-outer', 'moon-inner', closed=True)
        self.add_polyline('star', (36, 8), (39, 15), (44, 18), (39, 21), (36, 28), (33, 21), (28, 18), (33, 15), closed=True)
        self.add_line('small-star', (44, 37), (44, 37))
