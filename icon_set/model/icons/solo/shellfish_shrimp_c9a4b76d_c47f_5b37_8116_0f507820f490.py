from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c9a4b76d-c47f-5b37-8116-0f507820f490'
SOURCE_PATH = 'pictographic-primitives/animals/shellfish shrimp_c9a4b76d-c47f-5b37-8116-0f507820f490.svg'
AUTHOR = 'gpt-6'


class Shrimp(Solo48):
    icon_id = 'shrimp'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/marine"
    aliases = ()
    keywords = ('shrimp', 'prawn', 'shellfish', 'seafood', 'sea', 'marine', 'curl', 'food')

    def build(self) -> None:
        self.add_line('head-top', (8, 14), (27, 14))
        self.add_arc('back', (27, 14), (46, 33), radius_x=19, radius_y=19, sweep=True, large_arc=False)
        self.add_arc('rump', (46, 33), (30, 46), radius_x=16, radius_y=13, sweep=True, large_arc=False)
        self.add_line('tail-base', (30, 46), (6, 46))
        self.add_line('tail-fan-1', (6, 46), (2, 41))
        self.add_line('tail-fan-2', (2, 41), (10, 37))
        self.add_line('tail-fan-3', (10, 37), (10, 30))
        self.add_arc('tail-curve', (10, 30), (16, 40), radius_x=6, radius_y=10, sweep=True, large_arc=False)
        self.add_line('inner-bottom', (16, 40), (28, 40))
        self.add_arc('inner-body', (28, 40), (28, 26), radius_x=8, radius_y=7, sweep=False, large_arc=False)
        self.add_line('chin', (28, 26), (20, 26))
        self.add_arc('head-front', (20, 26), (8, 14), radius_x=12, radius_y=12, sweep=True, large_arc=False)
        self.add_contour('outline', 'head-top', 'back', 'rump', 'tail-base', 'tail-fan-1', 'tail-fan-2', 'tail-fan-3', 'tail-curve', 'inner-bottom', 'inner-body', 'chin', 'head-front', closed=True)
        self.add_arc('antenna-curl', (14, 14), (14, 2), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_line('antenna', (14, 2), (32, 2))
        self.add_contour('antenna-shape', 'antenna-curl', 'antenna', closed=False)
        self.relate("connect", 'antenna-shape', 'outline')
        self.add_line('segment', (34, 28), (44, 25))
        self.relate("connect", 'segment', 'outline')
