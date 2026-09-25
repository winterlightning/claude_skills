"""Yuan Sign: Two broad diagonal arms converge on a vertical stem, with one horizontal crossbar at their junction. Generate this component alone; exclude Circle Frame.

Construction: The Y-shaped currency glyph retains exactly one crossbar, as in this source.
Keyshape: VRECT_XL; final SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'da791db0-6bf9-4cbb-a255-5be5b52e759e'
SOURCE_PATH = 'pictographic-primitives/state/circle yuan_da791db0-6bf9-4cbb-a255-5be5b52e759e.svg'
AUTHOR = 'gpt-6'


class YuanSignState93(Sub32):
    icon_id = 'yuan-sign-state-93'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('yuan', 'sign', 'broad', 'diagonal', 'arms', 'converge', 'vertical', 'stem')

    def build(self):
        self.add_polyline('arms',(4,2),(16,18),(28,2))
        self.add_line('stem',(16,18),(16,30))
        self.add_line('bar',(8,18),(24,18))
        self.relate('connect','arms','stem')
        self.relate('connect','arms','bar')
        self.relate('connect','stem','bar')
