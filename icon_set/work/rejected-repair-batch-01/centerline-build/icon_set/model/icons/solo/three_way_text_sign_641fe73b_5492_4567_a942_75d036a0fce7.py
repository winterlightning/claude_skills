"""3 WAY reflowed as 3W / AY to retain every character at 48px. SQUARE ink (6,6)-(42,42). Lucide type informs the monoline construction; A has a triangular counter."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '641fe73b-5492-4567-a942-75d036a0fce7'
SOURCE_PATH = 'pictographic-primitives/transportation/3 way_641fe73b-5492-4567-a942-75d036a0fce7.svg'
AUTHOR = 'gpt-6'

class ThreeWayTextSign(Solo48):
    icon_id = 'three-way-text-sign'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('3 way', 'three way', 'junction', 'intersection', 'stop', 'road sign', 'text', 'traffic')

    def build(self) -> None:
        self.add_polyline('number-outline',(6,6),(18,6),(18,14),(18,22),(6,22))
        self.add_line('number-middle',(10,14),(18,14))
        self.relate('connect','number-outline','number-middle')

        self.add_polyline('w',(26,6),(26,22),(34,14),(42,22),(42,6))
        self.add_polyline('a-outline',(6,42),(8,39),(14,30),(20,39),(22,42))
        self.add_line('a-bar',(8,39),(20,39))
        self.relate('connect','a-outline','a-bar')
        self.add_polyline('y-arms',(30,30),(36,36),(42,30))
        self.add_line('y-stem',(36,36),(36,42))
        self.relate('connect','y-arms','y-stem')
