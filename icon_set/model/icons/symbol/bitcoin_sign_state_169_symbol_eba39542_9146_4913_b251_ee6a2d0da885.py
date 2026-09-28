"""Bitcoin Sign: An uppercase B has two rounded bowls and two short parallel stems projecting above and below its horizontal ends. Generate this component alone; exclude Round Speech Bubble.

Construction: The B-shaped currency glyph retains both pairs of short projecting stems.
Keyshape: VRECT_XL; final SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'eba39542-9146-4913-b251-ee6a2d0da885'
SOURCE_PATH = 'pictographic-primitives/state/messages bubble circle bitcoin_eba39542-9146-4913-b251-ee6a2d0da885.svg'
AUTHOR = 'gpt-6'

class BitcoinSignState169ContainerSymbol(Sub32):
    icon_id = 'bitcoin-sign-state-169-symbol'
    related_origin_icon_id = 'bitcoin-sign-state-169'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/bitcoin-sign-state-169'
    counterpart_icon_id = 'bitcoin-sign-state-169'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('bitcoin', 'sign', 'uppercase', 'b', 'rounded', 'bowls', 'short', 'parallel')

    def build(self):
        self.add_line('stem', (6, 6), (6, 26))
        self.add_line('upper-top', (4, 6), (18, 6))
        self.add_arc('upper-bowl', (18, 6), (18, 16), radius_x=10, radius_y=5)
        self.add_line('middle', (18, 16), (6, 16))
        self.add_contour('upper', 'upper-top', 'upper-bowl', 'middle')
        self.add_line('lower-top', (6, 16), (18, 16))
        self.add_arc('lower-bowl', (18, 16), (18, 26), radius_x=10, radius_y=5)
        self.add_line('lower-bottom', (18, 26), (4, 26))
        self.add_contour('lower', 'lower-top', 'lower-bowl', 'lower-bottom')
        self.relate('connect', 'stem', 'upper')
        self.relate('connect', 'stem', 'lower')
        self.relate('connect', 'upper', 'lower')
        for x in (10, 18):
            self.add_line(f'top-{x}', (x, 2), (x, 6))
            self.add_line(f'bottom-{x}', (x, 26), (x, 30))
            self.relate('connect', 'upper', f'top-{x}')
            self.relate('connect', 'lower', f'bottom-{x}')
