"""Fresh SOLO48 revision of car-horn from the claimed reference.

The original and rejected drawing were compared before this construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts
from icon_set.model.icons.solo._payments_batch02 import small_dollar

SOURCE_ICON_ID = '6e120b10-f09c-4f71-9e1d-244b8eb9fd47'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__car-horn/20260927T071330Z-thuan-mac-1/reference/horn_6e120b10-f09c-4f71-9e1d-244b8eb9fd47.svg'
AUTHOR = 'gpt-6'

class CarHorn(Solo48):
    icon_id = 'car-horn'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    categories = ("transportation", "primitives")
    aliases = ()
    keywords = ('horn', 'car horn', 'sound', 'honk', 'dashboard', 'trumpet', 'alert', 'vehicle')

    def build(self) -> None:

        # Source has a sharp left bell, long tube, lower loop and two short marks.
        poly(self,'bell',(4,16),(18,24),(4,32),closed=True)
        poly(self,'tube',(18,24),(44,24))
        path(self,'loop',(28,24),('L',(28,34)),('A',6,6,False,(34,40)),
             ('A',6,6,False,(40,34)),('L',(40,24)))
        line(self,'sound-one',(28,8),(32,8))
        line(self,'sound-two',(38,8),(42,8))
        contacts(self)
