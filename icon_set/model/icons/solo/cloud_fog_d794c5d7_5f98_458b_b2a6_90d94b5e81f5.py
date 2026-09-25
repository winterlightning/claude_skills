"""An open-bottom cloud has a large rounded crown and uneven smaller lobes at its sides. Two staggered horizontal mist bands sit beneath it, ending in a separated dash at the right.

Reduced small lobes and precipitation count where needed; cloud remains a natural weather subject.
Construction reference: Lucide cloud: large crown, smaller side lobe, coherent contour.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd794c5d7-5f98-458b-b2a6-90d94b5e81f5'
SOURCE_PATH = 'pictographic-primitives/weather/cloud mist_d794c5d7-5f98-458b-b2a6-90d94b5e81f5.svg'
AUTHOR = 'gpt-6'

class CloudFog(Solo48):
    icon_id = 'cloud-fog'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "weather"
    aliases = ()
    keywords = ('cloud', 'fog', 'mist', 'haze', 'weather', 'atmosphere')

    def build(self) -> None:
        # Live HRECT_XL visible bounds: (2, 6, 46, 42).
        self.add_arc('cloud-dome', (18, 20), (32, 14), radius_x=14, radius_y=6, sweep=True, large_arc=True)
        self.add_line('cloud-shoulder', (32, 14), (36, 14))
        self.add_arc('cloud-right', (36, 14), (36, 20), radius_x=8, radius_y=3, sweep=True, large_arc=False)
        self.add_contour('cloud', 'cloud-dome', 'cloud-shoulder', 'cloud-right', closed=False)
        self.add_line('fog-upper', (6, 32), (42, 32))
        self.add_line('fog-lower', (12, 40), (36, 40))
