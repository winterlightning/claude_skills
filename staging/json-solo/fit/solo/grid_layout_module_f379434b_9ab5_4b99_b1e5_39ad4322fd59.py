"""Grid layout module (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f379434b-9ab5-4b99-b1e5-39ad4322fd59'
SOURCE_PATH = 'icons-json/interface-essential/grid layout module_f379434b-9ab5-4b99-b1e5-39ad4322fd59.json'
AUTHOR = 'json_to_solo'

class GridLayoutModuleInterfaceEssential(Solo48):
    icon_id = 'grid-layout-module-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('grid', 'layout', 'module', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (24, 18), (24, 4))
        self.add_line('sym-e1', (24, 44), (24, 27))
        self.add_line('sym-e2', (40, 4), (40, 18))
        self.add_line('sym-e3', (40, 26), (40, 44))
        self.add_line('sym-e4', (8, 4), (8, 18))
        self.add_line('sym-e5', (8, 26), (8, 44))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1')
        self.add_contour('sym-c2', 'sym-e2')
        self.add_contour('sym-c3', 'sym-e3')
        self.add_contour('sym-c4', 'sym-e4')
        self.add_contour('sym-c5', 'sym-e5')
