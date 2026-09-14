"""Maltese cross (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '72946ff1-9da2-454f-9aa9-c78f7dceadf1'
SOURCE_PATH = 'icons-json/symbol/maltese cross_72946ff1-9da2-454f-9aa9-c78f7dceadf1.json'
AUTHOR = 'json_to_solo'

class MalteseCrossSymbol(Solo48):
    icon_id = 'maltese-cross-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('maltese', 'cross', 'symbol')

    def build(self):
        self.add_bezier('sym-e0', (6, 15), ((9.256, 16.26), (12.531, 18.345), (16, 19)))
        self.add_bezier('sym-e1', (16, 19), ((16.352, 19.065), (18.885, 19.09), (19, 19)))
        self.add_bezier('sym-e2', (19, 19), ((19.049, 18.959), (19.025, 17.221), (19, 17)))
        self.add_bezier('sym-e3', (19, 17), ((18.755, 15.151), (17.835, 12.677), (17, 11)))
        self.add_line('sym-e4', (17, 11), (15, 6))
        self.add_line('sym-e5', (15, 6), (32, 6))
        self.add_bezier('sym-e6', (32, 6), ((30.985, 9.289), (29.712, 12.629), (29, 16)))
        self.add_bezier('sym-e7', (29, 16), ((28.943, 16.265), (29, 18.397), (29, 19)))
        self.add_bezier('sym-e8', (29, 19), ((29, 19.085), (28.983, 18.985), (29, 19)))
        self.add_bezier('sym-e9', (29, 19), ((29.082, 19.074), (31.648, 19.065), (32, 19)))
        self.add_bezier('sym-e10', (32, 19), ((35.485, 18.362), (38.711, 16.211), (42, 15)))
        self.add_line('sym-e11', (42, 15), (42, 24))
        self.add_line('sym-e12', (42, 24), (42, 33))
        self.add_bezier('sym-e13', (42, 33), ((38.711, 31.789), (35.485, 29.638), (32, 29)))
        self.add_bezier('sym-e14', (32, 29), ((31.648, 28.935), (29.082, 28.926), (29, 29)))
        self.add_bezier('sym-e15', (29, 29), ((28.983, 29.015), (29, 28.915), (29, 29)))
        self.add_bezier('sym-e16', (29, 29), ((29, 29.603), (28.943, 31.735), (29, 32)))
        self.add_bezier('sym-e17', (29, 32), ((29.712, 35.371), (30.985, 38.711), (32, 42)))
        self.add_line('sym-e18', (32, 42), (15, 42))
        self.add_line('sym-e19', (15, 42), (17, 37))
        self.add_bezier('sym-e20', (17, 37), ((17.835, 35.323), (18.755, 32.849), (19, 31)))
        self.add_bezier('sym-e21', (19, 31), ((19.025, 30.779), (19.049, 29.041), (19, 29)))
        self.add_bezier('sym-e22', (19, 29), ((18.885, 28.91), (16.352, 28.935), (16, 29)))
        self.add_bezier('sym-e23', (16, 29), ((12.531, 29.655), (9.256, 31.74), (6, 33)))
        self.add_line('sym-e24', (6, 33), (6, 24))
        self.add_line('sym-e25', (6, 24), (6, 15))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', closed=True)
