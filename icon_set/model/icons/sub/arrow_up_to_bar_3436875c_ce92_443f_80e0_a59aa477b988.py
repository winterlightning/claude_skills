"""Arrow Up to Bar: A tall straight arrow points upward to the centre of a horizontal bar. Two diagonal arms descend from its tip, forming a broad arrowhead beneath the bar.

Construction: Vertical reflection of the down-to-bar topology, with an eight-unit rail gap.
Keyshape: VRECT_L; extremes follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '3436875c-ce92-443f-80e0-a59aa477b988'
SOURCE_PATH = 'pictographic-primitives/state/arrow up celsius_3436875c-ce92-443f-80e0-a59aa477b988.svg'
AUTHOR = 'gpt-6'


class ArrowUpToBar(Sub32):
    icon_id = 'arrow-up-to-bar'
    keyshape = Keyshape.VRECT_L
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = "primitives/mark"
    aliases = ()
    keywords = ('arrow', 'up', 'bar', 'tall', 'straight', 'points', 'upward', 'centre')

    def build(self):
        self.add_line("shaft", (16,10), (16,30))
        self.add_polyline("head", (6,20), (16,10), (26,20))
        self.relate("connect", "shaft", "head")
        self.add_line("rail", (6,2), (26,2))
