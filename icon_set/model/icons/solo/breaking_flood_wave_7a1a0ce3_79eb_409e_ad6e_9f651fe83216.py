"""A tall wave rises from an undulating waterline and curls inward toward the left. A second smooth parallel wave runs below the broad base of the crest.

Kept the inward curl and broad breaking wave body; removed the secondary lower waterline.
Construction reference: No useful exact local wave match; coherent circular crest and broad elliptical trough.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7a1a0ce3-79eb-409e-ad6e-9f651fe83216'
SOURCE_PATH = 'pictographic-primitives/weather/flood_7a1a0ce3-79eb-409e-ad6e-9f651fe83216.svg'
AUTHOR = 'gpt-6'

class BreakingFloodWave(Solo48):
    icon_id = 'breaking-flood-wave'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/weather"
    aliases = ()
    keywords = ('flood', 'wave', 'water', 'sea', 'swell', 'disaster')

    def build(self) -> None:
        # Live HRECT_XL visible bounds: (2, 6, 46, 42).
        self.add_arc('outer', (6, 20), (36, 20), radius_x=16, radius_y=12, sweep=True, large_arc=False)
        self.add_line('outer-fall', (36, 20), (36, 28))
        self.add_arc('outer-toe', (36, 28), (42, 32), radius_x=8, radius_y=4, sweep=False, large_arc=False)
        self.add_arc('trough-right', (42, 32), (24, 40), radius_x=20, radius_y=8, sweep=True, large_arc=False)
        self.add_arc('trough-left', (24, 40), (10, 36), radius_x=14, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('inner-lower', (10, 36), (14, 30), radius_x=4, radius_y=6, sweep=False, large_arc=False)
        self.add_arc('inner-upper', (14, 30), (6, 20), radius_x=10, radius_y=10, sweep=False, large_arc=False)
        self.add_contour('wave', 'outer', 'outer-fall', 'outer-toe', 'trough-right', 'trough-left', 'inner-lower', 'inner-upper', closed=True)
