"""Time nine to five 1 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4457d45a-d996-492d-949d-ff0115d87338'
SOURCE_PATH = 'icons-json/interface-essential/time nine to five 1_4457d45a-d996-492d-949d-ff0115d87338.json'
AUTHOR = 'json_to_solo'

class TimeNineToFive1InterfaceEssential(Solo48):
    icon_id = 'time-nine-to-five-1-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('time', 'nine', 'to', 'five', 'interface-essential')

    def build(self):
        self.add_line('e0', (35, 32), (35, 38))
        self.add_line('e1', (40, 38), (35, 38))
        self.add_line('e2', (31, 16), (22, 26))
        self.add_arc('e3-1', (24, 42), (6, 24), radius_x=18)
        self.add_arc('e3-2', (6, 24), (24, 6), radius_x=18)
        self.add_arc('e3-3', (24, 6), (42, 24), radius_x=18)
        self.add_line('e3-4', (42, 24), (40, 32))
        self.add_line('e3-5', (40, 32), (35, 38))
        self.add_contour('c0', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5')
        self.add_contour('c1', 'e0')
        self.add_contour('c2', 'e1')
        self.add_contour('c3', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
