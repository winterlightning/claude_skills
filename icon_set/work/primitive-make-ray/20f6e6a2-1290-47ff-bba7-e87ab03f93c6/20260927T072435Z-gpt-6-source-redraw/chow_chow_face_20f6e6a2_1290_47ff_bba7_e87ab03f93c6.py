"""Fresh SOLO48 revision of chow-chow-face from the claimed reference.

The original and rejected drawing were compared before this construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts
from icon_set.model.icons.solo._payments_batch02 import small_dollar

SOURCE_ICON_ID = '20f6e6a2-1290-47ff-bba7-e87ab03f93c6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__chow-chow-face/20260927T071330Z-thuan-mac-1/reference/chow chow_20f6e6a2-1290-47ff-bba7-e87ab03f93c6.svg'
AUTHOR = 'gpt-6'

class ChowChowFace(Solo48):
    icon_id = 'chow-chow-face'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    categories = ("pets", "primitives")
    aliases = ()
    keywords = ('dog', 'chow-chow', 'face', 'breed', 'fluffy', 'mane', 'pet')

    def build(self) -> None:

        # Fluffy mane with round ears and compact nose in place of a frown.
        path(self,'mane',(18,12),('A',6,6,True,(6,12)),
             ('A',10,30,True,(16,42)),('L',(32,42)),
             ('A',10,30,True,(42,12)),('A',6,6,True,(30,12)),
             ('L',(18,12)),closed=True)
        self.add_dot('eye-left',(16,23));self.add_dot('eye-right',(32,23))
        self.add_dot('nose',(24,30))
        path(self,'mouth',(19,36),('A',5,4,False,(29,36)))
        contacts(self)
