"""Navigation right 1 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '43edf023-72b1-5d09-b638-a6f2ec544a41'
SOURCE_PATH = 'icons-json/interface-essential/navigation right 1_43edf023-72b1-5d09-b638-a6f2ec544a41.json'
AUTHOR = 'json_to_solo'

class NavigationRight1(Solo48):
    icon_id = 'navigation-right-1'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('navigation', 'right', 'interface-essential')

    def build(self):
        self.add_line('e0', (28, 40), (44, 24))
        self.add_line('e1', (44, 24), (28, 8))
        self.add_line('e2', (34, 24), (4, 24))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
