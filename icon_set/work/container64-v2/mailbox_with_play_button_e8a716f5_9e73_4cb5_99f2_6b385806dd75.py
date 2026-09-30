"""Banded vertical media frame with its central play triangle.

Preserve the whole subject per the authoritative TODO decision. The source
reads as a media frame, not a physical mailbox. VRECT_XL (6,2)-(58,62)
supports a tall shell, paired rails and top/bottom bands. Lucide
panels-top-left informs shared divider nodes and rounded perimeter turns.
All frame geometry mirrors about x=32; the play triangle points right.
Complete the clipped lower shell; omit no semantic component.
Hosting via compose.py: check-mark validates; plus-sign-state-131 is invalid
for parallel spacing against play; heart-state-63 returns review for rail
contact. Legacy probe IDs plus/heart/check are absent from this registry.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (mailbox-with-play-button VRECT_XL -> VRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = 'e8a716f5-9e73-4cb5-99f2-6b385806dd75'
SOURCE_PATH = 'pictographic-primitives/emails/mailbox post_e8a716f5-9e73-4cb5-99f2-6b385806dd75.svg'
AUTHOR = 'claude-opus-5-5'


class Drawing(Container64):
    icon_id = 'mailbox-with-play-button'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'emails'
    categories = ('emails', 'primitives')
    aliases = ('banded vertical media frame',)
    keywords = ('mailbox', 'with', 'play', 'button')

    def build(self) -> None:
        self.add_line('shell-0', (18, 4), (20, 4))
        self.add_line('shell-1', (20, 4), (44, 4))
        self.add_line('shell-2', (44, 4), (46, 4))
        self.add_arc('shell-3', (46, 4), (54, 12), radius_x=8)
        self.add_line('shell-4', (54, 12), (54, 52))
        self.add_arc('shell-5', (54, 52), (46, 60), radius_x=8)
        self.add_line('shell-6', (46, 60), (44, 60))
        self.add_line('shell-7', (44, 60), (20, 60))
        self.add_line('shell-8', (20, 60), (18, 60))
        self.add_arc('shell-9', (18, 60), (10, 52), radius_x=8)
        self.add_line('shell-10', (10, 52), (10, 12))
        self.add_arc('shell-11', (10, 12), (18, 4), radius_x=8)
        self.add_line('left-rail-1', (20, 4), (20, 16))
        self.add_line('left-rail-2', (20, 16), (20, 52))
        self.add_line('left-rail-3', (20, 52), (20, 60))
        self.add_line('right-rail-1', (44, 4), (44, 16))
        self.add_line('right-rail-2', (44, 16), (44, 52))
        self.add_line('right-rail-3', (44, 52), (44, 60))
        self.add_line('top-band', (20, 16), (44, 16))
        self.add_line('bottom-band', (20, 52), (44, 52))
        self.add_line('play-1', (28, 26), (36, 34))
        self.add_line('play-2', (36, 34), (28, 42))
        self.add_line('play-3', (28, 42), (28, 26))
        self.add_contour('shell', 'shell-0', 'shell-1', 'shell-2', 'shell-3', 'shell-4', 'shell-5', 'shell-6', 'shell-7', 'shell-8', 'shell-9', 'shell-10', 'shell-11', closed=True)
        self.add_contour('left-rail', 'left-rail-1', 'left-rail-2', 'left-rail-3')
        self.add_contour('right-rail', 'right-rail-1', 'right-rail-2', 'right-rail-3')
        self.add_contour('play', 'play-1', 'play-2', 'play-3', closed=True)
        self.relate('connect', 'shell', 'left-rail')
        self.relate('connect', 'shell', 'right-rail')
        self.relate('connect', 'top-band', 'left-rail')
        self.relate('connect', 'top-band', 'right-rail')
        self.relate('connect', 'bottom-band', 'left-rail')
        self.relate('connect', 'bottom-band', 'right-rail')
