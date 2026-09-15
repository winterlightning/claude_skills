"""Navigation direction left (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd246a2fd-8a0d-50c5-a0a7-5e7a3544282a'
SOURCE_PATH = 'pictographic-primitives/interface-essential/navigation direction left_d246a2fd-8a0d-50c5-a0a7-5e7a3544282a.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class NavigationDirectionLeftInterfaceEssential(Solo48):
    icon_id = 'navigation-direction-left-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('navigation', 'direction', 'left', 'interface-essential')

    def build(self):
        self.add_line('e0', (17, 4), (8, 15))
        self.add_line('e1', (8, 15), (27, 15))
        self.add_line('e2', (29, 44), (21, 44))
        self.add_line('e3', (17, 26), (8, 15))
        self.add_arc('e4-1', (27, 15), (39, 24), radius_x=13)
        self.add_line('e4-2', (39, 24), (40, 30))
        self.add_arc('e4-3', (40, 30), (29, 44), radius_x=15)
        self.add_contour('c0', 'e0', 'e1', 'e4-1', 'e4-2', 'e4-3', 'e2')
        self.add_contour('c1', 'e3')
