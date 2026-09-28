"""Layout dashboard 1 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd6b2c6a1-cb44-4501-af37-391de583e4ff'
SOURCE_PATH = 'pictographic-primitives/interface-essential/layout dashboard 1_d6b2c6a1-cb44-4501-af37-391de583e4ff.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class LayoutDashboard1(Solo48):
    icon_id = 'layout-dashboard-1'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('layout', 'dashboard', 'interface-essential')

    def build(self):
        self.add_arc('e0-top', (6, 13), (20, 13), radius_x=7)
        self.add_arc('e0-bottom', (20, 13), (6, 13), radius_x=7)
        self.add_arc('e1-top', (28, 13), (42, 13), radius_x=7)
        self.add_arc('e1-bottom', (42, 13), (28, 13), radius_x=7)
        self.add_arc('e2-top', (6, 35), (20, 35), radius_x=7)
        self.add_arc('e2-bottom', (20, 35), (6, 35), radius_x=7)
        self.add_arc('e3-top', (28, 35), (42, 35), radius_x=7)
        self.add_arc('e3-bottom', (42, 35), (28, 35), radius_x=7)
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
        self.add_contour('e1', 'e1-top', 'e1-bottom', closed=True)
