'shop-sign: independent smooth-curve repair.\n\nConstruction: Hanging shop sign on a shared centered hanger; four rounded sign corners.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/signpost.svg and atomic-debug/signpost.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'ef0b754b-7f5c-4dca-81ee-ac4219b79501'
SOURCE_PATH = 'pictographic-primitives/shopping/shop sign_ef0b754b-7f5c-4dca-81ee-ac4219b79501.svg'
AUTHOR = 'gpt-6'


class ShopSign(Solo48):
    icon_id = 'shop-sign'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('shop', 'sign', 'shopping')
    keyshape = Keyshape.HRECT_L

    def build(self):
        box(self,'sign',4,18,44,40,4,xs=(14,34))
        poly(self,'hanger',(14,18),(24,8),(34,18))
        contacts(self)
