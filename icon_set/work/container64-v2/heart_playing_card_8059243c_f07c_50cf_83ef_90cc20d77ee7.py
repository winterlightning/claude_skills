"""An upright rounded playing card containing a heart. VRECT_L preserves its portrait proportions. The heart uses two mirrored cubic sections meeting at its cleft and pointed base; smooth lobe tangents. The card has radius-6 corners.

Source rendered and inspected before authoring. Preserve the saved user classification.
Lucide image and ticket-x originals and atomic geometry informed coherent contours
and rounded enclosures; human reference used only for the three human scenes.
Hosting via compose.py using existing sub IDs: plus-sign-batch-04 valid, heart-state-63 review, check-mark review.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (heart-playing-card VRECT_L -> VRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = '8059243c-f07c-50cf-83ef-90cc20d77ee7'
SOURCE_PATH = 'pictographic-primitives/entertainment/fortune telling tarot_8059243c-f07c-50cf-83ef-90cc20d77ee7.svg'
AUTHOR = 'claude-opus-5-5'


class QueueIcon(Container64):
    icon_id = 'heart-playing-card'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'entertainment'
    categories = ('entertainment', 'primitives')
    aliases = ('Heart Playing Card',)
    keywords = ('heart', 'playing', 'card')

    def build(self) -> None:
        self.add_line('card-0', (18, 4), (46, 4))
        self.add_arc('card-1', (46, 4), (52, 10), radius_x=6)
        self.add_line('card-2', (52, 10), (52, 54))
        self.add_arc('card-3', (52, 54), (46, 60), radius_x=6)
        self.add_line('card-4', (46, 60), (18, 60))
        self.add_arc('card-5', (18, 60), (12, 54), radius_x=6)
        self.add_line('card-6', (12, 54), (12, 10))
        self.add_arc('card-7', (12, 10), (18, 4), radius_x=6)
        self.add_bezier('heart', (32, 26), ((19.75, 11.882), (11, 31.143), (32, 41.765)), ((53, 31.143), (44.25, 11.882), (32, 26)))
        self.add_contour('card', 'card-0', 'card-1', 'card-2', 'card-3', 'card-4', 'card-5', 'card-6', 'card-7', closed=True)
        self.add_contour('suit', 'heart', closed=True)
