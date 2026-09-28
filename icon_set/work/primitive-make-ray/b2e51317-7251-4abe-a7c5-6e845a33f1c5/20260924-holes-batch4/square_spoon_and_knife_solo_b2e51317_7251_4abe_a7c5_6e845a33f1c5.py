"""square folk: repaired SOLO48 composition.
Plan: Distinct utensil silhouettes and a coherent enclosure.
Keyshape: SQUARE matches the enclosing tile.
Reduction: Knife blade reduced to an open outer edge; its tiny triangular pocket is removed.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._payments_batch01 import circle, rounded_rect

SOURCE_ICON_ID = 'b2e51317-7251-4abe-a7c5-6e845a33f1c5'
SOURCE_PATH = 'pictographic-primitives/other/square folk_b2e51317-7251-4abe-a7c5-6e845a33f1c5.svg'
AUTHOR = "gpt-6"
CONSTRUCTION_REFERENCES = 'utensils'

class Drawing(Solo48):
    icon_id = 'square-spoon-and-knife-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'square spoon and knife')

    def build(self):
        rounded_rect(self, 'outline', 6, 6, 42, 42, 5)
        circle(self, 'spoon', 19, 18, 3)
        self.add_line('handle', (19, 21), (19, 33))
        self.relate('connect', 'spoon', 'handle')
        self.add_polyline('knife', (31, 33), (31, 15), (33, 23))
