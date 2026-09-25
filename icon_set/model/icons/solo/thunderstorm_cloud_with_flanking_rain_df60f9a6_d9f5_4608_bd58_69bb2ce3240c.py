"""A rounded closed cloud sits above a central zigzag lightning bolt flanked by two diagonal rain strokes. The rain falls toward the lower left on either side of the bolt.

Reduced small lobes and precipitation count where needed; cloud remains a natural weather subject.
Construction reference: Lucide cloud: large crown, smaller side lobe, coherent contour.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'df60f9a6-d9f5-4608-bd58-69bb2ce3240c'
SOURCE_PATH = 'pictographic-primitives/weather/weather cloud thunder rain_df60f9a6-d9f5-4608-bd58-69bb2ce3240c.svg'
AUTHOR = 'gpt-6'

class ThunderstormCloudWithFlankingRain(Solo48):
    icon_id = 'thunderstorm-cloud-with-flanking-rain'
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
