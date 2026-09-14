"""Square envelope; moved the sun up one unit and retained the snowline and mountain.

SQUARE: visible ink (4, 4, 44, 44). Square envelope preserves the subject’s near-equal overall width and height.
Lucide mountain-snow: snowline attaches to the mountain silhouette.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '99f40798-d32b-4978-8d5c-7e9dc3adf2dd'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-07/volcano_99f40798-d32b-4978-8d5c-7e9dc3adf2dd.svg'
AUTHOR = 'gpt-6'

class SnowCappedMountainWithSunVariant3(Solo48):
    icon_id = 'snow-capped-mountain-with-sun-v3'
    variant_of = 'snow-capped-mountain-with-sun-v2'
    variant_label = 'Exact keyshape envelope and clear spacing'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/landmarks'
    aliases = ()
    keywords = ('mountain', 'volcano', 'fuji', 'peak', 'snow', 'sun', 'landscape', 'nature', 'landmark')

    def build(self) -> None:
        self.add_arc('left-lower', (6, 42), (14, 27), radius_x=55, sweep=False)
        self.add_arc('left-upper', (14, 27), (18, 17), radius_x=55, sweep=False)
        self.add_line('summit', (18, 17), (30, 17))
        self.add_arc('right-upper', (30, 17), (34, 27), radius_x=55, sweep=False)
        self.add_arc('right-lower', (34, 27), (42, 42), radius_x=55, sweep=False)
        self.add_contour('mountain', 'left-lower', 'left-upper', 'summit', 'right-upper', 'right-lower')
        self.add_polyline('snowline', (14, 27), (20, 31), (25, 26), (31, 31))
        self.relate('connect', 'snowline', 'mountain')
        self.add_arc('sun-top', (6, 9), (12, 9), sweep=True, radius_x=3, radius_y=3)
        self.add_arc('sun-bottom', (12, 9), (6, 9), sweep=True, radius_x=3, radius_y=3)
        self.add_contour('sun', 'sun-top', 'sun-bottom', closed=True)
