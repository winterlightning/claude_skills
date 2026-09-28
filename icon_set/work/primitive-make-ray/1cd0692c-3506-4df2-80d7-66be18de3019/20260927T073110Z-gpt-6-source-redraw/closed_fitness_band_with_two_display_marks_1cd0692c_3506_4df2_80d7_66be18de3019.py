"""Fresh SOLO48 revision of closed-fitness-band-with-two-display-marks from the claimed reference.

The original and rejected drawing were compared before this construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts
from icon_set.model.icons.solo._payments_batch02 import small_dollar

SOURCE_ICON_ID = '1cd0692c-3506-4df2-80d7-66be18de3019'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__closed-fitness-band-with-two-display-marks/20260927T071330Z-thuan-mac-1/reference/wearable smart watch_1cd0692c-3506-4df2-80d7-66be18de3019.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'closed-fitness-band-with-two-display-marks'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'devices'
    categories = ('primitives', 'devices')
    aliases = ()
    keywords = ('smart', 'fitness', 'band')

    def build(self) -> None:

        box(self,'band',4,8,44,40,16,xs=(24,))
        path(self,'divider',(24,8),('A',8,16,True,(24,40)))
        line(self,'mark-one',(12,18),(16,18))
        line(self,'mark-two',(12,27),(16,27))
        contacts(self)
