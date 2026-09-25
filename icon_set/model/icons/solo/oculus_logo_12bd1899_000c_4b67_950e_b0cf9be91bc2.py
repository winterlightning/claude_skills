'oculus-logo: independent smooth-curve repair.\n\nConstruction: Capsule-like rounded enclosure with equal semicircular ends; centered interior where present.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/rectangle-horizontal.svg and atomic-debug/rectangle-horizontal.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '12bd1899-000c-4b67-950e-b0cf9be91bc2'
SOURCE_PATH = 'pictographic-primitives/logos/oculus logo_12bd1899-000c-4b67-950e-b0cf9be91bc2.svg'
AUTHOR = 'gpt-6'


class OculusLogo(Solo48):
    icon_id = 'oculus-logo'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('oculus', 'logo', 'logos')
    keyshape = Keyshape.HRECT_L

    def build(self):
        box(self,'outline',4,8,44,40,16)
        box(self,"inner",15,19,33,29,5)
        contacts(self)
