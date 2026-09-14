"""Data (diagrams), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ae294363-6122-428f-9a27-307296bcea92'
SOURCE_PATH = 'icons-json/diagrams/data_ae294363-6122-428f-9a27-307296bcea92.json'
AUTHOR = 'json_to_solo'

class DataDiagrams(Solo48):
    icon_id = 'data-diagrams'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'diagrams'
    aliases = ()
    keywords = ('data', 'diagrams')

    def build(self):
        self.add_line('e0', (42, 17), (42, 35))
        self.add_line('e1', (6, 35), (6, 14))
        self.add_arc('e2', (42, 25), (6, 25), radius_x=34)
        self.add_arc('e3-1', (42, 14), (6, 14), radius_x=37)
        self.add_line('e3-2', (6, 14), (7, 10))
        self.add_arc('e3-3', (7, 10), (11, 8), radius_x=10)
        self.add_line('e3-4', (11, 8), (25, 6))
        self.add_arc('e3-5', (25, 6), (37, 8), radius_x=39)
        self.add_arc('e3-6', (37, 8), (42, 12), radius_x=7)
        self.add_line('e3-7', (42, 12), (42, 16))
        self.add_arc('e3-8', (42, 16), (42, 17), radius_x=24, sweep=False)
        self.add_arc('e4-1', (42, 35), (37, 40), radius_x=6)
        self.add_line('e4-2', (37, 40), (24, 42))
        self.add_line('e4-3', (24, 42), (15, 41))
        self.add_arc('e4-4', (15, 41), (9, 39), radius_x=26)
        self.add_arc('e4-5', (9, 39), (6, 35), radius_x=5)
        self.add_contour('c0', 'e2')
        self.add_contour('c1', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e3-6', 'e3-7', 'e3-8', 'e0', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5', 'e1')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
