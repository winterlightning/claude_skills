# Variant of wolf-head; parent file remains unchanged.
'Wolf head with upright triangular ear, long snout and angular cheek; intentionally directional. Lucide dog informs eye placement.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5980d529-a023-5a54-8f17-b3538741399a'
SOURCE_PATH = 'pictographic-primitives/animals/wolf_5980d529-a023-5a54-8f17-b3538741399a.svg'
AUTHOR = 'gpt-6'

class WolfHeadVariant2(Solo48):
    icon_id = 'wolf-head-v2'
    variant_of = 'wolf-head'
    variant_label = 'Long muzzle and angular wolf ruff'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/animals'
    aliases = ()
    keywords = ('wolf', 'head', 'profile', 'minimal', 'snout', 'ear', 'canine', 'dog')

    def build(self) -> None:
        # VRECT_XL centerline extremes (6,6)-(42,42).
        self.add_polyline('outline', (6,40), (12,25), (15,16), (18,6), (28,15), (32,20), (42,22), (42,28), (34,33), (28,33), (21,40), (22,42))
        self.add_dot('eye', (23,24))
