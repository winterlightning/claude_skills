"""Arrow Right: A horizontal shaft ends in two diagonal arms that form an open right-facing arrowhead. Generate this component alone; exclude Circle Frame.

Construction: A horizontal right arrow retains its long shaft and open diagonal head.
Keyshape: HRECT_XL; final SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '90afee1d-c8d3-4450-9484-ad9b41908249'
SOURCE_PATH = 'pictographic-primitives/state/circle arrow right_90afee1d-c8d3-4450-9484-ad9b41908249.svg'
AUTHOR = 'gpt-6'

class ArrowRightState49ContainerSymbol(Sub32):
    icon_id = 'arrow-right-state-49-symbol'
    related_origin_icon_id = 'arrow-right-state-49'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/arrow-right-state-49'
    counterpart_icon_id = 'arrow-right-state-49'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('arrow', 'right', 'horizontal', 'shaft', 'ends', 'diagonal', 'arms', 'that')

    def build(self):
        self.add_line('shaft', (2, 16), (30, 16))
        self.add_polyline('head', (18, 4), (30, 16), (18, 28))
        self.relate('connect', 'shaft', 'head')
