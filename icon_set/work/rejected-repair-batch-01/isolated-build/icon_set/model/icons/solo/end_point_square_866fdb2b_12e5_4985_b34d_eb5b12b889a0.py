"""End point square (devices), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '866fdb2b-12e5-4985-b34d-eb5b12b889a0'
SOURCE_PATH = 'pictographic-primitives/devices/end point square_866fdb2b-12e5-4985-b34d-eb5b12b889a0.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class EndPointSquare(Solo48):
    icon_id = 'end-point-square'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'devices'
    aliases = ()
    keywords = ('end', 'point', 'square', 'devices')

    def build(self):
        self.add_line('e0', (4, 24), (29, 24))
        self.add_line('e1', (29, 24), (29, 40))
        self.add_line('e2', (29, 40), (44, 40))
        self.add_line('e3', (44, 40), (44, 8))
        self.add_line('e4', (44, 8), (29, 8))
        self.add_line('e5', (29, 8), (29, 24))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e3', 'e4', 'e5', closed=True)
        self.relate('connect', 'c0', 'c1')
