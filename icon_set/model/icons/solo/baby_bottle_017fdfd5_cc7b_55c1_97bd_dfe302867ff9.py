from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '017fdfd5-cc7b-55c1-97bd-dfe302867ff9'
SOURCE_PATH = 'pictographic-primitives/babies/baby care bottle_017fdfd5-cc7b-55c1-97bd-dfe302867ff9.svg'
AUTHOR = 'gpt-6'

class BabyBottle(Solo48):
    icon_id = 'baby-bottle'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/baby-care"
    aliases = ()
    keywords = ('bottle', 'baby', 'milk', 'feeding', 'teat', 'infant', 'formula', 'nursing')

    # Designed to centerline extremes (11, 2)–(37, 46).
    def build(self) -> None:
        self.add_line('body-1', (11, 18), (11, 39))
        self.add_arc('body-2', (11, 39), (18, 46), radius_x=7, radius_y=7, sweep=False)
        self.add_line('body-3', (18, 46), (30, 46))
        self.add_arc('body-4', (30, 46), (37, 39), radius_x=7, radius_y=7, sweep=False)
        self.add_line('body-5', (37, 39), (37, 18))
        self.add_line('body-6', (37, 18), (11, 18))
        self.add_contour('body', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', closed=True)
        self.add_line('teat-1', (16, 18), (16, 12))
        self.add_arc('teat-2', (16, 12), (20, 8), radius_x=4, radius_y=4, sweep=True)
        self.add_line('teat-3', (20, 8), (20, 6))
        self.add_arc('teat-4', (20, 6), (28, 6), radius_x=4, radius_y=4, sweep=True)
        self.add_line('teat-5', (28, 6), (28, 8))
        self.add_arc('teat-6', (28, 8), (32, 12), radius_x=4, radius_y=4, sweep=True)
        self.add_line('teat-7', (32, 12), (32, 18))
        self.add_contour('teat', 'teat-1', 'teat-2', 'teat-3', 'teat-4', 'teat-5', 'teat-6', 'teat-7', closed=False)
        self.relate("connect", "body", "teat")
