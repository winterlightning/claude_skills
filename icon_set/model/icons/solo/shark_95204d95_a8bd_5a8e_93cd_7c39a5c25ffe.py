"""shark: HRECT_L ink (0,6)-(48,42). Left-swimming profile, dorsal, pectoral and fork tail; minor lower fin omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '95204d95-a8bd-5a8e-93cd-7c39a5c25ffe'
SOURCE_PATH = 'pictographic-primitives/animals/shark_95204d95-a8bd-5a8e-93cd-7c39a5c25ffe.svg'
AUTHOR = 'gpt-6'


class Shark(Solo48):
    icon_id = 'shark'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/marine"
    aliases = ()
    keywords = ('shark', 'fish', 'fin', 'sea', 'ocean', 'predator', 'swim', 'marine')

    def build(self) -> None:
        self.add_arc('body-1', (2, 25), (19, 17), radius_x=30, radius_y=24, sweep=True)
        self.add_arc('body-2', (19, 17), (27, 8), radius_x=16, radius_y=16, sweep=True)
        self.add_line('body-3', (27, 8), (27, 18))
        self.add_arc('body-4', (27, 18), (38, 22), radius_x=36, radius_y=28, sweep=True)
        self.add_arc('body-5', (38, 22), (46, 14), radius_x=20, radius_y=20, sweep=True)
        self.add_arc('body-6', (46, 14), (46, 36), radius_x=32, radius_y=32, sweep=False)
        self.add_arc('body-7', (46, 36), (38, 29), radius_x=20, radius_y=20, sweep=True)
        self.add_arc('body-8', (38, 29), (26, 33), radius_x=36, radius_y=28, sweep=True)
        self.add_line('body-9', (26, 33), (26, 40))
        self.add_line('body-10', (26, 40), (19, 32))
        self.add_arc('body-11', (19, 32), (2, 25), radius_x=30, radius_y=24, sweep=True)
        self.add_contour('body', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', 'body-7', 'body-8', 'body-9', 'body-10', 'body-11', closed=True)
        self.add_arc('gill-1', (19, 25), (19, 32), radius_x=10, radius_y=10, sweep=True)
        self.add_contour('gill', 'gill-1', closed=False)
        self.relate("connect", 'body', 'gill')
