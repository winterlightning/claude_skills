"""Two scalloped blossoms on angled stems in a rounded vase; tiny twig omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '17b4e4f0-64b5-500d-a432-783026ce580b'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-02/decoration cherry blossom vase_17b4e4f0-64b5-500d-a432-783026ce580b.svg'
AUTHOR = 'gpt-6'

class TwoBlossomVase(Solo48):
    icon_id = 'two-blossom-vase'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/decoration"
    aliases = ()
    keywords = ('vase', 'blossom', 'flowers', 'stems', 'cherry', 'bouquet', 'decor')

    def build(self) -> None:
        # VRECT_XL: exact SOLO48 extremes; geometry authored on the integer grid.
        self.add_arc('left0', (8, 7), (14, 7), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('left1', (14, 7), (14, 13), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('left2', (14, 13), (8, 13), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('left3', (8, 13), (8, 7), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('left', 'left0', 'left1', 'left2', 'left3', closed=True)
        self.add_arc('right0', (34, 5), (40, 5), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('right1', (40, 5), (40, 11), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('right2', (40, 11), (34, 11), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('right3', (34, 11), (34, 5), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('right', 'right0', 'right1', 'right2', 'right3', closed=True)
        self.add_line('left-stem', (11, 16), (24, 30))
        self.add_line('right-stem', (37, 14), (24, 30))
        self.relate('connect', 'left', 'left-stem')
        self.relate('connect', 'right', 'right-stem')
        self.relate('connect', 'left-stem', 'right-stem')
        self.add_line('vase-1', (24, 30), (32, 30))
        self.add_line('vase-2', (32, 30), (32, 38))
        self.add_arc('base', (32, 38), (16, 38), radius_x=8, radius_y=8, sweep=True)
        self.add_line('side', (16, 38), (16, 30))
        self.add_line('lip', (16, 30), (24, 30))
        self.add_contour('pot', 'vase-1', 'vase-2', 'base', 'side', 'lip', closed=True)
        self.relate('connect', 'left-stem', 'pot')
        self.relate('connect', 'right-stem', 'pot')
