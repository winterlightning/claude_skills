"""Wireless Arcs: Three separate curved strokes nest above one another, growing wider toward the top. Each bows upward around the same centre, without a dot or any enclosing shape.

Construction: Three nested signal arcs share x16; baseline and radii set independently to clear neighbouring ink.
Keyshape: HRECT_L; extremes follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'a2bdace2-2a1a-4fef-a5e1-bc6b29bda0f7'
SOURCE_PATH = 'pictographic-primitives/state/smart_a2bdace2-2a1a-4fef-a5e1-bc6b29bda0f7.svg'
AUTHOR = 'gpt-6'


class WirelessArcs(Sub32):
    icon_id = 'wireless-arcs'
    keyshape = Keyshape.HRECT_L
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = "state"
    aliases = ()
    keywords = ('wireless', 'arcs', 'separate', 'curved', 'strokes', 'nest', 'another', 'growing')

    def build(self):
        for name,left,y,rx,ry in (("outer",2,14,14,8),("middle",8,20,8,6),("inner",13,26,3,1)):
            self.add_arc(name,(left,y),(32-left,y),radius_x=rx,radius_y=ry)
