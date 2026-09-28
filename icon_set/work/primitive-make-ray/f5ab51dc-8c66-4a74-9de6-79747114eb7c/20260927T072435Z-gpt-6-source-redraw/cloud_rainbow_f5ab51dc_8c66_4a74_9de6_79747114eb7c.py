"""Fresh SOLO48 revision of cloud-rainbow from the claimed reference.

The original and rejected drawing were compared before this construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts
from icon_set.model.icons.solo._payments_batch02 import small_dollar

SOURCE_ICON_ID = 'f5ab51dc-8c66-4a74-9de6-79747114eb7c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cloud-rainbow/20260927T071330Z-thuan-mac-1/reference/weather cloud rainbow_f5ab51dc-8c66-4a74-9de6-79747114eb7c.svg'
AUTHOR = "gpt-6"

class CloudRainbow(Solo48):
    icon_id = 'cloud-rainbow'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "weather"
    categories = ("weather", "primitives")
    aliases = ()
    keywords = ('cloud', 'rainbow', 'sky', 'weather', 'arc', 'sunlight')

    def build(self) -> None:

        # Larger cloud with two concentric rainbow sweeps rising to the right.
        path(self,'cloud',(12,40),('A',8,5,True,(8,30)),
             ('A',8,6,True,(20,24)),('A',8,6,True,(32,30)),
             ('A',8,5,True,(28,40)),('L',(12,40)),closed=True)
        path(self,'rainbow-outer',(20,24),('A',24,16,True,(44,8)))
        path(self,'rainbow-inner',(28,30),('A',16,12,True,(44,18)))
        contacts(self)
