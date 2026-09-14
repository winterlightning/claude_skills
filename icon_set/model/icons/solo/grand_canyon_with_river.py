# Review candidate; original preserved.
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
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('left-cliff-1', (6, 42), (6, 20))
        self.add_line('left-cliff-2', (6, 20), (10, 20))
        self.add_line('left-cliff-3', (10, 20), (14, 30))
        self.add_line('ridge-1', (6, 12), (12, 6))
        self.add_line('ridge-2', (12, 6), (22, 6))
        self.add_line('ridge-3', (22, 6), (28, 12))
        self.add_line('right-cliff-1', (42, 42), (42, 22))
        self.add_line('right-cliff-2', (42, 22), (38, 22))
        self.add_line('right-cliff-3', (38, 22), (36, 32))
        self.add_arc('river-upper', (29, 25), (21, 36), radius_x=14, radius_y=14, large_arc=False, sweep=False)
        self.add_arc('river-lower', (21, 36), (28, 41), radius_x=12, radius_y=12, large_arc=False, sweep=False)
        self.add_arc('sun-top', (36, 9), (42, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('sun-bottom', (42, 9), (36, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('left-cliff', *('left-cliff-1', 'left-cliff-2', 'left-cliff-3'), closed=False)
        self.add_contour('ridge', *('ridge-1', 'ridge-2', 'ridge-3'), closed=False)
        self.add_contour('right-cliff', *('right-cliff-1', 'right-cliff-2', 'right-cliff-3'), closed=False)
        self.add_contour('river', *('river-upper', 'river-lower'), closed=False)
        self.add_contour('sun', *('sun-top', 'sun-bottom'), closed=True)
