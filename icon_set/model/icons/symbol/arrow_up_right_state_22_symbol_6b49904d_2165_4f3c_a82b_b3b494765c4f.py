"""Arrow Up Right: A long diagonal shaft rises from lower left to upper right. A horizontal top arm and a vertical right arm meet at its endpoint to form the arrowhead.

Construction: A rising diagonal shaft meets the original horizontal and vertical arrowhead.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '6b49904d-2165-4f3c-a82b-b3b494765c4f'
SOURCE_PATH = 'pictographic-primitives/state/arrow up right_6b49904d-2165-4f3c-a82b-b3b494765c4f.svg'
AUTHOR = 'gpt-6'

class ArrowUpRightState22ContainerSymbol(Sub32):
    icon_id = 'arrow-up-right-state-22-symbol'
    related_origin_icon_id = 'arrow-up-right-state-22'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/arrow-up-right-state-22'
    counterpart_icon_id = 'arrow-up-right-state-22'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('arrow', 'up', 'right', 'long', 'diagonal', 'shaft', 'rises', 'lower')

    def build(self):
        self.add_line('shaft', (2, 30), (30, 2))
        self.add_polyline('head', (16, 2), (30, 2), (30, 16))
        self.relate('connect', 'shaft', 'head')
