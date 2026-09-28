"""Fresh SOLO48 revision of hoodie-with-cuffed-sleeves from its claimed original reference.

The original and rejected drawing were compared before this construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '5ea4efe7-6268-556c-b803-08c8ca011cf1'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hoodie-with-cuffed-sleeves/20260927T061852Z-thuan-mac-1/reference/hoodie_5ea4efe7-6268-556c-b803-08c8ca011cf1.svg'
AUTHOR = "gpt-6"

class BatchSolo(Solo48):
    icon_id = 'hoodie-with-cuffed-sleeves'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'clothes'
    categories = ('primitives', 'clothes')
    aliases = ()
    keywords = ('hoodie', 'with', 'cuffed', 'sleeves')

    def build(self) -> None:

        path(self,'outline',(14,14),('A',10,8,True,(34,14)),
             ('A',8,10,True,(42,24)),('L',(42,36)),('L',(38,38)),
             ('L',(34,36)),('L',(34,42)),('L',(14,42)),('L',(14,36)),
             ('L',(10,38)),('L',(6,36)),('L',(6,24)),
             ('A',8,10,True,(14,14)),closed=True)
        poly(self,'hood-fold',(14,14),(24,22),(34,14))
        line(self,'neck-seam',(24,22),(24,27))
        line(self,'left-sleeve',(14,26),(14,36))
        line(self,'right-sleeve',(34,26),(34,36))
        contacts(self)
