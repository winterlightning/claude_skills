"""Alluvium (_uncategorized_02), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b3e4a9c7-dc3d-4a9b-81c9-23a3db70e396'
SOURCE_PATH = 'icons-json/_uncategorized_02/alluvium_b3e4a9c7-dc3d-4a9b-81c9-23a3db70e396.json'
AUTHOR = 'json_to_solo'

class AlluviumUncategorized02(Solo48):
    icon_id = 'alluvium-uncategorized-02'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_02'
    aliases = ()
    keywords = ('alluvium', '_uncategorized_02')

    def build(self):
        self.add_line('e0', (21, 10), (26, 13))
        self.add_line('e1', (21, 23), (26, 25))
        self.add_line('e2', (21, 35), (26, 38))
        self.add_bezier('e3', (4, 12), ((6.018, 10.326), (8.118, 9.022), (10.455, 8.48)), ((11.218, 8.295), (12.018, 8.025), (12.809, 8.025)), ((12.982, 8.025), (13.164, 8), (13.336, 8)), ((13.339, 8), (13.342, 8), (13.344, 8)), ((13.515, 8), (13.694, 8.025), (13.873, 8.025)), ((16.1, 8.025), (18.936, 8.88), (21, 10)))
        self.add_bezier('e4', (26, 13), ((30.545, 15.462), (35.255, 16.32), (39.782, 13.206)), ((41.309, 12.148), (42.655, 10.428), (44, 9)))
        self.add_bezier('e5', (4, 24), ((9.509, 19.532), (15.145, 19.825), (21, 23)))
        self.add_bezier('e6', (26, 25), ((33.173, 28.889), (38.036, 29.04), (44, 22)))
        self.add_bezier('e7', (4, 36), ((9.436, 31.348), (15.191, 31.849), (21, 35)))
        self.add_bezier('e8', (26, 38), ((27.627, 38.874), (30.327, 39.988), (32.064, 39.988)), ((32.162, 39.988), (32.269, 40), (32.368, 40)), ((32.37, 40), (32.371, 40), (32.373, 40)), ((32.509, 40), (32.636, 39.988), (32.773, 39.988)), ((33.627, 39.988), (34.5, 39.545), (35.327, 39.262)), ((38.736, 38.092), (41.364, 36.089), (44, 33)))
        self.add_contour('c0', 'e3', 'e0', 'e4')
        self.add_contour('c1', 'e5', 'e1', 'e6')
        self.add_contour('c2', 'e7', 'e2', 'e8')
