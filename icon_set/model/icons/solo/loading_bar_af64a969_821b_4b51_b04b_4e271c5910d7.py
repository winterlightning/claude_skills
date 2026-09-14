"""Loading bar (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'af64a969-821b-4b51-b04b-4e271c5910d7'
SOURCE_PATH = 'icons-json/interface-essential/loading bar_af64a969-821b-4b51-b04b-4e271c5910d7.json'
AUTHOR = 'json_to_solo'

class LoadingBarInterfaceEssential(Solo48):
    icon_id = 'loading-bar-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('loading', 'bar', 'interface-essential')

    def build(self):
        self.add_line('e0', (31, 8), (37, 8))
        self.add_line('e1', (38, 40), (11, 40))
        self.add_line('e2', (10, 8), (31, 8))
        self.add_line('e3', (31, 8), (19, 40))
        self.add_arc('e4-1', (37, 8), (43, 16), radius_x=8)
        self.add_arc('e4-2', (43, 16), (44, 23), radius_x=27)
        self.add_line('e4-3', (44, 23), (42, 34))
        self.add_arc('e4-4', (42, 34), (38, 40), radius_x=8)
        self.add_arc('e5-1', (11, 40), (6, 34), radius_x=7)
        self.add_arc('e5-2', (6, 34), (4, 23), radius_x=33)
        self.add_arc('e5-3', (4, 23), (6, 13), radius_x=26)
        self.add_arc('e5-4', (6, 13), (10, 8), radius_x=6)
        self.add_contour('c0', 'e0', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e1', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e2', 'e3')
