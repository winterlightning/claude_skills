"""Photo time lapse (photography), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e24a3ba0-192d-4a3a-8c1f-b6fa91c84ee7'
SOURCE_PATH = 'pictographic-primitives/photography/photo time lapse_e24a3ba0-192d-4a3a-8c1f-b6fa91c84ee7.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class PhotoTimeLapse(Solo48):
    icon_id = 'photo-time-lapse'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'photography'
    aliases = ()
    keywords = ('photo', 'time', 'lapse', 'photography')

    def build(self):
        # Plan: restore exact straight junctions; remove short fitted corner detours.
        # Reference: existing subject and its ideal straight-edge intersections.
        self.add_line('e0', (24, 14), (24, 25))
        self.add_line('e1', (24, 25), (32, 32))
        self.add_arc('e2-top', (4, 24), (44, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e2-bottom', (44, 24), (4, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_contour('c0', 'e0', 'e1', closed=False)
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)
