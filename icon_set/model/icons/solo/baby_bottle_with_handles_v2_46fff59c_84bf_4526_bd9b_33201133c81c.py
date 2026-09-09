"""Diagonal handled baby bottle: teat meets both body corners. SQUARE (2,2)-(46,46). Preserves handles, tilt and nipple; no detail omitted. No additional useful Lucide match."""
# Variant of baby-bottle-with-handles; parent file remains unchanged.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '46fff59c-84bf-4526-bd9b-33201133c81c'
SOURCE_PATH = 'pictographic-primitives/babies/milk bottle handle_46fff59c-84bf-4526-bd9b-33201133c81c.svg'
AUTHOR = 'gpt-6'

class BabyBottleWithHandlesVariant2(Solo48):
    icon_id = 'baby-bottle-with-handles-v2'
    variant_of = 'baby-bottle-with-handles'
    variant_label = 'Join teat to body corners'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/baby-care'
    aliases = ()
    keywords = ('bottle', 'handles', 'baby', 'milk', 'feeding', 'sippy', 'teat', 'infant')

    def build(self) -> None:
        self.add_arc('bottle-1', (2, 34), (14, 46), radius_x=12, radius_y=12, sweep=False)
        self.add_arc('bottle-2', (14, 46), (22, 42), radius_x=10, radius_y=10, sweep=False)
        self.add_line('bottle-3', (22, 42), (38, 26))
        self.add_line('bottle-4', (38, 26), (22, 10))
        self.add_line('bottle-5', (22, 10), (6, 26))
        self.add_arc('bottle-6', (6, 26), (2, 34), radius_x=10, radius_y=10, sweep=False)
        self.add_contour('bottle', 'bottle-1', 'bottle-2', 'bottle-3', 'bottle-4', 'bottle-5', 'bottle-6', closed=True)
        self.add_line('teat-1', (22, 10), (34, 6))
        self.add_arc('teat-2', (34, 6), (40, 2), radius_x=6, radius_y=4, sweep=True)
        self.add_arc('teat-3', (40, 2), (46, 8), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('teat-4', (46, 8), (42, 14), radius_x=4, radius_y=6, sweep=True)
        self.add_line('teat-5', (42, 14), (38, 26))
        self.add_contour('teat', 'teat-1', 'teat-2', 'teat-3', 'teat-4', 'teat-5', closed=False)
        self.add_arc('handle-left-1', (8, 24), (20, 12), radius_x=9, radius_y=9, large_arc=True, sweep=True)
        self.add_contour('handle-left', 'handle-left-1', closed=False)
        self.add_arc('handle-right-1', (36, 28), (24, 40), radius_x=9, radius_y=9, large_arc=True, sweep=True)
        self.add_contour('handle-right', 'handle-right-1', closed=False)
        self.relate('connect', 'bottle', 'teat')
        self.relate('connect', 'bottle', 'handle-left')
        self.relate('connect', 'bottle', 'handle-right')
