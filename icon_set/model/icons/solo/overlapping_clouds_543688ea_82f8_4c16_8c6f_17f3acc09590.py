"""A small rounded cloud overlaps the lower portion of a larger cloud behind it. Both have high curved crowns and smaller side lobes, with a level base on the foreground cloud.

Retained a large round rear cloud and a smaller foreground cloud; omitted tiny secondary lobes.
Construction reference: Lucide cloud: joined large and small lobes; intentional diagonal overlap.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '543688ea-82f8-4c16-8c6f-17f3acc09590'
SOURCE_PATH = 'pictographic-primitives/weather/weather clouds_543688ea-82f8-4c16-8c6f-17f3acc09590.svg'
AUTHOR = 'gpt-6'

class OverlappingClouds(Solo48):
    icon_id = 'overlapping-clouds'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/weather"
    aliases = ()
    keywords = ('cloud', 'overcast', 'sky', 'weather', 'cloudy', 'atmosphere')

    def build(self) -> None:
        # Live HRECT_XL visible bounds: (2, 6, 46, 42).
        self.add_arc('front-left', (12, 40), (12, 30), radius_x=8, radius_y=5, sweep=True, large_arc=False)
        self.add_arc('front-crown', (12, 30), (28, 30), radius_x=8, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('front-right', (28, 30), (28, 40), radius_x=8, radius_y=5, sweep=True, large_arc=False)
        self.add_line('front-base', (28, 40), (12, 40))
        self.add_contour('front', 'front-left', 'front-crown', 'front-right', 'front-base', closed=True)
        self.add_line('back-start', (12, 30), (12, 24))
        self.add_arc('back-crown', (12, 24), (42, 24), radius_x=16, radius_y=16, sweep=True, large_arc=False)
        self.add_arc('back-right', (42, 24), (28, 40), radius_x=16, radius_y=16, sweep=True, large_arc=False)
        self.add_contour('back', 'back-start', 'back-crown', 'back-right', closed=False)
        self.relate("connect", 'front', 'back')
