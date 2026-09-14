"""Maltese cross (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '72946ff1-9da2-454f-9aa9-c78f7dceadf1'
SOURCE_PATH = 'icons-json/symbol/maltese cross_72946ff1-9da2-454f-9aa9-c78f7dceadf1.json'
AUTHOR = 'json_to_solo'

class MalteseCross(Solo48):
    icon_id = 'maltese-cross'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('maltese', 'cross', 'symbol')

    def build(self):
        self.add_arc('sym-e0', (6, 15), (16, 19), radius_x=47, sweep=False)
        self.add_line('sym-e1', (16, 19), (19, 19))
        self.add_arc('sym-e2', (19, 19), (19, 17), radius_x=22)
        self.add_arc('sym-e3', (19, 17), (17, 11), radius_x=21, sweep=False)
        self.add_line('sym-e4', (17, 11), (15, 6))
        self.add_line('sym-e5', (15, 6), (32, 6))
        self.add_line('sym-e6', (32, 6), (29, 16))
        self.add_arc('sym-e7', (29, 16), (29, 19), radius_x=28, sweep=False)
        self.add_arc('sym-e9', (29, 19), (32, 19), radius_x=33)
        self.add_arc('sym-e10', (32, 19), (42, 15), radius_x=46, sweep=False)
        self.add_line('sym-e11', (42, 15), (42, 24))
        self.add_line('sym-e12', (42, 24), (42, 33))
        self.add_arc('sym-e13', (42, 33), (32, 29), radius_x=46, sweep=False)
        self.add_arc('sym-e14', (32, 29), (29, 29), radius_x=33)
        self.add_arc('sym-e16', (29, 29), (29, 32), radius_x=29)
        self.add_line('sym-e17', (29, 32), (32, 42))
        self.add_line('sym-e18', (32, 42), (15, 42))
        self.add_line('sym-e19', (15, 42), (17, 37))
        self.add_arc('sym-e20', (17, 37), (19, 31), radius_x=21, sweep=False)
        self.add_arc('sym-e21', (19, 31), (19, 29), radius_x=22)
        self.add_arc('sym-e22', (19, 29), (16, 29), radius_x=28, sweep=False)
        self.add_arc('sym-e23', (16, 29), (6, 33), radius_x=48, sweep=False)
        self.add_line('sym-e24', (6, 33), (6, 24))
        self.add_line('sym-e25', (6, 24), (6, 15))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', closed=True)
