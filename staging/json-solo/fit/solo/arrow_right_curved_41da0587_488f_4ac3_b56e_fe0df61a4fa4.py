"""Arrow right curved (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '41da0587-488f-4ac3-b56e-fe0df61a4fa4'
SOURCE_PATH = 'icons-json/symbol/arrow right curved_41da0587-488f-4ac3-b56e-fe0df61a4fa4.json'
AUTHOR = 'json_to_solo'

class ArrowRightCurvedSymbol(Solo48):
    icon_id = 'arrow-right-curved-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('arrow', 'right', 'curved', 'symbol')

    def build(self):
        self.add_line('e0', (33, 8), (44, 18))
        self.add_line('e1', (27, 18), (44, 18))
        self.add_line('e2', (33, 27), (44, 18))
        self.add_line('e3-1', (4, 40), (6, 30))
        self.add_arc('e3-2', (6, 30), (12, 23), radius_x=22)
        self.add_arc('e3-3', (12, 23), (27, 18), radius_x=21)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e3-1', 'e3-2', 'e3-3', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
