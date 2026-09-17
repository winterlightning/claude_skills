"""Arrow Down to Bar: A straight downward arrow meets the centre of a short horizontal bar. Its long upright shaft ends in two diagonal arms forming a broad symmetrical arrowhead.

Construction: Shared vertical axis; arrow head and shaft join; lower rail remains detached.
Keyshape: VRECT_L; extremes follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'b5a12afc-a7a7-4386-bd15-6dfd6b581879'
SOURCE_PATH = 'pictographic-primitives/state/arrow down celsius_b5a12afc-a7a7-4386-bd15-6dfd6b581879.svg'
AUTHOR = 'gpt-6'


class ArrowDownToBar(Sub32):
    icon_id = 'arrow-down-to-bar'
    keyshape = Keyshape.VRECT_L
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = "primitives/mark"
    aliases = ()
    keywords = ('arrow', 'down', 'bar', 'straight', 'downward', 'meets', 'centre', 'short')

    def build(self):
        self.add_line("shaft", (16,2), (16,22))
        self.add_polyline("head", (6,12), (16,22), (26,12))
        self.relate("connect", "shaft", "head")
        self.add_line("rail", (6,30), (26,30))
