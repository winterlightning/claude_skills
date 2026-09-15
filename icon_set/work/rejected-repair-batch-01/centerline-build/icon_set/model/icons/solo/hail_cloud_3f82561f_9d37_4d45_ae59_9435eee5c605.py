"""A closed cloud has a high rounded crown, smaller side lobes, and a broad curved lower edge. Three short diagonal precipitation marks hang beneath it at staggered heights.

Reduced small lobes and precipitation count where needed; cloud remains a natural weather subject.
Construction reference: Lucide cloud: large crown, smaller side lobe, coherent contour.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3f82561f-9d37-4d45-ae59-9435eee5c605'
SOURCE_PATH = 'pictographic-primitives/weather/weather cloud hail_3f82561f-9d37-4d45-ae59-9435eee5c605.svg'
AUTHOR = 'gpt-6'

class HailCloud(Solo48):
    icon_id = 'hail-cloud'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/weather"
    aliases = ()
    keywords = ('cloud', 'hail', 'precipitation', 'storm', 'weather', 'ice')

    def build(self) -> None:
        # Live HRECT_XL visible bounds: (2, 6, 46, 42).
        self.add_arc('cloud-dome', (18, 24), (32, 16), radius_x=14, radius_y=8, sweep=True, large_arc=True)
        self.add_line('cloud-shoulder', (32, 16), (36, 16))
        self.add_arc('cloud-right', (36, 16), (36, 24), radius_x=8, radius_y=4, sweep=True, large_arc=False)
        self.add_line('cloud-base', (36, 24), (18, 24))
        self.add_contour('cloud', 'cloud-dome', 'cloud-shoulder', 'cloud-right', 'cloud-base', closed=True)
        self.add_line('hail-0', (14, 36), (12, 40))
        self.add_line('hail-1', (26, 36), (24, 40))
        self.add_line('hail-2', (38, 36), (36, 40))
