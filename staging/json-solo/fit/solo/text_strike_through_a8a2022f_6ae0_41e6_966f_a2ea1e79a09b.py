"""Text strike through (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a8a2022f-6ae0-41e6-966f-a2ea1e79a09b'
SOURCE_PATH = 'icons-json/interface-essential/text strike through_a8a2022f-6ae0-41e6-966f-a2ea1e79a09b.json'
AUTHOR = 'json_to_solo'

class TextStrikeThroughInterfaceEssential(Solo48):
    icon_id = 'text-strike-through-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('text', 'strike', 'through', 'interface-essential')

    def build(self):
        self.add_line('e0', (20, 22), (27, 24))
        self.add_line('e1', (6, 26), (31, 26))
        self.add_line('e2', (42, 26), (31, 26))
        self.add_arc('e3-1', (32, 15), (23, 6), radius_x=9, sweep=False)
        self.add_line('e3-2', (23, 6), (18, 7))
        self.add_arc('e3-3', (18, 7), (14, 13), radius_x=8, sweep=False)
        self.add_arc('e3-4', (14, 13), (20, 22), radius_x=8, sweep=False)
        self.add_arc('e4', (27, 24), (31, 26), radius_x=21)
        self.add_arc('e5-1', (13, 32), (22, 42), radius_x=10, sweep=False)
        self.add_line('e5-2', (22, 42), (29, 40))
        self.add_arc('e5-3', (29, 40), (31, 38), radius_x=9, sweep=False)
        self.add_arc('e5-4', (31, 38), (31, 26), radius_x=9, sweep=False)
        self.add_contour('c0', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e0', 'e4')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e5-1', 'e5-2', 'e5-3', 'e5-4')
        self.add_contour('c3', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
