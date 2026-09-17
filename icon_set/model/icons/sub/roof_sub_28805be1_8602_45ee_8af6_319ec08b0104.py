"""Roof: Two long diagonal strokes meet at a shallow central peak, creating an open gabled roof. The matching slopes descend toward widely separated left and right ends without walls underneath.

Construction: Two mirrored straight roof slopes share one apex, with no enclosure or wall.
Keyshape: HRECT_S; extremes follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '28805be1-8602-45ee-8af6-319ec08b0104'
SOURCE_PATH = 'pictographic-primitives/state/roof_28805be1-8602-45ee-8af6-319ec08b0104.svg'
AUTHOR = 'gpt-6'


class RoofSub(Sub32):
    icon_id = 'roof-sub'
    keyshape = Keyshape.HRECT_S
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = "primitives/mark"
    aliases = ()
    keywords = ('roof', 'long', 'diagonal', 'strokes', 'meet', 'shallow', 'central', 'peak')

    def build(self):
        self.add_polyline("roof",(2,22),(16,10),(30,22))
