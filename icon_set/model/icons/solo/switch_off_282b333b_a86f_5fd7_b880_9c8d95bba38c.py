"""Switch off (furnitures), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '282b333b-a86f-5fd7-b880-9c8d95bba38c'
SOURCE_PATH = 'icons-json/furnitures/switch off_282b333b-a86f-5fd7-b880-9c8d95bba38c.json'
AUTHOR = 'gpt-6'

class SwitchOff(Solo48):
    icon_id = 'switch-off'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    aliases = ()
    keywords = ('switch', 'off', 'furnitures')

    def build(self):
        self.add_line('sym-e0', (30, 24), (18, 24))
        self.add_line('sym-e1', (18, 24), (18, 33))
        self.add_arc('sym-e2', (18, 33), (20, 35), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('sym-e3', (20, 35), (28, 35))
        self.add_arc('sym-e5', (28, 35), (30, 33), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('sym-e6', (30, 33), (30, 15))
        self.add_arc('sym-e8', (30, 15), (28, 13), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('sym-e9', (28, 13), (20, 13))
        self.add_arc('sym-e11', (20, 13), (18, 15), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('sym-e12', (18, 15), (18, 24))
        self.add_line('sym-e13', (24, 44), (37, 44))
        self.add_arc('sym-e15', (37, 44), (40, 41), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('sym-e16', (40, 41), (40, 7))
        self.add_arc('sym-e18', (40, 7), (37, 4), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('sym-e20', (37, 4), (11, 4))
        self.add_arc('sym-e23', (11, 4), (8, 7), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('sym-e24', (8, 7), (8, 41))
        self.add_arc('sym-e26', (8, 41), (11, 44), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('sym-e28', (11, 44), (24, 44))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e5', 'sym-e6', 'sym-e8', 'sym-e9', 'sym-e11', 'sym-e12', closed=False)
        self.add_contour('sym-c1', 'sym-e13', 'sym-e15', 'sym-e16', 'sym-e18', 'sym-e20', 'sym-e23', 'sym-e24', 'sym-e26', 'sym-e28', closed=True)
