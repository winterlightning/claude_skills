"""Wi-Fi: Three nested upward-bowed arcs sit above a small circular signal dot, widening progressively toward the top. Generate this component alone; exclude Prohibition Frame.

Construction: Three nested shallow arcs sit above an outlined circular signal dot. The outlined dot is retained, not replaced by a filled dot.
Keyshape: SQUARE; authored to the SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '83d88267-02ad-4867-a07f-e6512912bb84'
SOURCE_PATH = 'pictographic-primitives/state/wifi slash_83d88267-02ad-4867-a07f-e6512912bb84.svg'
AUTHOR = 'gpt-6'


class WiFi(Sub32):
    icon_id = 'wi-fi'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('wi', 'fi', 'nested', 'upward', 'bowed', 'arcs', 'sit', 'small')

    def build(self):
        self.add_arc('outer',(2,8),(30,8),radius_x=14,radius_y=6)
        self.add_arc('middle',(7,14),(25,14),radius_x=9,radius_y=5)
        self.add_arc('inner',(12,18),(20,18),radius_x=4,radius_y=2)
        self.add_arc('dot-top',(13,27),(19,27),radius_x=3)
        self.add_arc('dot-bottom',(19,27),(13,27),radius_x=3)
        self.add_contour('dot','dot-top','dot-bottom',closed=True)
