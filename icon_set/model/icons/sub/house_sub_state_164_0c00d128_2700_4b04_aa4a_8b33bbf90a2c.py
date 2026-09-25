"""House: A house has a pointed roof with projecting eaves and a compact body whose lower corners are rounded, without doors or windows. Generate this component alone; exclude Speech Bubble.

Construction: A simple gabled house has open projecting eaves and a blank closed body; no doorway is added.
Keyshape: SQUARE; final SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '0c00d128-2700-4b04-aa4a-8b33bbf90a2c'
SOURCE_PATH = 'pictographic-primitives/state/message bubble house_0c00d128-2700-4b04-aa4a-8b33bbf90a2c.svg'
AUTHOR = 'gpt-6'


class HouseSubState164(Sub32):
    icon_id = 'house-sub-state-164'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('house', 'pointed', 'roof', 'projecting', 'eaves', 'compact', 'body', 'whose')

    def build(self):
        self.add_polyline('roof',(2,16),(16,2),(30,16))
        self.add_line('left',(6,12),(6,27))
        self.add_arc('lower-left',(6,27),(9,30),radius_x=3,sweep=False)
        self.add_line('base',(9,30),(23,30))
        self.add_arc('lower-right',(23,30),(26,27),radius_x=3,sweep=False)
        self.add_line('right',(26,27),(26,12))
        self.add_contour('body','left','lower-left','base','lower-right','right')
        self.relate('connect','body','roof')
