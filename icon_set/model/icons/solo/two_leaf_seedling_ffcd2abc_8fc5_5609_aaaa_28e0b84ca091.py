"""Two pointed leaves rise from a rimmed pot. VRECT_XL (5,2)-(43,46). Lucide sprout informs coherent leaf arcs; taller right leaf preserves natural asymmetry. Rim reduced to one broad line."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ffcd2abc-8fc5-5609-aaaa-28e0b84ca091'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-04/indoor plant_ffcd2abc-8fc5-5609-aaaa-28e0b84ca091.svg'
AUTHOR = 'gpt-6'


class TwoLeafSeedling(Solo48):
    icon_id = 'two-leaf-seedling-in-rimmed-pot'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/decoration"
    aliases = ()
    keywords = ('seedling', 'plant', 'leaves', 'pot', 'sprout', 'growth', 'garden')

    def build(self) -> None:
        self.add_arc('left-top', (5, 9), (23, 23), radius_x=18, radius_y=14, sweep=True, large_arc=False)
        self.add_arc('left-bottom', (23, 23), (5, 9), radius_x=18, radius_y=14, sweep=True, large_arc=False)
        self.add_contour('left-leaf', 'left-top', 'left-bottom', closed=True)
        self.add_arc('right-top', (23, 23), (43, 2), radius_x=20, radius_y=21, sweep=True, large_arc=False)
        self.add_arc('right-bottom', (43, 2), (23, 23), radius_x=20, radius_y=21, sweep=True, large_arc=False)
        self.add_contour('right-leaf', 'right-top', 'right-bottom', closed=True)
        self.relate('connect', 'left-leaf', 'right-leaf')
        self.add_line('stem', (23, 23), (23, 32))
        self.relate('connect', 'stem', 'left-leaf')
        self.relate('connect', 'stem', 'right-leaf')
        self.add_line('pot-top', (9, 32), (39, 32))
        self.add_line('pot-r', (39, 32), (37, 43))
        self.add_arc('pot-br', (37, 43), (34, 46), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_line('pot-b', (34, 46), (14, 46))
        self.add_arc('pot-bl', (14, 46), (11, 43), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_line('pot-l', (11, 43), (9, 32))
        self.add_contour('pot', 'pot-top', 'pot-r', 'pot-br', 'pot-b', 'pot-bl', 'pot-l', closed=True)
        self.relate('connect', 'stem', 'pot')
        self.add_line('rim-left', (5, 32), (9, 32))
        self.add_line('rim-right', (39, 32), (43, 32))
        self.relate('connect', 'rim-left', 'pot')
        self.relate('connect', 'rim-right', 'pot')
