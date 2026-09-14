"""Design tool magnet (design), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0e02914e-c94e-4b48-b911-4bfe965bc93a'
SOURCE_PATH = 'icons-json/design/design tool magnet_0e02914e-c94e-4b48-b911-4bfe965bc93a.json'
AUTHOR = 'json_to_solo'

class DesignToolMagnetDesign(Solo48):
    icon_id = 'design-tool-magnet-design'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('design', 'tool', 'magnet')

    def build(self):
        self.add_line('e0', (6, 15), (17, 15))
        self.add_line('e1', (6, 15), (6, 6))
        self.add_line('e2', (6, 6), (17, 6))
        self.add_line('e3', (17, 6), (17, 15))
        self.add_line('e4', (6, 15), (6, 24))
        self.add_line('e5', (42, 25), (42, 15))
        self.add_line('e6', (17, 15), (17, 23))
        self.add_line('e7', (31, 23), (31, 15))
        self.add_line('e8', (31, 15), (42, 15))
        self.add_line('e9', (31, 15), (31, 6))
        self.add_line('e10', (31, 6), (42, 6))
        self.add_line('e11', (42, 6), (42, 15))
        self.add_arc('e12-1', (6, 24), (24, 42), radius_x=18, sweep=False)
        self.add_arc('e12-2', (24, 42), (42, 25), radius_x=19, sweep=False)
        self.add_arc('e13-1', (17, 23), (22, 31), radius_x=8, sweep=False)
        self.add_arc('e13-2', (22, 31), (31, 23), radius_x=7, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e3')
        self.add_contour('c2', 'e4', 'e12-1', 'e12-2', 'e5')
        self.add_contour('c3', 'e6', 'e13-1', 'e13-2', 'e7')
        self.add_contour('c4', 'e8')
        self.add_contour('c5', 'e9', 'e10', 'e11')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
