from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9a13b720-4d4a-4f90-a952-2dc87f3480fe'
SOURCE_PATH = 'pictographic-primitives/animals/shellfish lobster_9a13b720-4d4a-4f90-a952-2dc87f3480fe.svg'
AUTHOR = 'gpt-6'


class Lobster(Solo48):
    icon_id = 'lobster'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/marine"
    aliases = ()
    keywords = ('lobster', 'crayfish', 'shellfish', 'claws', 'seafood', 'sea', 'marine', 'antennae')

    def build(self) -> None:
        self.add_arc('body-top', (18, 26), (30, 26), radius_x=6, radius_y=12, sweep=True, large_arc=False)
        self.add_arc('body-bottom', (30, 26), (18, 26), radius_x=6, radius_y=12, sweep=True, large_arc=False)
        self.add_contour('body', 'body-top', 'body-bottom', closed=True)
        self.add_arc('left-antenna', (24, 14), (14, 2), radius_x=10, radius_y=12, sweep=False, large_arc=False)
        self.relate("connect", 'left-antenna', 'body')
        self.add_arc('left-claw-outer', (2, 13), (7, 29), radius_x=5, radius_y=16, sweep=True, large_arc=False)
        self.add_arc('left-claw-inner', (7, 29), (12, 13), radius_x=5, radius_y=16, sweep=True, large_arc=False)
        self.add_contour('left-claw', 'left-claw-outer', 'left-claw-inner', closed=False)
        self.add_line('left-arm', (7, 29), (18, 26))
        self.relate("connect", 'left-arm', 'left-claw')
        self.relate("connect", 'left-arm', 'body')
        self.add_line('left-tail-1', (24, 38), (14, 46))
        self.add_line('left-tail-2', (14, 46), (14, 38))
        self.add_contour('left-tail', 'left-tail-1', 'left-tail-2', closed=False)
        self.relate("connect", 'left-tail', 'body')
        self.add_arc('right-antenna', (24, 14), (34, 2), radius_x=10, radius_y=12, sweep=True, large_arc=False)
        self.relate("connect", 'right-antenna', 'body')
        self.add_arc('right-claw-outer', (46, 13), (41, 29), radius_x=5, radius_y=16, sweep=False, large_arc=False)
        self.add_arc('right-claw-inner', (41, 29), (36, 13), radius_x=5, radius_y=16, sweep=False, large_arc=False)
        self.add_contour('right-claw', 'right-claw-outer', 'right-claw-inner', closed=False)
        self.add_line('right-arm', (41, 29), (30, 26))
        self.relate("connect", 'right-arm', 'right-claw')
        self.relate("connect", 'right-arm', 'body')
        self.add_line('right-tail-1', (24, 38), (34, 46))
        self.add_line('right-tail-2', (34, 46), (34, 38))
        self.add_contour('right-tail', 'right-tail-1', 'right-tail-2', closed=False)
        self.relate("connect", 'right-tail', 'body')
