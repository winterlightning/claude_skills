"""A low volcano with a flat crater sits beneath a wavy horizontal water surface. Two short rising squiggles occupy the gap between the crater and the waterline.

Reduced rising squiggles to two separated bubbles; retained mountain below the water surface.
Construction reference: No exact local match; repeated arc water pattern.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '147db3b6-d001-4901-a834-3393931ba4ae'
SOURCE_PATH = 'pictographic-primitives/weather/underwater volcano_147db3b6-d001-4901-a834-3393931ba4ae.svg'
AUTHOR = 'gpt-6'

class UnderwaterVolcano(Solo48):
    icon_id = 'underwater-volcano'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "weather"
    aliases = ()
    keywords = ('volcano', 'underwater', 'eruption', 'sea', 'vent', 'geology')

    def build(self) -> None:
        # Live HRECT_XL visible bounds: (2, 6, 46, 42).
        self.add_arc('surface-0', (4, 8), (14, 8), radius_x=5, radius_y=3, sweep=False, large_arc=False)
        self.add_arc('surface-1', (14, 8), (24, 8), radius_x=5, radius_y=3, sweep=False, large_arc=False)
        self.add_arc('surface-2', (24, 8), (34, 8), radius_x=5, radius_y=3, sweep=False, large_arc=False)
        self.add_arc('surface-3', (34, 8), (44, 8), radius_x=5, radius_y=3, sweep=False, large_arc=False)
        self.add_contour('surface', 'surface-0', 'surface-1', 'surface-2', 'surface-3', closed=False)
        self.add_polyline('mountain', (4, 40), (16, 29), (32, 29), (44, 40), closed=False)
        self.add_line('bubble-left', (19, 20), (19, 20))
        self.add_line('bubble-right', (29, 20), (29, 20))
