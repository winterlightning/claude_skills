"""Design tool magnet (design), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e12', (6, 24), ((6, 24.106), (6, 24.205), (6.008, 24.311)), ((6.008, 25.865), (6.409, 27.51), (6.867, 28.983)), ((9.134, 36.191), (15.769, 41.992), (23.542, 41.992)), ((23.622, 41.992), (23.703, 42), (23.783, 42)), ((23.785, 42), (23.786, 42), (23.787, 42)), ((24.074, 42), (24.36, 41.992), (24.646, 41.992)), ((32.583, 41.992), (39.398, 35.79), (41.354, 28.336)), ((41.648, 27.224), (42, 26.145), (42, 25)))
        self.add_bezier('e13', (17, 23), ((17, 29.66), (24.524, 34.579), (29.302, 28.876)), ((29.956, 28.099), (30.431, 27.175), (30.725, 26.209)), ((31.012, 25.293), (31, 23.974), (31, 23)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e3')
        self.add_contour('c2', 'e4', 'e12', 'e5')
        self.add_contour('c3', 'e6', 'e13', 'e7')
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
