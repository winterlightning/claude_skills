"""An explosion beside a house, representing war damage and displacement.
Plan: SQUARE accommodates the upper-left blast and lower-right house. Visible ink bounds: (4, 4, 44, 44).
Reduction: Inner capsule, house door and detached impact rays omitted. Burst rebalanced to retain multiple irregular rays and sufficient clearance to the house.
Construction: No useful exact Lucide match; supplied explosion composition and Lucide house roof/wall construction."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '922ba268-0492-4ece-8f41-54253b52949a'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_32/refugee immigration war 2_922ba268-0492-4ece-8f41-54253b52949a.svg'
AUTHOR = 'gpt-6'
PLAN = 'An explosion beside a house, representing war damage and displacement.'
OMISSIONS = 'Inner capsule, house door and detached impact rays omitted. Burst rebalanced to retain multiple irregular rays and sufficient clearance to the house.'
CONSTRUCTION_REFERENCES = 'No useful exact Lucide match; supplied explosion composition and Lucide house roof/wall construction.'
KEYSHAPE_INK_BOUNDS = (4, 4, 44, 44)

class Drawing(Solo48):
    icon_id = 'refugee-immigration-war-2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('refugee', 'immigration', 'war', '2')

    def build(self):
        self.add_polyline('explosion', (16, 6), (19, 10), (25, 7), (22, 13), (26, 16), (21, 18), (22, 22), (18, 21), (16, 26), (13, 22), (7, 25), (10, 19), (6, 16), (10, 13), (7, 7), (13, 10), closed=True)
        self.add_polyline('house', (26, 30), (34, 24), (42, 30), (42, 42), (26, 42), closed=True)
