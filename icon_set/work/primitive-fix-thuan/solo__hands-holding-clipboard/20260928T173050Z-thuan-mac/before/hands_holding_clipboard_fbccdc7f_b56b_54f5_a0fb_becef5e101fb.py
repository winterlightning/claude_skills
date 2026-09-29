"""Two hands grip the lower sides of an upright clipboard, with thumbs reaching inward over its face. A rounded tab rises at the top, and three horizontal lines represent the written contents.
Lucide clipboard rounded top clip; mirrored physical grasping hands. Three text rules reduced to one.
Keyshape SQUARE; centerline extremes (6,6)-(42,42). Square envelope balances the complete scene. Source inspected as a standalone physical or conceptual subject."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fbccdc7f-b56b-54f5-a0fb-becef5e101fb'
SOURCE_PATH = 'pictographic-primitives/work/food delivery order manage_fbccdc7f-b56b-54f5-a0fb-becef5e101fb.svg'
AUTHOR = 'gpt-6'


class HandsHoldingClipboard(Solo48):
    icon_id = 'hands-holding-clipboard'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "work"
    categories = ("work", "primitives")
    aliases = ()
    keywords = ('hands', 'clipboard', 'order', 'document', 'list', 'holding')

    def build(self) -> None:
        self.add_line('board-1', (12, 31), (12, 9))
        self.add_line('board-2', (12, 9), (18, 9))
        self.add_arc('clip-top', (18, 9), (30, 9), radius_x=6, radius_y=3, sweep=True, large_arc=False)
        self.add_line('board-right-1', (30, 9), (36, 9))
        self.add_line('board-right-2', (36, 9), (36, 31))
        self.add_contour('clipboard', 'board-1', 'board-2', 'clip-top', 'board-right-1', 'board-right-2', closed=False)
        self.add_line('text', (21, 18), (27, 18))
        self.add_polyline('left-hand', (6, 42), (6, 33), (12, 25), (19, 30), (14, 36), (14, 42), closed=False)
        self.relate("connect", 'left-hand', 'clipboard')
        self.add_polyline('right-hand', (42, 42), (42, 33), (36, 25), (29, 30), (34, 36), (34, 42), closed=False)
        self.relate("connect", 'right-hand', 'clipboard')
        self.add_line('bottom', (14, 42), (34, 42))
        self.relate("connect", 'bottom', 'left-hand')
        self.relate("connect", 'bottom', 'right-hand')
