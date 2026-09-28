'A hand extends rightward from a square cuff with its thumb raised diagonally upward. Three short finger creases mark the outer edge of the closed fist.\n\nConstruction: Side-view thumb gesture with a broad fist and wrist cuff; knuckle creases omitted. Mirrored direction is intentional. Bounds (4,8)-(44,40).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '34dbfa4a-d967-4f1c-bfb7-67c27a92ef1d'
SOURCE_PATH = 'pictographic-primitives/wayfinding/thumb up like_34dbfa4a-d967-4f1c-bfb7-67c27a92ef1d.svg'
AUTHOR = 'gpt-6'

class ThumbsUp(Solo48):
    icon_id = 'thumbs-up'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('thumb', 'up', 'hand', 'like', 'gesture', 'fist')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_line('outline-1', (4, 24), (12, 24))
        self.add_line('outline-2', (12, 24), (24, 8))
        self.add_line('outline-3', (24, 8), (30, 8))
        self.add_line('outline-4', (30, 8), (30, 20))
        self.add_line('outline-5', (30, 20), (40, 20))
        self.add_line('outline-6', (40, 20), (44, 24))
        self.add_line('outline-7', (44, 24), (44, 36))
        self.add_line('outline-8', (44, 36), (40, 40))
        self.add_line('outline-9', (40, 40), (12, 40))
        self.add_line('outline-10', (12, 40), (4, 40))
        self.add_line('outline-11', (4, 40), (4, 24))
        self.add_line('cuff', (12, 24), (12, 40))
        self.add_contour('outline', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', 'outline-6', 'outline-7', 'outline-8', 'outline-9', 'outline-10', 'outline-11', closed=True)
        self.relate('connect', 'cuff', 'outline')
