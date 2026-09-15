"""Three heart blooms on uneven branches grow from a square pot; tiny leaf twists omitted.

Construction references: Lucide heart, hand, sprout, balloon, cake, car and users-round as applicable.
SOLO48 live-contract centerline bounds: VRECT_L (8,4)-(40,44),
HRECT_L (4,8)-(44,40), SQUARE (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e88fb37a-e605-4d7e-a557-9e046dcb12ba'
SOURCE_PATH = 'pictographic-primitives/romance/love plant_e88fb37a-e605-4d7e-a557-9e046dcb12ba.svg'
AUTHOR = 'gpt-6'

class ThreeHeartPlantInSquarePotVariant2(Solo48):
    icon_id = 'three-heart-plant-in-square-pot-v2'
    variant_of = 'three-heart-plant-in-square-pot'
    variant_label = 'Hole and centerline reconstruction'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/romance'
    aliases = ()
    keywords = ('heart', 'plant', 'pot', 'branch', 'flower', 'romance')

    def build(self):
        """Rebuild three equal heart leaves with open counters; spread side leaves and place their shared branches below the leaf tips."""

        def heart(n, cx, y, tip):
            self.add_arc(n + '-l', (cx, y), (cx - 6, y), radius_x=3, sweep=False)
            self.add_line(n + '-left', (cx - 6, y), (cx, tip))
            self.add_line(n + '-right', (cx, tip), (cx + 6, y))
            self.add_arc(n + '-r', (cx + 6, y), (cx, y), radius_x=3, sweep=False)
            self.add_contour(n, n + '-l', n + '-left', n + '-right', n + '-r', closed=True)
        heart('centre', 24, 9, 19)
        heart('left', 12, 22, 32)
        heart('right', 36, 22, 32)
        self.add_polyline('stem', (24, 19), (24, 34), (24, 34))
        self.add_line('branch-l', (12, 32), (24, 34))
        self.add_line('branch-r', (36, 32), (24, 34))
        for a, b in [('centre', 'stem'), ('left', 'branch-l'), ('right', 'branch-r'), ('stem', 'branch-l'), ('stem', 'branch-r'), ('branch-l', 'branch-r')]:
            self.relate('connect', a, b)
        self.add_polyline('pot', (18, 34), (24, 34), (30, 34), (30, 42), (18, 42), closed=True)
        self.relate('connect', 'pot', 'stem')
