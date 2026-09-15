'pin-interface-essential: distinct review variant.\n\nConstruction: Location pin with a larger circular opening and a lighter visual center; preserve the continuous pin silhouette.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nConstruction reference: map-pin from the previously inspected Lucide original and atomic-debug library.\nPrevious canonical model is preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '85a2d016-7773-52ae-a800-9fa66b8f9b53'
SOURCE_PATH = 'pictographic-primitives/interface-essential/pin_85a2d016-7773-52ae-a800-9fa66b8f9b53.svg'
AUTHOR = 'gpt-6'


class PinInterfaceEssentialVariant2(Solo48):
    icon_id = 'pin-interface-essential-v2'
    variant_of = 'pin-interface-essential'
    variant_label = 'Distinct subject and smooth curves'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('pin', 'interface-essential')
    keyshape = Keyshape.VRECT_L

    def build(self):
        path(self,'pin',(24,44),('C',(18,36),(8,27),(8,20)),('A',16,16,True,(24,4)),('A',16,16,True,(40,20)),('C',(40,27),(30,36),(24,44)),closed=True)
        ellipse(self,'opening',24,20,7)
        contacts(self)
