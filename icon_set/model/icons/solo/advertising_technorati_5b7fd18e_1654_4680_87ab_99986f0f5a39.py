"""Advertising technorati (_uncategorized_01), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5b7fd18e-1654-4680-87ab-99986f0f5a39'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_01/advertising technorati_5b7fd18e-1654-4680-87ab-99986f0f5a39.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class AdvertisingTechnorati(Solo48):
    icon_id = 'advertising-technorati'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('advertising', 'technorati', '_uncategorized_01')

    def build(self):
        # Plan: absorb microscopic detours into neighboring cubics; retain the true extremes.
        # Reference: original stroke graph and contour extremes.
        self.add_line('e0', (8, 40), (16, 36))
        self.add_line('e1', (16, 36), (20, 37))
        self.add_line('e2', (10, 32), (8, 40))
        self.add_bezier('e3', (20, 37), ((21.945, 37.362), (24.545, 36.825), (26.482, 36.514)), ((32.673, 35.528), (39.355, 33.204), (42.427, 27.705)), ((43.282, 26.181), (44.0, 24.243999999999996), (44, 22.493)), ((44, 22.257), (43.991, 22.013), (43.991, 21.777)), ((43.991, 13.389), (32.973, 8.017), (24.982, 8.017)), ((24.749, 8.017), (24.514, 8), (24.282, 8)), ((23.809, 8), (23.336, 8.017), (22.864, 8.017)), ((14.918, 8.017), (4.0, 13.549999999999999), (4, 21.895)), ((4, 22.164), (4.009, 22.425), (4.009, 22.695)), ((4.009, 26.771), (6.782, 29.592), (10, 32)))
        self.add_contour('c0', 'e0', 'e1', 'e3', 'e2', closed=True)
