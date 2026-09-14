"""Corrected keyshape selection to match the existing square proportions.

SQUARE: visible ink (4, 4, 44, 44). Square envelope preserves the subject’s near-equal overall width and height.
No useful exact local Lucide match; retained the inspected parent silhouette.
"""
# Independent revision; parent models preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f7cd190d-39d7-4ce3-bab1-4aea0bd95ca5'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-07/volcano_f7cd190d-39d7-4ce3-bab1-4aea0bd95ca5.svg'
AUTHOR = 'gpt-6'

class EruptingVolcanoVariant2(Solo48):
    icon_id = 'erupting-volcano-v2'
    variant_of = 'erupting-volcano'
    variant_label = 'Exact keyshape envelope and clear spacing'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/landmarks'
    aliases = ()
    keywords = ('volcano', 'eruption', 'lava', 'crater', 'mountain', 'nature', 'disaster', 'landscape')

    def build(self) -> None:
        self.add_arc('left-flank', (6, 42), (17, 22), radius_x=40, sweep=False)
        self.add_line('crater', (17, 22), (31, 22))
        self.add_arc('right-flank', (31, 22), (42, 42), radius_x=40, sweep=False)
        self.add_contour('volcano', 'left-flank', 'crater', 'right-flank')
        self.add_line('central-ejecta', (24, 12), (24, 6))
        self.add_arc('left-ejecta', (15, 13), (9, 7), radius_x=8, sweep=False)
        self.add_arc('right-ejecta', (33, 13), (39, 7), radius_x=8, sweep=True)
