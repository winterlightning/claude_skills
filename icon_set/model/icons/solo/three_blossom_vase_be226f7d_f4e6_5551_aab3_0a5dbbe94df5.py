"""Three scalloped blossoms above a rounded vase; small side leaf omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'be226f7d-f4e6-5551-aab3-0a5dbbe94df5'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-02/decoration flower vase_be226f7d-f4e6-5551-aab3-0a5dbbe94df5.svg'
AUTHOR = 'gpt-6'

class ThreeBlossomVase(Solo48):
    icon_id = 'three-blossom-vase'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/decoration"
    aliases = ()
    keywords = ('vase', 'flowers', 'blossoms', 'bouquet', 'leaf', 'plant', 'decor')

    def build(self) -> None:
        # VRECT_XL: exact SOLO48 extremes; geometry authored on the integer grid.
        self.add_arc('left0', (8, 5), (14, 5), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('left1', (14, 5), (14, 11), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('left2', (14, 11), (8, 11), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('left3', (8, 11), (8, 5), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('left', 'left0', 'left1', 'left2', 'left3', closed=True)
        self.add_arc('right0', (34, 5), (40, 5), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('right1', (40, 5), (40, 11), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('right2', (40, 11), (34, 11), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('right3', (34, 11), (34, 5), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('right', 'right0', 'right1', 'right2', 'right3', closed=True)
        self.add_arc('front0', (21, 23), (27, 23), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('front1', (27, 23), (27, 29), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('front2', (27, 29), (21, 29), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('front3', (21, 29), (21, 23), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('front', 'front0', 'front1', 'front2', 'front3', closed=True)
        self.add_line('left-stem', (11, 14), (21, 23))
        self.add_line('right-stem', (37, 14), (27, 23))
        self.relate('connect', 'left-stem', 'left')
        self.relate('connect', 'left-stem', 'front')
        self.relate('connect', 'right-stem', 'right')
        self.relate('connect', 'right-stem', 'front')
        self.add_line('pot-top-1', (24, 32), (34, 32))
        self.add_line('pot-top-2', (34, 32), (34, 40))
        self.add_arc('pot-r', (34, 40), (28, 46), radius_x=6, radius_y=6, sweep=True)
        self.add_line('pot-base', (28, 46), (20, 46))
        self.add_arc('pot-l', (20, 46), (14, 40), radius_x=6, radius_y=6, sweep=True)
        self.add_line('pot-side-1', (14, 40), (14, 32))
        self.add_line('pot-side-2', (14, 32), (24, 32))
        self.add_contour('pot', 'pot-top-1', 'pot-top-2', 'pot-r', 'pot-base', 'pot-l', 'pot-side-1', 'pot-side-2', closed=True)
        self.relate('connect', 'pot', 'front')
