"""Fresh SOLO48 revision of helmet-97a9265b from its claimed original reference.

The original and rejected drawing were compared before this construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '97a9265b-3cf4-420c-8a2b-da7cd9955c06'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__helmet-97a9265b/20260927T061852Z-thuan-mac-1/reference/helmet_97a9265b-3cf4-420c-8a2b-da7cd9955c06.svg'
AUTHOR = "gpt-6"

class Helmet97a9265b(Solo48):
    icon_id = 'helmet-97a9265b'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    categories = ('protection', 'state', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('helmet', 'protection')
    keyshape = Keyshape.HRECT_L

    def build(self) -> None:

        # Shallow dome, broad baseline, and one centered vertical construction mark.
        line(self,'brim',(4,40),(44,40))
        path(self,'dome',(8,40),('A',16,24,True,(24,16)),('A',16,24,True,(40,40)))
        line(self,'crest-top',(24,8),(24,16))
        line(self,'crest-inner',(24,16),(24,26))
        contacts(self)
