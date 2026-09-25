'headphones: independent smooth-curve repair.\n\nConstruction: Headphones with a true elliptical headband and paired soft rectangular ear pads; attachments meet at pad corners.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/headphones.svg and atomic-debug/headphones.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '1107c9dd-40f5-4f90-9797-a72017359e90'
SOURCE_PATH = 'pictographic-primitives/symbol/headset_1107c9dd-40f5-4f90-9797-a72017359e90.svg'
AUTHOR = 'gpt-6'


class Headphones(Solo48):
    icon_id = 'headphones'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('headphones', 'headset', 'audio', 'music', 'listen', 'sound', 'support', 'earphones')
    keyshape = Keyshape.HRECT_L

    def build(self):
        path(self,'band',(4,31),('L',(4,24)),('A',20,16,True,(24,8)),('A',20,16,True,(44,24)),('L',(44,31)))
        box(self,'left-pad',4,28,14,40,3)
        box(self,'right-pad',34,28,44,40,3)
        contacts(self)
