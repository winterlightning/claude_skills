"""Judge man (avatars), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e8fb8e23-2308-4fdf-ac4b-d8a8d044a6df'
SOURCE_PATH = 'icons-json/avatars/judge man_e8fb8e23-2308-4fdf-ac4b-d8a8d044a6df.json'
AUTHOR = 'json_to_solo'

class JudgeManAvatars(Solo48):
    icon_id = 'judge-man-avatars'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('judge', 'man', 'avatars')

    def build(self):
        self.add_line('e0', (13, 34), (13, 37))
        self.add_line('e1', (35, 37), (34, 33))
        self.add_arc('e2-1', (13, 34), (18, 18), radius_x=16)
        self.add_arc('e2-2', (18, 18), (30, 18), radius_x=12)
        self.add_arc('e2-3', (30, 18), (34, 33), radius_x=12)
        self.add_arc('e3', (13, 34), (34, 33), radius_x=13, sweep=False)
        self.add_arc('e4-1', (13, 37), (9, 40), radius_x=5)
        self.add_line('e4-2', (9, 40), (5, 39))
        self.add_line('e4-3', (5, 39), (4, 36))
        self.add_arc('e4-4', (4, 36), (6, 33), radius_x=4)
        self.add_arc('e4-5', (6, 33), (4, 30), radius_x=5)
        self.add_arc('e4-6', (4, 30), (7, 26), radius_x=5)
        self.add_arc('e4-7', (7, 26), (8, 16), radius_x=16)
        self.add_arc('e4-8', (8, 16), (17, 9), radius_x=16)
        self.add_line('e4-9', (17, 9), (24, 8))
        self.add_line('e4-10', (24, 8), (31, 9))
        self.add_arc('e4-11', (31, 9), (39, 15), radius_x=15)
        self.add_arc('e4-12', (39, 15), (42, 27), radius_x=17)
        self.add_line('e4-13', (42, 27), (44, 30))
        self.add_arc('e4-14', (44, 30), (42, 33), radius_x=4)
        self.add_arc('e4-15', (42, 33), (44, 36), radius_x=4)
        self.add_line('e4-16', (44, 36), (43, 39))
        self.add_line('e4-17', (43, 39), (39, 40))
        self.add_arc('e4-18', (39, 40), (35, 37), radius_x=5)
        self.add_contour('c0', 'e2-1', 'e2-2', 'e2-3')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e0', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5', 'e4-6', 'e4-7', 'e4-8', 'e4-9', 'e4-10', 'e4-11', 'e4-12', 'e4-13', 'e4-14', 'e4-15', 'e4-16', 'e4-17', 'e4-18', 'e1')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
