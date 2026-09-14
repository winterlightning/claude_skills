"""Ghost scare (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd3eaffac-83bd-5771-b93b-97075edcfae5'
SOURCE_PATH = 'icons-json/smileys/ghost scare_d3eaffac-83bd-5771-b93b-97075edcfae5.json'
AUTHOR = 'json_to_solo'

class GhostScare(Solo48):
    icon_id = 'ghost-scare'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('ghost', 'scare', 'smileys')

    def build(self):
        self.add_arc('sym-e0', (13, 21), (7, 18), radius_x=19)
        self.add_arc('sym-e1', (7, 18), (5, 16), radius_x=28, sweep=False)
        self.add_line('sym-e3', (5, 16), (4, 16))
        self.add_line('sym-e4', (4, 16), (4, 17))
        self.add_line('sym-e6', (4, 17), (4, 18))
        self.add_arc('sym-e7', (4, 18), (5, 21), radius_x=8, sweep=False)
        self.add_arc('sym-e8', (5, 21), (13, 29), radius_x=17, sweep=False)
        self.add_arc('sym-e9', (13, 29), (11, 35), radius_x=11)
        self.add_line('sym-e10', (11, 35), (9, 38))
        self.add_line('sym-e11', (9, 38), (12, 40))
        self.add_line('sym-e12', (12, 40), (19, 39))
        self.add_line('sym-e13', (19, 39), (24, 40))
        self.add_line('sym-e19', (24, 40), (29, 39))
        self.add_line('sym-e20', (29, 39), (36, 40))
        self.add_line('sym-e21', (36, 40), (39, 38))
        self.add_line('sym-e22', (39, 38), (37, 35))
        self.add_arc('sym-e23', (37, 35), (35, 29), radius_x=11)
        self.add_arc('sym-e24', (35, 29), (43, 21), radius_x=16, sweep=False)
        self.add_line('sym-e25', (43, 21), (44, 18))
        self.add_line('sym-e26', (44, 18), (44, 17))
        self.add_line('sym-e28', (44, 17), (44, 16))
        self.add_line('sym-e29', (44, 16), (43, 16))
        self.add_arc('sym-e31', (43, 16), (41, 18), radius_x=27, sweep=False)
        self.add_arc('sym-e32', (41, 18), (35, 21), radius_x=19)
        self.add_line('sym-e33', (35, 21), (35, 17))
        self.add_line('sym-e34', (35, 17), (34, 15))
        self.add_arc('sym-e35', (34, 15), (25, 8), radius_x=10, sweep=False)
        self.add_line('sym-e36', (25, 8), (24, 8))
        self.add_arc('sym-e37', (24, 8), (23, 8), radius_x=37)
        self.add_arc('sym-e38', (23, 8), (14, 15), radius_x=10, sweep=False)
        self.add_line('sym-e39', (14, 15), (13, 17))
        self.add_line('sym-e40', (13, 17), (13, 21))
        self.add_line('sym-e41', (13, 21), (13, 29))
        self.add_line('sym-e43', (35, 21), (35, 29))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e3', 'sym-e4', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e28', 'sym-e29', 'sym-e31', 'sym-e32', 'sym-e33', 'sym-e34', 'sym-e35', 'sym-e36', 'sym-e37', 'sym-e38', 'sym-e39', 'sym-e40', 'sym-e41')
        self.add_contour('sym-c2', 'sym-e43')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
