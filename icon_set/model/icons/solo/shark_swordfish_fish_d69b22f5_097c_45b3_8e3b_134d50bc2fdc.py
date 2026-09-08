"""leaping-swordfish: SQUARE ink (0,0)-(48,48). Rising billfish with forked tail; droplets reduced to two strokes."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd69b22f5-097c-45b3-8e3b-134d50bc2fdc'
SOURCE_PATH = 'pictographic-primitives/animals/shark swordfish fish_d69b22f5-097c-45b3-8e3b-134d50bc2fdc.svg'
AUTHOR = 'gpt-6'


class LeapingSwordfish(Solo48):
    icon_id = 'leaping-swordfish'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/marine"
    aliases = ()
    keywords = ('swordfish', 'marlin', 'jump', 'leap', 'droplets', 'sea', 'fishing', 'sport')

    def build(self) -> None:
        self.add_arc('body-1', (5, 22), (17, 11), radius_x=34, radius_y=28, sweep=True)
        self.add_line('body-2', (17, 11), (30, 7))
        self.add_arc('body-3', (30, 7), (20, 27), radius_x=20, radius_y=20, sweep=True)
        self.add_arc('body-4', (20, 27), (19, 38), radius_x=10, radius_y=10, sweep=False)
        self.add_line('body-5', (19, 38), (27, 34))
        self.add_arc('body-6', (27, 34), (27, 46), radius_x=22, radius_y=22, sweep=False)
        self.add_line('body-7', (27, 46), (19, 42))
        self.add_arc('body-8', (19, 42), (2, 29), radius_x=17, radius_y=15, sweep=True)
        self.add_arc('body-9', (2, 29), (5, 22), radius_x=17, radius_y=15, sweep=True)
        self.add_contour('body', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', 'body-7', 'body-8', 'body-9', closed=True)
        self.add_line('bill-1', (30, 7), (46, 2))
        self.add_contour('bill', 'bill-1', closed=False)
        self.add_line('dorsal-1', (5, 22), (7, 4))
        self.add_arc('dorsal-2', (7, 4), (17, 11), radius_x=22, radius_y=22, sweep=True)
        self.add_contour('dorsal', 'dorsal-1', 'dorsal-2', closed=False)
        self.add_line('splash-top-1', (39, 25), (36, 29))
        self.add_contour('splash-top', 'splash-top-1', closed=False)
        self.add_line('splash-low-1', (38, 38), (43, 35))
        self.add_contour('splash-low', 'splash-low-1', closed=False)
        self.relate("connect", 'body', 'dorsal')
        self.relate("connect", 'body', 'bill')
