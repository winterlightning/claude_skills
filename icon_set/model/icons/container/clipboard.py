"""A rounded clipboard with a semicircular clip joined to its top edge.

VRECT_XL: centerline (6,2)-(58,62), visible (4,0)-(60,64), preserving
an upright board. Lucide clipboard informs the rounded board and centered
attachment. The old flat-topped clip is replaced by a true radius-10 half
circle, sharing its bottom chord with the board. Bilateral symmetry is exact.
Feedback briefs 154 and 175 request the same change.
Hosting measured with compose.py: plus valid, heart valid, check valid.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (clipboard VRECT_XL -> VRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = None
SOURCE_PATH = None
FEEDBACK_PATHS = ('/Users/jakesdev/Downloads/feedback-briefs 2/container/154-clipboard.md', '/Users/jakesdev/Downloads/feedback-briefs 2/container/175-clipboard.md')
AUTHOR = 'claude-opus-5-5'


class ClipboardContainer(Container64):
    icon_id = 'clipboard'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ('blank-clipboard', 'blank-document-clipboard', 'blank-office-clipboard', 'rounded-office-clipboard', 'semicircular-clip-board')
    keywords = ('board', 'clip', 'blank', 'page', 'semicircle')

    def build(self) -> None:
        self.add_line('board-chord', (23, 13), (41, 13))
        self.add_line('board-top-right', (41, 13), (48, 14))
        self.add_arc('board-corner-ne', (48, 14), (54, 20), radius_x=6)
        self.add_line('board-right', (54, 20), (54, 54))
        self.add_arc('board-corner-se', (54, 54), (48, 60), radius_x=6)
        self.add_line('board-bottom', (48, 60), (16, 60))
        self.add_arc('board-corner-sw', (16, 60), (10, 54), radius_x=6)
        self.add_line('board-left', (10, 54), (10, 20))
        self.add_arc('board-corner-nw', (10, 20), (16, 14), radius_x=6)
        self.add_line('board-top-left', (16, 14), (23, 13))
        self.add_arc('clip', (23, 13), (41, 13), radius_x=9)
        self.add_contour('board', 'board-top-right', 'board-corner-ne', 'board-right', 'board-corner-se', 'board-bottom', 'board-corner-sw', 'board-left', 'board-corner-nw', 'board-top-left')
        self.relate('connect', 'board', 'clip')
        self.relate('connect', 'board', 'board-chord')
        self.relate('connect', 'clip', 'board-chord')
