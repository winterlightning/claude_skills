"""Sidebar dots right (apps), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
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
        self.add_arc('sym-e2', (42, 8), (44, 10), radius_x=2)
        self.add_line('sym-e3', (44, 10), (44, 24))
        self.add_line('sym-e4', (44, 24), (44, 38))
        self.add_arc('sym-e5', (44, 38), (42, 40), radius_x=2)
        self.add_line('sym-e6', (42, 40), (30, 40))
        self.add_line('sym-e7', (30, 40), (6, 40))
        self.add_arc('sym-e8', (6, 40), (5, 40), radius_x=1, sweep=False)
        self.add_arc('sym-e9', (5, 40), (4, 39), radius_x=2, sweep=False)
        self.add_line('sym-e10', (4, 39), (4, 24))
        self.add_line('sym-e11', (4, 24), (4, 9))
        self.add_line('sym-e12', (4, 9), (5, 8))
        self.add_line('sym-e13', (5, 8), (6, 8))
        self.add_line('sym-e14', (6, 8), (30, 8))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14')
