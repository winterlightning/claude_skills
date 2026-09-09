# Variant of brontosaurus; parent file remains unchanged.
"""Long-necked sauropod with a curved tapering tail, two legs and an asymmetric profile. SQUARE bounds (2,2)-(46,46). No useful local Lucide dinosaur match; retain the original silhouette with coherent tail arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2b7b6c5f-c04e-5ce2-a62b-3da414005113'
SOURCE_PATH = 'pictographic-primitives/animals/dinosaur brontosaurus_2b7b6c5f-c04e-5ce2-a62b-3da414005113.svg'
AUTHOR = 'gpt-6'

class BrontosaurusVariant2(Solo48):
    icon_id = 'brontosaurus-v2'
    variant_of = 'brontosaurus'
    variant_label = 'Sweeping curved tail'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('dinosaur', 'brontosaurus', 'sauropod', 'longneck', 'prehistoric', 'jurassic', 'reptile', 'extinct')

    def build(self) -> None:
        self.add_arc('head', (8, 12), (8, 2), radius_x=6, radius_y=5)
        self.add_line('crown', (8, 2), (12, 2))
        self.add_arc('nape', (12, 2), (18, 8), radius_x=6)
        self.add_line('neck', (18, 8), (20, 26))
        self.add_arc('back', (20, 26), (36, 28), radius_x=16, radius_y=8)
        self.add_arc('tail-1', (36,28), (46,34), radius_x=14, sweep=False)
        self.add_arc('tail-2', (46,34), (38,38), radius_x=10)
        self.add_arc('tail-3', (38,38), (32,36), radius_x=10)
        self.add_line('tail-4', (32, 36), (32, 46))
        self.add_line('tail-5', (32, 46), (24, 46))
        self.add_line('tail-6', (24, 46), (24, 36))
        self.add_line('tail-7', (24, 36), (16, 34))
        self.add_line('tail-8', (16, 34), (16, 46))
        self.add_line('tail-9', (16, 46), (8, 46))
        self.add_line('tail-10', (8, 46), (8, 12))
        self.add_contour('dinosaur', 'head', 'crown', 'nape', 'neck', 'back', *['tail-' + str(i) for i in range(1, 11)], closed=True)
