from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ba3b7416-8143-5dcf-8dad-7b14c1ad66f2'
SOURCE_PATH = 'pictographic-primitives/animals/shark_ba3b7416-8143-5dcf-8dad-7b14c1ad66f2.svg'
AUTHOR = 'gpt-6'


class SimpleShark(Solo48):
    icon_id = 'simple-shark'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('shark', 'fish', 'fin', 'sea', 'ocean', 'predator', 'swim', 'marine')

    def build(self) -> None:
        self.add_polyline('tail-upper',(10,22),(4,14),(4,24),(4,34),(10,28),(24,32),(24,40),(33,33))
        self.add_bezier('nose',(33,33),((39,32),(44,28),(44,25)),((44,21),(37,18),(30,17)))
        self.add_polyline('dorsal',(30,17),(21,8),(21,18),(10,22))
        self.relate('connect','tail-upper','nose');self.relate('connect','nose','dorsal');self.relate('connect','dorsal','tail-upper')
