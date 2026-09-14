"""Loading bar (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a1357f44-093c-4bb6-93d6-7521033c44d2'
SOURCE_PATH = 'icons-json/interface-essential/loading bar_a1357f44-093c-4bb6-93d6-7521033c44d2.json'
AUTHOR = 'json_to_solo'

class LoadingBarA1357f44(Solo48):
    icon_id = 'loading-bar-a1357f44'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('loading', 'bar', 'interface-essential')

    def build(self):
        self.add_line('e0', (26, 40), (30, 8))
        self.add_line('e1', (14, 40), (19, 8))
        self.add_line('e2', (12, 8), (39, 8))
        self.add_line('e3', (38, 40), (10, 40))
        self.add_arc('e4-1', (10, 40), (5, 34), radius_x=6)
        self.add_line('e4-2', (5, 34), (4, 20))
        self.add_line('e4-3', (4, 20), (6, 11))
        self.add_arc('e4-4', (6, 11), (9, 8), radius_x=6)
        self.add_arc('e4-5', (9, 8), (12, 8), radius_x=13, sweep=False)
        self.add_arc('e5-1', (39, 8), (43, 13), radius_x=5)
        self.add_line('e5-2', (43, 13), (44, 25))
        self.add_line('e5-3', (44, 25), (44, 30))
        self.add_arc('e5-4', (44, 30), (42, 37), radius_x=21)
        self.add_arc('e5-5', (42, 37), (39, 40), radius_x=5)
        self.add_line('e5-6', (39, 40), (38, 40))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5', 'e2', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e5-5', 'e5-6', 'e3', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c2')
