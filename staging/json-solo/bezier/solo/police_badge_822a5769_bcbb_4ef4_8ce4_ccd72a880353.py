"""Police badge (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '822a5769-bcbb-4ef4-8ce4-ccd72a880353'
SOURCE_PATH = 'icons-json/symbol/police badge_822a5769-bcbb-4ef4-8ce4-ccd72a880353.json'
AUTHOR = 'json_to_solo'

class PoliceBadgeSymbol(Solo48):
    icon_id = 'police-badge-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('police', 'badge', 'symbol')

    def build(self):
        self.add_line('sym-e0', (24, 20), (24, 26))
        self.add_line('sym-e1', (37, 5), (40, 9))
        self.add_bezier('sym-e2', (40, 9), ((38.139, 12.4), (35.728, 14.882), (37, 19)))
        self.add_line('sym-e3', (37, 19), (39, 25))
        self.add_bezier('sym-e4', (39, 25), ((39.236, 25.755), (40, 27.227), (40, 28)))
        self.add_bezier('sym-e5', (40, 28), ((40, 28.091), (40, 28.909), (40, 29)))
        self.add_bezier('sym-e6', (40, 29), ((40, 29.945), (39.337, 30.145), (39, 31)))
        self.add_bezier('sym-e7', (39, 31), ((38.688, 31.809), (38.446, 33.255), (38, 34)))
        self.add_bezier('sym-e8', (38, 34), ((36.476, 36.509), (34.375, 37.536), (32, 39)))
        self.add_line('sym-e9', (32, 39), (26, 43))
        self.add_bezier('sym-e10', (26, 43), ((25.512, 43.3), (24.488, 43.7), (24, 44)))
        self.add_bezier('sym-e11', (24, 44), ((23.943, 43.951), (24.057, 44), (24, 44)))
        self.add_bezier('sym-e12', (24, 44), ((23.985, 44), (24.015, 44), (24, 44)))
        self.add_bezier('sym-e13', (24, 44), ((23.985, 44), (24.015, 44), (24, 44)))
        self.add_bezier('sym-e14', (24, 44), ((23.943, 44), (24.057, 43.951), (24, 44)))
        self.add_bezier('sym-e15', (24, 44), ((23.512, 43.7), (22.488, 43.3), (22, 43)))
        self.add_line('sym-e16', (22, 43), (16, 39))
        self.add_bezier('sym-e17', (16, 39), ((13.625, 37.536), (11.524, 36.509), (10, 34)))
        self.add_bezier('sym-e18', (10, 34), ((9.554, 33.255), (9.312, 31.809), (9, 31)))
        self.add_bezier('sym-e19', (9, 31), ((8.663, 30.145), (8, 29.945), (8, 29)))
        self.add_bezier('sym-e20', (8, 29), ((8, 28.909), (8, 28.091), (8, 28)))
        self.add_bezier('sym-e21', (8, 28), ((8, 27.227), (8.764, 25.755), (9, 25)))
        self.add_line('sym-e22', (9, 25), (11, 19))
        self.add_bezier('sym-e23', (11, 19), ((12.272, 14.882), (9.861, 12.4), (8, 9)))
        self.add_line('sym-e24', (8, 9), (11, 5))
        self.add_bezier('sym-e25', (11, 5), ((13.981, 6.527), (17.775, 7.191), (21, 6)))
        self.add_bezier('sym-e26', (21, 6), ((21.842, 5.691), (22.276, 5.555), (23, 5)))
        self.add_bezier('sym-e27', (23, 5), ((23.312, 4.755), (23.688, 4.245), (24, 4)))
        self.add_bezier('sym-e28', (24, 4), ((24.002, 4.001), (23.998, 4), (24, 4)))
        self.add_bezier('sym-e29', (24, 4), ((24.005, 4), (23.995, 4), (24, 4)))
        self.add_bezier('sym-e30', (24, 4), ((24.002, 4), (23.998, 4), (24, 4)))
        self.add_bezier('sym-e31', (24, 4), ((24.005, 4), (23.995, 4), (24, 4)))
        self.add_bezier('sym-e32', (24, 4), ((24.002, 4), (23.998, 4.001), (24, 4)))
        self.add_bezier('sym-e33', (24, 4), ((24.312, 4.245), (24.688, 4.755), (25, 5)))
        self.add_bezier('sym-e34', (25, 5), ((25.724, 5.555), (26.158, 5.691), (27, 6)))
        self.add_bezier('sym-e35', (27, 6), ((30.225, 7.191), (34.019, 6.527), (37, 5)))
        self.add_bezier('sym-e36', (24, 4), ((23.998, 4), (24.002, 4), (24, 4)))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29', 'sym-e30', 'sym-e31', 'sym-e32', 'sym-e33', 'sym-e34', 'sym-e35', closed=True)
        self.add_contour('sym-c2', 'sym-e36', closed=True)
        self.relate('connect', 'sym-c1', 'sym-c2')
