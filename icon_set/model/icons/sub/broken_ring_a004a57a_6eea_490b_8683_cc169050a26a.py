"""Broken Ring: Three separated curved segments suggest an inner circular ring with broad gaps between them. Generate this component alone; exclude Circle Frame.

Construction: Three separated arc segments trace one centred circular ring; the source enclosure is excluded.
Keyshape: CIRCLE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'a004a57a-6eea-490b-8683-cc169050a26a'
SOURCE_PATH = 'pictographic-primitives/state/slice_a004a57a-6eea-490b-8683-cc169050a26a.svg'
AUTHOR = 'gpt-6'


class BrokenRing(Sub32):
    icon_id = 'broken-ring'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('broken', 'ring', 'separated', 'curved', 'segments', 'suggest', 'inner', 'circular')

    def build(self):
        self.add_arc("top-left",(2,14),(14,2),radius_x=12)
        self.add_arc("right",(24,4),(24,28),radius_x=6,radius_y=12)
        self.add_arc("bottom",(16,30),(4,22),radius_x=12,radius_y=8)
