'pin-interface-essential: independent smooth-curve repair.\n\nConstruction: Map pin with a circular crown, tangent tapered shoulders and a centered circular opening.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/map-pin.svg and atomic-debug/map-pin.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '85a2d016-7773-52ae-a800-9fa66b8f9b53'
SOURCE_PATH = 'pictographic-primitives/interface-essential/pin_85a2d016-7773-52ae-a800-9fa66b8f9b53.svg'
AUTHOR = 'gpt-6'


class PinInterfaceEssential(Solo48):
    icon_id = 'pin-interface-essential'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('pin', 'interface-essential')
    keyshape = Keyshape.VRECT_L

    def build(self):
        path(self,'pin',(24,44),('C',(18,36),(8,27),(8,20)),('A',16,16,True,(24,4)),('A',16,16,True,(40,20)),('C',(40,27),(30,36),(24,44)),closed=True)
        ellipse(self,'opening',24,20,5)
        contacts(self)
