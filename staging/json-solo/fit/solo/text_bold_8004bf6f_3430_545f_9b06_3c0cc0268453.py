"""Text bold (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8004bf6f-3430-545f-9b06-3c0cc0268453'
SOURCE_PATH = 'icons-json/interface-essential/text bold_8004bf6f-3430-545f-9b06-3c0cc0268453.json'
AUTHOR = 'json_to_solo'

class TextBoldInterfaceEssential(Solo48):
    icon_id = 'text-bold-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('text', 'bold', 'interface-essential')

    def build(self):
        self.add_line('e0', (30, 44), (8, 44))
        self.add_line('e1', (8, 44), (8, 4))
        self.add_line('e2', (8, 4), (28, 4))
        self.add_line('e3', (30, 24), (8, 24))
        self.add_arc('e4-1', (28, 4), (38, 10), radius_x=12)
        self.add_arc('e4-2', (38, 10), (30, 24), radius_x=11)
        self.add_arc('e4-3', (30, 24), (40, 34), radius_x=11)
        self.add_arc('e4-4', (40, 34), (30, 44), radius_x=10)
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e4-1', 'e4-2', 'e4-3', 'e4-4', closed=True)
        self.add_contour('c1', 'e3')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
