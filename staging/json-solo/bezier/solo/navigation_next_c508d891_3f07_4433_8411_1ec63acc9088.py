"""Navigation next (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c508d891-3f07-4433-8411-1ec63acc9088'
SOURCE_PATH = 'icons-json/interface-essential/navigation next_c508d891-3f07-4433-8411-1ec63acc9088.json'
AUTHOR = 'json_to_solo'

class NavigationNextInterfaceEssential(Solo48):
    icon_id = 'navigation-next-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('navigation', 'next', 'interface-essential')

    def build(self):
        self.add_line('e0', (37, 8), (42, 14))
        self.add_line('e1', (42, 14), (44, 16))
        self.add_line('e2', (26, 16), (44, 16))
        self.add_line('e3', (37, 25), (44, 16))
        self.add_line('e4', (25, 8), (5, 8))
        self.add_line('e5', (4, 10), (4, 38))
        self.add_line('e6', (6, 40), (25, 40))
        self.add_line('e7', (28, 38), (28, 26))
        self.add_bezier('e8', (18, 31), ((18.055, 26.2), (17.264, 20.51), (21.445, 17.52)), ((22.736, 16.61), (24.455, 16), (26, 16)))
        self.add_bezier('e9', (5, 8), ((4.718, 8.42), (4.209, 8.86), (4.064, 9.37)), ((4.009, 9.57), (4.064, 9.8), (4, 10)))
        self.add_bezier('e10', (4, 38), ((4.055, 38.16), (4.027, 38.35), (4.091, 38.51)), ((4.336, 39.22), (5.273, 40), (6, 40)))
        self.add_bezier('e11', (25, 40), ((25.218, 40), (25.345, 39.98), (25.564, 39.98)), ((26.527, 39.98), (28, 39.18), (28, 38)))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e8', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4', 'e9', 'e5', 'e10', 'e6', 'e11', 'e7')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
