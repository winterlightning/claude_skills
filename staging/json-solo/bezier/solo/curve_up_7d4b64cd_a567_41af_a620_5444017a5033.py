"""Curve up (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7d4b64cd-a567-41af-a620-5444017a5033'
SOURCE_PATH = 'icons-json/arrows/curve up_7d4b64cd-a567-41af-a620-5444017a5033.json'
AUTHOR = 'json_to_solo'

class CurveUp7d4b64cd(Solo48):
    icon_id = 'curve-up-7d4b64cd'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('curve', 'up', 'arrows')

    def build(self):
        self.add_line('e0', (38, 6), (42, 11))
        self.add_line('e1', (6, 6), (6, 33))
        self.add_line('e2', (25, 33), (25, 20))
        self.add_line('e3', (33, 11), (42, 11))
        self.add_line('e4', (38, 16), (42, 11))
        self.add_bezier('e5', (6, 33), ((6, 33.638), (6.229, 34.325), (6.409, 34.931)), ((7.538, 38.662), (11.04, 41.992), (15.098, 41.992)), ((15.219, 41.992), (15.332, 42), (15.452, 42)), ((15.454, 42), (15.456, 42), (15.458, 42)), ((15.638, 42), (15.826, 41.992), (16.006, 41.992)), ((20.236, 41.992), (23.64, 38.465), (24.54, 34.546)), ((24.646, 34.08), (25, 33.475), (25, 33)))
        self.add_bezier('e6', (25, 20), ((25, 19.395), (25.039, 18.567), (25.195, 17.978)), ((26.045, 14.845), (28.246, 12.325), (31.355, 11.31)), ((31.838, 11.155), (32.501, 11), (33, 11)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e5', 'e2', 'e6', 'e3')
        self.add_contour('c2', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
