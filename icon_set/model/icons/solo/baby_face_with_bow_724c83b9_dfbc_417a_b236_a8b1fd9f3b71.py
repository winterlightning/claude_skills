"""A smiling baby face with two crossing ribbon loops without a knot. Lucide baby informs ear bumps and sparse facial detail."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '724c83b9-dfbc-417a-b236-a8b1fd9f3b71'
SOURCE_PATH = 'pictographic-primitives/babies/baby girl_724c83b9-dfbc-417a-b236-a8b1fd9f3b71.svg'
AUTHOR = 'gpt-6'


class BabyFaceWithBow(Solo48):
    icon_id = 'baby-face-with-bow'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/babies"
    aliases = ()
    keywords = ('baby', 'face', 'with', 'bow', 'infant', 'nursery')

    def build(self) -> None:
        # Centerline extremes: (2,2)-(46,46).
        self.add_arc('temple-right', (36, 14), (40, 24), radius_x=14, radius_y=14, sweep=True, large_arc=False)
        self.add_arc('ear-right', (40, 24), (40, 32), radius_x=6, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('chin-right', (40, 32), (24, 46), radius_x=16, radius_y=14, sweep=True, large_arc=False)
        self.add_arc('chin-left', (24, 46), (8, 32), radius_x=16, radius_y=14, sweep=True, large_arc=False)
        self.add_arc('ear-left', (8, 32), (8, 24), radius_x=6, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('temple-left', (8, 24), (12, 14), radius_x=14, radius_y=14, sweep=True, large_arc=False)
        self.add_contour('face', 'temple-right', 'ear-right', 'chin-right', 'chin-left', 'ear-left', 'temple-left', closed=False)
        self.add_arc('eye-left', (14, 26), (20, 26), radius_x=4, radius_y=2, sweep=False, large_arc=False)
        self.add_arc('eye-right', (28, 26), (34, 26), radius_x=4, radius_y=2, sweep=False, large_arc=False)
        self.add_arc('smile', (20, 36), (28, 36), radius_x=6, radius_y=3, sweep=False, large_arc=False)
        self.add_line('bow-cross-down', (12, 2), (36, 14))
        self.add_arc('bow-right-end', (36, 14), (36, 2), radius_x=6, radius_y=6, sweep=False, large_arc=False)
        self.add_line('bow-cross-up', (36, 2), (12, 14))
        self.add_arc('bow-left-end', (12, 14), (12, 2), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_contour('bow', 'bow-cross-down', 'bow-right-end', 'bow-cross-up', 'bow-left-end', closed=True)
        self.relate("connect", 'face', 'bow')
