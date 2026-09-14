"""Arrow angle up (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '95cae625-b690-4c5b-ade6-1ec2bc5b1e96'
SOURCE_PATH = 'icons-json/symbol/arrow angle up_95cae625-b690-4c5b-ade6-1ec2bc5b1e96.json'
AUTHOR = 'json_to_solo'

class ArrowAngleUpSymbol(Solo48):
    icon_id = 'arrow-angle-up-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('arrow', 'angle', 'up', 'symbol')

    def build(self):
        self.add_line('sym-e0', (24, 8), (24, 8))
        self.add_bezier('sym-e1', (24, 8), ((24.409, 8.239), (24.606, 9.37), (25, 10)))
        self.add_line('sym-e2', (25, 10), (44, 40))
        self.add_bezier('sym-e3', (24, 8), ((23.591, 8.239), (23.394, 9.37), (23, 10)))
        self.add_line('sym-e4', (23, 10), (4, 40))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2')
        self.add_contour('sym-c1', 'sym-e3', 'sym-e4')
        self.relate('connect', 'sym-c0', 'sym-c1')
