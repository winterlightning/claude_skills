"""A rounded cloud occupies the lower-left foreground, with a tall crescent moon emerging behind its upper-right side. The moon opens rightward and its lower tip disappears behind the cloud.

Reduced secondary lobes and rain count; preserved rightward crescent behind a lower-left cloud.
Construction reference: Lucide moon and cloud: coherent overlapping silhouettes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '742a56dd-ee6a-4cf9-b147-bd0d263abf06'
SOURCE_PATH = 'pictographic-primitives/weather/weather night cloudy_742a56dd-ee6a-4cf9-b147-bd0d263abf06.svg'
AUTHOR = 'gpt-6'

class MoonCloud(Solo48):
    icon_id = 'moon-cloud'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "weather"
    categories = ("weather", "primitives")
    aliases = ()
    keywords = ('moon', 'cloud', 'night', 'sky', 'cloudy', 'weather')

    def build(self) -> None:
        # Live HRECT_XL visible bounds: (2, 6, 46, 42).
        self.add_arc('front-left', (12, 40), (12, 30), radius_x=8, radius_y=5, sweep=True, large_arc=False)
        self.add_arc('front-crown', (12, 30), (28, 30), radius_x=8, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('front-right', (28, 30), (28, 40), radius_x=8, radius_y=5, sweep=True, large_arc=False)
        self.add_line('front-base', (28, 40), (12, 40))
        self.add_contour('front', 'front-left', 'front-crown', 'front-right', 'front-base', closed=True)
        self.add_arc('moon-outer', (44, 8), (44, 24), radius_x=12, radius_y=8, sweep=False, large_arc=False)
        self.add_arc('moon-inner', (44, 24), (44, 8), radius_x=3, radius_y=8, sweep=True, large_arc=False)
        self.add_contour('moon', 'moon-outer', 'moon-inner', closed=True)
