"""Lab protection glasses (science), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c6456c8f-9c22-54f5-8ffc-ddc18ca120ed'
SOURCE_PATH = 'icons-json/science/lab protection glasses_c6456c8f-9c22-54f5-8ffc-ddc18ca120ed.json'
AUTHOR = 'gpt-6'

class LabProtectionGlasses(Solo48):
    icon_id = 'lab-protection-glasses'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'science'
    aliases = ()
    keywords = ('lab', 'protection', 'glasses', 'science')

    def build(self):
        self.add_line('sym-e0', (24, 20), (35, 20))
        self.add_line('sym-e2', (35, 20), (41, 22))
        self.add_line('sym-e3', (41, 22), (43, 22))
        self.add_line('sym-e4', (43, 22), (44, 25))
        self.add_line('sym-e5', (44, 25), (44, 31))
        self.add_arc('sym-e6', (44, 31), (44, 32), radius_x=34, radius_y=34, large_arc=False, sweep=False)
        self.add_line('sym-e7', (44, 32), (42, 37))
        self.add_line('sym-e8', (42, 37), (40, 38))
        self.add_line('sym-e9', (40, 38), (33, 40))
        self.add_arc('sym-e10', (33, 40), (32, 40), radius_x=34, radius_y=34, large_arc=False, sweep=False)
        self.add_arc('sym-e11', (32, 40), (29, 36), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('sym-e12', (29, 36), (27, 31))
        self.add_arc('sym-e13', (27, 31), (24, 30), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_arc('sym-e14', (24, 30), (21, 31), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('sym-e15', (21, 31), (19, 36))
        self.add_arc('sym-e16', (19, 36), (16, 40), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('sym-e17', (16, 40), (15, 40), radius_x=23, radius_y=23, large_arc=False, sweep=False)
        self.add_line('sym-e18', (15, 40), (8, 38))
        self.add_arc('sym-e19', (8, 38), (6, 37), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('sym-e20', (6, 37), (4, 32), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('sym-e21', (4, 32), (4, 25))
        self.add_arc('sym-e23', (4, 25), (5, 22), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_line('sym-e24', (5, 22), (7, 22))
        self.add_line('sym-e25', (7, 22), (13, 20))
        self.add_line('sym-e26', (13, 20), (24, 20))
        self.add_arc('sym-e28', (31, 10), (34, 8), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('sym-e30', (34, 8), (39, 13), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('sym-e31', (39, 13), (43, 22))
        self.add_line('sym-e32', (17, 10), (14, 8))
        self.add_arc('sym-e34', (14, 8), (9, 13), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_line('sym-e35', (9, 13), (5, 22))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', closed=True)
        self.add_contour('sym-c1', 'sym-e28', 'sym-e30', 'sym-e31', closed=False)
        self.add_contour('sym-c2', 'sym-e32', 'sym-e34', 'sym-e35', closed=False)
