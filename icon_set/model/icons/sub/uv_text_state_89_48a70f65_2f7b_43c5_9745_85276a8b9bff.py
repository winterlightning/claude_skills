"""UV Text: An uppercase U with a rounded bottom stands beside an uppercase V formed by two sloping strokes. Generate this component alone; exclude Circle Frame.

Construction: An upright U and V retain the source letter order and shared baseline.
Keyshape: HRECT_XL; final SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '48a70f65-2f7b-43c5-9745-85276a8b9bff'
SOURCE_PATH = 'pictographic-primitives/state/circle uv_48a70f65-2f7b-43c5-9745-85276a8b9bff.svg'
AUTHOR = 'gpt-6'


class UvTextState89(Sub32):
    icon_id = 'uv-text-state-89'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('uv', 'text', 'uppercase', 'u', 'rounded', 'bottom', 'stands', 'beside')

    def build(self):
        self.add_line('left',(2,4),(2,23))
        self.add_arc('bottom',(2,23),(12,23),radius_x=5,sweep=False)
        self.add_line('right',(12,23),(12,4))
        self.add_contour('u','left','bottom','right')
        self.add_polyline('v',(20,4),(25,28),(30,4))
