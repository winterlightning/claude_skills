# Variant of brontosaurus; parent file remains unchanged.
"""Long-necked sauropod with a curved tapering tail, two legs and an asymmetric profile. SQUARE bounds (6,6)-(42,42). No useful local Lucide dinosaur match; retain the original silhouette with coherent tail arcs."""
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
        self.add_arc('head', (8, 12), (8, 6), radius_x=6, radius_y=5)
        self.add_line('crown', (8, 6), (12, 6))
        self.add_arc('nape', (12, 6), (18, 8), radius_x=6)
        self.add_line('neck', (18, 8), (20, 26))
        self.add_arc('back', (20, 26), (36, 28), radius_x=16, radius_y=8)
        self.add_arc('tail-1', (36,28), (42,34), radius_x=14, sweep=False)
        self.add_arc('tail-2', (42,34), (38,38), radius_x=10)
        self.add_arc('tail-3', (38,38), (32,36), radius_x=10)
        self.add_line('tail-4', (32, 36), (32, 42))
        self.add_line('tail-5', (32, 42), (24, 42))
        self.add_line('tail-6', (24, 42), (24, 36))
        self.add_line('tail-7', (24, 36), (16, 34))
        self.add_line('tail-8', (16, 34), (16, 42))
        self.add_line('tail-9', (16, 42), (8, 42))
        self.add_line('tail-10', (8, 42), (8, 12))
        self.add_contour('dinosaur', 'head', 'crown', 'nape', 'neck', 'back', *['tail-' + str(i) for i in range(6, 11)], closed=True)
