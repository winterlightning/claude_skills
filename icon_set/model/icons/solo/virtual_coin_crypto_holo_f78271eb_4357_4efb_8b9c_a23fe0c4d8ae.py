'virtual-coin-crypto-holo: independent smooth-curve repair.\n\nConstruction: Holo emblem with two mirrored half-ellipses and a centered transverse bar.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/braces.svg and atomic-debug/braces.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'f78271eb-4357-4efb-8b9c-a23fe0c4d8ae'
SOURCE_PATH = 'pictographic-primitives/finance/virtual coin crypto holo_f78271eb-4357-4efb-8b9c-a23fe0c4d8ae.svg'
AUTHOR = 'gpt-6'


class VirtualCoinCryptoHolo(Solo48):
    icon_id = 'virtual-coin-crypto-holo'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'finance'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'holo', 'finance')
    keyshape = Keyshape.HRECT_L

    def build(self):
        path(self,'left',(4,8),('A',14,16,True,(18,24)),('A',14,16,True,(4,40)))
        path(self,'right',(44,8),('A',14,16,False,(30,24)),('A',14,16,False,(44,40)))
        line(self,'bar',(10,24),(38,24))
        contacts(self)
