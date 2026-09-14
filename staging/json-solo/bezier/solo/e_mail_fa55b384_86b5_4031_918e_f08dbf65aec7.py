"""E mail (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fa55b384-86b5-4031-918e-f08dbf65aec7'
SOURCE_PATH = 'icons-json/symbol/e mail_fa55b384-86b5-4031-918e-f08dbf65aec7.json'
AUTHOR = 'json_to_solo'

class EMailFa55b384(Solo48):
    icon_id = 'e-mail-fa55b384'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('e', 'mail', 'symbol')

    def build(self):
        self.add_bezier('sym-e0', (24, 27), ((22.726, 26.887), (21.142, 26.114), (20, 25)))
        self.add_line('sym-e1', (20, 25), (4, 9))
        self.add_line('sym-e2', (4, 9), (4, 38))
        self.add_bezier('sym-e3', (4, 38), ((4.109, 38.19), (4, 38.83), (4, 39)))
        self.add_bezier('sym-e4', (4, 39), ((4.209, 39.28), (5.664, 39.86), (6, 40)))
        self.add_bezier('sym-e5', (6, 40), ((6.255, 40), (5.736, 39.94), (6, 40)))
        self.add_bezier('sym-e6', (6, 40), ((6.118, 40), (6.882, 39.98), (7, 40)))
        self.add_line('sym-e7', (7, 40), (24, 40))
        self.add_line('sym-e8', (24, 40), (41, 40))
        self.add_bezier('sym-e9', (41, 40), ((41.118, 39.98), (41.882, 40), (42, 40)))
        self.add_bezier('sym-e10', (42, 40), ((42.264, 39.94), (41.745, 40), (42, 40)))
        self.add_bezier('sym-e11', (42, 40), ((42.336, 39.86), (43.791, 39.28), (44, 39)))
        self.add_bezier('sym-e12', (44, 39), ((44, 38.83), (43.891, 38.19), (44, 38)))
        self.add_line('sym-e13', (44, 38), (44, 9))
        self.add_line('sym-e14', (44, 9), (28, 25))
        self.add_bezier('sym-e15', (28, 25), ((26.858, 26.114), (25.274, 26.887), (24, 27)))
        self.add_line('sym-e16', (4, 9), (4, 8))
        self.add_line('sym-e17', (4, 8), (24, 8))
        self.add_line('sym-e18', (24, 8), (44, 8))
        self.add_line('sym-e19', (44, 8), (44, 9))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', closed=True)
        self.add_contour('sym-c1', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
