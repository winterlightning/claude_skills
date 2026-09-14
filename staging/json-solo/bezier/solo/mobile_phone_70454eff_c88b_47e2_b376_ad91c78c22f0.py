"""Mobile phone (phones), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '70454eff-c88b-47e2-b376-ad91c78c22f0'
SOURCE_PATH = 'icons-json/phones/mobile phone_70454eff-c88b-47e2-b376-ad91c78c22f0.json'
AUTHOR = 'json_to_solo'

class MobilePhone(Solo48):
    icon_id = 'mobile-phone'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'phones'
    aliases = ()
    keywords = ('mobile', 'phone', 'phones')

    def build(self):
        self.add_line('sym-e0', (8, 36), (40, 36))
        self.add_line('sym-e1', (40, 36), (40, 7))
        self.add_bezier('sym-e2', (40, 7), ((40, 5.727), (37.723, 4), (36, 4)))
        self.add_line('sym-e3', (36, 4), (24, 4))
        self.add_line('sym-e4', (24, 4), (12, 4))
        self.add_bezier('sym-e5', (12, 4), ((10.277, 4), (8, 5.727), (8, 7)))
        self.add_line('sym-e6', (8, 7), (8, 36))
        self.add_line('sym-e7', (8, 36), (8, 38))
        self.add_bezier('sym-e8', (8, 38), ((8, 38.909), (8, 39.1), (8, 40)))
        self.add_bezier('sym-e9', (8, 40), ((8, 41.409), (9.314, 43.282), (11, 44)))
        self.add_bezier('sym-e10', (11, 44), ((11.209, 44), (10.791, 43.936), (11, 44)))
        self.add_bezier('sym-e11', (11, 44), ((11.185, 44), (11.815, 43.991), (12, 44)))
        self.add_line('sym-e12', (12, 44), (24, 44))
        self.add_line('sym-e13', (24, 44), (36, 44))
        self.add_bezier('sym-e14', (36, 44), ((36.185, 43.991), (36.815, 44), (37, 44)))
        self.add_bezier('sym-e15', (37, 44), ((37.209, 43.936), (36.791, 44), (37, 44)))
        self.add_bezier('sym-e16', (37, 44), ((38.686, 43.282), (40, 41.409), (40, 40)))
        self.add_bezier('sym-e17', (40, 40), ((40, 39.1), (40, 38.909), (40, 38)))
        self.add_line('sym-e18', (40, 38), (40, 36))
        self.add_line('sym-e19', (20, 12), (28, 12))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18')
        self.add_contour('sym-c1', 'sym-e19')
