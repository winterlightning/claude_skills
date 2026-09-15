'symbol-medical: independent smooth-curve repair.\n\nConstruction: Outlined medical cross with equal arm widths and rounded outside corners; re-entrant corners preserve the cross.\nKeyshape: SQUARE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/plus.svg and atomic-debug/plus.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'c2218007-b6c4-5c1b-9355-0c9d6d72fb5c'
SOURCE_PATH = 'pictographic-primitives/protection/symbol medical_c2218007-b6c4-5c1b-9355-0c9d6d72fb5c.svg'
AUTHOR = 'gpt-6'


class SymbolMedicalVariant2(Solo48):
    icon_id = 'symbol-medical-v2'
    variant_of = 'symbol-medical'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('symbol', 'medical', 'protection')
    keyshape = Keyshape.SQUARE

    def build(self):
        path(self,'cross',(21,6),('L',(27,6)),('A',3,3,True,(30,9)),('L',(30,18)),('L',(39,18)),('A',3,3,True,(42,21)),('L',(42,27)),('A',3,3,True,(39,30)),('L',(30,30)),('L',(30,39)),('A',3,3,True,(27,42)),('L',(21,42)),('A',3,3,True,(18,39)),('L',(18,30)),('L',(9,30)),('A',3,3,True,(6,27)),('L',(6,21)),('A',3,3,True,(9,18)),('L',(18,18)),('L',(18,9)),('A',3,3,True,(21,6)),closed=True)
        contacts(self)
