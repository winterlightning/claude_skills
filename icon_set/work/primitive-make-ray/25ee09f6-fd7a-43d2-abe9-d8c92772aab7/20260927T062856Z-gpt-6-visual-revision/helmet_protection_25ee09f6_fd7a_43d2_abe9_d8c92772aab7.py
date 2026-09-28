"""Fresh SOLO48 revision of helmet-protection from its claimed original reference.

The original and rejected drawing were compared before this construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '25ee09f6-fd7a-43d2-abe9-d8c92772aab7'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__helmet-protection/20260927T061852Z-thuan-mac-1/reference/helmet_25ee09f6-fd7a-43d2-abe9-d8c92772aab7.svg'
AUTHOR = "gpt-6"

class HelmetProtection(Solo48):
    icon_id = 'helmet-protection'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    categories = ('protection', 'primitives')
    aliases = ()
    keywords = ('helmet', 'protection')
    keyshape = Keyshape.HRECT_L

    def build(self) -> None:

        # One broad central reinforcement bounded by twin edges.
        path(self,'dome',(8,30),('L',(8,20)),('A',12,12,True,(20,8)),
             ('L',(28,8)),('A',12,12,True,(40,20)),('L',(40,30)))
        box(self,'brim',4,30,44,40,2,xs=(8,20,28,40))
        line(self,'strip-left',(20,8),(20,30))
        line(self,'strip-right',(28,8),(28,30))
        contacts(self)
