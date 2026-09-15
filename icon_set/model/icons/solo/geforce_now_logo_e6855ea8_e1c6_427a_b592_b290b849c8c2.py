'geforce-now-logo: independent smooth-curve repair.\n\nConstruction: Preserve the two smooth signal arches and hollow circular terminal; center the ring at (24,36), radius 4, with generous clearance above it.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/wifi.svg and atomic-debug/wifi.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'e6855ea8-e1c6-427a-b592-b290b849c8c2'
SOURCE_PATH = 'pictographic-primitives/logos/geforce now logo_e6855ea8-e1c6-427a-b592-b290b849c8c2.svg'
AUTHOR = 'gpt-6'


class GeforceNowLogo(Solo48):
    icon_id = 'geforce-now-logo'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('geforce', 'now', 'logo', 'logos')
    keyshape = Keyshape.HRECT_L

    def build(self):
        path(self,'outer',(4,18),('C',(10,12),(17,8),(24,8)),('C',(31,8),(38,12),(44,18)))
        path(self,'inner',(13,28),('C',(19,20),(29,20),(35,28)))
        ellipse(self,'terminal',24,36,4)
        contacts(self)
