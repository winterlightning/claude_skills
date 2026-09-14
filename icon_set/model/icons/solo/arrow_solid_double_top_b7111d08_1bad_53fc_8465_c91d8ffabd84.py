"""Arrow solid double top (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b7111d08-1bad-53fc-8465-c91d8ffabd84'
SOURCE_PATH = 'icons-json/arrows/arrow solid double top_b7111d08-1bad-53fc-8465-c91d8ffabd84.json'
AUTHOR = 'json_to_solo'

class ArrowSolidDoubleTop(Solo48):
    icon_id = 'arrow-solid-double-top'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'solid', 'double', 'top', 'arrows')

    def build(self):
        self.add_line('sym-e0', (24, 4), (24, 4))
        self.add_line('sym-e1', (24, 4), (40, 14))
        self.add_line('sym-e2', (40, 14), (40, 23))
        self.add_line('sym-e3', (40, 23), (24, 15))
        self.add_line('sym-e4', (24, 15), (8, 23))
        self.add_line('sym-e5', (8, 23), (8, 14))
        self.add_line('sym-e6', (8, 14), (24, 4))
        self.add_line('sym-e7', (24, 36), (40, 44))
        self.add_line('sym-e8', (40, 44), (40, 35))
        self.add_line('sym-e9', (40, 35), (24, 25))
        self.add_line('sym-e10', (24, 25), (8, 35))
        self.add_line('sym-e11', (8, 35), (8, 44))
        self.add_line('sym-e12', (8, 44), (24, 36))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', closed=True)
        self.add_contour('sym-c1', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', closed=True)
