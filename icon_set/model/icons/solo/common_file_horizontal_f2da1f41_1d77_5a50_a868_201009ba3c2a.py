"""Common file horizontal (files), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f2da1f41-1d77-5a50-a868-201009ba3c2a'
SOURCE_PATH = 'pictographic-primitives/files/common file horizontal_f2da1f41-1d77-5a50-a868-201009ba3c2a.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class CommonFileHorizontal(Solo48):
    icon_id = 'common-file-horizontal'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'files'
    aliases = ()
    keywords = ('common', 'file', 'horizontal', 'files')

    def build(self):
        # Plan: restore exact straight junctions; remove short fitted corner detours.
        # Reference: existing subject and its ideal straight-edge intersections.
        self.add_line('e0', (4, 40), (4, 8))
        self.add_line('e1', (4, 8), (35, 8))
        self.add_line('e2', (44, 18), (44, 40))
        self.add_line('e3', (44, 40), (4, 40))
        self.add_arc('e6', (35, 8), (44, 18), radius_x=19, radius_y=19, large_arc=False, sweep=True)
        self.add_contour('c0', 'e0', 'e1', 'e6', 'e2', 'e3', closed=True)
