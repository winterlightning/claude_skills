# Repair: Widen both wrist openings equally; retain the joined prayer palms.
"""Two hands meet palm to palm with the fingers pointing upward. Their long outer edges taper toward the joined fingertips, and the wrists angle outward symmetrically below the touching palms.

Construction: Two mirrored palms meet at the fingertips and central seam; flared wrists remain open. Bounds (8,4)-(40,44).
Lucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f9dce8af-e570-53d4-a5f0-38448c1f750b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__praying-hands/20260927T153747Z-thuan-mac-1/reference/hand pray_f9dce8af-e570-53d4-a5f0-38448c1f750b.svg'
AUTHOR = "gpt-6"

class PrayingHands(Solo48):
    icon_id = 'praying-hands'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('prayer', 'hands', 'palms', 'gesture', 'thanks', 'worship')

    def build(self) -> None:
        # Mirrored raised palms meet along a single central seam; wrists flare outward.
        self.add_polyline('left-outer', (8, 44), (14, 36), (14, 30), (18, 16), (24, 4))
        self.add_polyline('right-outer', (40, 44), (34, 36), (34, 30), (30, 16), (24, 4))
        self.add_line('palms-seam', (24, 4), (24, 32))
        self.add_polyline('left-wrist', (24, 32), (22, 38), (18, 44))
        self.add_polyline('right-wrist', (24, 32), (26, 38), (30, 44))
        for other in ('left-outer', 'right-outer', 'left-wrist', 'right-wrist'):
            self.relate('connect', 'palms-seam', other)
