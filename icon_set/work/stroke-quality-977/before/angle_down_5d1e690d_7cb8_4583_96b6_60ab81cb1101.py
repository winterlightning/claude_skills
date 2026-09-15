"""Angle down (_uncategorized_03), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5d1e690d-7cb8-4583-96b6-60ab81cb1101'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_03/angle down_5d1e690d-7cb8-4583-96b6-60ab81cb1101.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class AngleDown(Solo48):
    icon_id = 'angle-down'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_03'
    aliases = ()
    keywords = ('angle', 'down', '_uncategorized_03')

    def build(self):
        self.add_line('sym-e0', (6, 6), (42, 42))
        self.add_arc('sym-e1', (42, 42), (42, 40), radius_x=41)
        self.add_line('sym-e2', (42, 40), (42, 23))
        self.add_line('sym-e3', (23, 42), (40, 42))
        self.add_arc('sym-e4-1', (40, 42), (41, 42), radius_x=41)
        self.add_line('sym-e4-2', (41, 42), (42, 42))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2')
        self.add_contour('sym-c1', 'sym-e3', 'sym-e4-1', 'sym-e4-2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
