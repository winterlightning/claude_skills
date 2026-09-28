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

        path(self,'cloud',(24,20),('C',(30,18),(34,22),(34,26)),
             ('C',(40,26),(42,32),(40,36)),('C',(38,40),(34,40),(30,40)),
             ('L',(12,40)),('C',(4,40),(4,36),(4,32)),
             ('C',(4,26),(10,22),(16,24)),('C',(18,20),(20,20),(24,20)),closed=True)
        path(self,'rainbow-outer',(24,20),('A',20,12,True,(44,8)))
        path(self,'rainbow-inner',(34,26),('A',10,8,True,(44,18)))
        contacts(self)
