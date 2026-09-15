'underwear-bikini-bottom: independent smooth-curve repair.\n\nConstruction: Bikini bottom with a straight waistband and two smooth mirrored leg cutouts.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/shirt.svg and atomic-debug/shirt.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'c64c1abc-c9b3-5e7f-a6bc-d29a3ad87828'
SOURCE_PATH = 'pictographic-primitives/clothes/underwear bikini bottom_c64c1abc-c9b3-5e7f-a6bc-d29a3ad87828.svg'
AUTHOR = 'gpt-6'


class UnderwearBikiniBottomVariant2(Solo48):
    icon_id = 'underwear-bikini-bottom-v2'
    variant_of = 'underwear-bikini-bottom'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'clothes'
    aliases = ()
    keywords = ('underwear', 'bikini', 'bottom', 'clothes')
    keyshape = Keyshape.HRECT_L

    def build(self):
        path(self,'garment',(4,8),('L',(44,8)),('L',(44,16)),('C',(32,16),(28,27),(28,40)),('L',(20,40)),('C',(20,27),(16,16),(4,16)),('L',(4,8)),closed=True)
        contacts(self)
