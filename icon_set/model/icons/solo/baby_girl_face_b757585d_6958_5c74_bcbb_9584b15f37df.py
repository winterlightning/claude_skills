"""A smiling baby face with a centre knot between two bow loops. Lucide baby informs ear bumps and sparse facial detail."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b757585d-6958-5c74-bcbb-9584b15f37df'
SOURCE_PATH = 'pictographic-primitives/babies/baby girl_b757585d-6958-5c74-bcbb-9584b15f37df.svg'
AUTHOR = 'gpt-6'


class BabyGirlFace(Solo48):
    icon_id = 'baby-girl-face'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/babies"
    aliases = ()
    keywords = ('baby', 'girl', 'face', 'infant', 'nursery')

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
        self.add_arc('knot-top', (21, 8), (27, 8), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('knot-bottom', (27, 8), (21, 8), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_contour('knot', 'knot-top', 'knot-bottom', closed=True)
        self.add_line('bow-left-top', (21, 8), (12, 2))
        self.add_arc('bow-left-end', (12, 2), (12, 14), radius_x=6, radius_y=6, sweep=False, large_arc=False)
        self.add_line('bow-left-bottom', (12, 14), (21, 8))
        self.add_contour('bow-left', 'bow-left-top', 'bow-left-end', 'bow-left-bottom', closed=True)
        self.add_line('bow-right-top', (27, 8), (36, 2))
        self.add_arc('bow-right-end', (36, 2), (36, 14), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_line('bow-right-bottom', (36, 14), (27, 8))
        self.add_contour('bow-right', 'bow-right-top', 'bow-right-end', 'bow-right-bottom', closed=True)
        self.relate("connect", 'knot', 'bow-left')
        self.relate("connect", 'knot', 'bow-right')
        self.relate("connect", 'face', 'bow-left')
        self.relate("connect", 'face', 'bow-right')
