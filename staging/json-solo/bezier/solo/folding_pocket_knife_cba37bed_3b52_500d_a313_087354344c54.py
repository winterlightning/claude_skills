"""Folding pocket knife (tools), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cba37bed-3b52-500d-a313-087354344c54'
SOURCE_PATH = 'icons-json/tools/folding pocket knife_cba37bed-3b52-500d-a313-087354344c54.json'
AUTHOR = 'json_to_solo'

class FoldingPocketKnife(Solo48):
    icon_id = 'folding-pocket-knife'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'tools'
    aliases = ()
    keywords = ('folding', 'pocket', 'knife', 'tools')

    def build(self):
        self.add_line('e0', (31, 42), (11, 42))
        self.add_line('e1', (10, 31), (27, 31))
        self.add_line('e2', (31, 30), (33, 29))
        self.add_line('e3', (17, 20), (27, 31))
        self.add_bezier('e4', (38, 27), ((39.915, 28.145), (41.059, 29.547), (41.689, 31.773)), ((41.828, 32.239), (41.992, 32.763), (41.992, 33.254)), ((41.992, 33.391), (42, 33.52), (42, 33.656)), ((42, 33.658), (42, 33.661), (42, 33.663)), ((42, 33.867), (41.984, 34.072), (41.984, 34.276)), ((41.984, 39.897), (35.283, 41.992), (30.685, 41.992)), ((30.635, 41.992), (31.049, 42), (31, 42)))
        self.add_bezier('e5', (11, 42), ((10.935, 42), (10.786, 42), (10.729, 41.992)), ((8.275, 41.992), (6.008, 39.177), (6.008, 36.821)), ((6, 36.765), (6, 36.7), (6, 36.644)), ((6, 36.643), (6, 36.642), (6, 36.641)), ((6, 36.518), (6.008, 36.395), (6.008, 36.281)), ((6.008, 34.808), (7.137, 33.008), (8.291, 32.157)), ((8.831, 31.765), (9.386, 31.205), (10, 31)))
        self.add_bezier('e6', (27, 31), ((28.285, 31), (30.026, 30.712), (31, 30)))
        self.add_bezier('e7', (33, 29), ((34.645, 27.855), (35.946, 26.787), (38, 27)))
        self.add_bezier('e8', (38, 27), ((36.126, 25.077), (34.047, 23.542), (32.108, 21.685)), ((27.788, 17.545), (23.378, 13.495), (18.33, 10.23)), ((16.555, 9.085), (14.755, 7.947), (12.881, 6.965)), ((12.518, 6.78), (11.324, 6), (10.927, 6)), ((10.921, 6), (10.915, 6), (10.909, 6)), ((10.909, 6.065), (10.909, 6.131), (10.909, 6.205)), ((10.909, 6.401), (10.901, 6.597), (10.901, 6.802)), ((10.901, 7.8), (10.991, 8.79), (11.171, 9.772)), ((11.866, 13.576), (14.39, 17.185), (17, 20)))
        self.add_contour('c0', 'e4', 'e0', 'e5', 'e1', 'e6', 'e2', 'e7')
        self.add_contour('c1', 'e8', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c1', 'c0')
