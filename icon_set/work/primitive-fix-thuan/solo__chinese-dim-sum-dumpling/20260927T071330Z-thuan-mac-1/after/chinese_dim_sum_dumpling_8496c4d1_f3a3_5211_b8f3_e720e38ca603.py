"""Fresh SOLO48 revision of chinese-dim-sum-dumpling from the claimed reference.

The original and rejected drawing were compared before this construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts
from icon_set.model.icons.solo._payments_batch02 import small_dollar

SOURCE_ICON_ID = '8496c4d1-f3a3-5211-b8f3-e720e38ca603'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__chinese-dim-sum-dumpling/20260927T071330Z-thuan-mac-1/reference/dimsum chinese dumpling_8496c4d1-f3a3-5211-b8f3-e720e38ca603.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'chinese-dim-sum-dumpling'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('chinese', 'dim', 'sum', 'dumpling')

    def build(self) -> None:

        path(self,'dumpling',(24,6),('L',(30,10)),('L',(30,14)),
             ('C',(30,19),(42,23),(42,31)),('C',(42,40),(34,42),(24,42)),
             ('C',(14,42),(6,40),(6,31)),('C',(6,23),(18,19),(18,14)),
             ('L',(18,10)),('L',(24,6)),closed=True)
        line(self,'pleat-left',(20,26),(20,32))
        line(self,'pleat-right',(28,26),(28,32))
        contacts(self)
