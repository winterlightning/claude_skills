"""Watch time (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1a8c69be-fb9f-54b3-88fd-f2244b2ab490'
SOURCE_PATH = 'icons-json/interface-essential/watch time_1a8c69be-fb9f-54b3-88fd-f2244b2ab490.json'
AUTHOR = 'json_to_solo'

class WatchTimeInterfaceEssential(Solo48):
    icon_id = 'watch-time-interface-essential'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('watch', 'time', 'interface-essential')

    def build(self):
        self.add_line('e0', (24, 13), (24, 23))
        self.add_line('e1', (27, 27), (30, 30))
        self.add_arc('e2-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e2-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e3', (24, 23), (27, 27), radius_x=15, sweep=False)
        self.add_contour('c0', 'e0', 'e3', 'e1')
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)
