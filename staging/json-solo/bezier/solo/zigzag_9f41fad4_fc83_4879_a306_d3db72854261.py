"""Zigzag (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9f41fad4-fc83-4879-a306-d3db72854261'
SOURCE_PATH = 'icons-json/interface-essential/zigzag_9f41fad4-fc83-4879-a306-d3db72854261.json'
AUTHOR = 'json_to_solo'

class Zigzag(Solo48):
    icon_id = 'zigzag'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('zigzag', 'interface-essential')

    def build(self):
        self.add_line('e0', (33, 6), (39, 12))
        self.add_line('e1', (6, 42), (35, 42))
        self.add_line('e2', (35, 27), (13, 27))
        self.add_line('e3', (13, 12), (39, 12))
        self.add_line('e4', (33, 17), (39, 12))
        self.add_bezier('e5', (35, 42), ((35.515, 42), (36.592, 41.714), (37.075, 41.525)), ((39.766, 40.47), (41.992, 37.688), (41.992, 34.718)), ((41.992, 34.638), (42, 34.557), (42, 34.477)), ((42, 34.475), (42, 34.474), (42, 34.473)), ((42, 34.325), (41.992, 34.178), (41.992, 34.031)), ((41.992, 30.856), (39.415, 28.377), (36.535, 27.551)), ((36.248, 27.469), (35.278, 27), (35, 27)))
        self.add_bezier('e6', (13, 27), ((12.722, 27), (11.768, 27.076), (11.482, 26.978)), ((8.569, 26.029), (6.008, 22.887), (6.008, 19.737)), ((6.008, 19.664), (6, 19.59), (6, 19.516)), ((6, 19.402), (6.008, 19.287), (6.008, 19.173)), ((6.008, 16.015), (8.005, 13.355), (10.852, 12.161)), ((11.335, 11.965), (12.485, 12), (13, 12)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e5', 'e2', 'e6', 'e3')
        self.add_contour('c2', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
