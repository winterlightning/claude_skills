'Fortress: symmetric battlements and a broad wall; deliberate corners replace uneven fitted edges.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '662fb562-2043-4728-8a10-72a8034ebd9b'
SOURCE_PATH = 'pictographic-primitives/protection/fortress_662fb562-2043-4728-8a10-72a8034ebd9b.svg'
AUTHOR = 'gpt-6'

class Fortress(Solo48):
    icon_id = 'fortress'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('fortress', 'protection')

    def build(self):
        # Fortress: three equal battlements with 8-unit openings and a balanced broad wall.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        p('castle',(4,8),(12,8),(12,16),(20,16),(20,8),(28,8),(28,16),(36,16),(36,8),(44,8),(44,24),(38,28),(38,40),(10,40),(10,28),(4,24),(4,8))
