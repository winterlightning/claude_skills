'Two hands meet palm to palm with the fingers pointing upward. Their long outer edges taper toward the joined fingertips, and the wrists angle outward symmetrically below the touching palms.\n\nConstruction: Two mirrored palms meet at the fingertips and central seam; flared wrists remain open. Bounds (8,4)-(40,44).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f9dce8af-e570-53d4-a5f0-38448c1f750b'
SOURCE_PATH = 'pictographic-primitives/wayfinding/hand pray_f9dce8af-e570-53d4-a5f0-38448c1f750b.svg'
AUTHOR = 'gpt-6'

class PrayingHands(Solo48):
    icon_id = 'praying-hands'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('prayer', 'hands', 'palms', 'gesture', 'thanks', 'worship')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_line('left-1', (8, 44), (16, 34))
        self.add_line('left-2', (16, 34), (16, 16))
        self.add_line('left-3', (16, 16), (24, 4))
        self.add_line('left-4', (24, 4), (24, 30))
        self.add_line('left-5', (24, 30), (24, 34))
        self.add_line('left-6', (24, 34), (14, 44))
        self.add_line('right-1', (40, 44), (32, 34))
        self.add_line('right-2', (32, 34), (32, 16))
        self.add_line('right-3', (32, 16), (24, 4))
        self.add_line('right-4', (24, 4), (24, 30))
        self.add_line('right-5', (24, 30), (24, 34))
        self.add_line('right-6', (24, 34), (34, 44))
        self.add_contour('left', 'left-1', 'left-2', 'left-3', 'left-4', 'left-5', 'left-6', closed=False)
        self.add_contour('right', 'right-1', 'right-2', 'right-3', 'right-4', 'right-5', 'right-6', closed=False)
        self.relate('connect', 'left', 'right')
