"""An open-bottom sun with short outward rays sits above three wavy horizontal bands. The lower bands become shorter, forming a tapered stack beneath the rounded sun.

Removed small rays and the smallest haze band; retained sun and wavy heat bands.
Construction reference: Lucide sun: simple round solar crown; repeated tangent wave pattern.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9e2f3033-98e7-4217-9974-b26635bf4221'
SOURCE_PATH = 'pictographic-primitives/weather/heat wax seal_9e2f3033-98e7-4217-9974-b26635bf4221.svg'
AUTHOR = 'gpt-6'

class SunHeatHaze(Solo48):
    icon_id = 'sun-heat-haze'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/weather"
    aliases = ()
    keywords = ('sun', 'heat', 'haze', 'hot', 'weather', 'climate')

    def build(self) -> None:
        # Live HRECT_XL visible bounds: (2, 6, 46, 42).
        self.add_arc('sun', (12, 20), (36, 20), radius_x=12, radius_y=12, sweep=True, large_arc=False)
        self.add_arc('haze-0-a', (6, 29), (24, 29), radius_x=10, radius_y=1, sweep=False, large_arc=False)
        self.add_arc('haze-0-b', (24, 29), (42, 29), radius_x=10, radius_y=1, sweep=True, large_arc=False)
        self.add_contour('haze-0', 'haze-0-a', 'haze-0-b', closed=False)
        self.add_arc('haze-1-a', (6, 39), (24, 39), radius_x=10, radius_y=1, sweep=False, large_arc=False)
        self.add_arc('haze-1-b', (24, 39), (42, 39), radius_x=10, radius_y=1, sweep=True, large_arc=False)
        self.add_contour('haze-1', 'haze-1-a', 'haze-1-b', closed=False)
