'button-next: independent smooth-curve repair.\n\nConstruction: Forward triangle and a distinct terminal bar; retain their functional spacing.\nKeyshape: SQUARE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/skip-forward.svg and atomic-debug/skip-forward.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'b7f10f98-32db-4098-99df-acee5e6b2494'
SOURCE_PATH = 'pictographic-primitives/interface-essential/button next_b7f10f98-32db-4098-99df-acee5e6b2494.svg'
AUTHOR = 'gpt-6'


class ButtonNextVariant2(Solo48):
    icon_id = 'button-next-v2'
    variant_of = 'button-next'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('button', 'next', 'interface-essential')
    keyshape = Keyshape.SQUARE

    def build(self):
        poly(self,'triangle',(6,6),(30,24),(6,42),closed=True)
        line(self,'stop',(42,6),(42,42))
        contacts(self)
