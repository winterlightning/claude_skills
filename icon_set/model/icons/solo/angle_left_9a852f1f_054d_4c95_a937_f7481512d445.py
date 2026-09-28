"""Angle left (_uncategorized_03), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9a852f1f-054d-4c95-a937-f7481512d445'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_03/angle left_9a852f1f-054d-4c95-a937-f7481512d445.svg'
AUTHOR = 'gpt-6'

class AngleLeft(Solo48):
    icon_id = 'angle-left'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('angle', 'left', '_uncategorized_03')

    def build(self):
        self.add_line('sym-e0', (44, 24), (4, 24))
        self.add_line('sym-e2', (4, 24), (21, 40))
        self.add_line('sym-e3', (21, 8), (4, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e2', closed=False)
        self.add_contour('sym-c1', 'sym-e3', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
