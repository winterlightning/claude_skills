"""A broad crater cone ejecting lava; small flank lightning mark omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f7cd190d-39d7-4ce3-bab1-4aea0bd95ca5'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-07/volcano_f7cd190d-39d7-4ce3-bab1-4aea0bd95ca5.svg'
AUTHOR = 'gpt-6'

class EruptingVolcano(Solo48):
    icon_id = 'erupting-volcano'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/landmarks'
    aliases = ()
    keywords = ('volcano', 'eruption', 'lava', 'crater', 'mountain', 'nature', 'disaster', 'landscape')

    def build(self) -> None:
        # HRECT_XL centerline extremes (2,5)-(46,43).
        self.add_arc('left-flank', (2, 43), (17, 22), radius_x=40, sweep=False)
        self.add_line('crater', (17, 22), (31, 22))
        self.add_arc('right-flank', (31, 22), (46, 43), radius_x=40, sweep=False)
        self.add_contour('volcano', 'left-flank', 'crater', 'right-flank')
        self.add_line('central-ejecta', (24, 12), (24, 5))
        self.add_arc('left-ejecta', (15, 13), (9, 7), radius_x=8, sweep=False)
        self.add_arc('right-ejecta', (33, 13), (39, 7), radius_x=8, sweep=True)
