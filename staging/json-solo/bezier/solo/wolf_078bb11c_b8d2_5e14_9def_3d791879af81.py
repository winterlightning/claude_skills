"""Wolf (animals), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '078bb11c-b8d2-5e14-9def-3d791879af81'
SOURCE_PATH = 'icons-json/animals/wolf_078bb11c-b8d2-5e14-9def-3d791879af81.json'
AUTHOR = 'json_to_solo'

class Wolf(Solo48):
    icon_id = 'wolf'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('wolf', 'animals')

    def build(self):
        self.add_line('e0', (26, 6), (26, 13))
        self.add_line('e1', (35, 22), (42, 25))
        self.add_line('e2', (35, 31), (30, 30))
        self.add_bezier('e3', (6, 26), ((6.074, 25.845), (6.057, 26.103), (6.139, 25.955)), ((6.245, 25.784), (6.425, 25.669), (6.548, 25.505)), ((7.186, 24.614), (7.661, 23.591), (8.291, 22.683)), ((9.796, 20.531), (11.572, 18.575), (13.601, 16.898)), ((14.395, 16.244), (15.213, 15.63), (16.088, 15.074)), ((16.735, 14.656), (17.52, 14.313), (18.085, 13.773)), ((18.551, 13.323), (18.526, 12.275), (18.731, 11.678)), ((18.903, 11.179), (19.173, 10.688), (19.435, 10.23)), ((20.94, 7.62), (23.235, 6.638), (26, 6)))
        self.add_bezier('e4', (26, 13), ((27.931, 13.368), (29.351, 14.141), (30.701, 15.704)), ((32.673, 17.986), (31.776, 20.388), (35, 22)))
        self.add_bezier('e5', (42, 25), ((42, 25.245), (42, 25.309), (42, 25.555)), ((42, 25.775), (41.444, 26.725), (41.329, 26.995)), ((40.274, 29.449), (37.733, 31.393), (35, 31)))
        self.add_bezier('e6', (30, 30), ((28.781, 29.828), (27.215, 30.267), (26.365, 31.061)), ((23.272, 33.925), (24.722, 38.343), (25, 42)))
        self.add_contour('c0', 'e3', 'e0', 'e4', 'e1', 'e5', 'e2', 'e6')
