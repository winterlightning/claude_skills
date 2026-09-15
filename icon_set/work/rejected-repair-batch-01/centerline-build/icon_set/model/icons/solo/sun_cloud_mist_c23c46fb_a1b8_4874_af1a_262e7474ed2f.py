"""Restored a recognizable solar disk with two rays behind a fuller cloud; retained mist or rain beneath the cloud.

Construction: Lucide cloud-sun and cloud-sun-rain: round exposed sun with rays and an open cloud for precipitation.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c23c46fb-a1b8-4874-af1a-262e7474ed2f'
SOURCE_PATH = 'pictographic-primitives/weather/cloud mist sun_c23c46fb-a1b8-4874-af1a-262e7474ed2f.svg'
AUTHOR = 'gpt-6'

class SunCloudMist(Solo48):
    icon_id = 'sun-cloud-mist'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/weather'
    aliases = ()
    keywords = ('sun', 'cloud', 'mist', 'haze', 'weather', 'atmosphere')

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
        self.add_line('mist', (6, 42), (42, 42))
