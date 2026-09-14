"""Dynamic (diagrams), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ea1bde8b-e7f7-4fc3-b915-1043468acb6d'
SOURCE_PATH = 'icons-json/diagrams/dynamic_ea1bde8b-e7f7-4fc3-b915-1043468acb6d.json'
AUTHOR = 'json_to_solo'

class DynamicDiagrams(Solo48):
    icon_id = 'dynamic-diagrams'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'diagrams'
    aliases = ()
    keywords = ('dynamic', 'diagrams')

    def build(self):
        self.add_line('e0', (11, 32), (11, 26))
        self.add_line('e1', (13, 24), (35, 24))
        self.add_arc('e2-top', (6, 37), (16, 37), radius_x=5)
        self.add_arc('e2-bottom', (16, 37), (6, 37), radius_x=5)
        self.add_arc('e3-top', (32, 11), (42, 11), radius_x=5)
        self.add_arc('e3-bottom', (42, 11), (32, 11), radius_x=5)
        self.add_bezier('e4', (11, 26), ((11.442, 25.035), (12.067, 24.466), (13, 24)))
        self.add_bezier('e5', (35, 24), ((35.573, 23.722), (35.725, 23.485), (36.117, 22.928)), ((37.009, 21.652), (36.665, 17.726), (37, 16)))
        self.add_contour('c0', 'e0', 'e4', 'e1', 'e5')
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
        self.relate('connect', 'c0', 'e2')
        self.relate('connect', 'c0', 'e3')
