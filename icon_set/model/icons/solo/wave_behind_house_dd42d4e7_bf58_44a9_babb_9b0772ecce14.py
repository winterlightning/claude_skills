"""A small pitched-roof house with a square window stands amid two rows of waves. A much larger curling wave rises behind the house and bends over toward its roof.

Kept the small house under a much larger breaking wave; omitted the window and extra waterline.
Construction reference: No useful exact local wave match; coherent circular crest and broad elliptical trough.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dd42d4e7-bf58-44a9-babb-9b0772ecce14'
SOURCE_PATH = 'pictographic-primitives/weather/flood house wave_dd42d4e7-bf58-44a9-babb-9b0772ecce14.svg'
AUTHOR = 'gpt-6'

class WaveBehindHouse(Solo48):
    icon_id = 'wave-behind-house'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/weather"
    aliases = ()
    keywords = ('flood', 'house', 'wave', 'tsunami', 'water', 'disaster')

    def build(self) -> None:
        # Live HRECT_XL visible bounds: (2, 6, 46, 42).
        self.add_polyline('house', (6, 40), (6, 30), (12, 22), (20, 30), (20, 40), closed=True)
        self.add_arc('wave-outer', (20, 8), (42, 32), radius_x=24, radius_y=24, sweep=True, large_arc=False)
        self.add_arc('wave-toe', (42, 32), (20, 40), radius_x=24, radius_y=8, sweep=True, large_arc=False)
        self.add_arc('wave-inner-lower', (20, 40), (28, 28), radius_x=8, radius_y=12, sweep=False, large_arc=False)
        self.add_arc('wave-inner-upper', (28, 28), (20, 8), radius_x=8, radius_y=20, sweep=False, large_arc=False)
        self.add_contour('wave', 'wave-outer', 'wave-toe', 'wave-inner-lower', 'wave-inner-upper', closed=True)
        self.relate("connect", 'wave', 'house')
