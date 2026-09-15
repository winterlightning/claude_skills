'Sabre-tooth profile: preserve the open rear contour and long fang, with a round ear and smooth jaw. Exact SQUARE extrema.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '84e8cc32-4f07-4abc-b10f-ca70cb883ea0'
SOURCE_PATH = 'pictographic-primitives/animals/tiger head_84e8cc32-4f07-4abc-b10f-ca70cb883ea0.svg'
AUTHOR = 'gpt-6'


class SabreToothHead(Solo48):
    icon_id = 'sabre-tooth-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('sabre tooth', 'tiger', 'fang', 'head', 'profile', 'prehistoric', 'big cat', 'extinct')

    def build(self) -> None:
        self.add_line('skull',(6,20),(32,11))
        self.add_arc('ear',(32,11),(42,11),radius_x=5)
        self.add_bezier('cheek',(42,20),((42,27),(40,34),(36,38)))
        self.add_bezier('jaw',(36,38),((31,35),(23,34),(16,36)))
        self.add_line('lower-jaw',(16,36),(20,42))
        self.add_bezier('fang',(20,42),((15,41),(11,35),(10,30)))
        self.add_polyline('muzzle',(10,30),(6,32),(6,20))
        self.add_contour('upper','skull','ear')
        self.add_contour('lower','cheek','jaw','lower-jaw','fang')
        self.relate('connect','muzzle','upper')
        self.relate('connect','muzzle','lower')
        self.add_bezier('upper-jaw',(10,30),((15,28),(20,26),(24,26)))
        self.relate('connect','upper-jaw','muzzle')
        self.relate('connect','upper-jaw','lower')
        self.add_dot('eye',(31,21))
