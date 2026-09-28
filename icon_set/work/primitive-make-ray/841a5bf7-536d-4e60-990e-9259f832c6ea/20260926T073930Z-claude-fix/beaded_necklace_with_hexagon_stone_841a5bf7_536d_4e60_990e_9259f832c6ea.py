"""Simplify the necklace to three dot beads, paired curved chain sections, and one hexagonal pendant. Applied to the original icon identity."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '841a5bf7-536d-4e60-990e-9259f832c6ea'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__beaded-necklace-with-hexagon-stone/20260926T073831Z-thuan-mac/reference/necklace stone_841a5bf7-536d-4e60-990e-9259f832c6ea.svg'
AUTHOR = "claude-opus-5-5"

class BeadedNecklaceWithHexagonStone(Solo48):
    icon_id = 'beaded-necklace-with-hexagon-stone'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    categories = ('primitives', 'accessories')
    aliases = ()
    keywords = ('necklace', 'bead', 'stone', 'hexagon', 'gem', 'jewellery', 'jewelry', 'pendant', 'accessory')

    def build(self):
        # Redraw (no reviewer text; matched to the reference): a beaded necklace with a hexagonal
        # stone. The beads are round dots strung on a V, 8.5 apart centre to centre (45-degree
        # steps of (6, 6)): (6, 6), (12, 12), (18, 18) and mirrored (42, 6), (36, 12), (30, 18).
        # At the bottom of the V a short link drops from (24, 24) to the stone's top vertex
        # (24, 28); the stone is a pointy-top hexagon (24, 28)-(30, 31)-(30, 39)-(24, 42)-
        # (18, 39)-(18, 31). (Ring beads read as a molecule: attempts/v1-deep-v.svg,
        # attempts/v2-ring-beads.svg.)
        for i, (x, y) in enumerate(((6, 6), (12, 12), (18, 18), (30, 18), (36, 12), (42, 6))):
            self.add_dot(f'bead-{i + 1}', (x, y))
        self.add_line('link', (24, 24), (24, 28))
        self.add_polyline('stone', (24, 28), (30, 31), (30, 39), (24, 42), (18, 39), (18, 31), closed=True)
        self.relate('connect', 'link', 'stone')
