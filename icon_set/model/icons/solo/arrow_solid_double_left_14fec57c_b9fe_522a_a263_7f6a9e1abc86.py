"""Arrow solid double left (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '14fec57c-b9fe-522a-a263-7f6a9e1abc86'
SOURCE_PATH = 'icons-json/arrows/arrow solid double left_14fec57c-b9fe-522a-a263-7f6a9e1abc86.json'
AUTHOR = 'json_to_solo'

class ArrowSolidDoubleLeft(Solo48):
    icon_id = 'arrow-solid-double-left'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'solid', 'double', 'left', 'arrows')

    def build(self):
        self.add_line('sym-e0', (4, 24), (4, 24))
        self.add_line('sym-e1', (4, 24), (14, 8))
        self.add_line('sym-e2', (14, 8), (23, 8))
        self.add_line('sym-e3', (23, 8), (15, 24))
        self.add_line('sym-e4', (15, 24), (23, 40))
        self.add_line('sym-e5', (23, 40), (14, 40))
        self.add_line('sym-e6', (14, 40), (4, 24))
        self.add_line('sym-e7', (44, 8), (35, 8))
        self.add_line('sym-e8', (35, 8), (25, 24))
        self.add_line('sym-e9', (25, 24), (35, 40))
        self.add_line('sym-e10', (35, 40), (44, 40))
        self.add_line('sym-e11', (44, 40), (36, 24))
        self.add_line('sym-e12', (36, 24), (44, 8))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', closed=True)
        self.add_contour('sym-c1', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', closed=True)
