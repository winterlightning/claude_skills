"""Mobile phone (mobile), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b193343f-83cb-42e1-82cf-a7eac0dd3950'
SOURCE_PATH = 'icons-json/mobile/mobile phone_b193343f-83cb-42e1-82cf-a7eac0dd3950.json'
AUTHOR = 'json_to_solo'

class MobilePhoneB193343f(Solo48):
    icon_id = 'mobile-phone-b193343f'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'mobile'
    aliases = ()
    keywords = ('mobile', 'phone')

    def build(self):
        self.add_line('sym-e0', (22, 36), (26, 36))
        self.add_line('sym-e1', (35, 44), (24, 44))
        self.add_line('sym-e2', (24, 44), (13, 44))
        self.add_bezier('sym-e3', (13, 44), ((12.951, 44), (13.049, 44), (13, 44)))
        self.add_bezier('sym-e4', (13, 44), ((10.932, 44), (8, 41.473), (8, 40)))
        self.add_line('sym-e5', (8, 40), (8, 8))
        self.add_bezier('sym-e6', (8, 8), ((8, 6.6), (11.117, 4), (13, 4)))
        self.add_bezier('sym-e7', (13, 4), ((13.049, 4), (12.951, 4), (13, 4)))
        self.add_line('sym-e8', (13, 4), (24, 4))
        self.add_line('sym-e9', (24, 4), (35, 4))
        self.add_bezier('sym-e10', (35, 4), ((35.049, 4), (34.951, 4), (35, 4)))
        self.add_bezier('sym-e11', (35, 4), ((36.883, 4), (40, 6.6), (40, 8)))
        self.add_line('sym-e12', (40, 8), (40, 40))
        self.add_bezier('sym-e13', (40, 40), ((40, 41.473), (37.068, 44), (35, 44)))
        self.add_bezier('sym-e14', (35, 44), ((34.951, 44), (35.049, 44), (35, 44)))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', closed=True)
