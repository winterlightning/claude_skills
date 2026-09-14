"""Mail (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '75ad5383-92bd-435c-984f-c475f5f845c1'
SOURCE_PATH = 'icons-json/symbol/mail_75ad5383-92bd-435c-984f-c475f5f845c1.json'
AUTHOR = 'json_to_solo'

class Mail75ad5383(Solo48):
    icon_id = 'mail-75ad5383'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('mail', 'symbol')

    def build(self):
        self.add_line('sym-e0', (24, 25), (4, 13))
        self.add_line('sym-e1', (4, 13), (4, 33))
        self.add_bezier('sym-e2', (4, 33), ((4, 33.4), (4, 33.6), (4, 34)))
        self.add_bezier('sym-e3', (4, 34), ((4, 36.66), (5.255, 40), (8, 40)))
        self.add_bezier('sym-e4', (8, 40), ((8.073, 40), (8.927, 40), (9, 40)))
        self.add_line('sym-e5', (9, 40), (24, 40))
        self.add_line('sym-e6', (24, 40), (39, 40))
        self.add_bezier('sym-e7', (39, 40), ((39.073, 40), (39.927, 40), (40, 40)))
        self.add_bezier('sym-e8', (40, 40), ((42.745, 40), (44, 36.66), (44, 34)))
        self.add_bezier('sym-e9', (44, 34), ((44, 33.6), (44, 33.4), (44, 33)))
        self.add_line('sym-e10', (44, 33), (44, 13))
        self.add_line('sym-e11', (44, 13), (24, 25))
        self.add_line('sym-e12', (24, 8), (9, 8))
        self.add_bezier('sym-e13', (9, 8), ((8.791, 8), (8.2, 8), (8, 8)))
        self.add_bezier('sym-e14', (8, 8), ((5.855, 8), (4, 10.76), (4, 13)))
        self.add_bezier('sym-e15', (4, 13), ((4, 13.09), (4, 12.91), (4, 13)))
        self.add_line('sym-e16', (24, 8), (39, 8))
        self.add_bezier('sym-e17', (39, 8), ((39.209, 8), (39.8, 8), (40, 8)))
        self.add_bezier('sym-e18', (40, 8), ((42.145, 8), (44, 10.76), (44, 13)))
        self.add_bezier('sym-e19', (44, 13), ((44, 13.09), (44, 12.91), (44, 13)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', closed=True)
        self.add_contour('sym-c1', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15')
        self.add_contour('sym-c2', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
