"""Love it (social), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '54beec6b-78e6-560f-949a-e5fec2914bb2'
SOURCE_PATH = 'icons-json/social/love it_54beec6b-78e6-560f-949a-e5fec2914bb2.json'
AUTHOR = 'json_to_solo'

class LoveItSocial(Solo48):
    icon_id = 'love-it-social'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'social'
    aliases = ()
    keywords = ('love', 'it', 'social')

    def build(self):
        self.add_bezier('sym-e0', (24, 13), ((24.055, 12.924), (23.945, 13.076), (24, 13)))
        self.add_bezier('sym-e1', (24, 13), ((24.336, 12.554), (24.636, 12.429), (25, 12)))
        self.add_bezier('sym-e2', (25, 12), ((26.1, 10.695), (27.336, 9.657), (29, 9)))
        self.add_bezier('sym-e3', (29, 9), ((30.362, 8.464), (31.613, 8), (33, 8)))
        self.add_bezier('sym-e4', (33, 8), ((38.455, 8), (44, 11.481), (44, 17)))
        self.add_bezier('sym-e5', (44, 17), ((44, 17.067), (44, 17.924), (44, 18)))
        self.add_bezier('sym-e6', (44, 18), ((44, 21.352), (41.591, 24.743), (39, 27)))
        self.add_line('sym-e7', (39, 27), (24, 40))
        self.add_line('sym-e8', (24, 40), (9, 27))
        self.add_bezier('sym-e9', (9, 27), ((6.409, 24.743), (4, 21.352), (4, 18)))
        self.add_bezier('sym-e10', (4, 18), ((4, 17.924), (4, 17.067), (4, 17)))
        self.add_bezier('sym-e11', (4, 17), ((4, 11.481), (9.545, 8), (15, 8)))
        self.add_bezier('sym-e12', (15, 8), ((16.387, 8), (17.638, 8.464), (19, 9)))
        self.add_bezier('sym-e13', (19, 9), ((20.664, 9.657), (21.9, 10.695), (23, 12)))
        self.add_bezier('sym-e14', (23, 12), ((23.364, 12.429), (23.664, 12.554), (24, 13)))
        self.add_bezier('sym-e15', (24, 13), ((24.055, 13.076), (23.945, 12.924), (24, 13)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', closed=True)
