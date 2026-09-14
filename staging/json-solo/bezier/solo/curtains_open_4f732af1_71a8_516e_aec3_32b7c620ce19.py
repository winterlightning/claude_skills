"""Curtains open (building), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4f732af1-71a8-516e-aec3-32b7c620ce19'
SOURCE_PATH = 'icons-json/building/curtains open_4f732af1-71a8-516e-aec3-32b7c620ce19.json'
AUTHOR = 'json_to_solo'

class CurtainsOpenBuilding(Solo48):
    icon_id = 'curtains-open-building'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    aliases = ()
    keywords = ('curtains', 'open', 'building')

    def build(self):
        self.add_bezier('sym-e0', (35, 26), ((32.374, 31.335), (32.188, 36.15), (32, 42)))
        self.add_line('sym-e1', (32, 42), (42, 42))
        self.add_line('sym-e2', (42, 42), (42, 26))
        self.add_line('sym-e3', (42, 26), (42, 6))
        self.add_line('sym-e4', (42, 6), (26, 6))
        self.add_line('sym-e5', (26, 6), (24, 6))
        self.add_line('sym-e6', (24, 6), (22, 6))
        self.add_line('sym-e7', (22, 6), (6, 6))
        self.add_line('sym-e8', (6, 6), (6, 26))
        self.add_line('sym-e9', (6, 26), (6, 42))
        self.add_line('sym-e10', (6, 42), (16, 42))
        self.add_bezier('sym-e11', (16, 42), ((15.812, 36.15), (15.626, 31.335), (13, 26)))
        self.add_line('sym-e12', (13, 26), (6, 26))
        self.add_line('sym-e13', (35, 26), (42, 26))
        self.add_bezier('sym-e14', (35, 26), ((28.397, 21.484), (26.319, 13.74), (26, 6)))
        self.add_bezier('sym-e15', (13, 26), ((19.603, 21.484), (21.681, 13.74), (22, 6)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12')
        self.add_contour('sym-c1', 'sym-e13')
        self.add_contour('sym-c2', 'sym-e14')
        self.add_contour('sym-c3', 'sym-e15')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
