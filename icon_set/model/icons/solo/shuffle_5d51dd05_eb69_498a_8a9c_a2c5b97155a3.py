'Shuffle: two smooth crossing routes share their real central crossing and end in equal arrowheads.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5d51dd05-eb69-498a-8a9c-a2c5b97155a3'
SOURCE_PATH = 'pictographic-primitives/interface-essential/shuffle_5d51dd05-eb69-498a-8a9c-a2c5b97155a3.svg'
AUTHOR = 'gpt-6'

class Shuffle(Solo48):
    icon_id = 'shuffle'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('shuffle', 'interface-essential')

    def build(self) -> None:
        self.add_bezier('rising',(6,36),((15,36),(18,30),(24,24)),((30,18),(33,12),(42,12)))
        self.add_bezier('falling',(6,12),((15,12),(18,18),(24,24)),((30,30),(33,36),(42,36)))
        self.relate('connect','rising','falling')
        self.add_polyline('upper-head',(36,6),(42,12),(36,18))
        self.add_polyline('lower-head',(36,30),(42,36),(36,42))
        self.relate('connect','upper-head','rising');self.relate('connect','lower-head','falling')
