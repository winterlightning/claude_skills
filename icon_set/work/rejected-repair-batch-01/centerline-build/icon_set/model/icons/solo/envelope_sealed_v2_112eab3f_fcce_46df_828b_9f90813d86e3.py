'envelope-sealed: independent smooth-curve repair.\n\nConstruction: Back of sealed envelope: corner folds joined by a central vertical seam.\nKeyshape: SQUARE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/mail.svg and atomic-debug/mail.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '112eab3f-fcce-46df-828b-9f90813d86e3'
SOURCE_PATH = 'pictographic-primitives/emails/envelope sealed_112eab3f-fcce-46df-828b-9f90813d86e3.svg'
AUTHOR = 'gpt-6'


class EnvelopeSealedVariant2(Solo48):
    icon_id = 'envelope-sealed-v2'
    variant_of = 'envelope-sealed'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'emails'
    aliases = ()
    keywords = ('envelope', 'sealed', 'emails')
    keyshape = Keyshape.SQUARE

    def build(self):
        box(self,'envelope',6,6,42,42,3)
        poly(self,'fold-top',(9,6),(16,14),(24,14),(32,14),(39,6))
        poly(self,'fold-bottom',(9,42),(16,34),(24,34),(32,34),(39,42))
        line(self,'seam',(24,14),(24,34))
        contacts(self)
