"""Train (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ee7ba955-fff5-44da-adeb-fbf4332ebf4d'
SOURCE_PATH = 'icons-json/symbol/train_ee7ba955-fff5-44da-adeb-fbf4332ebf4d.json'
AUTHOR = 'gpt-6'

class Train(Solo48):
    icon_id = 'train'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('train', 'symbol')

    def build(self):
        self.add_line('sym-e0', (40, 13), (8, 13))
        self.add_line('sym-e1', (8, 13), (8, 10))
        self.add_arc('sym-e3', (8, 10), (14, 4), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('sym-e5', (14, 4), (34, 4))
        self.add_arc('sym-e8', (34, 4), (40, 10), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('sym-e10', (40, 10), (40, 29))
        self.add_arc('sym-e13', (40, 29), (36, 33), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('sym-e14', (36, 33), (32, 34))
        self.add_line('sym-e15', (32, 34), (16, 34))
        self.add_line('sym-e16', (16, 34), (12, 33))
        self.add_arc('sym-e17', (12, 33), (8, 29), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('sym-e19', (8, 29), (8, 13))
        self.add_line('sym-e20', (32, 34), (38, 44))
        self.add_line('sym-e21', (16, 34), (10, 44))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e3', 'sym-e5', 'sym-e8', 'sym-e10', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e19', closed=False)
        self.add_contour('sym-c1', 'sym-e20', closed=False)
        self.add_contour('sym-c2', 'sym-e21', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
