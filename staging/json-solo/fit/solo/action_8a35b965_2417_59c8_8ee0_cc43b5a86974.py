"""Action (diagrams), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8a35b965-2417-59c8-8ee0-cc43b5a86974'
SOURCE_PATH = 'icons-json/diagrams/action_8a35b965-2417-59c8-8ee0-cc43b5a86974.json'
AUTHOR = 'json_to_solo'

class ActionDiagrams(Solo48):
    icon_id = 'action-diagrams'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'diagrams'
    aliases = ()
    keywords = ('action', 'diagrams')

    def build(self):
        self.add_line('e0', (33, 31), (26, 31))
        self.add_line('e1', (21, 23), (13, 18))
        self.add_line('e2', (21, 23), (13, 28))
        self.add_line('e3', (13, 28), (6, 23))
        self.add_line('e4', (6, 23), (13, 18))
        self.add_line('e5', (21, 23), (32, 23))
        self.add_line('e6', (13, 18), (13, 13))
        self.add_line('e7', (13, 28), (13, 32))
        self.add_line('e8', (11, 6), (17, 6))
        self.add_line('e9', (17, 13), (13, 13))
        self.add_line('e10', (42, 19), (32, 19))
        self.add_line('e11', (32, 19), (32, 26))
        self.add_line('e12', (32, 26), (42, 26))
        self.add_line('e13', (42, 26), (42, 19))
        self.add_arc('e14-top', (8, 37), (18, 37), radius_x=5)
        self.add_arc('e14-bottom', (18, 37), (8, 37), radius_x=5)
        self.add_arc('e15', (37, 26), (33, 31), radius_x=4)
        self.add_arc('e16-1', (13, 13), (10, 6), radius_x=4, large_arc=True)
        self.add_arc('e16-2', (10, 6), (11, 6), radius_x=11, sweep=False)
        self.add_arc('e17-1', (17, 6), (20, 11), radius_x=4)
        self.add_arc('e17-2', (20, 11), (17, 13), radius_x=3)
        self.add_contour('c0', 'e15', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3', 'e4')
        self.add_contour('c3', 'e5')
        self.add_contour('c4', 'e6')
        self.add_contour('c5', 'e7')
        self.add_contour('c6', 'e16-1', 'e16-2', 'e8', 'e17-1', 'e17-2', 'e9', closed=True)
        self.add_contour('c7', 'e10', 'e11', 'e12', 'e13', closed=True)
        self.add_contour('e14', 'e14-top', 'e14-bottom', closed=True)
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c0', 'c7')
        self.relate('connect', 'c3', 'c7')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c5', 'e14')
