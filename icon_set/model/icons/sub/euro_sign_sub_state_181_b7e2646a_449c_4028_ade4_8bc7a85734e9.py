"""Euro Sign: A broad C-shaped curve opens right and is crossed midway by a single short horizontal bar. Generate this component alone; exclude Rectangle Frame.

Construction: A genuinely circular open C retains the original single midline crossbar.
Keyshape: CIRCLE; final SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'b7e2646a-449c-4028-ade4-8bc7a85734e9'
SOURCE_PATH = 'pictographic-primitives/state/money bill euro_b7e2646a-449c-4028-ade4-8bc7a85734e9.svg'
AUTHOR = 'gpt-6'


class EuroSignSubState181(Sub32):
    icon_id = 'euro-sign-sub-state-181'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('euro', 'sign', 'broad', 'c', 'shaped', 'curve', 'opens', 'right')

    def build(self):
        self.add_arc('upper',(22,4),(4,16),radius_x=13,sweep=False)
        self.add_arc('lower',(4,16),(22,28),radius_x=13,sweep=False)
        self.add_contour('c','upper','lower')
        self.add_line('bar',(2,16),(18,16))
        self.relate('connect','c','bar')
