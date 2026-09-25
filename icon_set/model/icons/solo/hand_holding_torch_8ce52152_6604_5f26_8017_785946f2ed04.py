"""A hand entering from the right grips a bent-head torch; four crowded finger outlines reduced to a thumb and two grip lines."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8ce52152-6604-5f26-8017-785946f2ed04'
SOURCE_PATH = 'pictographic-primitives/tools/handheld torch hold_8ce52152-6604-5f26-8017-785946f2ed04.svg'
AUTHOR = 'gpt-6'

class HandHoldingTorch(Solo48):
    icon_id = 'hand-holding-torch'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "tools"
    aliases = ()
    keywords = ('hand', 'holding', 'torch', 'grip', 'handheld', 'fist', 'blowtorch', 'tool')

    def build(self) -> None:
        self.add_polyline('torch',(6,6),(24,6),(24,18),(16,18),(16,14),(6,14),closed=True)
        self.add_polyline('grip',(42,24),(34,24),(28,18),(18,18),(14,22),(18,26),(26,26))
        self.relate('connect','grip','torch')
        self.add_polyline('hand',(18,26),(14,32),(14,42),(32,42),(36,36),(42,36))
        self.relate('connect','hand','grip')
        self.add_line('fingers',(14,34),(26,34))
        self.relate('connect','fingers','hand')
