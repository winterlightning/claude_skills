"""Adjustable lamp 2 (_uncategorized_01), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1a3dd3e8-27fe-40d4-9e28-a1002c878050'
SOURCE_PATH = 'icons-json/_uncategorized_01/adjustable lamp 2_1a3dd3e8-27fe-40d4-9e28-a1002c878050.json'
AUTHOR = 'json_to_solo'

class AdjustableLamp2Uncategorized01(Solo48):
    icon_id = 'adjustable-lamp-2-uncategorized-01'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_01'
    aliases = ()
    keywords = ('adjustable', 'lamp', '_uncategorized_01')

    def build(self):
        self.add_line('sym-e0', (24, 44), (24, 33))
        self.add_line('sym-e1', (24, 33), (31, 33))
        self.add_bezier('sym-e2', (31, 33), ((32.036, 33), (31.343, 32.745), (32, 32)))
        self.add_line('sym-e3', (32, 32), (30, 20))
        self.add_bezier('sym-e4', (30, 20), ((29.453, 19.409), (28.808, 19), (28, 19)))
        self.add_line('sym-e5', (28, 19), (24, 19))
        self.add_line('sym-e6', (24, 19), (20, 19))
        self.add_bezier('sym-e7', (20, 19), ((19.192, 19), (18.547, 19.409), (18, 20)))
        self.add_line('sym-e8', (18, 20), (16, 32))
        self.add_bezier('sym-e9', (16, 32), ((16.657, 32.745), (15.964, 33), (17, 33)))
        self.add_line('sym-e10', (17, 33), (24, 33))
        self.add_bezier('sym-e11', (24, 4), ((24.173, 4.003), (24.824, 4), (25, 4)))
        self.add_bezier('sym-e12', (25, 4), ((32.385, 4), (40, 11.682), (40, 20)))
        self.add_bezier('sym-e13', (40, 20), ((40, 20.064), (40, 19.927), (40, 20)))
        self.add_bezier('sym-e14', (40, 20), ((40, 20.218), (40, 19.782), (40, 20)))
        self.add_line('sym-e15', (29, 44), (24, 44))
        self.add_line('sym-e16', (24, 44), (19, 44))
        self.add_bezier('sym-e17', (24, 4), ((23.827, 4.003), (23.176, 4), (23, 4)))
        self.add_bezier('sym-e18', (23, 4), ((15.615, 4), (8, 11.682), (8, 20)))
        self.add_bezier('sym-e19', (8, 20), ((8, 20.064), (8, 19.927), (8, 20)))
        self.add_bezier('sym-e20', (8, 20), ((8, 20.218), (8, 19.782), (8, 20)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10')
        self.add_contour('sym-c1', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14')
        self.add_contour('sym-c2', 'sym-e15', 'sym-e16')
        self.add_contour('sym-c3', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
