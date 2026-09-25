"""A curled rat with round ear, pointed face and wrapping tail. Extrema (6,6)-(42,42). Lucide rat informs round ear and eye; whisker and tiny paws omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1f6d0811-0adb-4d0f-bbe8-0474f1122591'
SOURCE_PATH = 'pictographic-primitives/animals/rat curve_1f6d0811-0adb-4d0f-bbe8-0474f1122591.svg'
AUTHOR = 'gpt-6'


class CurledRat(Solo48):
    icon_id = 'curled-rat'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals'
    aliases = ()
    keywords = ('rat', 'mouse', 'curled', 'rodent', 'tail', 'animal', 'round', 'zodiac')

    def build(self) -> None:
        # A curled rat with round ear, pointed face and wrapping tail. Extrema (6,6)-(42,42). Lucide rat informs round ear and eye; whisker and tiny paws omitted.
        self.add_arc('ear-top', (12, 8), (6, 14), radius_x=7, radius_y=7, sweep=False)
        self.add_bezier('ear-bottom', (6, 14), *(((6, 17.2325716), (7.16125546, 20.39737339), (10, 22)),))
        self.add_line('neck', (10, 22), (10, 26))
        self.add_bezier('body-left', (10, 26), *(((11.92947252, 35.46246434), (20.34478473, 42), (30, 42)),))
        self.add_arc('body-right', (30, 42), (42, 25), radius_x=16, radius_y=21, sweep=False)
        self.add_bezier('tail-rise', (42, 25), *(((42, 19.4561661), (41.75220913, 13.64440026), (40, 10)),))
        self.add_contour('body', 'ear-top', 'ear-bottom', 'neck', 'body-left', 'body-right', 'tail-rise')
        self.add_bezier('brow', (12, 8), *(((16.85920035, 6.24779087), (24.60822146, 6), (32, 6)),))
        self.add_line('nose', (32, 6), (32, 10))
        self.add_arc('face', (32, 10), (22, 20), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('chest', (22, 20), (29, 32), radius_x=20, radius_y=20, sweep=False)
        self.add_contour('head', 'brow', 'nose', 'face', 'chest')
        self.relate("connect", 'head', 'body')
        self.add_arc('haunch', (29, 32), (38, 28), radius_x=10, radius_y=10, sweep=True)
        self.relate("connect", 'head', 'haunch')
