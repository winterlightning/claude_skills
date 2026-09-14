"""Batch-04/hat cowboy (accessories), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '102a699a-efb8-5111-a65a-a03761946e2d'
SOURCE_PATH = 'icons-json/accessories/batch-04/hat cowboy_102a699a-efb8-5111-a65a-a03761946e2d.json'
AUTHOR = 'json_to_solo'

class Batch04HatCowboy(Solo48):
    icon_id = 'batch-04-hat-cowboy'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'hat', 'cowboy', 'accessories')

    def build(self):
        self.add_line('sym-e1', (24, 11), (20, 8))
        self.add_line('sym-e2', (20, 8), (19, 8))
        self.add_arc('sym-e4', (19, 8), (15, 15), radius_x=8, sweep=False)
        self.add_line('sym-e5', (15, 15), (13, 26))
        self.add_arc('sym-e6', (13, 26), (24, 28), radius_x=34, sweep=False)
        self.add_arc('sym-e7', (24, 28), (35, 26), radius_x=34, sweep=False)
        self.add_line('sym-e8', (35, 26), (33, 15))
        self.add_arc('sym-e9', (33, 15), (29, 8), radius_x=8, sweep=False)
        self.add_line('sym-e11', (29, 8), (28, 8))
        self.add_line('sym-e12', (28, 8), (24, 11))
        self.add_line('sym-e14', (10, 25), (7, 22))
        self.add_line('sym-e15', (7, 22), (6, 21))
        self.add_line('sym-e16', (6, 21), (4, 24))
        self.add_line('sym-e18', (4, 24), (4, 25))
        self.add_arc('sym-e19', (4, 25), (7, 31), radius_x=14, sweep=False)
        self.add_arc('sym-e20', (7, 31), (19, 40), radius_x=20, sweep=False)
        self.add_line('sym-e21', (19, 40), (20, 40))
        self.add_line('sym-e22', (20, 40), (24, 40))
        self.add_line('sym-e23', (24, 40), (28, 40))
        self.add_line('sym-e24', (28, 40), (29, 40))
        self.add_arc('sym-e25', (29, 40), (41, 31), radius_x=20, sweep=False)
        self.add_arc('sym-e26', (41, 31), (44, 25), radius_x=13, sweep=False)
        self.add_line('sym-e27', (44, 25), (44, 24))
        self.add_line('sym-e29', (44, 24), (42, 21))
        self.add_line('sym-e30', (42, 21), (41, 22))
        self.add_line('sym-e31', (41, 22), (38, 25))
        self.add_line('sym-e32', (38, 25), (35, 26))
        self.add_line('sym-e33', (13, 26), (10, 25))
        self.add_contour('sym-c0', 'sym-e1', 'sym-e2', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e11', 'sym-e12', closed=True)
        self.add_contour('sym-c1', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e29', 'sym-e30', 'sym-e31', 'sym-e32')
        self.add_contour('sym-c2', 'sym-e33')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
