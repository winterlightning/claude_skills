"""Rewind (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0e803931-8f3a-4725-b041-336a1a6b4321'
SOURCE_PATH = 'icons-json/interface-essential/rewind_0e803931-8f3a-4725-b041-336a1a6b4321.json'
AUTHOR = 'json_to_solo'

class RewindInterfaceEssential(Solo48):
    icon_id = 'rewind-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('rewind', 'interface-essential')

    def build(self):
        self.add_line('e0', (21, 20), (4, 8))
        self.add_line('e1', (4, 8), (4, 40))
        self.add_line('e2', (4, 40), (21, 28))
        self.add_line('e3', (44, 24), (21, 9))
        self.add_line('e4', (21, 9), (21, 39))
        self.add_line('e5', (21, 39), (44, 24))
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e3', 'e4', 'e5', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
