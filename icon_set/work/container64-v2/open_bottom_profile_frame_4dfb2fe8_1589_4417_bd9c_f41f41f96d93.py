"""An upright rectangular profile frame with softly rounded top corners, two long vertical sides, and no bottom edge. Exclude the avatar.

Plan: One continuous open U frame, top corner radius six; no bottom edge. Bounds (6,2)-(58,62).
Hosting at the standard slot: add-sub32: valid, heart-state-63: valid, check-mark: valid.
Construction reference: Lucide briefcase-business: tangent quarter-circle corners.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (open-bottom-profile-frame VRECT_XL -> VRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = '4dfb2fe8-1589-4417-bd9c-f41f41f96d93'
SOURCE_ICON_IDS = ('4dfb2fe8-1589-4417-bd9c-f41f41f96d93',)
SOURCE_PATH = 'pictographic-primitives/other/rectangle user_4dfb2fe8-1589-4417-bd9c-f41f41f96d93.svg'
AUTHOR = 'claude-opus-5-5'


class OpenBottomProfileFrame(Container64):
    icon_id = 'open-bottom-profile-frame'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases = ()
    keywords = ('open', 'bottom', 'profile', 'frame')

    def build(self) -> None:
        self.add_line('left', (10, 60), (10, 10))
        self.add_arc('top-left', (10, 10), (16, 4), radius_x=6)
        self.add_line('top', (16, 4), (48, 4))
        self.add_arc('top-right', (48, 4), (54, 10), radius_x=6)
        self.add_line('right', (54, 10), (54, 60))
        self.add_contour('frame', 'left', 'top-left', 'top', 'top-right', 'right')
