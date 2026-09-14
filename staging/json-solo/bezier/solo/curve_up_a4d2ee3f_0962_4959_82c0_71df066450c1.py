"""Curve up (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a4d2ee3f-0962-4959-82c0-71df066450c1'
SOURCE_PATH = 'icons-json/arrows/curve up_a4d2ee3f-0962-4959-82c0-71df066450c1.json'
AUTHOR = 'json_to_solo'

class CurveUpA4d2ee3f(Solo48):
    icon_id = 'curve-up-a4d2ee3f'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('curve', 'up', 'arrows')

    def build(self):
        self.add_line('e0', (37, 6), (42, 11))
        self.add_line('e1', (6, 42), (17, 42))
        self.add_line('e2', (22, 35), (22, 17))
        self.add_line('e3', (28, 11), (42, 11))
        self.add_line('e4', (37, 16), (42, 11))
        self.add_bezier('e5', (17, 42), ((17.434, 42), (17.52, 41.812), (17.937, 41.681)), ((20.22, 40.936), (21.537, 38.858), (22.094, 36.633)), ((22.175, 36.297), (22, 35.311), (22, 35)))
        self.add_bezier('e6', (22, 17), ((22, 16.771), (22.511, 16.825), (22.568, 16.571)), ((23.035, 14.174), (24.777, 11.891), (27.158, 11.155)), ((27.428, 11.081), (27.73, 11), (28, 11)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e5', 'e2', 'e6', 'e3')
        self.add_contour('c2', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
