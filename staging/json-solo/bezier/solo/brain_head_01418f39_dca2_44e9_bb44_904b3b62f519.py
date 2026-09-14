"""Brain head (health), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '01418f39-dca2-44e9-bb44-904b3b62f519'
SOURCE_PATH = 'icons-json/health/brain head_01418f39-dca2-44e9-bb44-904b3b62f519.json'
AUTHOR = 'json_to_solo'

class BrainHeadHealth(Solo48):
    icon_id = 'brain-head-health'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('brain', 'head', 'health')

    def build(self):
        self.add_line('e0', (36, 44), (36, 32))
        self.add_line('e1', (12, 14), (8, 27))
        self.add_line('e2', (11, 28), (11, 33))
        self.add_line('e3', (16, 38), (19, 38))
        self.add_line('e4', (19, 38), (19, 44))
        self.add_bezier('e5', (36, 32), ((36, 31.727), (35.832, 31.591), (35.949, 31.345)), ((36.118, 30.973), (36.514, 30.673), (36.758, 30.364)), ((37.229, 29.764), (37.617, 29.127), (37.962, 28.436)), ((39.04, 26.282), (39.992, 22.891), (39.992, 20.464)), ((39.992, 20.338), (40, 20.213), (40, 20.096)), ((40, 20.095), (40, 20.093), (40, 20.091)), ((40, 19.8), (39.983, 19.5), (39.983, 19.209)), ((39.983, 11.045), (33.457, 4.018), (25.903, 4.018)), ((25.709, 4.018), (25.524, 4), (25.331, 4)), ((25.33, 4), (25.329, 4), (25.328, 4)), ((25.269, 4), (25.203, 4), (25.145, 4)), ((19.107, 4), (14.021, 7.891), (12, 14)))
        self.add_bezier('e6', (8, 27), ((8.118, 27.164), (8.109, 27.091), (8.244, 27.245)), ((8.817, 27.855), (10.301, 27.991), (11, 28)))
        self.add_bezier('e7', (11, 33), ((11, 35.045), (14.114, 38), (16, 38)))
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e6', 'e2', 'e7', 'e3', 'e4')
