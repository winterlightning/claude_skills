"""Wireless Waves: Two broad curved wireless waves sit one above the other. Generate this component alone; exclude Payment Card.

Construction: Two upward-bowed waves mirror around x16 with a generous gap.
Keyshape: HRECT_L; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'bee75746-47a6-40de-8e1b-8dbf994b4ff7'
SOURCE_PATH = 'pictographic-primitives/state/card wifi_bee75746-47a6-40de-8e1b-8dbf994b4ff7.svg'
AUTHOR = 'gpt-6'


class WirelessWaves(Sub32):
    icon_id = 'wireless-waves'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('wireless', 'waves', 'broad', 'curved', 'sit', 'other')

    def build(self):
        self.add_arc('outer',(2,18),(30,18),radius_x=14,radius_y=12)
        self.add_arc('inner',(8,26),(24,26),radius_x=8,radius_y=8)
