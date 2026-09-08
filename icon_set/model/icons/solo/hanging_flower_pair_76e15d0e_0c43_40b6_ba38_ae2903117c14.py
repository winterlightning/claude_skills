"""Unequal hanging stems carry a leaf and a downward-facing flower; tiny lower petal omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '76e15d0e-0c43-40b6-ba38-ae2903117c14'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-02/hanging flowers_76e15d0e-0c43-40b6-ba38-ae2903117c14.svg'
AUTHOR = 'gpt-6'

class HangingFlowerPair(Solo48):
    icon_id = 'hanging-flower-pair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/decoration"
    aliases = ()
    keywords = ('flower', 'hanging', 'petals', 'stem', 'leaf', 'botanical', 'decor')

    def build(self) -> None:
        # VRECT_XL: exact SOLO48 extremes; geometry authored on the integer grid.
        self.add_line('left-stem', (16, 2), (16, 28))
        self.add_arc('leaf-a', (16, 28), (5, 39), radius_x=11, radius_y=11, sweep=True)
        self.add_arc('leaf-b', (5, 39), (16, 28), radius_x=11, radius_y=11, sweep=True)
        self.add_contour('leaf', 'leaf-a', 'leaf-b', closed=True)
        self.relate('connect', 'left-stem', 'leaf')
        self.add_arc('tail-a', (16, 28), (19, 31), radius_x=3, radius_y=3, sweep=True)
        self.add_line('tail-b', (19, 31), (19, 46))
        self.add_contour('tail', 'tail-a', 'tail-b')
        self.relate('connect', 'tail', 'leaf')
        self.relate('connect', 'tail', 'left-stem')
        self.add_line('right-stem', (35, 8), (35, 24))
        self.add_arc('flower-a', (27, 32), (35, 24), radius_x=8, radius_y=8, sweep=True)
        self.add_arc('flower-b', (35, 24), (43, 32), radius_x=8, radius_y=8, sweep=True)
        self.add_arc('flower-c', (43, 32), (35, 32), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('flower-d', (35, 32), (27, 32), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('flower', 'flower-a', 'flower-b', 'flower-c', 'flower-d', closed=True)
        self.relate('connect', 'flower', 'right-stem')
