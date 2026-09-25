'Smaller round head with a visible eye, a distinct beak and a deep eggshell; Lucide bird and egg inform the construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '20c9a90e-2b2b-5596-bf5f-720461c74888'
SOURCE_PATH = 'pictographic-primitives/animals/chicken hatch_20c9a90e-2b2b-5596-bf5f-720461c74888.svg'
AUTHOR = 'gpt-6'


class HatchingChick(Solo48):
    icon_id = 'hatching-chick'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    categories = ("animals", "primitives")
    aliases = ()
    keywords = ('chick', 'egg', 'hatch', 'shell', 'birth', 'easter', 'bird', 'new')

    def build(self) -> None:
        # A small round chick rises above a deep, symmetric eggshell. The head and
        # shell are distinct silhouettes, joined at the two low points of the crack.
        # SQUARE centerline extremes are (6,6)-(42,42); all strokes stay 4 units.
        self.add_bezier('back',(16,32),((16,26),(14,21),(14,16)))
        self.add_arc('head',(14,16),(34,16),radius_x=10)
        self.add_line('bill-top',(34,16),(42,18))
        self.add_line('bill-bottom',(42,18),(32,22))
        self.add_line('breast',(32,22),(32,32))
        self.add_contour('chick','back','head','bill-top','bill-bottom','breast')
        self.add_dot('eye',(24,16))
        self.add_polyline('crack',(6,28),(16,32),(24,28),(32,32),(42,28))
        self.add_arc('shell',(42,28),(6,28),radius_x=18,radius_y=14)
        self.relate('connect','shell','crack')
        self.relate('connect','chick','crack')
