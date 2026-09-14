"""Zigzag (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9f41fad4-fc83-4879-a306-d3db72854261'
SOURCE_PATH = 'icons-json/interface-essential/zigzag_9f41fad4-fc83-4879-a306-d3db72854261.json'
AUTHOR = 'json_to_solo'

class Zigzag(Solo48):
    icon_id = 'zigzag'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('zigzag', 'interface-essential')

    def build(self):
        self.add_line('e0', (33, 6), (39, 12))
        self.add_line('e1', (6, 42), (35, 42))
        self.add_line('e2', (35, 27), (13, 27))
        self.add_line('e3', (13, 12), (39, 12))
        self.add_line('e4', (33, 17), (39, 12))
        self.add_arc('e5-1', (35, 42), (41, 38), radius_x=8, sweep=False)
        self.add_line('e5-2', (41, 38), (42, 34))
        self.add_arc('e5-3', (42, 34), (35, 27), radius_x=7, sweep=False)
        self.add_arc('e6-1', (13, 27), (6, 20), radius_x=8)
        self.add_line('e6-2', (6, 20), (8, 14))
        self.add_arc('e6-3', (8, 14), (13, 12), radius_x=7)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e5-1', 'e5-2', 'e5-3', 'e2', 'e6-1', 'e6-2', 'e6-3', 'e3')
        self.add_contour('c2', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
