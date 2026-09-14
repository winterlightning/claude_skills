"""Curve down large head (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3abee883-a907-4d15-9c15-669562a83a7f'
SOURCE_PATH = 'icons-json/arrows/curve down large head_3abee883-a907-4d15-9c15-669562a83a7f.json'
AUTHOR = 'json_to_solo'

class CurveDownLargeHeadArrows(Solo48):
    icon_id = 'curve-down-large-head-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('curve', 'down', 'large', 'head', 'arrows')

    def build(self):
        self.add_line('e0', (6, 6), (6, 13))
        self.add_line('e1', (12, 19), (26, 19))
        self.add_line('e2', (35, 27), (35, 42))
        self.add_line('e3', (26, 34), (35, 42))
        self.add_line('e4', (42, 34), (35, 42))
        self.add_arc('e5', (6, 13), (12, 19), radius_x=8, sweep=False)
        self.add_arc('e6', (26, 19), (35, 27), radius_x=10)
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e6', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
