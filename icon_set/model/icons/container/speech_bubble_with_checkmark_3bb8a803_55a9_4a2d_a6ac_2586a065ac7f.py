"""Checked message in a rounded bubble with lower-right tail.
HRECT_L extremes (2,10)-(62,54); body floor 42. Lucide message-square-text
informs continuous outline, tangent corners and detached message strokes.
Preserve whole subject per recorded user classification. Shared row step 8.
Hosting: plus-sign-state-131 and check-mark fail clearance; heart-state-63
is unresolved review (3 warnings). This filled message bubble hosts none of
these tested glyphs. Hosting reports are retained with queue batch evidence.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (speech-bubble-with-checkmark HRECT_L -> HRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = '3bb8a803-55a9-4a2d-a6ac-2586a065ac7f'
SOURCE_PATH = 'pictographic-primitives/chat/criteria_3bb8a803-55a9-4a2d-a6ac-2586a065ac7f.svg'
AUTHOR = 'claude-opus-5-5'


class CheckedSpeechBubble(Container64):
    icon_id = 'speech-bubble-with-checkmark'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'chat'
    categories = ('primitives', 'chat')
    aliases = ['Speech Bubble with Checkmark']
    keywords = ('speech', 'bubble', 'checkmark', 'message')

    def build(self) -> None:
        self.add_line('top', (8, 12), (56, 12))
        self.add_arc('ne', (56, 12), (60, 16), radius_x=4)
        self.add_line('tail-1', (60, 16), (60, 52))
        self.add_line('tail-2', (60, 52), (48, 42))
        self.add_line('tail-3', (48, 42), (8, 42))
        self.add_arc('sw', (8, 42), (4, 38), radius_x=4)
        self.add_line('left', (4, 38), (4, 16))
        self.add_arc('nw', (4, 16), (8, 12), radius_x=4)
        self.add_line('check-1', (14, 26), (19, 31))
        self.add_line('check-2', (19, 31), (27, 22))
        self.add_line('message-0', (35, 22), (50, 22))
        self.add_line('message-1', (35, 30), (50, 30))
        self.add_contour('bubble', 'top', 'ne', 'tail-1', 'tail-2', 'tail-3', 'sw', 'left', 'nw', closed=True)
        self.add_contour('check', 'check-1', 'check-2')
