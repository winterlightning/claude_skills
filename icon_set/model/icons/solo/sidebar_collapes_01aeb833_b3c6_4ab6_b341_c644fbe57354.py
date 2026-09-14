"""Sidebar collapes (apps), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '01aeb833-b3c6-4ab6-b341-c644fbe57354'
SOURCE_PATH = 'icons-json/apps/sidebar collapes_01aeb833-b3c6-4ab6-b341-c644fbe57354.json'
AUTHOR = 'json_to_solo'

class SidebarCollapes(Solo48):
    icon_id = 'sidebar-collapes'
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
        self.add_arc('e9', (41, 8), (44, 11), radius_x=3)
        self.add_arc('e10', (44, 37), (41, 40), radius_x=3)
        self.add_arc('e11', (7, 8), (4, 11), radius_x=3, sweep=False)
        self.add_arc('e12', (4, 37), (7, 40), radius_x=3, sweep=False)
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
