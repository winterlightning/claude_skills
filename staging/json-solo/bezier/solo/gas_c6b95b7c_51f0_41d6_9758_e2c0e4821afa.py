"""Gas (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c6b95b7c-51f0-41d6-9758-e2c0e4821afa'
SOURCE_PATH = 'icons-json/symbol/gas_c6b95b7c-51f0-41d6-9758-e2c0e4821afa.json'
AUTHOR = 'json_to_solo'

class GasC6b95b7c(Solo48):
    icon_id = 'gas-c6b95b7c'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('gas', 'symbol')

    def build(self):
        self.add_line('sym-e0', (12, 4), (16, 4))
        self.add_line('sym-e1', (16, 4), (32, 4))
        self.add_line('sym-e2', (32, 4), (36, 4))
        self.add_line('sym-e3', (32, 4), (32, 13))
        self.add_bezier('sym-e4', (32, 13), ((34.627, 12.936), (37.232, 12.473), (39, 15)))
        self.add_bezier('sym-e5', (39, 15), ((39.404, 15.564), (40, 17.273), (40, 18)))
        self.add_line('sym-e6', (40, 18), (40, 39))
        self.add_bezier('sym-e7', (40, 39), ((40, 39.036), (40, 38.964), (40, 39)))
        self.add_bezier('sym-e8', (40, 39), ((40, 41.436), (36.114, 44), (34, 44)))
        self.add_bezier('sym-e9', (34, 44), ((33.958, 44), (34.042, 44), (34, 44)))
        self.add_bezier('sym-e10', (34, 44), ((33.966, 44), (34.034, 44), (34, 44)))
        self.add_line('sym-e11', (34, 44), (24, 44))
        self.add_line('sym-e12', (24, 44), (14, 44))
        self.add_bezier('sym-e13', (14, 44), ((13.966, 44), (14.034, 44), (14, 44)))
        self.add_bezier('sym-e14', (14, 44), ((13.958, 44), (14.042, 44), (14, 44)))
        self.add_bezier('sym-e15', (14, 44), ((11.886, 44), (8, 41.436), (8, 39)))
        self.add_bezier('sym-e16', (8, 39), ((8, 38.964), (8, 39.036), (8, 39)))
        self.add_line('sym-e17', (8, 39), (8, 18))
        self.add_bezier('sym-e18', (8, 18), ((8, 17.273), (8.596, 15.564), (9, 15)))
        self.add_bezier('sym-e19', (9, 15), ((10.768, 12.473), (13.373, 12.936), (16, 13)))
        self.add_line('sym-e20', (16, 13), (16, 4))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2')
        self.add_contour('sym-c1', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
