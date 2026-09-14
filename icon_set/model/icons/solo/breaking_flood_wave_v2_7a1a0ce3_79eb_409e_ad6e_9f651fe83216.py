# Variant of breaking-flood-wave; parent file remains unchanged.
"""Rebuilt as an open breaking crest with an inward curl and a separate waterline; removed the closed shell-like outline.

Construction: Supplied weather reference: open crest, inward curl and waterline. No useful local Lucide wave match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7a1a0ce3-79eb-409e-ad6e-9f651fe83216'
SOURCE_PATH = 'pictographic-primitives/weather/flood_7a1a0ce3-79eb-409e-ad6e-9f651fe83216.svg'
AUTHOR = 'gpt-6'

class BreakingFloodWaveVariant2(Solo48):
    icon_id = 'breaking-flood-wave-v2'
    variant_of = 'breaking-flood-wave'
    variant_label = 'Restore recognizable weather geometry'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/weather'
    aliases = ()
    keywords = ('flood', 'wave', 'water', 'sea', 'swell', 'disaster')

    def build(self) -> None:
        self.add_line('face', (42, 29), (42, 24))
        self.add_arc('crest', (42, 24), (6, 24), radius_x=20, radius_y=16, sweep=False, large_arc=False)
        self.add_arc('curl', (6, 24), (20, 24), radius_x=8, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('wash', (20, 24), (12, 29), radius_x=8, radius_y=5, sweep=True, large_arc=False)
        self.add_contour('breaking-wave', 'face', 'crest', 'curl', 'wash', closed=False)
        self.add_arc('water-left', (6, 39), (24, 39), radius_x=10, radius_y=1, sweep=False, large_arc=False)
        self.add_arc('water-right', (24, 39), (42, 39), radius_x=10, radius_y=1, sweep=True, large_arc=False)
        self.add_contour('water', 'water-left', 'water-right', closed=False)
