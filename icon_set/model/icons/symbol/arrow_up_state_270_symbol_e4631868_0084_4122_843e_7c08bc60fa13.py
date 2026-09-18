"""Arrow Up: A straight upright shaft ends in an open pointed head with two equal diagonal arms. Generate this component alone; exclude Circle Frame.

Construction: The upright arrow retains its open diagonal head and lower stem.
Keyshape: VRECT_XL; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'e4631868-0084-4122-843e-7c08bc60fa13'
SOURCE_PATH = 'pictographic-primitives/state/state upload_e4631868-0084-4122-843e-7c08bc60fa13.svg'
AUTHOR = 'gpt-6'

class ArrowUpState270ContainerSymbol(Sub32):
    icon_id = 'arrow-up-state-270-symbol'
    related_origin_icon_id = 'arrow-up-state-270'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/arrow-up-state-270'
    counterpart_icon_id = 'arrow-up-state-270'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('arrow', 'up', 'straight', 'upright', 'shaft', 'ends', 'open', 'pointed')

    def build(self):
        self.add_line('shaft', (16, 30), (16, 2))
        self.add_polyline('head', (4, 14), (16, 2), (28, 14))
        self.relate('connect', 'shaft', 'head')
