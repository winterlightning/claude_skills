"""Judo athlete man (avatars), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bc792bf4-601d-4b62-be0e-ae9f2cb6db06'
SOURCE_PATH = 'icons-json/avatars/judo athlete man_bc792bf4-601d-4b62-be0e-ae9f2cb6db06.json'
AUTHOR = 'json_to_solo'

class JudoAthleteManAvatars(Solo48):
    icon_id = 'judo-athlete-man-avatars'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('judo', 'athlete', 'man', 'avatars')

    def build(self):
        self.add_line('e0', (40, 20), (32, 20))
        self.add_arc('e1-1', (32, 20), (20, 16), radius_x=25)
        self.add_line('e1-2', (20, 16), (18, 15))
        self.add_arc('e1-3', (18, 15), (8, 20), radius_x=14)
        self.add_line('e2-1', (40, 20), (39, 32))
        self.add_arc('e2-2', (39, 32), (34, 40), radius_x=19)
        self.add_arc('e2-3', (34, 40), (24, 44), radius_x=15)
        self.add_arc('e2-4', (24, 44), (19, 43), radius_x=13)
        self.add_arc('e2-5', (19, 43), (12, 38), radius_x=16)
        self.add_arc('e2-6', (12, 38), (9, 32), radius_x=21)
        self.add_line('e2-7', (9, 32), (8, 25))
        self.add_line('e2-8', (8, 25), (8, 20))
        self.add_arc('e3-1', (40, 20), (24, 4), radius_x=17, sweep=False)
        self.add_arc('e3-2', (24, 4), (8, 19), radius_x=17, sweep=False)
        self.add_line('e3-3', (8, 19), (8, 20))
        self.add_contour('c0', 'e0', 'e1-1', 'e1-2', 'e1-3')
        self.add_contour('c1', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e2-6', 'e2-7', 'e2-8')
        self.add_contour('c2', 'e3-1', 'e3-2', 'e3-3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
