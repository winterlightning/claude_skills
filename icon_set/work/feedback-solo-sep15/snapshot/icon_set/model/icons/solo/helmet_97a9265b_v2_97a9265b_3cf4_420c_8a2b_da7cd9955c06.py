'helmet-97a9265b: independent smooth-curve repair.\n\nConstruction: Smooth dome helmet with a centered crest and broad baseline.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/hard-hat.svg and atomic-debug/hard-hat.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '97a9265b-3cf4-420c-8a2b-da7cd9955c06'
SOURCE_PATH = 'pictographic-primitives/protection/helmet_97a9265b-3cf4-420c-8a2b-da7cd9955c06.svg'
AUTHOR = 'gpt-6'


class Helmet97a9265bVariant2(Solo48):
    icon_id = 'helmet-97a9265b-v2'
    variant_of = 'helmet-97a9265b'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('helmet', 'protection')
    keyshape = Keyshape.HRECT_L

    def build(self):
        path(self,'dome',(4,40),('L',(4,30)),('A',20,20,True,(24,10)),('A',20,20,True,(44,30)),('L',(44,40)),('L',(4,40)),closed=True)
        line(self,'crest',(24,8),(24,24))
        contacts(self)
