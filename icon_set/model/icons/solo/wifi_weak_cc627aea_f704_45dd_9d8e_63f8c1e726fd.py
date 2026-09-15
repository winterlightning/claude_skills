'wifi-weak: independent smooth-curve repair.\n\nConstruction: Weak wireless signal with two smooth concentric arches and a centered cross.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/wifi.svg and atomic-debug/wifi.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'cc627aea-f704-45dd-9d8e-63f8c1e726fd'
SOURCE_PATH = 'pictographic-primitives/symbol/wifi weak_cc627aea-f704-45dd-9d8e-63f8c1e726fd.svg'
AUTHOR = 'gpt-6'


class WifiWeak(Solo48):
    icon_id = 'wifi-weak'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('wifi', 'weak', 'symbol')
    keyshape = Keyshape.HRECT_L

    def build(self):
        path(self,'outer',(4,18),('C',(10,12),(17,8),(24,8)),('C',(31,8),(38,12),(44,18)))
        path(self,'inner',(13,28),('C',(19,20),(29,20),(35,28)))
        line(self,'cross-a',(21,34),(27,40));line(self,'cross-b',(21,40),(27,34))
        contacts(self)
