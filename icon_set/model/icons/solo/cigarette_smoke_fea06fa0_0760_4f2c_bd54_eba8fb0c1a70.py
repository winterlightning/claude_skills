"""Horizontal cigarette with right filter and left smoke trail. Lucide cigarette informs the rectangular body, divider and separate smoke. One coherent smoke trail retained.

SOLO48 HRECT_L; live visible envelope (2, 6, 46, 42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fea06fa0-0760-4f2c-bd54-eba8fb0c1a70'
SOURCE_PATH = 'pictographic-primitives/symbol/smoking_fea06fa0-0760-4f2c-bd54-eba8fb0c1a70.svg'
AUTHOR = 'gpt-6'


class CigaretteSmoke(Solo48):
    icon_id = 'cigarette-smoke'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol",)
    aliases = ()
    keywords = ('smoking', 'cigarette', 'smoke', 'tobacco', 'area', 'nicotine', 'habit', 'lounge')

    def build(self) -> None:

        self.add_polyline('body',(4,30),(32,30),(44,30),(44,40),(32,40),(4,40),closed=True)
        self.add_line('filter',(32,30),(32,40))
        self.relate('connect','body','filter')
        self.add_line('smoke-rise',(4,20),(4,18))
        self.add_arc('smoke-lower-turn',(4,18),(10,12),radius_x=6)
        self.add_line('smoke-middle',(10,12),(18,12))
        self.add_arc('smoke-upper-turn',(18,12),(22,8),radius_x=4,sweep=False)
        self.add_contour('smoke','smoke-rise','smoke-lower-turn','smoke-middle','smoke-upper-turn')
