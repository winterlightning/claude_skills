"""Restored a recognizable solar disk with two rays behind a fuller cloud; retained mist or rain beneath the cloud.

Construction: Lucide cloud-sun and cloud-sun-rain: round exposed sun with rays and an open cloud for precipitation.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4318ef22-166f-424b-99cd-c393dd5b9db7'
SOURCE_PATH = 'pictographic-primitives/weather/weather rain_4318ef22-166f-424b-99cd-c393dd5b9db7.svg'
AUTHOR = 'gpt-6'

class SunShower(Solo48):
    icon_id = 'sun-shower'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'weather'
    aliases = ()
    keywords = ('sun', 'rain', 'cloud', 'shower', 'weather', 'daylight')

    def build(self) -> None:
        self.add_arc('cloud-left', (11, 32), (11, 24), radius_x=5, radius_y=4, sweep=True, large_arc=False)
        self.add_line('cloud-shoulder', (11, 24), (24, 24))
        self.add_arc('cloud-crown-left', (24, 24), (30, 18), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('cloud-crown-right', (30, 18), (36, 24), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('cloud-right', (36, 24), (36, 32), radius_x=6, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('cloud', 'cloud-left', 'cloud-shoulder', 'cloud-crown-left', 'cloud-crown-right', 'cloud-right', closed=False)
        self.add_arc('solar-disk', (24, 24), (30, 18), radius_x=6, radius_y=6, sweep=True, large_arc=True)
        self.relate("connect", 'solar-disk', 'cloud-shoulder')
        self.relate("connect", 'solar-disk', 'cloud-crown-left')
        self.relate("connect", 'solar-disk', 'cloud-crown-right')
        self.add_line('ray-left', (6, 16), (9, 16))
        self.add_line('ray-diagonal', (12, 6), (13, 7))
        self.add_line('rain-left', (18, 38), (14, 42))
        self.add_line('rain-right', (30, 38), (26, 42))
