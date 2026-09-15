"""A rounded clipboard with a semicircular clip joined to its top edge.

VRECT_XL: centerline (6,2)-(58,62), visible (4,0)-(60,64), preserving
an upright board. Lucide clipboard informs the rounded board and centered
attachment. The old flat-topped clip is replaced by a true radius-10 half
circle, sharing its bottom chord with the board. Bilateral symmetry is exact.
Feedback briefs 154 and 175 request the same change.
Hosting measured with compose.py: plus valid, heart valid, check valid.
"""
from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'gpt-6'
FEEDBACK_PATHS = (
    '/Users/jakesdev/Downloads/feedback-briefs 2/container/154-clipboard.md',
    '/Users/jakesdev/Downloads/feedback-briefs 2/container/175-clipboard.md',
)


class ClipboardContainer(Container64):
    icon_id = 'clipboard'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'containers'
    aliases = ('blank-clipboard', 'blank-document-clipboard', 'blank-office-clipboard', 'rounded-office-clipboard', 'semicircular-clip-board')
    keywords = ('board', 'clip', 'blank', 'page', 'semicircle')

    def build(self) -> None:
        # Plan: one rounded rectangle plus one semicircle sharing a chord.
        # Board owns dimensions/radius; clip owns one radius and shared nodes.
        axis, left, right, bottom, corner = 32, 6, 58, 62, 6
        radius, top = 10, 12
        clip_left, clip_right = (axis-radius, top), (axis+radius, top)
        self.add_line('board-chord', clip_left, clip_right)
        self.add_line('board-top-right', clip_right, (right-corner, top))
        self.add_arc('board-corner-ne', (right-corner, top), (right, top+corner), radius_x=corner)
        self.add_line('board-right', (right, top+corner), (right, bottom-corner))
        self.add_arc('board-corner-se', (right, bottom-corner), (right-corner, bottom), radius_x=corner)
        self.add_line('board-bottom', (right-corner, bottom), (left+corner, bottom))
        self.add_arc('board-corner-sw', (left+corner, bottom), (left, bottom-corner), radius_x=corner)
        self.add_line('board-left', (left, bottom-corner), (left, top+corner))
        self.add_arc('board-corner-nw', (left, top+corner), (left+corner, top), radius_x=corner)
        self.add_line('board-top-left', (left+corner, top), clip_left)
        self.add_contour('board', 'board-top-right', 'board-corner-ne',
                         'board-right', 'board-corner-se', 'board-bottom',
                         'board-corner-sw', 'board-left', 'board-corner-nw',
                         'board-top-left')
        self.add_arc('clip', clip_left, clip_right, radius_x=radius)
        self.relate('connect', 'board', 'clip')
        self.relate('connect', 'board', 'board-chord')
        self.relate('connect', 'clip', 'board-chord')
