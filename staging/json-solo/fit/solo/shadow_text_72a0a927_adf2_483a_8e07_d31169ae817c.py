"""Shadow text (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '72a0a927-adf2-483a-8e07-d31169ae817c'
SOURCE_PATH = 'icons-json/interface-essential/shadow text_72a0a927-adf2-483a-8e07-d31169ae817c.json'
AUTHOR = 'json_to_solo'

class ShadowTextInterfaceEssential(Solo48):
    icon_id = 'shadow-text-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('shadow', 'text', 'interface-essential')

    def build(self):
        self.add_line('e0', (8, 43), (12, 29))
        self.add_line('e1', (40, 44), (35, 29))
        self.add_line('e2', (12, 29), (19, 7))
        self.add_line('e3', (28, 7), (35, 29))
        self.add_line('e4', (12, 29), (35, 29))
        self.add_arc('e5-1', (19, 7), (23, 4), radius_x=5)
        self.add_arc('e5-2', (23, 4), (28, 7), radius_x=6)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e5-1', 'e5-2', 'e3')
        self.add_contour('c3', 'e4')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
