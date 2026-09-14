"""A small sun peeks from behind the upper-left side of an open-bottom cloud. Short rays surround the exposed sun, and two parallel undulating mist bands extend underneath.

Reduced sun rays and mist/rain marks while preserving the sun behind the cloud.
Construction reference: Lucide cloud and sun: large cloud contour with partial solar arc.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c23c46fb-a1b8-4874-af1a-262e7474ed2f'
SOURCE_PATH = 'pictographic-primitives/weather/cloud mist sun_c23c46fb-a1b8-4874-af1a-262e7474ed2f.svg'
AUTHOR = 'gpt-6'

class SunCloudMist(Solo48):
    icon_id = 'sun-cloud-mist'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/weather"
    aliases = ()
    keywords = ('sun', 'cloud', 'mist', 'haze', 'weather', 'atmosphere')

    def build(self) -> None:
        # Live HRECT_XL visible bounds: (2, 6, 46, 42).
        self.add_arc('cloud-left', (20, 28), (20, 20), radius_x=8, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('cloud-crown', (20, 20), (36, 20), radius_x=8, radius_y=8, sweep=True, large_arc=False)
        self.add_arc('cloud-right', (36, 20), (36, 28), radius_x=8, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('cloud', 'cloud-left', 'cloud-crown', 'cloud-right', closed=False)
        self.add_arc('sun', (6, 16), (12, 8), radius_x=8, radius_y=8, sweep=True, large_arc=False)
        self.add_line('mist', (6, 40), (42, 40))
