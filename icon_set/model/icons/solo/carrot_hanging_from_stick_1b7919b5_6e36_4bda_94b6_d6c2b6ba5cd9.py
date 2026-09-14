"""A carrot hangs diagonally from a short line attached near the end of a curved stick. Its tapered root has short surface marks and a lobed leafy top beside the suspension.
Lucide carrot rounded shoulder and tapered root. Curved rod, suspension and leafy top remain one physical assembly. Surface cuts omitted. Deliberately diagonal root and arching stick.
SQUARE: centerline extremes (6,6)-(42,42); freshly authored on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1b7919b5-6e36-4bda-94b6-d6c2b6ba5cd9'
SOURCE_PATH = 'pictographic-primitives/work/workflow coaching carrot bait_1b7919b5-6e36-4bda-94b6-d6c2b6ba5cd9.svg'
AUTHOR = 'gpt-6'


class CarrotHangingFromStick(Solo48):
    icon_id = 'carrot-hanging-from-stick'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/work"
    aliases = ()
    keywords = ('carrot', 'stick', 'bait', 'reward', 'vegetable', 'hanging')

    def build(self) -> None:
        self.add_line('stick-start', (6, 6), (16, 6))
        self.add_arc('stick', (16, 6), (42, 24), radius_x=26, radius_y=18, sweep=True, large_arc=False)
        self.add_contour('rod', 'stick-start', 'stick', closed=False)
        self.add_line('string', (16, 6), (16, 22))
        self.relate("connect", 'string', 'rod')
        self.add_arc('carrot-top-left', (10, 28), (16, 22), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('carrot-top-right', (16, 22), (22, 28), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_line('carrot-right', (22, 28), (24, 42))
        self.add_line('carrot-left', (24, 42), (10, 28))
        self.add_contour('carrot', 'carrot-top-left', 'carrot-top-right', 'carrot-right', 'carrot-left', closed=True)
        self.relate("connect", 'string', 'carrot')
        self.add_polyline('leaves', (8, 20), (16, 22), (22, 18), closed=False)
        self.relate("connect", 'leaves', 'string')
        self.relate("connect", 'leaves', 'carrot')
