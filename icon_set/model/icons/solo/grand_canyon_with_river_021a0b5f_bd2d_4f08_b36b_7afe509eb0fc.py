"""A winding river separates stepped canyon walls; fine strata omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '021a0b5f-bd2d-4f08-b36b-7afe509eb0fc'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-07/grand canyon usa 1_021a0b5f-bd2d-4f08-b36b-7afe509eb0fc.svg'
AUTHOR = 'gpt-6'

class GrandCanyonWithRiver(Solo48):
    icon_id = 'grand-canyon-with-river'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/landmarks'
    aliases = ()
    keywords = ('grand canyon', 'canyon', 'usa', 'arizona', 'river', 'cliff', 'landscape', 'nature', 'landmark')

    def build(self) -> None:
        # SQUARE centerline extremes (2,2)-(46,46).
        self.add_polyline('left-cliff', (2, 46), (2, 20), (10, 20), (14, 30))
        self.add_polyline('ridge', (6, 12), (12, 2), (22, 2), (28, 12))
        self.add_polyline('right-cliff', (46, 46), (46, 22), (38, 22), (36, 32))
        self.add_arc('river-upper', (30, 24), (20, 36), radius_x=16, sweep=False)
        self.add_arc('river-lower', (20, 36), (28, 46), radius_x=14, sweep=False)
        self.add_contour('river', 'river-upper', 'river-lower')
        self.add_arc('sun-top', (35, 7), (45, 7), radius_x=5, sweep=True)
        self.add_arc('sun-bottom', (45, 7), (35, 7), radius_x=5, sweep=True)
        self.add_contour('sun', 'sun-top', 'sun-bottom', closed=True)
