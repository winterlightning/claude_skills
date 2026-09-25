"""Navigation right circle (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9df37805-d24e-447f-86c4-dfef7e691d13'
SOURCE_PATH = 'pictographic-primitives/interface-essential/navigation right circle_9df37805-d24e-447f-86c4-dfef7e691d13.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class NavigationRightCircle(Solo48):
    icon_id = 'navigation-right-circle'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('navigation', 'right', 'circle', 'interface-essential')

    def build(self):
        self.add_line('e0', (35, 8), (44, 18))
        self.add_line('e1', (4, 40), (4, 31))
        self.add_line('e2', (17, 18), (44, 18))
        self.add_line('e3', (35, 27), (44, 18))
        self.add_arc('e4', (4, 31), (17, 18), radius_x=14)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e4', 'e2')
        self.add_contour('c2', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
