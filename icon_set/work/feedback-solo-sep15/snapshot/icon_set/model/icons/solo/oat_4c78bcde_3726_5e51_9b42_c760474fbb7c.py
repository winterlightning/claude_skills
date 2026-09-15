"""Oat (food), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4c78bcde-3726-5e51-9b42-c760474fbb7c'
SOURCE_PATH = 'pictographic-primitives/food/oat_4c78bcde-3726-5e51-9b42-c760474fbb7c.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Oat(Solo48):
    icon_id = 'oat'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('oat', 'food')

    def build(self):
        # Plan: absorb microscopic detours into neighboring cubics; retain the true extremes.
        # Reference: original stroke graph and contour extremes.
        self.add_line('e0', (11, 42), (37, 6))
        self.add_bezier('e1', (37, 6), ((38.524, 8.091), (39.983, 9.6), (39.983, 12.364)), ((39.992, 12.445), (39.992, 12.558), (40, 12.64)), ((40, 13.294), (39.983, 13.956), (39.983, 14.609)), ((39.983, 23.645), (32.589, 35.3), (25.819, 40.2)), ((23.175, 42.109), (19.782, 44.0), (16.497, 44)), ((16.362, 43.991), (16.227, 43.991), (16.084, 43.982)), ((14.291, 43.982), (12.524, 42.964), (11, 42)))
        self.add_bezier('e2', (37, 6), ((35.316, 4.945), (34.299, 4.018), (32.303, 4.018)), ((32.135, 4.018), (31.963, 4), (31.786, 4)), ((31.72, 4), (31.645, 4.009), (31.579, 4.018)), ((29.768, 4.018), (27.899, 4.582), (26.223, 5.273)), ((18.552, 8.427), (12.935, 16.036), (9.945, 24.073)), ((8.901, 26.864), (8.008, 30.1), (8.008, 33.136)), ((8.008, 33.288), (8, 33.448), (8, 33.591)), ((8, 33.745), (8.008, 33.9), (8.008, 34.045)), ((8.008, 37.073), (9.181, 39.827), (11, 42)))
        self.add_contour('c0', 'e1', closed=False)
        self.add_contour('c1', 'e2', 'e0', closed=True)
        self.relate('connect', 'c0', 'c1')
