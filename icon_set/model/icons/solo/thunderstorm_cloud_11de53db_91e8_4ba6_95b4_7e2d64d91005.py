"""A closed rounded cloud with a flat base sits above a diagonal rain stroke and a small zigzag lightning bolt. Both weather marks descend beneath the cloud.

Reduced small lobes and precipitation count where needed; cloud remains a natural weather subject.
Construction reference: Lucide cloud: large crown, smaller side lobe, coherent contour.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '11de53db-91e8-4ba6-95b4-7e2d64d91005'
SOURCE_PATH = 'pictographic-primitives/weather/weather cloud rain thunder_11de53db-91e8-4ba6-95b4-7e2d64d91005.svg'
AUTHOR = 'gpt-6'

class ThunderstormCloud(Solo48):
    icon_id = 'thunderstorm-cloud'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "weather"
    aliases = ()
    keywords = ('cloud', 'thunder', 'lightning', 'rain', 'storm', 'weather')

    def build(self) -> None:
        # Live HRECT_XL visible bounds: (2, 6, 46, 42).
        self.add_arc('cloud-dome', (18, 24), (32, 16), radius_x=14, radius_y=8, sweep=True, large_arc=True)
        self.add_line('cloud-shoulder', (32, 16), (36, 16))
        self.add_arc('cloud-right', (36, 16), (36, 24), radius_x=8, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('cloud', 'cloud-dome', 'cloud-shoulder', 'cloud-right', closed=False)
        self.add_line('rain', (12, 34), (7, 40))
        self.add_polyline('lightning', (36, 24), (24, 32), (39, 32), (27, 40), closed=False)
        self.relate("connect", 'cloud', 'lightning')
