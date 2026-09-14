"""Skate (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '76c38c7b-cbba-4778-a811-f79c71a23620'
SOURCE_PATH = 'icons-json/symbol/skate_76c38c7b-cbba-4778-a811-f79c71a23620.json'
AUTHOR = 'json_to_solo'

class SkateSymbol(Solo48):
    icon_id = 'skate-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('skate', 'symbol')

    def build(self):
        self.add_line('e0', (12, 24), (38, 24))
        self.add_bezier('e1', (4, 8), ((5.591, 15.12), (7.936, 20.72), (10.773, 23.04)), ((11.2, 23.387), (11.564, 24), (12, 24)))
        self.add_bezier('e2', (38, 24), ((40.764, 24), (42.045, 21.493), (43.745, 15.04)), ((43.891, 14.507), (43.882, 13.56), (44, 13)))
        self.add_dot('e3', (13, 40))
        self.add_dot('e4', (34, 40))
        self.add_contour('c0', 'e1', 'e0', 'e2')
