'round-bud-vase-v2: Rebalanced the three buds and deepened the vase. Keyshape VRECT_L; SOLO48 stroke 4. Reviewed at 48 px in both themes.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b6d820eb-0b98-4c05-838c-9bade7c068de'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-01/cherry blossom vase_b6d820eb-0b98-4c05-838c-9bade7c068de.svg'
AUTHOR = 'gpt-6'

class RoundBudVase(Solo48):
    icon_id = 'round-bud-vase'
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
        for name, x, y in [('left', 11, 15), ('top', 24, 7), ('right', 37, 15)]:
            self.add_arc(name + '-bud-a', (x, y + 3), (x, y - 3), radius_x=3)
            self.add_arc(name + '-bud-b', (x, y - 3), (x, y + 3), radius_x=3)
            self.add_contour(name + '-bud', name + '-bud-a', name + '-bud-b', closed=True)
            self.add_line(name + '-stem', (x, y + 3), (24, 30))
            self.relate('connect', name + '-stem', name + '-bud')
            self.relate('connect', name + '-stem', 'mouth')
        for a, b in [('left', 'top'), ('left', 'right'), ('top', 'right')]:
            self.relate('connect', a + '-stem', b + '-stem')
