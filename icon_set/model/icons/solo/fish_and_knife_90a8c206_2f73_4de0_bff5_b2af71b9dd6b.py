"""A kitchen knife lies above a right-facing fish. HRECT_L centerline extremes (6,8)-(42,40) fit the horizontal scene. Lucide fish-symbol informs the simple body and tail; source governs the knife placement. Round the blade tip and enlarge blade and fish interiors for legibility; omit no requested part. Directional asymmetry preserves the blade and fish orientation."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '90a8c206-2f73-4de0-bff5-b2af71b9dd6b'
SOURCE_PATH = 'pictographic-primitives/symbol/fish with knife_90a8c206-2f73-4de0-bff5-b2af71b9dd6b.svg'
AUTHOR = 'gpt-6'


class FishAndKnife(Solo48):
    icon_id = 'fish-and-knife'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    aliases = ()
    keywords = ('fish', 'knife', 'seafood', 'cooking', 'kitchen', 'fillet', 'food', 'butcher')

    def build(self) -> None:
        # Envelope repair: shared boundary nodes and cardinal curve extrema;
        # retain the subject, grid, stroke, and declared physical joins.
        self.add_line('knife-spine', (4, 8), (32,8))
        self.add_line('knife-bolster', (32,8), (32,17))
        self.add_line('knife-edge', (32,17), (14,17))
        self.add_arc('knife-tip', (14,17), (4, 8), radius_x=10, radius_y=9)
        self.add_contour('blade', 'knife-spine', 'knife-bolster', 'knife-edge', 'knife-tip', closed=True)
        self.add_line('handle', (32,8), (44, 8))
        self.relate('connect', 'blade', 'handle')
        self.add_arc('fish-back', (16,33), (44, 33), radius_x=14, radius_y=7)
        self.add_arc('fish-belly', (44, 33), (16,33), radius_x=14, radius_y=7)
        self.add_contour('fish', 'fish-back', 'fish-belly', closed=True)
        self.add_polyline('tail', (16,33), (4, 26), (4, 40), (16,33))
        self.relate('connect', 'fish', 'tail')
