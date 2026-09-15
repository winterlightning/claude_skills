"""Mobile phone control pause (state), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b4668e9a-a445-4547-ab4c-3cab57aef111'
SOURCE_PATH = 'pictographic-primitives/state/mobile phone control pause_b4668e9a-a445-4547-ab4c-3cab57aef111.svg'
AUTHOR = 'gpt-6'

class MobilePhoneControlPause(Solo48):
    icon_id = 'mobile-phone-control-pause'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('mobile', 'phone', 'control', 'pause', 'state')

    def build(self):
        self.add_line('sym-e0', (40, 36), (8, 36))
        self.add_line('sym-e1', (8, 36), (8, 8))
        self.add_arc('sym-e2', (8, 8), (12, 4), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('sym-e3', (12, 4), (36, 4))
        self.add_arc('sym-e7', (36, 4), (40, 8), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('sym-e8', (40, 8), (40, 38))
        self.add_arc('sym-e11-1', (40, 38), (39, 41), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('sym-e11-2', (39, 41), (36, 44))
        self.add_line('sym-e12', (36, 44), (14, 44))
        self.add_arc('sym-e16', (14, 44), (13, 44), radius_x=1, radius_y=1, large_arc=False, sweep=False)
        self.add_line('sym-e17', (13, 44), (12, 44))
        self.add_line('sym-e18-1', (12, 44), (9, 41))
        self.add_arc('sym-e18-2', (9, 41), (8, 38), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('sym-e19', (8, 38), (8, 36))
        self.add_line('sym-e21', (19, 14), (19, 26))
        self.add_line('sym-e22', (29, 14), (29, 26))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e7', 'sym-e8', 'sym-e11-1', 'sym-e11-2', 'sym-e12', 'sym-e16', 'sym-e17', 'sym-e18-1', 'sym-e18-2', 'sym-e19', closed=False)
        self.add_contour('sym-c1', 'sym-e21', closed=False)
        self.add_contour('sym-c2', 'sym-e22', closed=False)
