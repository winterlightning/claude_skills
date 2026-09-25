"""A rounded cloud with a level lower edge spans the upper image. Three long parallel rain strokes fall diagonally toward the lower left beneath the cloud.

Reduced small lobes and precipitation count where needed; cloud remains a natural weather subject.
Construction reference: Lucide cloud: large crown, smaller side lobe, coherent contour.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '146ba800-5030-4cfb-a422-02115d163a24'
SOURCE_PATH = 'pictographic-primitives/weather/weather cloud heavy rain_146ba800-5030-4cfb-a422-02115d163a24.svg'
AUTHOR = 'gpt-6'

class HeavyRainCloud(Solo48):
    icon_id = 'heavy-rain-cloud'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "weather"
    aliases = ()
    keywords = ('cloud', 'rain', 'downpour', 'precipitation', 'weather', 'storm')

    def build(self) -> None:
        # Live HRECT_XL visible bounds: (2, 6, 46, 42).
        self.add_arc('cloud-dome', (18, 24), (32, 16), radius_x=14, radius_y=8, sweep=True, large_arc=True)
        self.add_line('cloud-shoulder', (32, 16), (36, 16))
        self.add_arc('cloud-right', (36, 16), (36, 24), radius_x=8, radius_y=4, sweep=True, large_arc=False)
        self.add_line('cloud-base', (36, 24), (18, 24))
        self.add_contour('cloud', 'cloud-dome', 'cloud-shoulder', 'cloud-right', 'cloud-base', closed=True)
        self.add_line('rain-0', (14, 35), (9, 40))
        self.add_line('rain-1', (26, 35), (21, 40))
        self.add_line('rain-2', (38, 35), (33, 40))
