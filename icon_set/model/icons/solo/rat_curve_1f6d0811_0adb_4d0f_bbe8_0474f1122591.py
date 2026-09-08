"""A curled rat with round ear, pointed face and wrapping tail. Extrema (2,2)-(46,46). Lucide rat informs round ear and eye; whisker and tiny paws omitted."""
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
    category = 'animals/wildlife'
    aliases = ()
    keywords = ('rat', 'mouse', 'curled', 'rodent', 'tail', 'animal', 'round', 'zodiac')

    def build(self) -> None:
        # A curled rat with round ear, pointed face and wrapping tail. Extrema (2,2)-(46,46). Lucide rat informs round ear and eye; whisker and tiny paws omitted.
        self.add_arc('ear-top', (12, 8), (2, 14), radius_x=7, radius_y=7, sweep=False)
        self.add_arc('ear-bottom', (2, 14), (10, 22), radius_x=8, radius_y=8, sweep=False)
        self.add_line('neck', (10, 22), (10, 26))
        self.add_arc('body-left', (10, 26), (30, 46), radius_x=20, radius_y=20, sweep=False)
        self.add_arc('body-right', (30, 46), (46, 25), radius_x=16, radius_y=21, sweep=False)
        self.add_arc('tail-rise', (46, 25), (40, 10), radius_x=6, radius_y=15, sweep=False)
        self.add_contour('body', 'ear-top', 'ear-bottom', 'neck', 'body-left', 'body-right', 'tail-rise')
        self.add_arc('brow', (12, 8), (32, 2), radius_x=20, radius_y=6, sweep=True)
        self.add_line('nose', (32, 2), (32, 10))
        self.add_arc('face', (32, 10), (22, 20), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('chest', (22, 20), (29, 32), radius_x=20, radius_y=20, sweep=False)
        self.add_contour('head', 'brow', 'nose', 'face', 'chest')
        self.relate("connect", 'head', 'body')
        self.add_dot('eye', (22, 10))
        self.add_arc('haunch', (29, 32), (38, 28), radius_x=10, radius_y=10, sweep=True)
        self.relate("connect", 'head', 'haunch')
