# Review candidate; original preserved.
"""Unequal hanging stems carry a leaf and a downward-facing flower; tiny lower petal omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '76e15d0e-0c43-40b6-ba38-ae2903117c14'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-02/hanging flowers_76e15d0e-0c43-40b6-ba38-ae2903117c14.svg'
AUTHOR = 'gpt-6'

class HangingFlowerPair(Solo48):
    icon_id = 'hanging-flower-pair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'decoration'
    categories = ('primitives', 'decoration')
    aliases = ()
    keywords = ('flower', 'hanging', 'petals', 'stem', 'leaf', 'botanical', 'decor')

    def build(self) -> None:
        """Opening repair: Broadened the hanging leaf while retaining the separate flower and unequal stems."""
        self.add_line('left-stem', (16, 6), (16, 31))
        self.add_bezier('leaf-a',(16,31),((16,37),(12,42),(6,42)))
        self.add_bezier('leaf-b',(6,42),((6,35),(10,31),(16,31)))
        self.add_contour('leaf', 'leaf-a', 'leaf-b', closed=True)
        self.relate('connect', 'left-stem', 'leaf')
        self.add_line('right-stem', (35, 8), (35, 24))
        self.add_arc('flower-a', (27, 32), (35, 24), radius_x=8, radius_y=8, sweep=True)
        self.add_bezier('flower-b', (35, 24), *(((39.02383141, 24.50682851), (42, 27.9444996), (42, 32)),))
        self.add_arc('flower-c', (42, 32), (35, 32), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('flower-d', (35, 32), (27, 32), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('flower', 'flower-a', 'flower-b', 'flower-c', 'flower-d', closed=True)
        self.relate('connect', 'flower', 'right-stem')
