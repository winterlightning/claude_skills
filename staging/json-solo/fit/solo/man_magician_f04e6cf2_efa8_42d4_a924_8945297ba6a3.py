"""Man magician (avatars), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f04e6cf2-efa8-42d4-a924-8945297ba6a3'
SOURCE_PATH = 'icons-json/avatars/man magician_f04e6cf2-efa8-42d4-a924-8945297ba6a3.json'
AUTHOR = 'json_to_solo'

class ManMagicianAvatars(Solo48):
    icon_id = 'man-magician-avatars'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('man', 'magician', 'avatars')

    def build(self):
        self.add_line('sym-e0', (12, 18), (36, 18))
        self.add_line('sym-e1', (4, 24), (12, 25))
        self.add_line('sym-e2', (12, 25), (11, 9))
        self.add_arc('sym-e3', (11, 9), (22, 8), radius_x=79)
        self.add_line('sym-e4', (22, 8), (23, 8))
        self.add_arc('sym-e5', (23, 8), (24, 8), radius_x=39, sweep=False)
        self.add_arc('sym-e6', (24, 8), (25, 8), radius_x=40, sweep=False)
        self.add_line('sym-e7', (25, 8), (26, 8))
        self.add_line('sym-e8', (26, 8), (37, 9))
        self.add_line('sym-e9', (37, 9), (36, 25))
        self.add_line('sym-e10', (36, 25), (44, 24))
        self.add_line('sym-e11', (24, 25), (12, 25))
        self.add_line('sym-e12', (12, 25), (13, 31))
        self.add_line('sym-e13', (13, 31), (14, 35))
        self.add_arc('sym-e14', (14, 35), (23, 40), radius_x=11, sweep=False)
        self.add_arc('sym-e16', (23, 40), (24, 40), radius_x=27)
        self.add_line('sym-e17', (24, 40), (25, 40))
        self.add_arc('sym-e19', (25, 40), (34, 35), radius_x=11, sweep=False)
        self.add_line('sym-e20', (34, 35), (35, 31))
        self.add_line('sym-e21', (35, 31), (36, 25))
        self.add_line('sym-e22', (36, 25), (24, 25))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10')
        self.add_contour('sym-c2', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e16', 'sym-e17', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', closed=True)
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
