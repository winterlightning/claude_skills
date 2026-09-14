# Variant of breaking-flood-wave-v2; parent file remains unchanged.
"""Rebuilt as an open breaking crest with an inward curl and a separate waterline; removed the closed shell-like outline.

Construction: Supplied weather reference: open crest, inward curl and waterline. No useful local Lucide wave match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7a1a0ce3-79eb-409e-ad6e-9f651fe83216'
SOURCE_PATH = 'pictographic-primitives/weather/flood_7a1a0ce3-79eb-409e-ad6e-9f651fe83216.svg'
AUTHOR = 'gpt-6'

class BreakingFloodWaveVariant3(Solo48):
    icon_id = 'breaking-flood-wave-v3'
    variant_of = 'breaking-flood-wave-v2'
    variant_label = 'Restore recognizable weather geometry'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/weather'
    aliases = ()
    keywords = ('flood', 'wave', 'water', 'sea', 'swell', 'disaster')

    def build(self) -> None:
        self.add_arc('crest-lip', (12, 14), (24, 6), radius_x=12, radius_y=8, sweep=True, large_arc=False)
        self.add_arc('outer-face', (24, 6), (42, 29), radius_x=18, radius_y=23, sweep=True, large_arc=False)
        self.add_contour('outer', 'crest-lip', 'outer-face', closed=False)
        self.add_line('lip', (12, 14), (16, 14))
        self.add_arc('inner-upper', (16, 14), (26, 22), radius_x=10, radius_y=8, sweep=True, large_arc=False)
        self.add_arc('inner-lower', (26, 22), (24, 29), radius_x=13, radius_y=13, sweep=True, large_arc=False)
        self.add_contour('inner', 'lip', 'inner-upper', 'inner-lower', closed=False)
        self.relate("connect", 'outer', 'inner')
        self.add_arc('surface-left', (6, 29), (24, 29), radius_x=15, radius_y=15, sweep=True, large_arc=False)
        self.add_arc('surface-right', (24, 29), (42, 29), radius_x=15, radius_y=15, sweep=False, large_arc=False)
        self.add_contour('surface', 'surface-left', 'surface-right', closed=False)
        self.relate("connect", 'inner', 'surface')
        self.relate("connect", 'outer', 'surface')
        self.add_arc('water-left', (6, 39), (24, 39), radius_x=15, radius_y=15, sweep=True, large_arc=False)
        self.add_arc('water-right', (24, 39), (42, 39), radius_x=15, radius_y=15, sweep=False, large_arc=False)
        self.add_contour('water', 'water-left', 'water-right', closed=False)
