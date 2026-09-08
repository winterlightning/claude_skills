"""leaping-hammerhead: SQUARE ink (0,0)-(48,48). Intentional arcing pose and flat hammer head, two splash strokes."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '81d0c757-f2c2-5412-a942-65c0af7e738d'
SOURCE_PATH = 'pictographic-primitives/animals/shark hammer fish_81d0c757-f2c2-5412-a942-65c0af7e738d.svg'
AUTHOR = 'gpt-6'


class LeapingHammerhead(Solo48):
    icon_id = 'leaping-hammerhead'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/marine"
    aliases = ()
    keywords = ('hammerhead', 'shark', 'jump', 'leap', 'sea', 'splash', 'ocean', 'marine')

    def build(self) -> None:
        self.add_arc('body-1', (7, 21), (24, 2), radius_x=24, radius_y=24, sweep=True)
        self.add_line('body-2', (24, 2), (30, 7))
        self.add_line('body-3', (30, 7), (24, 10))
        self.add_arc('body-4', (24, 10), (36, 19), radius_x=32, radius_y=26, sweep=True)
        self.add_line('body-5', (36, 19), (46, 13))
        self.add_line('body-6', (46, 13), (40, 25))
        self.add_arc('body-7', (40, 25), (28, 44), radius_x=17, radius_y=17, sweep=True)
        self.add_line('body-8', (28, 44), (21, 46))
        self.add_line('body-9', (21, 46), (23, 37))
        self.add_line('body-10', (23, 37), (30, 39))
        self.add_arc('body-11', (30, 39), (33, 30), radius_x=6, radius_y=7, sweep=False)
        self.add_arc('body-12', (33, 30), (16, 16), radius_x=23, radius_y=23, sweep=True)
        self.add_line('body-13', (16, 16), (12, 25))
        self.add_line('body-14', (12, 25), (7, 21))
        self.add_contour('body', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', 'body-7', 'body-8', 'body-9', 'body-10', 'body-11', 'body-12', 'body-13', 'body-14', closed=True)
        self.add_line('splash-1', (2, 40), (8, 43))
        self.add_contour('splash', 'splash-1', closed=False)
        self.add_line('splash-high-1', (8, 33), (11, 36))
        self.add_contour('splash-high', 'splash-high-1', closed=False)
