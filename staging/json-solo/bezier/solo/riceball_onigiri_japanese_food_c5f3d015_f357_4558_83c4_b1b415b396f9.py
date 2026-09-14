"""Riceball onigiri japanese food (video-games), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c5f3d015-f357-4558-83c4-b1b415b396f9'
SOURCE_PATH = 'icons-json/video-games/riceball onigiri japanese food_c5f3d015-f357-4558-83c4-b1b415b396f9.json'
AUTHOR = 'json_to_solo'

class RiceballOnigiriJapaneseFoodVideoGames(Solo48):
    icon_id = 'riceball-onigiri-japanese-food-video-games'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('riceball', 'onigiri', 'japanese', 'food', 'video-games')

    def build(self):
        self.add_line('sym-e0', (16, 40), (32, 40))
        self.add_line('sym-e1', (32, 40), (32, 26))
        self.add_bezier('sym-e2', (32, 26), ((32, 25.158), (31.555, 24.556), (31, 24)))
        self.add_line('sym-e3', (31, 24), (24, 24))
        self.add_line('sym-e4', (24, 24), (17, 24))
        self.add_bezier('sym-e5', (17, 24), ((16.445, 24.556), (16, 25.158), (16, 26)))
        self.add_line('sym-e6', (16, 26), (16, 40))
        self.add_bezier('sym-e7', (16, 40), ((14.745, 40), (13.255, 40), (12, 40)))
        self.add_bezier('sym-e8', (12, 40), ((8.118, 40), (4, 36.781), (4, 33)))
        self.add_bezier('sym-e9', (4, 33), ((4, 32.747), (4, 32.253), (4, 32)))
        self.add_bezier('sym-e10', (4, 32), ((4, 31.882), (4, 32.126), (4, 32)))
        self.add_bezier('sym-e11', (4, 32), ((4, 31.023), (4.436, 29.825), (5, 29)))
        self.add_line('sym-e12', (5, 29), (18, 11))
        self.add_bezier('sym-e13', (18, 11), ((19.073, 9.434), (21.045, 8), (23, 8)))
        self.add_bezier('sym-e14', (23, 8), ((23.091, 8), (22.909, 8), (23, 8)))
        self.add_bezier('sym-e15', (23, 8), ((23.118, 8), (23.882, 8), (24, 8)))
        self.add_bezier('sym-e16', (24, 8), ((24.085, 8), (23.914, 8), (24, 8)))
        self.add_bezier('sym-e17', (24, 8), ((24.015, 8), (23.985, 8), (24, 8)))
        self.add_bezier('sym-e18', (24, 8), ((24.015, 8), (23.985, 8), (24, 8)))
        self.add_bezier('sym-e19', (24, 8), ((24.086, 8), (23.915, 8), (24, 8)))
        self.add_bezier('sym-e20', (24, 8), ((24.118, 8), (24.882, 8), (25, 8)))
        self.add_bezier('sym-e21', (25, 8), ((25.091, 8), (24.909, 8), (25, 8)))
        self.add_bezier('sym-e22', (25, 8), ((26.955, 8), (28.927, 9.434), (30, 11)))
        self.add_line('sym-e23', (30, 11), (43, 29))
        self.add_bezier('sym-e24', (43, 29), ((43.564, 29.825), (44, 31.023), (44, 32)))
        self.add_bezier('sym-e25', (44, 32), ((44, 32.126), (44, 31.882), (44, 32)))
        self.add_bezier('sym-e26', (44, 32), ((44, 32.253), (44, 32.747), (44, 33)))
        self.add_bezier('sym-e27', (44, 33), ((44, 36.781), (39.882, 40), (36, 40)))
        self.add_bezier('sym-e28', (36, 40), ((34.745, 40), (33.255, 40), (32, 40)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28')
