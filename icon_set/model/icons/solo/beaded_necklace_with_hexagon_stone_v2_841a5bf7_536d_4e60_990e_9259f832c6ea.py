# Variant of beaded-necklace-with-hexagon-stone; parent file remains unchanged.
"""A beaded necklace with a large hexagonal pendant. SQUARE extremes (2,2)-(46,46). Lucide gem informs a clean faceted outline; internal facets omitted. Symmetric round beads and exposed links replace densely packed elongated beads."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '841a5bf7-536d-4e60-990e-9259f832c6ea'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-05/necklace stone_841a5bf7-536d-4e60-990e-9259f832c6ea.svg'
AUTHOR = 'gpt-6'

class BeadedNecklaceWithHexagonStoneVariant2(Solo48):
    icon_id = 'beaded-necklace-with-hexagon-stone-v2'
    variant_of = 'beaded-necklace-with-hexagon-stone'
    variant_label = 'too complex, simplify'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('necklace', 'bead', 'stone', 'hexagon', 'gem', 'jewellery', 'jewelry', 'pendant', 'accessory')

    def build(self) -> None:
        # SQUARE extremes (2,2)-(46,46); four solid beads, no tiny holes or wires.
        self.add_dot('bead-left-top', (2,2))
        self.add_dot('bead-right-top', (46,2))
        self.add_dot('bead-left-low', (10,12))
        self.add_dot('bead-right-low', (38,12))
        self.add_polyline('chain', (18,21), (24,25), (30,21))
        self.add_line('link', (24,25), (24,30))
        self.add_polyline('stone', (24,30), (34,34), (34,42), (24,46), (14,42), (14,34), closed=True)
        self.relate('connect', 'chain', 'link')
        self.relate('connect', 'stone', 'link')
