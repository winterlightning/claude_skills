"""Loop manual (diagrams), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2c06654c-8d06-5a7b-95e0-7f57b63f8bac'
SOURCE_PATH = 'icons-json/diagrams/loop manual_2c06654c-8d06-5a7b-95e0-7f57b63f8bac.json'
AUTHOR = 'json_to_solo'

class LoopManualDiagrams(Solo48):
    icon_id = 'loop-manual-diagrams'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'diagrams'
    aliases = ()
    keywords = ('loop', 'manual', 'diagrams')

    def build(self):
        self.add_line('e0', (22, 29), (27, 16))
        self.add_arc('e1-1', (21, 16), (13, 8), radius_x=10, sweep=False)
        self.add_arc('e1-2', (13, 8), (6, 14), radius_x=8, sweep=False)
        self.add_line('e1-3', (6, 14), (4, 24))
        self.add_arc('e1-4', (4, 24), (5, 31), radius_x=25, sweep=False)
        self.add_arc('e1-5', (5, 31), (7, 36), radius_x=20, sweep=False)
        self.add_arc('e1-6', (7, 36), (13, 40), radius_x=7, sweep=False)
        self.add_arc('e1-7', (13, 40), (22, 29), radius_x=13, sweep=False)
        self.add_arc('e2-1', (27, 16), (35, 8), radius_x=9)
        self.add_arc('e2-2', (35, 8), (42, 14), radius_x=8)
        self.add_arc('e2-3', (42, 14), (44, 23), radius_x=22)
        self.add_line('e2-4', (44, 23), (42, 34))
        self.add_arc('e2-5', (42, 34), (35, 40), radius_x=8)
        self.add_arc('e2-6', (35, 40), (26, 30), radius_x=12)
        self.add_contour('c0', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', 'e1-6', 'e1-7', 'e0', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e2-6')
