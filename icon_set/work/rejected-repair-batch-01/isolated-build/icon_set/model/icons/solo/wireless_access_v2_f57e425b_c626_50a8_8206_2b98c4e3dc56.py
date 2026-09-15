'wireless-access: independent smooth-curve repair.\n\nConstruction: Wireless access symbol rotated in construction: concentric side-facing signal curves around a circular dot.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/wifi.svg and atomic-debug/wifi.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'f57e425b-c626-50a8-8206-2b98c4e3dc56'
SOURCE_PATH = 'pictographic-primitives/networks/wireless access_f57e425b-c626-50a8-8206-2b98c4e3dc56.svg'
AUTHOR = 'gpt-6'


class WirelessAccessVariant2(Solo48):
    icon_id = 'wireless-access-v2'
    variant_of = 'wireless-access'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'networks'
    aliases = ()
    keywords = ('wireless', 'access', 'networks')
    keyshape = Keyshape.HRECT_L

    def build(self):
        ellipse(self,'point',10,24,6)
        path(self,'inner',(26,14),('C',(34,20),(34,28),(26,34)))
        path(self,'outer',(35,8),('C',(47,17),(47,31),(35,40)))
        contacts(self)
