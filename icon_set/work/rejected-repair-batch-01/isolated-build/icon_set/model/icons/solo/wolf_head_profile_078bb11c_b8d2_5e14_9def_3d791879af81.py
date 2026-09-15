'Wolf profile with tall pointed ear, long angular muzzle and sloping nape; Lucide dog informs the isolated eye.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '078bb11c-b8d2-5e14-9def-3d791879af81'
SOURCE_PATH = 'pictographic-primitives/animals/wolf_078bb11c-b8d2-5e14-9def-3d791879af81.svg'
AUTHOR = 'gpt-6'

class WolfHeadProfile(Solo48):
    icon_id = 'wolf-head-profile'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/animals'
    aliases = ()
    keywords = ('wolf', 'head', 'profile', 'ears', 'snout', 'canine', 'dog', 'wild')

    def build(self) -> None:
        # SQUARE centerline extremes (6,6)-(42,42). Directional profile.
        self.add_polyline('outline', (6,40), (12,23), (17,17), (18,6), (28,15), (33,20), (42,24), (42,31), (32,32), (24,39), (24,42))
        self.add_dot('eye', (24,24))
