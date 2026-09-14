# Variant of round-bud-vase; parent file remains unchanged.
'round-bud-vase: Rebalanced the four buds, raised the side attachment and deepened the vase. Keyshape VRECT_L; SOLO48 stroke 4. Reviewed at 48 px in both themes.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b6d820eb-0b98-4c05-838c-9bade7c068de'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-01/cherry blossom vase_b6d820eb-0b98-4c05-838c-9bade7c068de.svg'
AUTHOR = 'gpt-6'

class RoundBudVaseVariant3(Solo48):
    icon_id = 'round-bud-vase-v3'
    variant_of = 'round-bud-vase'
    variant_label = 'Correct width and full spacing review'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/decoration'
    aliases = ()
    keywords = ('vase', 'buds', 'flowers', 'stems', 'bouquet', 'plant', 'decor')

    def build(self) -> None:
        self.add_polyline('mouth', (16, 30), (24, 30), (32, 30))
        self.add_arc('vase-right', (32, 30), (24, 44), radius_x=8, radius_y=14)
        self.add_arc('vase-left', (24, 44), (16, 30), radius_x=8, radius_y=14)
        self.add_contour('vase-body', 'vase-right', 'vase-left')
        self.relate('connect', 'mouth', 'vase-body')
        for name, x, y in [('left', 11, 15), ('top', 24, 7), ('right', 37, 15), ('side', 37, 28)]:
            self.add_arc(name + '-bud-a', (x - 3, y), (x + 3, y), radius_x=3)
            self.add_arc(name + '-bud-b', (x + 3, y), (x - 3, y), radius_x=3)
            self.add_contour(name + '-bud', name + '-bud-a', name + '-bud-b', closed=True)
            self.add_line(name + '-stem', ((x - 3, y) if name == 'side' else (x, y + 3)), (24, 30))
            self.relate('connect', name + '-stem', name + '-bud')
            self.relate('connect', name + '-stem', 'mouth')
        for a, b in [('left', 'top'), ('left', 'right'), ('left', 'side'), ('top', 'right'), ('top', 'side'), ('right', 'side')]:
            self.relate('connect', a + '-stem', b + '-stem')
