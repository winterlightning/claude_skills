"""Phone flash light (mobile), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a839aab1-1953-4a67-aa15-e9ae49616cd4'
SOURCE_PATH = 'pictographic-primitives/mobile/phone flash light_a839aab1-1953-4a67-aa15-e9ae49616cd4.svg'
AUTHOR = 'gpt-6'

class PhoneFlashLight(Solo48):
    icon_id = 'phone-flash-light'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'mobile'
    categories = ('mobile', 'primitives')
    aliases = ()
    keywords = ('phone', 'flash', 'light', 'mobile')

    def build(self):
        self.add_line('sym-e0', (8, 12), (40, 12))
        self.add_line('sym-e1', (40, 12), (40, 15))
        self.add_arc('sym-e2', (40, 15), (39, 16), radius_x=13, radius_y=13, large_arc=False, sweep=True)
        self.add_line('sym-e3', (39, 16), (33, 22))
        self.add_line('sym-e4', (33, 22), (33, 41))
        self.add_arc('sym-e7', (33, 41), (29, 44), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('sym-e8', (29, 44), (19, 44))
        self.add_arc('sym-e10', (19, 44), (15, 41), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('sym-e11', (15, 41), (15, 22))
        self.add_line('sym-e14', (15, 22), (9, 16))
        self.add_arc('sym-e15', (9, 16), (8, 15), radius_x=13, radius_y=13, large_arc=False, sweep=True)
        self.add_line('sym-e16', (8, 15), (8, 5))
        self.add_arc('sym-e18', (8, 5), (9, 4), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_line('sym-e20', (9, 4), (39, 4))
        self.add_arc('sym-e23', (39, 4), (40, 5), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_line('sym-e24', (40, 5), (40, 12))
        self.add_line('sym-e25', (24, 24), (24, 29))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e7', 'sym-e8', 'sym-e10', 'sym-e11', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e18', 'sym-e20', 'sym-e23', 'sym-e24', closed=False)
        self.add_contour('sym-c1', 'sym-e25', closed=False)
