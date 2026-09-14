"""Text underline (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b8a7ef4b-af1c-59bd-bb25-170aedf30b04'
SOURCE_PATH = 'icons-json/interface-essential/text underline_b8a7ef4b-af1c-59bd-bb25-170aedf30b04.json'
AUTHOR = 'json_to_solo'

class TextUnderline(Solo48):
    icon_id = 'text-underline'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('text', 'underline', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (6, 42), (42, 42))
        self.add_line('sym-e1', (24, 36), (25, 36))
        self.add_arc('sym-e2', (25, 36), (35, 30), radius_x=13, sweep=False)
        self.add_line('sym-e3', (35, 30), (36, 25))
        self.add_line('sym-e5', (36, 25), (36, 6))
        self.add_line('sym-e6', (24, 36), (23, 36))
        self.add_arc('sym-e7', (23, 36), (13, 30), radius_x=13)
        self.add_line('sym-e8', (13, 30), (12, 25))
        self.add_line('sym-e10', (12, 25), (12, 6))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e5')
        self.add_contour('sym-c2', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e10')
        self.relate('connect', 'sym-c1', 'sym-c2')
