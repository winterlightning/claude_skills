'cog-interface-essential: independent smooth-curve repair.\n\nConstruction: Six-tooth cog with repeated paired shoulders around a circular hub; purposeful tooth corners preserved.\nKeyshape: SQUARE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/settings.svg and atomic-debug/settings.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '3fdd5840-1a58-4cbe-bcb5-810d21e3c2dd'
SOURCE_PATH = 'pictographic-primitives/interface-essential/cog_3fdd5840-1a58-4cbe-bcb5-810d21e3c2dd.svg'
AUTHOR = 'gpt-6'


class CogInterfaceEssentialVariant2(Solo48):
    icon_id = 'cog-interface-essential-v2'
    variant_of = 'cog-interface-essential'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('cog', 'interface-essential')
    keyshape = Keyshape.SQUARE

    def build(self):
        poly(self,'gear',(20,6),(28,6),(30,14),(38,12),(42,18),(36,24),(42,30),(38,36),(30,34),(28,42),(20,42),(18,34),(10,36),(6,30),(12,24),(6,18),(10,12),(18,14),closed=True)
        ellipse(self,'hub',24,24,3)
        contacts(self)
