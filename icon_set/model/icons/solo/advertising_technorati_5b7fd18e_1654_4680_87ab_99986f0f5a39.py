"""Advertising technorati (_uncategorized_01), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5b7fd18e-1654-4680-87ab-99986f0f5a39'
SOURCE_PATH = 'icons-json/_uncategorized_01/advertising technorati_5b7fd18e-1654-4680-87ab-99986f0f5a39.json'
AUTHOR = 'json_to_solo'

class AdvertisingTechnorati(Solo48):
    icon_id = 'advertising-technorati'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_01'
    aliases = ()
    keywords = ('advertising', 'technorati', '_uncategorized_01')

    def build(self):
        self.add_line('e0', (8, 40), (16, 36))
        self.add_line('e1', (16, 36), (20, 37))
        self.add_line('e2', (10, 32), (8, 40))
        self.add_bezier('e3', (20, 37), ((21.945, 37.362), (24.545, 36.825), (26.482, 36.514)), ((32.673, 35.528), (39.355, 33.204), (42.427, 27.705)), ((43.282, 26.181), (43.991, 24.429), (43.991, 22.678)), ((43.991, 22.62), (44, 22.554), (44, 22.495)), ((44, 22.494), (44, 22.494), (44, 22.493)), ((44, 22.257), (43.991, 22.013), (43.991, 21.777)), ((43.991, 13.389), (32.973, 8.017), (24.982, 8.017)), ((24.749, 8.017), (24.525, 8), (24.293, 8)), ((24.289, 8), (24.286, 8), (24.282, 8)), ((23.809, 8), (23.336, 8.017), (22.864, 8.017)), ((14.918, 8.017), (4.009, 13.373), (4.009, 21.718)), ((4.009, 21.776), (4, 21.834), (4, 21.892)), ((4, 21.893), (4, 21.894), (4, 21.895)), ((4, 22.164), (4.009, 22.425), (4.009, 22.695)), ((4.009, 26.771), (6.782, 29.592), (10, 32)))
        self.add_contour('c0', 'e0', 'e1', 'e3', 'e2', closed=True)
