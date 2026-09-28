"""Fresh SOLO48 revision of bomb-lit-fuse from the claimed reference.

The original and rejected drawing were compared before this construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts
from icon_set.model.icons.solo._payments_batch02 import small_dollar

SOURCE_ICON_ID = '446e953d-43b9-407c-93c8-585b9ab83fde'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bomb-lit-fuse/20260927T071330Z-thuan-mac-1/reference/boom_446e953d-43b9-407c-93c8-585b9ab83fde.svg'
AUTHOR = 'gpt-6'

class BombLitFuse(Solo48):
    icon_id = 'bomb-lit-fuse'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol", "state")
    aliases = ()
    keywords = ('bomb', 'boom', 'explosion', 'fuse', 'blast', 'danger', 'detonate', 'spark')

    def build(self) -> None:

        # Round bomb and jagged burst; the rejected spark became an X.
        path(self,'bomb',(22,24),('A',10,10,True,(16,42)),
             ('A',10,10,True,(6,32)),('A',10,10,True,(22,24)),closed=True)
        line(self,'fuse',(22,24),(32,14))
        poly(self,'burst',(28,6),(32,14),(40,6),(37,15),(42,19),(34,19))
        contacts(self)
