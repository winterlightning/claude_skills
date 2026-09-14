"""A side-view whistle has a short rectangular mouthpiece extending left from a rounded body. A large circular opening occupies the body, and a small attachment loop projects at the rear.
Lucide rounded enclosure construction; no useful exact whistle match. Broad round chamber, large circular opening and left mouthpiece retained. Tiny rear attachment loop omitted. Intentional side-view asymmetry.
HRECT_L: centerline extremes (6,8)-(42,40); freshly authored on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '579de92e-a106-5aa9-b44e-aedf5ff37cbc'
SOURCE_PATH = 'pictographic-primitives/work/workflow coaching whistle_579de92e-a106-5aa9-b44e-aedf5ff37cbc.svg'
AUTHOR = 'gpt-6'


class Whistle(Solo48):
    icon_id = 'whistle'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/work"
    aliases = ()
    keywords = ('whistle', 'coach', 'sport', 'sound', 'referee', 'signal')

    def build(self) -> None:
        self.add_line('mouth-top', (6, 8), (28, 8))
        self.add_arc('body-right', (28, 8), (28, 40), radius_x=16, radius_y=16, sweep=True, large_arc=False)
        self.add_arc('body-bottom', (28, 40), (12, 24), radius_x=16, radius_y=16, sweep=True, large_arc=False)
        self.add_polyline('mouth', (12, 24), (12, 20), (6, 16), (6, 8), closed=False)
        self.relate("connect", 'mouth-top', 'body-right')
        self.relate("connect", 'body-right', 'body-bottom')
        self.relate("connect", 'body-bottom', 'mouth')
        self.relate("connect", 'mouth', 'mouth-top')
        self.add_arc('opening-top', (22, 24), (34, 24), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('opening-bottom', (34, 24), (22, 24), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_contour('opening', 'opening-top', 'opening-bottom', closed=True)
