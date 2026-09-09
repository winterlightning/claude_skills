# Variant of wolf-head-profile; parent file remains unchanged.
'Wolf profile with tall pointed ear, long angular muzzle and sloping nape; Lucide dog informs the isolated eye.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '078bb11c-b8d2-5e14-9def-3d791879af81'
SOURCE_PATH = 'pictographic-primitives/animals/wolf_078bb11c-b8d2-5e14-9def-3d791879af81.svg'
AUTHOR = 'gpt-6'

class WolfHeadProfileVariant2(Solo48):
    icon_id = 'wolf-head-profile-v2'
    variant_of = 'wolf-head-profile'
    variant_label = 'Angular wolf muzzle and pointed ear'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/animals'
    aliases = ()
    keywords = ('wolf', 'head', 'profile', 'ears', 'snout', 'canine', 'dog', 'wild')

    def build(self) -> None:
        # SQUARE centerline extremes (2,2)-(46,46). Directional profile.
        self.add_polyline('outline', (2,40), (12,23), (17,17), (18,2), (28,15), (33,20), (46,24), (43,31), (32,32), (24,39), (24,46))
        self.add_dot('eye', (24,24))
