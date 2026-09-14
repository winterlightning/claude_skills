"""Shadow text (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e5', (19, 7), ((19.43, 5.618), (21.32, 4.009), (22.9, 4.009)), ((23.008, 4.009), (23.126, 4), (23.235, 4)), ((23.237, 4), (23.238, 4), (23.24, 4)), ((23.32, 4), (23.39, 4.009), (23.46, 4.009)), ((25.12, 4.009), (27.53, 5.455), (28, 7)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e5', 'e3')
        self.add_contour('c3', 'e4')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
