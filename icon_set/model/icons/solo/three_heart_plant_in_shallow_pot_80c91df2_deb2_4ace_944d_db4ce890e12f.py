"""Three heart blooms rise from a shallow planter. Small feet and double rim are omitted.

Construction references: Lucide heart, hand-heart, sprout and balloon as applicable.
SOLO48 live-contract centerline bounds: VRECT_L (8,4)-(40,44),
HRECT_L (4,8)-(44,40), SQUARE (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '80c91df2-deb2-4ace-944d-db4ce890e12f'
SOURCE_PATH = 'pictographic-primitives/romance/lgbt love plant_80c91df2-deb2-4ace-944d-db4ce890e12f.svg'
AUTHOR = 'gpt-6'

class ThreeHeartPlantInShallowPot(Solo48):
    icon_id = 'three-heart-plant-in-shallow-pot'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/romance'
    aliases = ()
    keywords = ('heart', 'plant', 'pot', 'flower', 'romance', 'growth')

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
        self.add_polyline('stem', (24, 19), (24, 34))
        self.add_line('branch-l', (12, 32), (24, 34))
        self.add_line('branch-r', (36, 32), (24, 34))
        for a, b in [('centre', 'stem'), ('left', 'branch-l'), ('right', 'branch-r'), ('stem', 'branch-l'), ('stem', 'branch-r'), ('branch-l', 'branch-r')]:
            self.relate('connect', a, b)
        self.add_polyline('pot', (6, 34), (24, 34), (42, 34), (38, 42), (10, 42), closed=True)
        self.relate('connect', 'pot', 'stem')
