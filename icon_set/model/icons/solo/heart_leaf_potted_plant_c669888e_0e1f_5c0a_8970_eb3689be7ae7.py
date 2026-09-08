"""Three heart leaves in a tapered pot. SQUARE (2,2)-(46,46) accommodates spreading foliage. Lucide heart informs paired lobes. Leaf veins omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c669888e-0e1f-5c0a-8970-eb3689be7ae7'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-04/indoor plant_c669888e-0e1f-5c0a-8970-eb3689be7ae7.svg'
AUTHOR = 'gpt-6'


class HeartLeafPottedPlant(Solo48):
    icon_id = 'heart-leaf-potted-plant'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/decoration"
    aliases = ()
    keywords = ('plant', 'heart', 'leaves', 'pot', 'stems', 'foliage', 'decor')

    def build(self) -> None:
        self.add_arc('left-a', (10, 18), (2, 18), radius_x=4, radius_y=4, sweep=False, large_arc=False)
        self.add_line('left-b', (2, 18), (10, 28))
        self.add_line('left-c', (10, 28), (18, 18))
        self.add_arc('left-d', (18, 18), (10, 18), radius_x=4, radius_y=4, sweep=False, large_arc=False)
        self.add_contour('left', 'left-a', 'left-b', 'left-c', 'left-d', closed=True)
        self.add_line('left-stem', (10, 28), (10, 34))
        self.relate('connect', 'left', 'left-stem')
        self.add_arc('centre-a', (24, 6), (16, 6), radius_x=4, radius_y=4, sweep=False, large_arc=False)
        self.add_line('centre-b', (16, 6), (24, 16))
        self.add_line('centre-c', (24, 16), (32, 6))
        self.add_arc('centre-d', (32, 6), (24, 6), radius_x=4, radius_y=4, sweep=False, large_arc=False)
        self.add_contour('centre', 'centre-a', 'centre-b', 'centre-c', 'centre-d', closed=True)
        self.add_line('centre-stem', (24, 16), (24, 34))
        self.relate('connect', 'centre', 'centre-stem')
        self.add_arc('right-a', (38, 18), (30, 18), radius_x=4, radius_y=4, sweep=False, large_arc=False)
        self.add_line('right-b', (30, 18), (38, 28))
        self.add_line('right-c', (38, 28), (46, 18))
        self.add_arc('right-d', (46, 18), (38, 18), radius_x=4, radius_y=4, sweep=False, large_arc=False)
        self.add_contour('right', 'right-a', 'right-b', 'right-c', 'right-d', closed=True)
        self.add_line('right-stem', (38, 28), (38, 34))
        self.relate('connect', 'right', 'right-stem')
        self.add_line('pot-top', (7, 34), (41, 34))
        self.add_line('pot-r', (41, 34), (39, 43))
        self.add_arc('pot-br', (39, 43), (36, 46), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_line('pot-b', (36, 46), (12, 46))
        self.add_arc('pot-bl', (12, 46), (9, 43), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_line('pot-l', (9, 43), (7, 34))
        self.add_contour('pot', 'pot-top', 'pot-r', 'pot-br', 'pot-b', 'pot-bl', 'pot-l', closed=True)
        self.relate('connect', 'left-stem', 'pot')
        self.relate('connect', 'centre-stem', 'pot')
        self.relate('connect', 'right-stem', 'pot')
