'common-file-book: independent smooth-curve repair.\n\nConstruction: Open book cover with softly rounded lower corners and a shared central spine.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/book-open.svg and atomic-debug/book-open.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'b96cc234-b92b-5a2e-85a0-53a3b86bbc71'
SOURCE_PATH = 'pictographic-primitives/office/common file book_b96cc234-b92b-5a2e-85a0-53a3b86bbc71.svg'
AUTHOR = 'gpt-6'


class CommonFileBookVariant2(Solo48):
    icon_id = 'common-file-book-v2'
    variant_of = 'common-file-book'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('common', 'file', 'book', 'office')
    keyshape = Keyshape.HRECT_L

    def build(self):
        path(self,'book',(4,36),('L',(4,16)),('L',(12,8)),('L',(24,8)),('L',(36,8)),('L',(44,16)),('L',(44,36)),('A',4,4,True,(40,40)),('L',(24,40)),('L',(8,40)),('A',4,4,True,(4,36)),closed=True)
        line(self,'spine',(24,8),(24,40))
        contacts(self)
