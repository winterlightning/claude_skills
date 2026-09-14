"""Merge down (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e10d469e-de58-4e4f-87aa-40685044f87f'
SOURCE_PATH = 'icons-json/arrows/merge down_e10d469e-de58-4e4f-87aa-40685044f87f.json'
AUTHOR = 'json_to_solo'

class MergeDown(Solo48):
    icon_id = 'merge-down'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('merge', 'down', 'arrows')

    def build(self):
        self.add_line('e0', (24, 19), (24, 44))
        self.add_line('e1', (19, 39), (24, 44))
        self.add_line('e2', (29, 39), (24, 44))
        self.add_line('e3', (25, 15), (24, 19))
        self.add_bezier('e4', (8, 4), ((8.109, 4), (8.227, 4.009), (8.345, 4.009)), ((8.758, 4.009), (9.179, 4.009), (9.592, 4.009)), ((9.895, 4.009), (10.198, 4), (10.501, 4)), ((10.905, 4), (11.318, 4.009), (11.722, 4.009)), ((18.021, 4.009), (21.987, 8.945), (23.293, 15.191)), ((23.528, 16.309), (23.764, 17.882), (24, 19)))
        self.add_bezier('e5', (24, 18), ((24, 18.3), (24.008, 18.245), (24, 18.545)), ((24, 18.655), (24, 18.918), (24, 19)))
        self.add_bezier('e6', (40, 4), ((38.829, 4), (37.659, 4.018), (36.488, 4.018)), ((30.493, 4.018), (26.373, 9.064), (25, 15)))
        self.add_contour('c0', 'e4')
        self.add_contour('c1', 'e5')
        self.add_contour('c2', 'e0')
        self.add_contour('c3', 'e1')
        self.add_contour('c4', 'e2')
        self.add_contour('c5', 'e6', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c5', 'c0')
        self.relate('connect', 'c5', 'c1')
