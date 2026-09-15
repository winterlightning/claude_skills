"""Help wheel (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '32cc640b-fd6f-5d01-b576-fd631edb4656'
SOURCE_PATH = 'pictographic-primitives/interface-essential/help wheel_32cc640b-fd6f-5d01-b576-fd631edb4656.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class HelpWheel(Solo48):
    icon_id = 'help-wheel'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('help', 'wheel', 'interface-essential')

    def build(self):
        self.add_line('e0', (38, 38), (31, 32))
        self.add_line('e1', (17, 32), (10, 38))
        self.add_line('e2', (17, 16), (10, 10))
        self.add_line('e3', (38, 10), (31, 16))
        self.add_arc('e4-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e4-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e5-top', (13, 24), (35, 24), radius_x=11)
        self.add_arc('e5-bottom', (35, 24), (13, 24), radius_x=11)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
        self.add_contour('e5', 'e5-top', 'e5-bottom', closed=True)
        self.relate('connect', 'c0', 'e4')
        self.relate('connect', 'c0', 'e5')
        self.relate('connect', 'c1', 'e5')
        self.relate('connect', 'c1', 'e4')
        self.relate('connect', 'c2', 'e5')
        self.relate('connect', 'c2', 'e4')
        self.relate('connect', 'c3', 'e4')
        self.relate('connect', 'c3', 'e5')
