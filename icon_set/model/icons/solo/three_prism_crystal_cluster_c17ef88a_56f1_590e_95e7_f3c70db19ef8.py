"""Three pointed crystal prisms, central tallest; small cap facets omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c17ef88a-56f1-590e-95e7-f3c70db19ef8'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-02/decoration crystals_c17ef88a-56f1-590e-95e7-f3c70db19ef8.svg'
AUTHOR = 'gpt-6'

class ThreePrismCrystalCluster(Solo48):
    icon_id = 'three-prism-crystal-cluster'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/decoration"
    aliases = ()
    keywords = ('crystal', 'prism', 'cluster', 'mineral', 'quartz', 'geology', 'facets')

    def build(self) -> None:
        # SQUARE: exact SOLO48 extremes; geometry authored on the integer grid.
        self.add_polyline('central', (16, 46), (16, 12), (24, 2), (32, 12), (32, 46), closed=True)
        self.add_polyline('left', (16, 46), (8, 46), (2, 26), (6, 18), (16, 26), closed=False)
        self.add_polyline('right', (32, 46), (40, 46), (46, 26), (42, 18), (32, 26), closed=False)
        self.relate('connect', 'left', 'central')
        self.relate('connect', 'right', 'central')
