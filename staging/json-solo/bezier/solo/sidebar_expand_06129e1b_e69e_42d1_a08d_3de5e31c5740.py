"""Sidebar expand (apps), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '06129e1b-e69e-42d1-a08d-3de5e31c5740'
SOURCE_PATH = 'icons-json/apps/sidebar expand_06129e1b-e69e-42d1-a08d-3de5e31c5740.json'
AUTHOR = 'json_to_solo'

class SidebarExpandApps(Solo48):
    icon_id = 'sidebar-expand-apps'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'apps'
    aliases = ()
    keywords = ('sidebar', 'expand', 'apps')

    def build(self):
        self.add_line('e0', (16, 42), (40, 42))
        self.add_line('e1', (42, 40), (42, 8))
        self.add_line('e2', (40, 6), (16, 6))
        self.add_line('e3', (16, 42), (16, 6))
        self.add_line('e4', (16, 42), (8, 42))
        self.add_line('e5', (6, 40), (6, 8))
        self.add_line('e6', (8, 6), (16, 6))
        self.add_line('e7', (31, 17), (24, 24))
        self.add_line('e8', (24, 24), (31, 31))
        self.add_bezier('e9', (40, 42), ((41.53, 41.493), (41.468, 41.522), (42, 40)))
        self.add_bezier('e10', (42, 8), ((42, 7.959), (41.992, 8.381), (41.992, 8.34)), ((41.992, 7.219), (40.843, 6.548), (40, 6)))
        self.add_bezier('e11', (8, 42), ((6.478, 41.435), (6.565, 41.53), (6, 40)))
        self.add_bezier('e12', (6, 8), ((6, 7.926), (6.008, 8.315), (6.008, 8.242)), ((6.008, 7.17), (7.198, 6.499), (8, 6)))
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
