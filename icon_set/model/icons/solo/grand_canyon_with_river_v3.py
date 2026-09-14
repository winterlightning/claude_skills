# Review candidate; original preserved.
"""A winding river separates stepped canyon walls; fine strata omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '021a0b5f-bd2d-4f08-b36b-7afe509eb0fc'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-07/grand canyon usa 1_021a0b5f-bd2d-4f08-b36b-7afe509eb0fc.svg'
AUTHOR = 'gpt-6'

class GrandCanyonWithRiverVariant3(Solo48):
    icon_id = 'grand-canyon-with-river-v3'
    variant_of = 'grand-canyon-with-river'
    variant_label = 'Roomier openings — pending review'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/landmarks'
    aliases = ()
    keywords = ('grand canyon', 'canyon', 'usa', 'arizona', 'river', 'cliff', 'landscape', 'nature', 'landmark')

    def build(self) -> None:
        """Opening repair: Made the sun circular; preserved the canyon walls and river."""
        self.add_polyline('left-cliff', (6, 42), (6, 20), (10, 20), (14, 30))
        self.add_polyline('ridge', (6, 12), (12, 6), (22, 6), (28, 12))
        self.add_polyline('right-cliff', (42, 42), (42, 22), (38, 22), (36, 32))
        self.add_arc('river-upper', (30, 24), (20, 36), radius_x=16, sweep=False)
        self.add_arc('river-lower', (20, 36), (28, 42), radius_x=14, sweep=False)
        self.add_contour('river', 'river-upper', 'river-lower')
        self.add_arc('sun-top', (36, 9), (42, 9), sweep=True, radius_x=3, radius_y=3)
        self.add_arc('sun-bottom', (42, 9), (36, 9), sweep=True, radius_x=3, radius_y=3)
        self.add_contour('sun', 'sun-top', 'sun-bottom', closed=True)
