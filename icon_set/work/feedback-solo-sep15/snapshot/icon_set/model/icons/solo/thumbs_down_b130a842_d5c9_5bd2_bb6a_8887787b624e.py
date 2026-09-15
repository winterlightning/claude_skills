'A hand extends from a rectangular cuff at the left with its thumb pointing downward. The curled fingers form a rounded stack along the right edge of the broad fist.\n\nConstruction: Side-view thumb gesture with a broad fist and wrist cuff; knuckle creases omitted. Mirrored direction is intentional. Bounds (4,8)-(44,40).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b130a842-d5c9-5bd2-bb6a-8887787b624e'
SOURCE_PATH = 'pictographic-primitives/wayfinding/thumb down dislike_b130a842-d5c9-5bd2-bb6a-8887787b624e.svg'
AUTHOR = 'gpt-6'

class ThumbsDown(Solo48):
    icon_id = 'thumbs-down'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('thumb', 'down', 'hand', 'dislike', 'gesture', 'fist')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_line('outline-1', (4, 24), (12, 24))
        self.add_line('outline-2', (12, 24), (24, 40))
        self.add_line('outline-3', (24, 40), (30, 40))
        self.add_line('outline-4', (30, 40), (30, 28))
        self.add_line('outline-5', (30, 28), (40, 28))
        self.add_line('outline-6', (40, 28), (44, 24))
        self.add_line('outline-7', (44, 24), (44, 12))
        self.add_line('outline-8', (44, 12), (40, 8))
        self.add_line('outline-9', (40, 8), (12, 8))
        self.add_line('outline-10', (12, 8), (4, 8))
        self.add_line('outline-11', (4, 8), (4, 24))
        self.add_line('cuff', (12, 24), (12, 8))
        self.add_contour('outline', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', 'outline-6', 'outline-7', 'outline-8', 'outline-9', 'outline-10', 'outline-11', closed=True)
        self.relate('connect', 'cuff', 'outline')
