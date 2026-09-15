"""Angle down (_uncategorized_03), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5d1e690d-7cb8-4583-96b6-60ab81cb1101'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_03/angle down_5d1e690d-7cb8-4583-96b6-60ab81cb1101.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class AngleDown(Solo48):
    icon_id = 'angle-down'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_03'
    aliases = ()
    keywords = ('angle', 'down', '_uncategorized_03')

    def build(self):
        # Plan: restore exact straight junctions; remove short fitted corner detours.
        # Reference: existing subject and its ideal straight-edge intersections.
        self.add_line('sym-e0', (6, 6), (42, 42))
        self.add_line('sym-e2', (42, 42), (42, 23))
        self.add_line('sym-e3', (23, 42), (40, 42))
        self.add_arc('sym-e4-1', (40, 42), (41, 42), radius_x=41, radius_y=41, large_arc=False, sweep=True)
        self.add_line('sym-e4-2', (41, 42), (42, 42))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e2', closed=False)
        self.add_contour('sym-c1', 'sym-e3', 'sym-e4-1', 'sym-e4-2', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c1')
