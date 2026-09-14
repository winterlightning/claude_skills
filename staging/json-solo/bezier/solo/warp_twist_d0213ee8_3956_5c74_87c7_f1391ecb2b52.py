"""Warp twist (design), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd0213ee8-3956-5c74-87c7-f1391ecb2b52'
SOURCE_PATH = 'icons-json/design/warp twist_d0213ee8-3956-5c74-87c7-f1391ecb2b52.json'
AUTHOR = 'json_to_solo'

class WarpTwistDesign(Solo48):
    icon_id = 'warp-twist-design'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('warp', 'twist', 'design')

    def build(self):
        self.add_line('e0', (26, 22), (22, 25))
        self.add_line('e1', (42, 6), (6, 6))
        self.add_line('e2', (6, 6), (6, 42))
        self.add_line('e3', (6, 42), (42, 42))
        self.add_line('e4', (42, 42), (42, 6))
        self.add_bezier('e5', (28, 6), ((28.466, 7.432), (29.081, 8.962), (29.261, 10.484)), ((29.711, 14.264), (28.725, 19.275), (26, 22)))
        self.add_bezier('e6', (22, 25), ((21.411, 25.589), (21.292, 26.176), (20.825, 26.864)), ((18.379, 30.464), (17.823, 35.16), (18.96, 39.333)), ((19.205, 40.241), (19.681, 41.141), (20, 42)))
        self.add_contour('c0', 'e5', 'e0', 'e6')
        self.add_contour('c1', 'e1', 'e2', 'e3', 'e4', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
