"""Mobile phone (mobile), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bd6f95a5-0424-4a29-9485-44807fcb0342'
SOURCE_PATH = 'icons-json/mobile/mobile phone_bd6f95a5-0424-4a29-9485-44807fcb0342.json'
AUTHOR = 'json_to_solo'

class MobilePhone(Solo48):
    icon_id = 'mobile-phone'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'mobile'
    aliases = ()
    keywords = ('mobile', 'phone')

    def build(self):
        self.add_line('sym-e0', (8, 36), (40, 36))
        self.add_bezier('sym-e1', (40, 36), ((40, 37.282), (40, 38.718), (40, 40)))
        self.add_bezier('sym-e2', (40, 40), ((40, 41.782), (37.658, 44), (35, 44)))
        self.add_line('sym-e3', (35, 44), (24, 44))
        self.add_line('sym-e4', (24, 44), (13, 44))
        self.add_bezier('sym-e5', (13, 44), ((10.342, 44), (8, 41.782), (8, 40)))
        self.add_bezier('sym-e6', (8, 40), ((8, 38.718), (8, 37.282), (8, 36)))
        self.add_line('sym-e7', (8, 36), (8, 8))
        self.add_bezier('sym-e8', (8, 8), ((8, 6.609), (11.043, 4), (13, 4)))
        self.add_bezier('sym-e9', (13, 4), ((13.037, 4), (12.963, 4), (13, 4)))
        self.add_bezier('sym-e10', (13, 4), ((13.037, 4), (12.963, 4), (13, 4)))
        self.add_line('sym-e11', (13, 4), (24, 4))
        self.add_line('sym-e12', (24, 4), (35, 4))
        self.add_bezier('sym-e13', (35, 4), ((35.037, 4), (34.963, 4), (35, 4)))
        self.add_bezier('sym-e14', (35, 4), ((35.037, 4), (34.963, 4), (35, 4)))
        self.add_bezier('sym-e15', (35, 4), ((36.957, 4), (40, 6.609), (40, 8)))
        self.add_line('sym-e16', (40, 8), (40, 36))
        self.add_line('sym-e17', (24, 12), (24, 12))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16')
        self.add_contour('sym-c1', 'sym-e17', closed=True)
