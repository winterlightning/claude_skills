"""Card (business), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '25403358-b062-4eab-b82c-65ebffb2f3e3'
SOURCE_PATH = 'icons-json/business/card_25403358-b062-4eab-b82c-65ebffb2f3e3.json'
AUTHOR = 'json_to_solo'

class Card25403358(Solo48):
    icon_id = 'card-25403358'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('card', 'business')

    def build(self):
        self.add_line('e0', (31, 29), (36, 29))
        self.add_line('e1', (4, 15), (4, 34))
        self.add_line('e2', (8, 40), (39, 40))
        self.add_line('e3', (44, 35), (44, 19))
        self.add_line('e4', (44, 19), (44, 13))
        self.add_line('e5', (39, 8), (8, 8))
        self.add_line('e6', (4, 13), (4, 20))
        self.add_bezier('e7', (4, 34), ((4, 34.283), (4.009, 34.412), (4.009, 34.695)), ((4.009, 37.366), (5.273, 40), (7.427, 40)), ((7.5, 40), (7.927, 40), (8, 40)))
        self.add_bezier('e8', (39, 40), ((39.355, 40), (40.173, 39.975), (40.527, 39.975)), ((42.036, 39.975), (43.982, 37.403), (43.982, 35.36)), ((43.991, 35.262), (43.991, 35.098), (44, 35)))
        self.add_bezier('e9', (44, 13), ((43.991, 12.803), (43.991, 12.542), (43.982, 12.345)), ((43.982, 9.637), (42.109, 8.025), (40.309, 8.025)), ((40.127, 8.025), (39.945, 8), (39.764, 8)), ((39.655, 8), (39.1, 8), (39, 8)))
        self.add_bezier('e10', (8, 8), ((7.855, 8.012), (7.345, 8.012), (7.191, 8.025)), ((5.664, 8.025), (4.009, 9.932), (4.009, 12.049)), ((4.009, 12.148), (4, 12.246), (4, 12.345)), ((4, 12.542), (4, 12.803), (4, 13)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e7', 'e2', 'e8', 'e3', 'e4', 'e9', 'e5', 'e10', 'e6')
