"""Wireless Signal: Two nested curved arcs spread above a tiny central dot. The upper arc is wider than the lower one, and all three elements share the same vertical axis.

Construction: Two concentric shallow elliptical arcs and central signal dot; radii and baseline own spacing.
Keyshape: HRECT_L; extremes follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'e6789468-9cc2-4444-a388-10e9ec1fdcb5'
SOURCE_PATH = 'pictographic-primitives/state/electric waves 1_e6789468-9cc2-4444-a388-10e9ec1fdcb5.svg'
AUTHOR = 'gpt-6'


class WirelessSignal(Sub32):
    icon_id = 'wireless-signal'
    keyshape = Keyshape.HRECT_L
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = "state"
    categories = ("state",)
    aliases = ()
    keywords = ('wireless', 'signal', 'nested', 'curved', 'arcs', 'spread', 'tiny', 'central')

    def build(self):
        self.add_arc("outer", (2,14),(30,14),radius_x=14,radius_y=8)
        self.add_arc("inner", (9,18),(23,18),radius_x=7,radius_y=4)
        self.add_dot("signal",(16,26))
