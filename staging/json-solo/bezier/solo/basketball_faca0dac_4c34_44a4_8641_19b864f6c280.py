"""Basketball (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'faca0dac-4c34-44a4-8641-19b864f6c280'
SOURCE_PATH = 'icons-json/symbol/basketball_faca0dac-4c34-44a4-8641-19b864f6c280.json'
AUTHOR = 'json_to_solo'

class BasketballSymbol(Solo48):
    icon_id = 'basketball-symbol'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('basketball', 'symbol')

    def build(self):
        self.add_arc('sym-e0', (4, 24), (24, 4), radius_x=20)
        self.add_arc('sym-e1', (24, 4), (44, 24), radius_x=20)
        self.add_arc('sym-e2', (44, 24), (24, 44), radius_x=20)
        self.add_arc('sym-e3', (24, 44), (4, 24), radius_x=20)
        self.add_line('sym-e4', (44, 24), (29, 24))
        self.add_line('sym-e5', (29, 24), (24, 24))
        self.add_line('sym-e6', (24, 24), (19, 24))
        self.add_line('sym-e7', (19, 24), (4, 24))
        self.add_bezier('sym-e8', (29, 24), ((29.673, 30.682), (32.555, 34.064), (38, 38)))
        self.add_line('sym-e9', (24, 44), (24, 24))
        self.add_line('sym-e10', (24, 24), (24, 4))
        self.add_bezier('sym-e11', (19, 24), ((18.318, 30.855), (15.645, 33.927), (10, 38)))
        self.add_bezier('sym-e12', (29, 24), ((29.673, 17.318), (32.555, 13.936), (38, 10)))
        self.add_bezier('sym-e13', (19, 24), ((18.318, 17.145), (15.645, 14.073), (10, 10)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', closed=True)
        self.add_contour('sym-c1', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7')
        self.add_contour('sym-c2', 'sym-e8')
        self.add_contour('sym-c3', 'sym-e9', 'sym-e10')
        self.add_contour('sym-c4', 'sym-e11')
        self.add_contour('sym-c5', 'sym-e12')
        self.add_contour('sym-c6', 'sym-e13')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2', 'sym-c5')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c4', 'sym-c6')
        self.relate('connect', 'sym-c1', 'sym-c5')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c5')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c6')
        self.relate('connect', 'sym-c1', 'sym-c4')
        self.relate('connect', 'sym-c1', 'sym-c6')
        self.relate('connect', 'sym-c1', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c5')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c6')
        self.relate('connect', 'sym-c0', 'sym-c4')
