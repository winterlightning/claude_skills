"""Stylized Burning Fire Flame."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e5ff2f28-6c3b-4881-9079-8431921c8a69'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/fire/feed burner logo_e5ff2f28-6c3b-4881-9079-8431921c8a69.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'flame-with-curved-inner-swish'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'fire'
    aliases = ()
    keywords = ('fire', 'flame', 'swish', 'burning', 'heat', 'logo', 'blaze')

    def build(self):
        # Plan: Wide flame with a high left tip, right spur and curved inner swish. Lucide smooth bowl. Bounds (6,6)-(42,42); deliberately irregular silhouette.
        self.add_bezier('outer',(20,6),((14,11),(8,16),(8,23)),((8,29),(6,29),(6,34)),((6,40),(14,42),(24,42)),((34,42),(42,40),(42,35)),((42,30),(36,31),(36,25)),((36,22),(34,19),(32,18)),((33,22),(24,24),(24,19)),((28,15),(21,12),(20,6)))
        self.add_contour('outline','outer',closed=True)
        self.add_bezier('swish',(17,28),((18,34),(25,35),(28,30)))
