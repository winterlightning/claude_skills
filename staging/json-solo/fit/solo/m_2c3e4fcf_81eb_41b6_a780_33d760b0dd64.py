"""M (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2c3e4fcf-81eb-41b6-a780-33d760b0dd64'
SOURCE_PATH = 'icons-json/typeface/M_2c3e4fcf-81eb-41b6-a780-33d760b0dd64.json'
AUTHOR = 'json_to_solo'

class M2c3e4fcf(Solo48):
    icon_id = 'm-2c3e4fcf'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('m', 'typeface')

    def build(self):
        self.add_line('sym-e0', (6, 42), (13, 9))
        self.add_arc('sym-e1', (13, 9), (15, 6), radius_x=3)
        self.add_arc('sym-e4', (15, 6), (17, 11), radius_x=5)
        self.add_line('sym-e5', (17, 11), (23, 34))
        self.add_line('sym-e7', (23, 34), (24, 35))
        self.add_line('sym-e8', (24, 35), (25, 34))
        self.add_line('sym-e10', (25, 34), (31, 11))
        self.add_arc('sym-e11', (31, 11), (33, 6), radius_x=5)
        self.add_arc('sym-e14', (33, 6), (35, 9), radius_x=3)
        self.add_line('sym-e15', (35, 9), (42, 42))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e4', 'sym-e5', 'sym-e7', 'sym-e8', 'sym-e10', 'sym-e11', 'sym-e14', 'sym-e15')
