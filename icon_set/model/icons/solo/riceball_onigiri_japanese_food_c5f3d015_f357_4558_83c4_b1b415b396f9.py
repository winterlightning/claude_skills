"""Riceball onigiri japanese food (video-games), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c5f3d015-f357-4558-83c4-b1b415b396f9'
SOURCE_PATH = 'icons-json/video-games/riceball onigiri japanese food_c5f3d015-f357-4558-83c4-b1b415b396f9.json'
AUTHOR = 'json_to_solo'

class RiceballOnigiriJapaneseFood(Solo48):
    icon_id = 'riceball-onigiri-japanese-food'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('riceball', 'onigiri', 'japanese', 'food', 'video-games')

    def build(self):
        self.add_line('sym-e0', (16, 40), (32, 40))
        self.add_line('sym-e1', (32, 40), (32, 26))
        self.add_arc('sym-e2', (32, 26), (31, 24), radius_x=2, sweep=False)
        self.add_line('sym-e3', (31, 24), (24, 24))
        self.add_line('sym-e4', (24, 24), (17, 24))
        self.add_arc('sym-e5', (17, 24), (16, 26), radius_x=2, sweep=False)
        self.add_line('sym-e6', (16, 26), (16, 40))
        self.add_line('sym-e7', (16, 40), (12, 40))
        self.add_arc('sym-e8-1', (12, 40), (7, 38), radius_x=8)
        self.add_arc('sym-e8-2', (7, 38), (4, 33), radius_x=6)
        self.add_line('sym-e9', (4, 33), (4, 32))
        self.add_arc('sym-e11', (4, 32), (5, 29), radius_x=5)
        self.add_line('sym-e12', (5, 29), (18, 11))
        self.add_arc('sym-e13', (18, 11), (23, 8), radius_x=7)
        self.add_arc('sym-e15', (23, 8), (24, 8), radius_x=39, sweep=False)
        self.add_line('sym-e20', (24, 8), (25, 8))
        self.add_arc('sym-e22', (25, 8), (30, 11), radius_x=7)
        self.add_line('sym-e23', (30, 11), (43, 29))
        self.add_arc('sym-e24', (43, 29), (44, 32), radius_x=5)
        self.add_line('sym-e26', (44, 32), (44, 33))
        self.add_arc('sym-e27-1', (44, 33), (41, 38), radius_x=6)
        self.add_arc('sym-e27-2', (41, 38), (36, 40), radius_x=8)
        self.add_line('sym-e28', (36, 40), (32, 40))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8-1', 'sym-e8-2', 'sym-e9', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e15', 'sym-e20', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e26', 'sym-e27-1', 'sym-e27-2', 'sym-e28')
