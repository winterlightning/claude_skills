from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '41bb3775-67e6-5a7f-bc03-6922fe35a73f'
SOURCE_PATH = 'pictographic-primitives/animals/shellfish crab_41bb3775-67e6-5a7f-bc03-6922fe35a73f.svg'
AUTHOR = 'gpt-6'


class Crab(Solo48):
    icon_id = 'crab'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/marine"
    aliases = ()
    keywords = ('crab', 'claws', 'shellfish', 'sea', 'beach', 'seafood', 'cancer', 'marine')

    def build(self) -> None:
        self.add_arc('back', (12, 27), (36, 27), radius_x=12, radius_y=7, sweep=True, large_arc=False)
        self.add_arc('belly', (36, 27), (12, 27), radius_x=12, radius_y=13, sweep=True, large_arc=False)
        self.add_contour('body', 'back', 'belly', closed=True)
        self.add_arc('left-claw', (6, 2), (12, 16), radius_x=6, radius_y=14, sweep=True, large_arc=False)
        self.add_line('left-pincer', (12, 16), (17, 7))
        self.add_contour('left-claw-shape', 'left-claw', 'left-pincer', closed=False)
        self.add_line('left-arm', (12, 27), (12, 16))
        self.relate("connect", 'left-arm', 'body')
        self.relate("connect", 'left-arm', 'left-claw-shape')
        self.add_line('left-leg-1', (13, 33), (2, 36))
        self.add_line('left-leg-2', (2, 36), (2, 40))
        self.add_contour('left-leg', 'left-leg-1', 'left-leg-2', closed=False)
        self.relate("connect", 'left-leg', 'body')
        self.add_line('left-foot', (18, 39), (10, 46))
        self.relate("connect", 'left-foot', 'body')
        self.add_arc('right-claw', (42, 2), (36, 16), radius_x=6, radius_y=14, sweep=False, large_arc=False)
        self.add_line('right-pincer', (36, 16), (31, 7))
        self.add_contour('right-claw-shape', 'right-claw', 'right-pincer', closed=False)
        self.add_line('right-arm', (36, 27), (36, 16))
        self.relate("connect", 'right-arm', 'body')
        self.relate("connect", 'right-arm', 'right-claw-shape')
        self.add_line('right-leg-1', (35, 33), (46, 36))
        self.add_line('right-leg-2', (46, 36), (46, 40))
        self.add_contour('right-leg', 'right-leg-1', 'right-leg-2', closed=False)
        self.relate("connect", 'right-leg', 'body')
        self.add_line('right-foot', (30, 39), (38, 46))
        self.relate("connect", 'right-foot', 'body')
