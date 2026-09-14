"""Common file empty (files), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ec6cb18b-47f8-5fc6-be69-95fa07c27623'
SOURCE_PATH = 'icons-json/files/common file empty_ec6cb18b-47f8-5fc6-be69-95fa07c27623.json'
AUTHOR = 'json_to_solo'

class CommonFileEmpty(Solo48):
    icon_id = 'common-file-empty'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'files'
    aliases = ()
    keywords = ('common', 'file', 'empty', 'files')

    def build(self):
        self.add_line('e0', (27, 4), (11, 4))
        self.add_line('e1', (8, 8), (8, 41))
        self.add_line('e2', (11, 44), (37, 44))
        self.add_line('e3', (40, 41), (40, 13))
        self.add_arc('e4-1', (11, 4), (8, 7), radius_x=3, sweep=False)
        self.add_line('e4-2', (8, 7), (8, 8))
        self.add_arc('e5', (8, 41), (11, 44), radius_x=3, sweep=False)
        self.add_arc('e6', (37, 44), (40, 41), radius_x=3, sweep=False)
        self.add_arc('e7-1', (40, 13), (31, 4), radius_x=17, sweep=False)
        self.add_line('e7-2', (31, 4), (27, 4))
        self.add_contour('c0', 'e0', 'e4-1', 'e4-2', 'e1', 'e5', 'e2', 'e6', 'e3', 'e7-1', 'e7-2', closed=True)
