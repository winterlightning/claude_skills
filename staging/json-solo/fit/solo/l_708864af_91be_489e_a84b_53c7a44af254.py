"""L (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '708864af-91be-489e-a84b-53c7a44af254'
SOURCE_PATH = 'icons-json/typeface/l_708864af-91be-489e-a84b-53c7a44af254.json'
AUTHOR = 'json_to_solo'

class L708864af(Solo48):
    icon_id = 'l-708864af'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('l', 'typeface')

    def build(self):
        self.add_line('e0', (8, 4), (8, 36))
        self.add_line('e1-1', (8, 36), (10, 41))
        self.add_arc('e1-2', (10, 41), (15, 43), radius_x=12, sweep=False)
        self.add_arc('e1-3', (15, 43), (22, 44), radius_x=27, sweep=False)
        self.add_line('e1-4', (22, 44), (40, 41))
        self.add_contour('c0', 'e0', 'e1-1', 'e1-2', 'e1-3', 'e1-4')
