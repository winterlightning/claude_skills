"""A broad closed cloud has a high crown and smaller lobes around its sides. Two long parallel rain strokes descend diagonally toward the lower left beneath its base.

Reduced small lobes and precipitation count where needed; cloud remains a natural weather subject.
Construction reference: Lucide cloud: large crown, smaller side lobe, coherent contour.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3abb087a-01a9-407f-90c2-e7c2c156e840'
SOURCE_PATH = 'pictographic-primitives/weather/weather cloud rain_3abb087a-01a9-407f-90c2-e7c2c156e840.svg'
AUTHOR = 'gpt-6'

class RainCloud(Solo48):
    icon_id = 'rain-cloud'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/weather"
    aliases = ()
    keywords = ('cloud', 'rain', 'precipitation', 'shower', 'weather', 'water')

    def build(self) -> None:
        # Live HRECT_XL visible bounds: (2, 6, 46, 42).
        self.add_arc('cloud-dome', (18, 24), (32, 16), radius_x=14, radius_y=8, sweep=True, large_arc=True)
        self.add_line('cloud-shoulder', (32, 16), (36, 16))
        self.add_arc('cloud-right', (36, 16), (36, 24), radius_x=8, radius_y=4, sweep=True, large_arc=False)
        self.add_line('cloud-base', (36, 24), (18, 24))
        self.add_contour('cloud', 'cloud-dome', 'cloud-shoulder', 'cloud-right', 'cloud-base', closed=True)
        self.add_line('rain-0', (18, 35), (13, 40))
        self.add_line('rain-1', (32, 35), (27, 40))
