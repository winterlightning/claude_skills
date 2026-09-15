"""Email action read (emails), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '95be3f33-6e0e-5d19-bb59-c77813d869e8'
SOURCE_PATH = 'icons-json/emails/email action read_95be3f33-6e0e-5d19-bb59-c77813d869e8.json'
AUTHOR = 'gpt-6'

class EmailActionRead(Solo48):
    icon_id = 'email-action-read'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'emails'
    aliases = ()
    keywords = ('email', 'action', 'read', 'emails')

    def build(self):
        self.add_arc('sym-e0', (44, 14), (44, 13), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_arc('sym-e1', (44, 13), (39, 8), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_line('sym-e2', (39, 8), (9, 8))
        self.add_arc('sym-e4', (9, 8), (4, 13), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_line('sym-e5', (4, 13), (4, 35))
        self.add_line('sym-e9-1', (4, 35), (5, 38))
        self.add_arc('sym-e9-2', (5, 38), (8, 40), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_arc('sym-e10', (8, 40), (9, 40), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_line('sym-e11', (9, 40), (40, 40))
        self.add_arc('sym-e14-1', (40, 40), (43, 38), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('sym-e14-2', (43, 38), (44, 35))
        self.add_line('sym-e15', (44, 35), (44, 34))
        self.add_arc('sym-e16', (44, 34), (44, 33), radius_x=34, radius_y=34, large_arc=False, sweep=True)
        self.add_line('sym-e17', (44, 33), (44, 14))
        self.add_line('sym-e18', (44, 14), (29, 26))
        self.add_line('sym-e19', (29, 26), (24, 28))
        self.add_line('sym-e20', (24, 28), (19, 26))
        self.add_line('sym-e21', (19, 26), (4, 14))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e4', 'sym-e5', 'sym-e9-1', 'sym-e9-2', 'sym-e10', 'sym-e11', 'sym-e14-1', 'sym-e14-2', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', closed=False)
