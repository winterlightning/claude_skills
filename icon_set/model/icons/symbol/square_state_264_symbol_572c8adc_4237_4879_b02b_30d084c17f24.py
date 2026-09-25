"""Square: An upright square outline has four straight equal sides and an empty interior. Generate this component alone; exclude Circle Frame.

Construction: The source inner square retains an empty centre and four equal straight sides.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '572c8adc-4237-4879-b02b-30d084c17f24'
SOURCE_PATH = 'pictographic-primitives/state/square circle_572c8adc-4237-4879-b02b-30d084c17f24.svg'
AUTHOR = 'gpt-6'

class SquareState264ContainerSymbol(Sub32):
    icon_id = 'square-state-264-symbol'
    related_origin_icon_id = 'square-state-264'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/square-state-264'
    counterpart_icon_id = 'square-state-264'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('square', 'upright', 'outline', 'four', 'straight', 'equal', 'sides', 'empty')

    def build(self):
        self.add_polyline('square', (2, 2), (30, 2), (30, 30), (2, 30), closed=True)
