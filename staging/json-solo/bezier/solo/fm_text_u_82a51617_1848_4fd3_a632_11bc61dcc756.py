"""Fm (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '82a51617-1848-4fd3-a632-11bc61dcc756'
SOURCE_PATH = 'icons-json/symbol/fm (text u)_82a51617-1848-4fd3-a632-11bc61dcc756.json'
AUTHOR = 'json_to_solo'

class FmTextUSymbol(Solo48):
    icon_id = 'fm-text-u-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('fm', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (6, 14), (14, 14))
        self.add_line('e1', (6, 26), (6, 7))
        self.add_line('e2', (7, 6), (17, 6))
        self.add_line('e3', (24, 13), (24, 26))
        self.add_line('e4', (33, 17), (33, 26))
        self.add_line('e5', (42, 17), (42, 26))
        self.add_line('e6', (6, 42), (42, 42))
        self.add_bezier('e7', (6, 7), ((6.155, 6.714), (6.033, 6.278), (6.401, 6.09)), ((6.532, 6.025), (6.877, 6.065), (7, 6)))
        self.add_bezier('e8', (24, 17), ((24.393, 16.026), (24.859, 14.828), (25.759, 14.215)), ((28.181, 12.554), (32.485, 13.405), (33, 16.636)), ((33.041, 16.906), (33, 16.73), (33, 17)))
        self.add_bezier('e9', (33, 17), ((33.581, 15.568), (34.473, 14.067), (36.044, 13.642)), ((38.433, 12.995), (41.984, 14.165), (41.984, 17.119)), ((41.984, 17.234), (42, 16.885), (42, 17)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e7', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e8', 'e4')
        self.add_contour('c4', 'e9', 'e5')
        self.add_contour('c5', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c3', 'c2')
        self.relate('connect', 'c4', 'c3')
