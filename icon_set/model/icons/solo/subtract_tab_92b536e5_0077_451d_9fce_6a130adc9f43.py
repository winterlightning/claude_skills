"""Subtract tab (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '92b536e5-0077-451d-9fce-6a130adc9f43'
SOURCE_PATH = 'icons-json/interface-essential/subtract tab_92b536e5-0077-451d-9fce-6a130adc9f43.json'
AUTHOR = 'json_to_solo'

class SubtractTab(Solo48):
    icon_id = 'subtract-tab'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('subtract', 'tab', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (12, 24), (23, 24))
        self.add_line('sym-e1', (4, 24), (4, 38))
        self.add_line('sym-e2', (4, 38), (6, 40))
        self.add_line('sym-e3', (6, 40), (33, 40))
        self.add_line('sym-e4', (33, 40), (35, 39))
        self.add_line('sym-e5', (35, 39), (43, 26))
        self.add_line('sym-e6', (43, 26), (44, 24))
        self.add_line('sym-e9', (44, 24), (43, 22))
        self.add_line('sym-e10', (43, 22), (35, 9))
        self.add_line('sym-e11', (35, 9), (33, 8))
        self.add_line('sym-e12', (33, 8), (6, 8))
        self.add_line('sym-e13', (6, 8), (4, 10))
        self.add_line('sym-e14', (4, 10), (4, 24))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', closed=True)
