"""Mobile phone (phones), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0ccd2887-dbd0-4ab5-a736-e2ba5438da4d'
SOURCE_PATH = 'icons-json/phones/mobile phone_0ccd2887-dbd0-4ab5-a736-e2ba5438da4d.json'
AUTHOR = 'json_to_solo'

class MobilePhone0ccd2887(Solo48):
    icon_id = 'mobile-phone-0ccd2887'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'phones'
    aliases = ()
    keywords = ('mobile', 'phone', 'phones')

    def build(self):
        self.add_line('sym-e0', (8, 34), (40, 34))
        self.add_bezier('sym-e1', (40, 34), ((40, 35.973), (40, 38.027), (40, 40)))
        self.add_bezier('sym-e2', (40, 40), ((40, 41.882), (37.794, 44), (35, 44)))
        self.add_bezier('sym-e3', (35, 44), ((34.951, 44), (35.049, 43.991), (35, 44)))
        self.add_line('sym-e4', (35, 44), (24, 44))
        self.add_line('sym-e5', (24, 44), (13, 44))
        self.add_bezier('sym-e6', (13, 44), ((12.951, 43.991), (13.049, 44), (13, 44)))
        self.add_bezier('sym-e7', (13, 44), ((10.206, 44), (8, 41.882), (8, 40)))
        self.add_bezier('sym-e8', (8, 40), ((8, 38.027), (8, 35.973), (8, 34)))
        self.add_line('sym-e9', (8, 34), (8, 8))
        self.add_bezier('sym-e10', (8, 8), ((8, 6.291), (10.674, 4), (13, 4)))
        self.add_line('sym-e11', (13, 4), (24, 4))
        self.add_line('sym-e12', (24, 4), (35, 4))
        self.add_bezier('sym-e13', (35, 4), ((37.326, 4), (40, 6.291), (40, 8)))
        self.add_line('sym-e14', (40, 8), (40, 34))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14')
