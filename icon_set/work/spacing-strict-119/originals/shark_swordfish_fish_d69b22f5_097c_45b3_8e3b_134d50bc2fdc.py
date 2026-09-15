"""leaping-swordfish: SQUARE ink (6,6)-(42,42). Rising billfish with forked tail; droplets reduced to two strokes."""
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
        self.add_arc('body-1', (6, 22), (17, 11), radius_x=34, radius_y=28, sweep=True)
        self.add_line('body-2', (17, 11), (30, 7))
        self.add_arc('body-3', (30, 7), (20, 27), radius_x=20, radius_y=20, sweep=True)
        self.add_bezier('body-4',(20,27),((18,30),(17,33),(18,36)))
        self.add_line('body-5',(18,36),(27,32))
        self.add_bezier('body-6',(27,32),((26,35),(26,39),(27,42)))
        self.add_line('body-7', (27, 42), (19, 42))
        self.add_arc('body-8', (19, 42), (6, 29), radius_x=17, radius_y=15, sweep=True)
        self.add_bezier('body-9', (6, 29), *(((6, 26.69932107), (6, 24.30067893), (6, 22)),))
        self.add_contour('body', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', 'body-7', 'body-8', 'body-9', closed=True)
        self.add_line('bill-1', (30, 7), (42, 6))
        self.add_contour('bill', 'bill-1', closed=False)
        self.add_line('dorsal-1', (6, 22), (7, 6))
        self.add_arc('dorsal-2', (7, 6), (17, 11), radius_x=22, radius_y=22, sweep=True)
        self.add_contour('dorsal', 'dorsal-1', 'dorsal-2', closed=False)
        self.add_line('splash-top-1', (39, 25), (36, 29))
        self.add_contour('splash-top', 'splash-top-1', closed=False)
        self.add_line('splash-low-1', (38, 38), (42, 35))
        self.add_contour('splash-low', 'splash-low-1', closed=False)
        self.relate("connect", 'body', 'dorsal')
        self.relate("connect", 'body', 'bill')
