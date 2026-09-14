"""Rate (diagrams), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '787378d6-0323-49b8-9328-c0c2be52d812'
SOURCE_PATH = 'icons-json/diagrams/rate_787378d6-0323-49b8-9328-c0c2be52d812.json'
AUTHOR = 'json_to_solo'

class Rate(Solo48):
    icon_id = 'rate'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'diagrams'
    aliases = ()
    keywords = ('rate', 'diagrams')

    def build(self):
        self.add_line('e0', (6, 25), (12, 24))
        self.add_line('e1', (12, 24), (42, 24))
        self.add_line('e2', (6, 25), (11, 30))
        self.add_line('e3', (11, 30), (23, 42))
        self.add_line('e4', (23, 42), (42, 24))
        self.add_line('e5', (6, 25), (23, 6))
        self.add_line('e6', (24, 6), (42, 24))
        self.add_line('e7', (23, 6), (24, 6))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e3', 'e4')
        self.add_contour('c2', 'e5', 'e7', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
