'Wolf head with upright triangular ear, long snout and angular cheek; intentionally directional. Lucide dog informs eye placement.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5980d529-a023-5a54-8f17-b3538741399a'
SOURCE_PATH = 'pictographic-primitives/animals/wolf_5980d529-a023-5a54-8f17-b3538741399a.svg'
AUTHOR = 'gpt-6'

class WolfHead(Solo48):
    icon_id = 'wolf-head'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/animals'
    aliases = ()
    keywords = ('wolf', 'head', 'profile', 'minimal', 'snout', 'ear', 'canine', 'dog')

    def build(self) -> None:
        # VRECT_L centerline extremes (8,4)-(40,44).
        self.add_polyline('outline', (8,40), (12,25), (15,16), (18,4), (28,15), (32,20), (40,22), (40,28), (34,33), (28,33), (21,40), (22,44))
        self.add_dot('eye', (23,24))
