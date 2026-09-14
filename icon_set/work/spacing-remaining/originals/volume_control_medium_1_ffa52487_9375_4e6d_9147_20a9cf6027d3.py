"""Volume control medium 1 (audio), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ffa52487-9375-4e6d-9147-20a9cf6027d3'
SOURCE_PATH = 'icons-json/audio/volume control medium 1_ffa52487-9375-4e6d-9147-20a9cf6027d3.json'
AUTHOR = 'json_to_solo'

class VolumeControlMedium1(Solo48):
    icon_id = 'volume-control-medium-1'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('volume', 'control', 'medium', 'audio')

    def build(self):
        self.add_arc('sym-e0', (42, 24), (42, 23), radius_x=28)
        self.add_arc('sym-e1', (42, 23), (38, 13), radius_x=15, sweep=False)
        self.add_arc('sym-e2', (36, 24), (35, 19), radius_x=8, sweep=False)
        self.add_line('sym-e3', (6, 24), (6, 19))
        self.add_arc('sym-e5', (6, 19), (8, 17), radius_x=2)
        self.add_line('sym-e6', (8, 17), (16, 17))
        self.add_arc('sym-e7', (16, 17), (17, 17), radius_x=17)
        self.add_line('sym-e8', (17, 17), (26, 6))
        self.add_arc('sym-e9', (26, 6), (27, 6), radius_x=61, sweep=False)
        self.add_line('sym-e12', (27, 6), (28, 6))
        self.add_line('sym-e13', (28, 6), (29, 8))
        self.add_line('sym-e14', (29, 8), (29, 24))
        self.add_line('sym-e15', (29, 24), (29, 40))
        self.add_line('sym-e16', (29, 40), (28, 42))
        self.add_arc('sym-e17', (28, 42), (27, 42), radius_x=31, sweep=False)
        self.add_line('sym-e20', (27, 42), (26, 42))
        self.add_line('sym-e21', (26, 42), (17, 31))
        self.add_arc('sym-e22', (17, 31), (16, 31), radius_x=19, sweep=False)
        self.add_line('sym-e23', (16, 31), (8, 31))
        self.add_arc('sym-e24', (8, 31), (6, 29), radius_x=2)
        self.add_line('sym-e26', (6, 29), (6, 24))
        self.add_arc('sym-e27', (42, 24), (42, 25), radius_x=28, sweep=False)
        self.add_arc('sym-e28', (42, 25), (38, 35), radius_x=15)
        self.add_arc('sym-e29', (36, 24), (35, 29), radius_x=8)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2')
        self.add_contour('sym-c2', 'sym-e3', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e26', closed=True)
        self.add_contour('sym-c3', 'sym-e27', 'sym-e28')
        self.add_contour('sym-c4', 'sym-e29')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c4')
