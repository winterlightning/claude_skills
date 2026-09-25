"""Panel (state), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1de766db-6e07-416c-b475-1e00f6b151b9'
SOURCE_PATH = 'pictographic-primitives/state/panel_1de766db-6e07-416c-b475-1e00f6b151b9.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Panel(Solo48):
    icon_id = 'panel'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('panel', 'state')

    def build(self):
        self.add_line('e0', (23, 8), (34, 8))
        self.add_line('e1', (35, 9), (39, 18))
        self.add_line('e2', (23, 8), (14, 8))
        self.add_line('e3', (13, 9), (9, 18))
        self.add_line('e4', (23, 8), (23, 28))
        self.add_line('e5', (23, 28), (5, 28))
        self.add_line('e6', (4, 27), (9, 18))
        self.add_line('e7', (39, 18), (44, 27))
        self.add_line('e8', (43, 28), (23, 28))
        self.add_line('e9', (23, 28), (23, 40))
        self.add_line('e10', (39, 18), (9, 18))
        self.add_arc('e11', (34, 8), (35, 9), radius_x=1)
        self.add_arc('e12', (14, 8), (13, 9), radius_x=1, sweep=False)
        self.add_arc('e13', (5, 28), (4, 27), radius_x=1)
        self.add_arc('e14', (44, 27), (43, 28), radius_x=1)
        self.add_contour('c0', 'e0', 'e11', 'e1')
        self.add_contour('c1', 'e2', 'e12', 'e3')
        self.add_contour('c2', 'e4', 'e5', 'e13', 'e6')
        self.add_contour('c3', 'e7', 'e14', 'e8', 'e9')
        self.add_contour('c4', 'e10')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c3')
