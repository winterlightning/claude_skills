"""Sidebar dots right (apps), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f1582b2e-7e62-55c0-b217-5620ae37d80d'
SOURCE_PATH = 'icons-json/apps/sidebar dots right_f1582b2e-7e62-55c0-b217-5620ae37d80d.json'
AUTHOR = 'json_to_solo'

class SidebarDotsRightApps(Solo48):
    icon_id = 'sidebar-dots-right-apps'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'apps'
    aliases = ()
    keywords = ('sidebar', 'dots', 'right', 'apps')

    def build(self):
        self.add_line('sym-e0', (30, 40), (30, 8))
        self.add_line('sym-e1', (30, 8), (42, 8))
        self.add_bezier('sym-e2', (42, 8), ((43.264, 8.396), (43.582, 8.829), (44, 10)))
        self.add_line('sym-e3', (44, 10), (44, 24))
        self.add_line('sym-e4', (44, 24), (44, 38))
        self.add_bezier('sym-e5', (44, 38), ((43.582, 39.171), (43.264, 39.604), (42, 40)))
        self.add_line('sym-e6', (42, 40), (30, 40))
        self.add_line('sym-e7', (30, 40), (6, 40))
        self.add_bezier('sym-e8', (6, 40), ((5.836, 40), (5.164, 40), (5, 40)))
        self.add_bezier('sym-e9', (5, 40), ((4.336, 40), (4.4, 39.387), (4, 39)))
        self.add_line('sym-e10', (4, 39), (4, 24))
        self.add_line('sym-e11', (4, 24), (4, 9))
        self.add_bezier('sym-e12', (4, 9), ((4.4, 8.613), (4.336, 8), (5, 8)))
        self.add_bezier('sym-e13', (5, 8), ((5.164, 8), (5.836, 8), (6, 8)))
        self.add_line('sym-e14', (6, 8), (30, 8))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14')
