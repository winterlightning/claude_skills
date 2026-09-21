"""4 WAY reflowed as 4W / AY to retain every character at 48px. SQUARE ink (6,6)-(42,42). Lucide type informs the monoline construction; A has a triangular counter."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '71e83a5c-ca8f-4fc3-96ff-5a4ac5b09283'
SOURCE_PATH = 'pictographic-primitives/transportation/4 way_71e83a5c-ca8f-4fc3-96ff-5a4ac5b09283.svg'
AUTHOR = 'gpt-6'

class FourWayTextSign(Solo48):
    icon_id = 'four-way-text-sign'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('4 way', 'four way', 'junction', 'intersection', 'stop', 'road sign', 'text', 'traffic')

    def build(self) -> None:
        self.add_polyline('number',(6,6),(6,14),(18,14),(18,6),(18,22))

        self.add_polyline('w',(26,6),(30,22),(34,14),(38,22),(42,6))
        self.add_polyline('a-outline',(6,42),(8,39),(14,30),(20,39),(22,42))
        self.add_line('a-bar',(8,39),(20,39))
        self.relate('connect','a-outline','a-bar')
        self.add_polyline('y-arms',(30,30),(36,36),(42,30))
        self.add_line('y-stem',(36,36),(36,42))
        self.relate('connect','y-arms','y-stem')
