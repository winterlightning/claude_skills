"""Archive drawer (content), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '72a5da42-f68e-5dd5-b2e5-34d0f9932450'
SOURCE_PATH = 'icons-json/content/archive drawer_72a5da42-f68e-5dd5-b2e5-34d0f9932450.json'
AUTHOR = 'json_to_solo'

class ArchiveDrawerContent(Solo48):
    icon_id = 'archive-drawer-content'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('archive', 'drawer', 'content')

    def build(self):
        self.add_line('sym-e0', (24, 40), (41, 40))
        self.add_line('sym-e1', (41, 40), (42, 40))
        self.add_arc('sym-e2', (42, 40), (44, 38), radius_x=2, sweep=False)
        self.add_arc('sym-e4', (44, 38), (44, 37), radius_x=38)
        self.add_line('sym-e5', (44, 37), (44, 25))
        self.add_arc('sym-e7', (44, 25), (42, 23), radius_x=2, sweep=False)
        self.add_line('sym-e8', (42, 23), (41, 23))
        self.add_arc('sym-e10', (41, 23), (40, 23), radius_x=47)
        self.add_line('sym-e11', (40, 23), (30, 23))
        self.add_arc('sym-e12', (30, 23), (27, 27), radius_x=3)
        self.add_line('sym-e13', (27, 27), (24, 27))
        self.add_line('sym-e14', (24, 27), (21, 27))
        self.add_arc('sym-e15', (21, 27), (18, 23), radius_x=3)
        self.add_line('sym-e16', (18, 23), (8, 23))
        self.add_line('sym-e17', (8, 23), (7, 23))
        self.add_line('sym-e19', (7, 23), (6, 23))
        self.add_arc('sym-e20', (6, 23), (4, 25), radius_x=2, sweep=False)
        self.add_line('sym-e22', (4, 25), (4, 37))
        self.add_line('sym-e23', (4, 37), (4, 38))
        self.add_arc('sym-e25', (4, 38), (6, 40), radius_x=2, sweep=False)
        self.add_line('sym-e26', (6, 40), (7, 40))
        self.add_line('sym-e27', (7, 40), (24, 40))
        self.add_line('sym-e28', (41, 23), (41, 11))
        self.add_arc('sym-e29', (41, 11), (39, 8), radius_x=3, sweep=False)
        self.add_line('sym-e30', (39, 8), (24, 8))
        self.add_line('sym-e31', (24, 8), (9, 8))
        self.add_arc('sym-e32', (9, 8), (7, 11), radius_x=3, sweep=False)
        self.add_line('sym-e33', (7, 11), (7, 23))
        self.add_line('sym-e34', (24, 18), (30, 18))
        self.add_line('sym-e35', (30, 18), (30, 23))
        self.add_line('sym-e36', (24, 18), (18, 18))
        self.add_line('sym-e37', (18, 18), (18, 23))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e4', 'sym-e5', 'sym-e7', 'sym-e8', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e19', 'sym-e20', 'sym-e22', 'sym-e23', 'sym-e25', 'sym-e26', 'sym-e27', closed=True)
        self.add_contour('sym-c1', 'sym-e28', 'sym-e29', 'sym-e30', 'sym-e31', 'sym-e32', 'sym-e33')
        self.add_contour('sym-c2', 'sym-e34', 'sym-e35')
        self.add_contour('sym-c3', 'sym-e36', 'sym-e37')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
