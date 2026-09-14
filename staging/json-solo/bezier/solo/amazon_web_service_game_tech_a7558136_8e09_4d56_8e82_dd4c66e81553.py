"""Amazon web service game tech (_uncategorized_02), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a7558136-8e09-4d56-8e82-dd4c66e81553'
SOURCE_PATH = 'icons-json/_uncategorized_02/amazon web service game tech_a7558136-8e09-4d56-8e82-dd4c66e81553.json'
AUTHOR = 'json_to_solo'

class AmazonWebServiceGameTechUncategorized02(Solo48):
    icon_id = 'amazon-web-service-game-tech-uncategorized-02'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_02'
    aliases = ()
    keywords = ('amazon', 'web', 'service', 'game', 'tech', '_uncategorized_02')

    def build(self):
        self.add_line('e0', (5, 17), (4, 34))
        self.add_line('e1', (12, 38), (17, 31))
        self.add_line('e2', (18, 30), (30, 30))
        self.add_line('e3', (31, 31), (36, 38))
        self.add_line('e4', (44, 34), (43, 17))
        self.add_line('e5', (29, 12), (19, 12))
        self.add_bezier('e6', (4, 34), ((4, 34.074), (4.009, 34.006), (4.009, 34.08)), ((4.009, 36.8), (6.145, 39.975), (8.2, 39.975)), ((8.327, 39.988), (8.455, 39.988), (8.582, 40)), ((8.645, 40), (8.7, 39.988), (8.764, 39.988)), ((9.709, 39.988), (11.345, 38.886), (12, 38)))
        self.add_bezier('e7', (17, 31), ((17.318, 30.569), (17.655, 30.394), (18, 30)))
        self.add_bezier('e8', (30, 30), ((30.173, 30.209), (30.764, 30.474), (30.927, 30.72)), ((31.064, 30.917), (30.864, 30.815), (31, 31)))
        self.add_bezier('e9', (36, 38), ((36.591, 38.8), (38.327, 39.988), (39.182, 39.988)), ((39.245, 39.988), (39.309, 40), (39.364, 40)), ((39.366, 40), (39.368, 40), (39.37, 40)), ((39.495, 40), (39.611, 40), (39.736, 39.988)), ((41.836, 39.988), (43.982, 36.898), (43.982, 34.092)), ((43.991, 34.006), (43.991, 34.086), (44, 34)))
        self.add_bezier('e10', (43, 17), ((42.773, 12.668), (38.564, 8.025), (35.509, 8.025)), ((35.382, 8.012), (35.255, 8.012), (35.118, 8)), ((34.991, 8.012), (34.864, 8.012), (34.736, 8.025)), ((32.4, 8.025), (30.864, 10.486), (29, 12)))
        self.add_bezier('e11', (19, 12), ((17.464, 10.215), (14.682, 8.012), (12.564, 8.012)), ((12.385, 8.012), (12.206, 8), (12.027, 8)), ((12.024, 8), (12.021, 8), (12.018, 8)), ((11.964, 8.012), (11.9, 8.012), (11.836, 8.025)), ((8.755, 8.025), (5.218, 12.815), (5, 17)))
        self.add_contour('c0', 'e0', 'e6', 'e1', 'e7', 'e2', 'e8', 'e3', 'e9', 'e4', 'e10', 'e5', 'e11', closed=True)
