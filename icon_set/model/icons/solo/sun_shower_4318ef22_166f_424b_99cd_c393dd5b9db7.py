"""A small sun with short rays peeks behind the upper-left side of a rounded open-bottom cloud. Two long diagonal rain strokes fall beneath the cloud toward the lower left.

Reduced sun rays and mist/rain marks while preserving the sun behind the cloud.
Construction reference: Lucide cloud and sun: large cloud contour with partial solar arc.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4318ef22-166f-424b-99cd-c393dd5b9db7'
SOURCE_PATH = 'pictographic-primitives/weather/weather rain_4318ef22-166f-424b-99cd-c393dd5b9db7.svg'
AUTHOR = 'gpt-6'

class SunShower(Solo48):
    icon_id = 'sun-shower'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/weather"
    aliases = ()
    keywords = ('sun', 'rain', 'cloud', 'shower', 'weather', 'daylight')

    def build(self) -> None:
        # Live HRECT_XL visible bounds: (2, 6, 46, 42).
        self.add_arc('cloud-left', (20, 28), (20, 20), radius_x=8, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('cloud-crown', (20, 20), (36, 20), radius_x=8, radius_y=8, sweep=True, large_arc=False)
        self.add_arc('cloud-right', (36, 20), (36, 28), radius_x=8, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('cloud', 'cloud-left', 'cloud-crown', 'cloud-right', closed=False)
        self.add_arc('sun', (6, 16), (12, 8), radius_x=8, radius_y=8, sweep=True, large_arc=False)
        self.add_line('rain-left', (24, 37), (21, 40))
        self.add_line('rain-right', (38, 37), (35, 40))
