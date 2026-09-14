"""Tooth (health), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9ec250e0-3b4c-4302-a78f-3f0f5baf59cb'
SOURCE_PATH = 'icons-json/health/tooth_9ec250e0-3b4c-4302-a78f-3f0f5baf59cb.json'
AUTHOR = 'json_to_solo'

class Tooth9ec250e0(Solo48):
    icon_id = 'tooth-9ec250e0'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('tooth', 'health')

    def build(self):
        self.add_line('sym-e0', (18, 37), (16, 42))
        self.add_arc('sym-e1', (16, 42), (14, 44), radius_x=3)
        self.add_arc('sym-e2', (14, 44), (11, 42), radius_x=4, sweep=False)
        self.add_arc('sym-e3', (11, 42), (11, 32), radius_x=18)
        self.add_line('sym-e4', (11, 32), (11, 28))
        self.add_arc('sym-e5', (11, 28), (9, 20), radius_x=14, sweep=False)
        self.add_arc('sym-e6', (9, 20), (8, 15), radius_x=14)
        self.add_line('sym-e7', (8, 15), (8, 14))
        self.add_line('sym-e8', (8, 14), (8, 13))
        self.add_arc('sym-e9', (8, 13), (16, 4), radius_x=10)
        self.add_line('sym-e10', (16, 4), (24, 6))
        self.add_line('sym-e13', (24, 6), (32, 4))
        self.add_arc('sym-e14', (32, 4), (40, 13), radius_x=10)
        self.add_arc('sym-e15', (40, 13), (40, 14), radius_x=23, sweep=False)
        self.add_arc('sym-e16', (40, 14), (40, 15), radius_x=1, sweep=False)
        self.add_arc('sym-e17', (40, 15), (39, 20), radius_x=14)
        self.add_arc('sym-e18', (39, 20), (37, 28), radius_x=14, sweep=False)
        self.add_line('sym-e19', (37, 28), (37, 32))
        self.add_arc('sym-e20', (37, 32), (37, 42), radius_x=18)
        self.add_arc('sym-e21', (37, 42), (34, 44), radius_x=4, sweep=False)
        self.add_arc('sym-e22', (34, 44), (32, 42), radius_x=3)
        self.add_line('sym-e23', (32, 42), (30, 37))
        self.add_arc('sym-e24', (30, 37), (28, 33), radius_x=12, sweep=False)
        self.add_arc('sym-e25', (28, 33), (24, 31), radius_x=5, sweep=False)
        self.add_arc('sym-e26', (24, 31), (20, 33), radius_x=5, sweep=False)
        self.add_arc('sym-e27', (20, 33), (18, 37), radius_x=12, sweep=False)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', closed=True)
