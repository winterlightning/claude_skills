"""Two offset wedding rings and a hexagonal gem. SQUARE (2,2)-(46,46) preserves the diagonal pair. Open rear band indicates overlap; gem facets omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6390c0da-0b86-4e37-8062-f088fcb1ef08'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-04/rings couple_6390c0da-0b86-4e37-8062-f088fcb1ef08.svg'
AUTHOR = 'astra-chatgpt'


class PairOfWeddingRings(Solo48):
    icon_id = 'pair-of-wedding-rings'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('ring', 'rings', 'wedding', 'engagement', 'couple', 'marriage', 'jewellery', 'jewelry', 'gem')

    def build(self) -> None:
        self.add_arc("front-r", (33, 20), (33, 46), radius_x=13)
        self.add_arc("front-l", (33, 46), (33, 20), radius_x=13)
        self.add_contour("front", "front-r", "front-l", closed=True)
        # Rear ring: top and left extrema are explicit circle endpoints.
        self.add_arc("rear-top", (2, 23), (14, 11), radius_x=12)
        self.add_arc("rear-shoulder", (14, 11), (21, 13), radius_x=12)
        self.add_arc("rear-bottom", (14, 35), (2, 23), radius_x=12)
        self.add_contour("rear", "rear-bottom", "rear-top", "rear-shoulder")
        self.add_polyline("gem", (9, 2), (19, 2), (24, 7), (19, 11), (14, 11), (9, 11), (4, 7), closed=True)
        self.relate("connect", "rear", "gem")
