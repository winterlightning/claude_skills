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

        # Restore the prior rounded mane; replace the angular frown with nose.
        self.add_arc('ear-left',(6,12),(18,12),radius_x=6)
        self.add_line('crown',(18,12),(30,12))
        self.add_arc('ear-right',(30,12),(42,12),radius_x=6)
        self.add_arc('mane-right',(42,12),(32,42),radius_x=10,radius_y=30)
        self.add_line('chin',(32,42),(16,42))
        self.add_arc('mane-left',(16,42),(6,12),radius_x=10,radius_y=30)
        self.add_contour('mane','ear-left','crown','ear-right','mane-right','chin','mane-left',closed=True)
        self.add_dot('eye-left',(16,23));self.add_dot('eye-right',(32,23))
        self.add_dot('nose',(24,30))
        contacts(self)
