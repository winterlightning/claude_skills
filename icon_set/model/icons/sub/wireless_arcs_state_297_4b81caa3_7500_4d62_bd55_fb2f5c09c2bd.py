"""Wireless Arcs: Two nested curved strokes spread upward from a common centre. Generate this component alone; exclude VR Headset.

Construction: Two shallow wireless arcs preserve the source without adding a signal dot.
Keyshape: HRECT_S; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '4b81caa3-7500-4d62-bd55-fb2f5c09c2bd'
SOURCE_PATH = 'pictographic-primitives/state/vr headset wifi_4b81caa3-7500-4d62-bd55-fb2f5c09c2bd.svg'
AUTHOR = 'gpt-6'


class WirelessArcsState297(Sub32):
    icon_id = 'wireless-arcs-state-297'
    keyshape = Keyshape.HRECT_S
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('wireless', 'arcs', 'nested', 'curved', 'strokes', 'spread', 'upward', 'common')

    def build(self):
        self.add_arc('outer',(2,16),(30,16),radius_x=14,radius_y=6)
        self.add_arc('inner',(8,22),(24,22),radius_x=8,radius_y=4)
