"""Sidebar collapes (apps), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '01aeb833-b3c6-4ab6-b341-c644fbe57354'
SOURCE_PATH = 'icons-json/apps/sidebar collapes_01aeb833-b3c6-4ab6-b341-c644fbe57354.json'
AUTHOR = 'json_to_solo'

class SidebarCollapesApps(Solo48):
    icon_id = 'sidebar-collapes-apps'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'apps'
    aliases = ()
    keywords = ('sidebar', 'collapes', 'apps')

    def build(self):
        self.add_line('e0', (32, 8), (41, 8))
        self.add_line('e1', (44, 11), (44, 37))
        self.add_line('e2', (41, 40), (32, 40))
        self.add_line('e3', (32, 8), (32, 40))
        self.add_line('e4', (32, 8), (7, 8))
        self.add_line('e5', (4, 11), (4, 37))
        self.add_line('e6', (7, 40), (32, 40))
        self.add_line('e7', (17, 18), (23, 24))
        self.add_line('e8', (23, 24), (17, 30))
        self.add_bezier('e9', (41, 8), ((42.318, 8), (44, 9.787), (44, 11)))
        self.add_bezier('e10', (44, 37), ((44, 37.034), (43.991, 37.549), (43.991, 37.583)), ((43.991, 38.829), (42.318, 40), (41, 40)))
        self.add_bezier('e11', (7, 8), ((5.545, 8), (4.391, 9.947), (4, 11)))
        self.add_bezier('e12', (4, 37), ((4.445, 38.036), (5.545, 40), (7, 40)))
        self.add_contour('c0', 'e0', 'e9', 'e1', 'e10', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4', 'e11', 'e5', 'e12', 'e6')
        self.add_contour('c3', 'e7', 'e8')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
