"""Arrow angle right (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9edbcf4f-df9f-48e0-94e9-f06f136a161b'
SOURCE_PATH = 'icons-json/symbol/arrow angle right_9edbcf4f-df9f-48e0-94e9-f06f136a161b.json'
AUTHOR = 'json_to_solo'

class ArrowAngleRightSymbol(Solo48):
    icon_id = 'arrow-angle-right-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('arrow', 'angle', 'right', 'symbol')

    def build(self):
        self.add_line('sym-e0', (40, 24), (40, 24))
        self.add_bezier('sym-e1', (40, 24), ((39.761, 24.409), (38.63, 24.606), (38, 25)))
        self.add_line('sym-e2', (38, 25), (8, 44))
        self.add_bezier('sym-e3', (40, 24), ((39.761, 23.591), (38.63, 23.394), (38, 23)))
        self.add_line('sym-e4', (38, 23), (8, 4))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2')
        self.add_contour('sym-c1', 'sym-e3', 'sym-e4')
        self.relate('connect', 'sym-c0', 'sym-c1')
