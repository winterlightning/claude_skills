"""Fresh SOLO48 revision of clouds-fog from the claimed reference.

The original and rejected drawing were compared before this construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts
from icon_set.model.icons.solo._payments_batch02 import small_dollar

SOURCE_ICON_ID = '476f30e3-d2e6-4f04-969d-9ab07ee0196a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__clouds-fog/20260927T071330Z-thuan-mac-1/reference/cloud mist_476f30e3-d2e6-4f04-969d-9ab07ee0196a.svg'
AUTHOR = "gpt-6"

class CloudsFog(Solo48):
    icon_id = 'clouds-fog'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "weather"
    categories = ("weather", "primitives")
    aliases = ()
    keywords = ('cloud', 'fog', 'mist', 'overcast', 'weather', 'atmosphere')

    def build(self) -> None:

        path(self,'clouds',(6,22),('C',(6,16),(11,14),(16,18)),
             ('C',(18,10),(22,8),(24,8)),
             ('C',(30,8),(32,14),(34,16)),
             ('C',(40,14),(42,18),(42,22)))
        line(self,'mist-upper',(4,32),(44,32))
        line(self,'mist-lower',(10,40),(38,40))
        contacts(self)
