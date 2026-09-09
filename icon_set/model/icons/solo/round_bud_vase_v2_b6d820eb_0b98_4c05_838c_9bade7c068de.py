# Variant of round-bud-vase; parent file remains unchanged.
"""Round vase with three bud stems, omitting the bottom-right branch. VRECT_XL retains the original extremities. Natural stem asymmetry is preserved; Lucide sprout informed the simple plant construction."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b6d820eb-0b98-4c05-838c-9bade7c068de'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-01/cherry blossom vase_b6d820eb-0b98-4c05-838c-9bade7c068de.svg'
AUTHOR = 'gpt-6'

class RoundBudVaseVariant2(Solo48):
    icon_id = 'round-bud-vase-v2'
    variant_of = 'round-bud-vase'
    variant_label = 'Remove lower right branch'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/decoration'
    aliases = ()
    keywords = ('vase', 'buds', 'flowers', 'stems', 'bouquet', 'plant', 'decor')

    def build(self) -> None:
        self.add_polyline('mouth', (16, 30), (24, 30), (32, 30))
        self.add_arc('vase-right', (32, 30), (24, 46), radius_x=10, radius_y=10)
        self.add_arc('vase-left', (24, 46), (16, 30), radius_x=10, radius_y=10)
        self.add_contour('vase-body', 'vase-right', 'vase-left')
        self.relate('connect', 'mouth', 'vase-body')
        for name, x, y in [('left', 8, 12), ('top', 22, 5), ('right', 40, 9)]:
            self.add_arc(name + '-bud-a', (x, y + 3), (x, y - 3), radius_x=3)
            self.add_arc(name + '-bud-b', (x, y - 3), (x, y + 3), radius_x=3)
            self.add_contour(name + '-bud', name + '-bud-a', name + '-bud-b', closed=True)
            self.add_line(name + '-stem', (x, y + 3), (24, 30))
            self.relate('connect', name + '-stem', name + '-bud')
            self.relate('connect', name + '-stem', 'mouth')
        for a, b in [('left', 'top'), ('left', 'right'), ('top', 'right')]:
            self.relate('connect', a + '-stem', b + '-stem')
