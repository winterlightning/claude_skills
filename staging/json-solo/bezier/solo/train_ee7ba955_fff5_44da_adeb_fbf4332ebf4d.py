"""Train (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ee7ba955-fff5-44da-adeb-fbf4332ebf4d'
SOURCE_PATH = 'icons-json/symbol/train_ee7ba955-fff5-44da-adeb-fbf4332ebf4d.json'
AUTHOR = 'json_to_solo'

class TrainSymbol(Solo48):
    icon_id = 'train-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('train', 'symbol')

    def build(self):
        self.add_line('sym-e0', (40, 13), (8, 13))
        self.add_line('sym-e1', (8, 13), (8, 10))
        self.add_bezier('sym-e2', (8, 10), ((8, 9.718), (8, 10.282), (8, 10)))
        self.add_bezier('sym-e3', (8, 10), ((8, 6.982), (10.51, 4), (14, 4)))
        self.add_bezier('sym-e4', (14, 4), ((14.07, 4), (13.93, 4), (14, 4)))
        self.add_line('sym-e5', (14, 4), (24, 4))
        self.add_line('sym-e6', (24, 4), (34, 4))
        self.add_bezier('sym-e7', (34, 4), ((34.07, 4), (33.93, 4), (34, 4)))
        self.add_bezier('sym-e8', (34, 4), ((37.49, 4), (40, 6.982), (40, 10)))
        self.add_bezier('sym-e9', (40, 10), ((40, 10.282), (40, 9.718), (40, 10)))
        self.add_line('sym-e10', (40, 10), (40, 13))
        self.add_line('sym-e11', (40, 13), (40, 29))
        self.add_bezier('sym-e12', (40, 29), ((40, 29.064), (40, 28.936), (40, 29)))
        self.add_bezier('sym-e13', (40, 29), ((40, 31.591), (38.25, 32.018), (36, 33)))
        self.add_line('sym-e14', (36, 33), (32, 34))
        self.add_line('sym-e15', (32, 34), (16, 34))
        self.add_line('sym-e16', (16, 34), (12, 33))
        self.add_bezier('sym-e17', (12, 33), ((9.75, 32.018), (8, 31.591), (8, 29)))
        self.add_bezier('sym-e18', (8, 29), ((8, 28.936), (8, 29.064), (8, 29)))
        self.add_line('sym-e19', (8, 29), (8, 13))
        self.add_line('sym-e20', (32, 34), (38, 44))
        self.add_line('sym-e21', (16, 34), (10, 44))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19')
        self.add_contour('sym-c1', 'sym-e20')
        self.add_contour('sym-c2', 'sym-e21')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
