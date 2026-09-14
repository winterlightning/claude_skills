"""Double arrow right (state), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7099ca2e-6b54-40e6-a460-b7c2704abd1f'
SOURCE_PATH = 'icons-json/state/double arrow right_7099ca2e-6b54-40e6-a460-b7c2704abd1f.json'
AUTHOR = 'json_to_solo'

class DoubleArrowRight7099ca2e(Solo48):
    icon_id = 'double-arrow-right-7099ca2e'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('double', 'arrow', 'right', 'state')

    def build(self):
        self.add_line('sym-e0', (29, 8), (44, 24))
        self.add_line('sym-e1', (44, 24), (29, 40))
        self.add_line('sym-e2', (29, 24), (4, 24))
        self.add_line('sym-e3', (29, 24), (14, 40))
        self.add_line('sym-e4', (29, 24), (14, 8))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2')
        self.add_contour('sym-c2', 'sym-e3')
        self.add_contour('sym-c3', 'sym-e4')
        self.relate('connect', 'sym-c1', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
