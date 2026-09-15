'electric-waves-1: independent smooth-curve repair.\n\nConstruction: Two concentric signal arches and a centered terminal dot; wide clear gaps.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/wifi.svg and atomic-debug/wifi.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'e6789468-9cc2-4444-a388-10e9ec1fdcb5'
SOURCE_PATH = 'pictographic-primitives/state/electric waves 1_e6789468-9cc2-4444-a388-10e9ec1fdcb5.svg'
AUTHOR = 'gpt-6'


class ElectricWaves1(Solo48):
    icon_id = 'electric-waves-1'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('electric', 'waves', 'state')
    keyshape = Keyshape.HRECT_L

    def build(self):
        path(self,'outer',(4,18),('C',(10,12),(17,8),(24,8)),('C',(31,8),(38,12),(44,18)))
        path(self,'inner',(13,28),('C',(19,20),(29,20),(35,28)))
        self.add_dot('dot',(24,40))
        contacts(self)
