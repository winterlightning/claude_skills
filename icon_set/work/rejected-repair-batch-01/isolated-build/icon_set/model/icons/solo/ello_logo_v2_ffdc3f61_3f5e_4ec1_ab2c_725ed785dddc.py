'ello-logo: independent smooth-curve repair.\n\nConstruction: Circular smile mark with a smooth half-ellipse mouth.\nKeyshape: CIRCLE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/circle.svg and atomic-debug/circle.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'ffdc3f61-3f5e-4ec1-ab2c-725ed785dddc'
SOURCE_PATH = 'pictographic-primitives/logos/ello logo_ffdc3f61-3f5e-4ec1-ab2c-725ed785dddc.svg'
AUTHOR = 'gpt-6'


class ElloLogoVariant2(Solo48):
    icon_id = 'ello-logo-v2'
    variant_of = 'ello-logo'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('ello', 'logo', 'logos')
    keyshape = Keyshape.CIRCLE

    def build(self):
        ellipse(self,'face',24,24,20)
        path(self,'smile',(14,25),('A',10,10,False,(34,25)))
        contacts(self)
