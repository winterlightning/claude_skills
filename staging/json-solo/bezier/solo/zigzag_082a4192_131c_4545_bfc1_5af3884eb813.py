"""Zigzag (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '082a4192-131c-4545-bfc1-5af3884eb813'
SOURCE_PATH = 'icons-json/interface-essential/zigzag_082a4192-131c-4545-bfc1-5af3884eb813.json'
AUTHOR = 'json_to_solo'

class Zigzag082a4192(Solo48):
    icon_id = 'zigzag-082a4192'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('zigzag', 'interface-essential')

    def build(self):
        self.add_line('e0', (24, 10), (33, 4))
        self.add_line('e1', (8, 44), (8, 24))
        self.add_line('e2', (10, 22), (29, 31))
        self.add_line('e3', (33, 29), (33, 4))
        self.add_line('e4', (40, 10), (33, 4))
        self.add_bezier('e5', (8, 24), ((8, 23.945), (8, 23.9), (8, 23.845)), ((8, 22.882), (9.052, 22.282), (10, 22)))
        self.add_bezier('e6', (29, 31), ((31.363, 31.127), (32.175, 30.627), (33, 29)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e5', 'e2', 'e6', 'e3')
        self.add_contour('c2', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
