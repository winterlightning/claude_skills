'shield-cd9ddfe2: independent smooth-curve repair.\n\nConstruction: Shield with a smooth domed top and a coherent curved lower bowl; centered detail kept spacious.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/shield.svg and atomic-debug/shield.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'cd9ddfe2-dfc2-5c87-aa38-d1de45646346'
SOURCE_PATH = 'pictographic-primitives/protection/shield_cd9ddfe2-dfc2-5c87-aa38-d1de45646346.svg'
AUTHOR = 'gpt-6'


class ShieldCd9ddfe2Variant2(Solo48):
    icon_id = 'shield-cd9ddfe2-v2'
    variant_of = 'shield-cd9ddfe2'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('shield', 'protection')
    keyshape = Keyshape.VRECT_L

    def build(self):
        path(self,'shield',(8,9),('C',(17,2.333333333),(31,2.333333333),(40,9)),('L',(40,23)),('C',(40,34),(32,41),(24,44)),('C',(16,41),(8,34),(8,23)),('L',(8,9)),closed=True)
        contacts(self)
