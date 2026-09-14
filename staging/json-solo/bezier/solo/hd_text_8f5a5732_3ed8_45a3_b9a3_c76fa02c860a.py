"""Hd (text) (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8f5a5732-3ed8-45a3-b9a3-c76fa02c860a'
SOURCE_PATH = 'icons-json/symbol/HD (text)_8f5a5732-3ed8-45a3-b9a3-c76fa02c860a.json'
AUTHOR = 'json_to_solo'

class HdTextSymbol(Solo48):
    icon_id = 'hd-text-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('hd', 'text', 'symbol')

    def build(self):
        self.add_line('sym-e0', (4, 8), (4, 24))
        self.add_line('sym-e1', (4, 24), (4, 40))
        self.add_line('sym-e2', (19, 24), (4, 24))
        self.add_line('sym-e3', (19, 40), (19, 24))
        self.add_line('sym-e4', (19, 24), (19, 8))
        self.add_line('sym-e5', (44, 24), (44, 20))
        self.add_bezier('sym-e6', (44, 20), ((43.991, 19.902), (44, 20.111), (44, 20)))
        self.add_bezier('sym-e7', (44, 20), ((44, 14.289), (39.273, 8), (35, 8)))
        self.add_bezier('sym-e8', (35, 8), ((34.927, 8), (35.082, 8), (35, 8)))
        self.add_bezier('sym-e9', (35, 8), ((34.927, 8), (35.073, 8), (35, 8)))
        self.add_line('sym-e10', (35, 8), (29, 8))
        self.add_line('sym-e11', (29, 8), (29, 24))
        self.add_line('sym-e12', (29, 24), (29, 40))
        self.add_line('sym-e13', (29, 40), (35, 40))
        self.add_bezier('sym-e14', (35, 40), ((35.073, 40), (34.927, 40), (35, 40)))
        self.add_bezier('sym-e15', (35, 40), ((35.082, 40), (34.927, 40), (35, 40)))
        self.add_bezier('sym-e16', (35, 40), ((39.273, 40), (44, 33.711), (44, 28)))
        self.add_bezier('sym-e17', (44, 28), ((44, 27.889), (43.991, 28.098), (44, 28)))
        self.add_line('sym-e18', (44, 28), (44, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2')
        self.add_contour('sym-c2', 'sym-e3', 'sym-e4')
        self.add_contour('sym-c3', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', closed=True)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
