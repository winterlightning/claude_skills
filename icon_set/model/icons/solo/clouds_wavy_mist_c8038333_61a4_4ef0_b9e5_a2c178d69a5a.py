"""A smaller closed cloud overlaps the lower-left portion of a taller cloud behind it. Two broad parallel undulating bands extend across the space below both clouds.

Removed extra tiny lobes and reduced lower bands; preserved the diagonal cloud overlap.
Construction reference: Lucide cloud: joined large and small lobes; intentional diagonal overlap.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c8038333-61a4-4ef0-b9e5-a2c178d69a5a'
SOURCE_PATH = 'pictographic-primitives/weather/cloud mist_c8038333-61a4-4ef0-b9e5-a2c178d69a5a.svg'
AUTHOR = 'gpt-6'

class CloudsWavyMist(Solo48):
    icon_id = 'clouds-wavy-mist'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "weather"
    categories = ("weather", "primitives")
    aliases = ()
    keywords = ('cloud', 'mist', 'haze', 'overcast', 'weather', 'atmosphere')

    def build(self) -> None:
        # Envelope repair: shared boundary nodes and cardinal curve extrema;
        # retain the subject, grid, stroke, and declared physical joins.
        # Live HRECT_XL visible bounds: (2, 6, 46, 42).
        self.add_arc('front-left', (12, 28), (12, 18), radius_x=8, radius_y=5, sweep=True, large_arc=False)
        self.add_arc('front-crown-left', (12, 18), (20, 12), radius_x=8, radius_y=6, sweep=True)
        self.add_arc('front-crown-right', (20, 12), (28, 18), radius_x=8, radius_y=6, sweep=True)
        self.add_arc('front-right', (28, 18), (28, 28), radius_x=8, radius_y=5, sweep=True, large_arc=False)
        self.add_line('front-base', (28, 28), (12, 28))
        self.add_contour('front', 'front-left', 'front-crown-left', 'front-crown-right', 'front-right', 'front-base', closed=True)
        self.add_arc('back-top', (20, 12), (36, 12), radius_x=8, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('back-side', (36, 12), (36, 24), radius_x=8, radius_y=6, sweep=True, large_arc=False)
        self.add_line('back-return', (36, 24), (36, 24))
        self.add_contour('back', 'back-top', 'back-side', 'back-return', closed=False)
        self.add_arc('mist-a', (6, 38), (24, 38), radius_x=9, radius_y=2, sweep=False, large_arc=False)
        self.add_arc('mist-b', (24, 38), (42, 38), radius_x=9, radius_y=2, sweep=True, large_arc=False)
        self.add_contour('mist', 'mist-a', 'mist-b', closed=False)
        self.relate("connect", "front", "back")
