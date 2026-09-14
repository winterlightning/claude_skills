"""Meta quest (technology), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9210afd9-195d-52c8-ae01-b8d2485089f3'
SOURCE_PATH = 'icons-json/technology/meta quest_9210afd9-195d-52c8-ae01-b8d2485089f3.json'
AUTHOR = 'json_to_solo'

class MetaQuest(Solo48):
    icon_id = 'meta-quest'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    aliases = ()
    keywords = ('meta', 'quest', 'technology')

    def build(self):
        self.add_arc('sym-e0', (39, 19), (38, 14), radius_x=26)
        self.add_arc('sym-e1', (38, 14), (29, 8), radius_x=11, sweep=False)
        self.add_line('sym-e3', (29, 8), (24, 8))
        self.add_line('sym-e4', (24, 8), (19, 8))
        self.add_arc('sym-e6', (19, 8), (10, 14), radius_x=11, sweep=False)
        self.add_arc('sym-e7', (10, 14), (9, 19), radius_x=26)
        self.add_arc('sym-e8', (9, 19), (4, 24), radius_x=5, sweep=False)
        self.add_line('sym-e10', (4, 24), (4, 33))
        self.add_line('sym-e11', (4, 33), (4, 35))
        self.add_arc('sym-e12', (4, 35), (8, 40), radius_x=6, sweep=False)
        self.add_arc('sym-e13', (8, 40), (9, 40), radius_x=20)
        self.add_line('sym-e14', (9, 40), (17, 40))
        self.add_arc('sym-e15', (17, 40), (18, 39), radius_x=6, sweep=False)
        self.add_line('sym-e16', (18, 39), (21, 36))
        self.add_line('sym-e17', (21, 36), (24, 35))
        self.add_line('sym-e18', (24, 35), (27, 36))
        self.add_line('sym-e19', (27, 36), (30, 39))
        self.add_arc('sym-e20', (30, 39), (31, 40), radius_x=7, sweep=False)
        self.add_line('sym-e21', (31, 40), (39, 40))
        self.add_line('sym-e22', (39, 40), (40, 40))
        self.add_arc('sym-e23', (40, 40), (44, 35), radius_x=6, sweep=False)
        self.add_line('sym-e24-1', (44, 35), (44, 34))
        self.add_line('sym-e24-2', (44, 34), (44, 33))
        self.add_line('sym-e25', (44, 33), (44, 24))
        self.add_arc('sym-e27', (44, 24), (39, 19), radius_x=5, sweep=False)
        self.add_arc('sym-e28', (39, 19), (36, 19), radius_x=70, sweep=False)
        self.add_line('sym-e29', (36, 19), (24, 19))
        self.add_line('sym-e30', (24, 19), (12, 19))
        self.add_arc('sym-e31', (12, 19), (9, 19), radius_x=70, sweep=False)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e3', 'sym-e4', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24-1', 'sym-e24-2', 'sym-e25', 'sym-e27', 'sym-e28', 'sym-e29', 'sym-e30', 'sym-e31')
