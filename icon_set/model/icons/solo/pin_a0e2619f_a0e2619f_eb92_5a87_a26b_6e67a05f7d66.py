'pin-a0e2619f: independent smooth-curve repair.\n\nConstruction: Map pin with a circular crown, tangent tapered shoulders and a centered circular opening.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/map-pin.svg and atomic-debug/map-pin.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'a0e2619f-eb92-5a87-a26b-6e67a05f7d66'
SOURCE_PATH = 'pictographic-primitives/interface-essential/pin_a0e2619f-eb92-5a87-a26b-6e67a05f7d66.svg'
AUTHOR = 'gpt-6'


class PinA0e2619f(Solo48):
    icon_id = 'pin-a0e2619f'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('pin', 'interface-essential')
    keyshape = Keyshape.VRECT_L

    def build(self):
        path(self,'pin',(24,44),('C',(18,36),(8,27),(8,20)),('A',16,16,True,(24,4)),('A',16,16,True,(40,20)),('C',(40,27),(30,36),(24,44)),closed=True)
        ellipse(self,'opening',24,20,5)
        contacts(self)
