"""Atom (other), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e1360ae7-7838-4ce4-ab4c-2158d5dcbebb'
SOURCE_PATH = 'icons-json/other/atom_e1360ae7-7838-4ce4-ab4c-2158d5dcbebb.json'
AUTHOR = 'json_to_solo'

class AtomOther(Solo48):
    icon_id = 'atom-other'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('atom', 'other')

    def build(self):
        self.add_line('sym-e0', (24, 22), (24, 26))
        self.add_arc('sym-e1', (40, 24), (38, 22), radius_x=25, sweep=False)
        self.add_arc('sym-e2', (38, 22), (24, 11), radius_x=54, sweep=False)
        self.add_line('sym-e3', (24, 11), (26, 10))
        self.add_arc('sym-e4', (26, 10), (35, 8), radius_x=22)
        self.add_line('sym-e5', (35, 8), (36, 8))
        self.add_line('sym-e7-1', (36, 8), (42, 10))
        self.add_line('sym-e7-2', (42, 10), (44, 15))
        self.add_arc('sym-e8', (44, 15), (44, 16), radius_x=1, sweep=False)
        self.add_arc('sym-e10', (44, 16), (40, 24), radius_x=13)
        self.add_arc('sym-e11', (40, 24), (38, 26), radius_x=25)
        self.add_arc('sym-e12', (38, 26), (24, 37), radius_x=54)
        self.add_line('sym-e13', (24, 37), (26, 38))
        self.add_line('sym-e14', (26, 38), (35, 40))
        self.add_line('sym-e15', (35, 40), (36, 40))
        self.add_line('sym-e17-1', (36, 40), (42, 38))
        self.add_line('sym-e17-2', (42, 38), (44, 33))
        self.add_line('sym-e18', (44, 33), (44, 32))
        self.add_arc('sym-e20', (44, 32), (40, 24), radius_x=13, sweep=False)
        self.add_arc('sym-e21', (8, 24), (10, 22), radius_x=25)
        self.add_arc('sym-e22', (10, 22), (24, 11), radius_x=54)
        self.add_line('sym-e23', (24, 11), (22, 10))
        self.add_arc('sym-e24', (22, 10), (13, 8), radius_x=22, sweep=False)
        self.add_line('sym-e25', (13, 8), (12, 8))
        self.add_line('sym-e27-1', (12, 8), (6, 10))
        self.add_line('sym-e27-2', (6, 10), (4, 15))
        self.add_line('sym-e28', (4, 15), (4, 16))
        self.add_arc('sym-e30', (4, 16), (8, 24), radius_x=13, sweep=False)
        self.add_arc('sym-e31', (8, 24), (10, 26), radius_x=25, sweep=False)
        self.add_arc('sym-e32', (10, 26), (24, 37), radius_x=54, sweep=False)
        self.add_line('sym-e33', (24, 37), (22, 38))
        self.add_arc('sym-e34', (22, 38), (13, 40), radius_x=22)
        self.add_arc('sym-e35', (13, 40), (12, 40), radius_x=22, sweep=False)
        self.add_line('sym-e37-1', (12, 40), (6, 38))
        self.add_line('sym-e37-2', (6, 38), (4, 33))
        self.add_line('sym-e38', (4, 33), (4, 32))
        self.add_arc('sym-e40', (4, 32), (8, 24), radius_x=13)
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e7-1', 'sym-e7-2', 'sym-e8', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e17-1', 'sym-e17-2', 'sym-e18', 'sym-e20', closed=True)
        self.add_contour('sym-c2', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e27-1', 'sym-e27-2', 'sym-e28', 'sym-e30', 'sym-e31', 'sym-e32', 'sym-e33', 'sym-e34', 'sym-e35', 'sym-e37-1', 'sym-e37-2', 'sym-e38', 'sym-e40', closed=True)
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
