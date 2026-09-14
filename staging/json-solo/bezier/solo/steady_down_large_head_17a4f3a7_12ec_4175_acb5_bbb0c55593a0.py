"""Steady down large head (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '17a4f3a7-12ec-4175-acb5-bbb0c55593a0'
SOURCE_PATH = 'icons-json/arrows/steady down large head_17a4f3a7-12ec-4175-acb5-bbb0c55593a0.json'
AUTHOR = 'json_to_solo'

class SteadyDownLargeHeadArrows(Solo48):
    icon_id = 'steady-down-large-head-arrows'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('steady', 'down', 'large', 'head', 'arrows')

    def build(self):
        self.add_line('e0', (8, 27), (18, 27))
        self.add_line('e1', (14, 39), (18, 44))
        self.add_line('e2', (23, 39), (18, 44))
        self.add_line('e3', (18, 27), (18, 14))
        self.add_line('e4', (31, 27), (18, 27))
        self.add_line('e5', (18, 27), (18, 44))
        self.add_bezier('e6', (18, 14), ((18, 13.491), (18.349, 12.773), (18.484, 12.282)), ((19.731, 7.818), (24.168, 4.009), (28.556, 4.009)), ((28.664, 4.009), (28.763, 4), (28.871, 4)), ((28.872, 4), (28.874, 4), (28.876, 4)), ((29.086, 4), (29.305, 4.009), (29.516, 4.009)), ((34.872, 4.009), (39.992, 9.264), (39.992, 15.109)), ((39.992, 15.172), (40, 15.226), (40, 15.288)), ((40, 15.289), (40, 15.29), (40, 15.291)), ((40, 15.527), (39.992, 15.755), (39.992, 15.991)), ((39.992, 20.536), (36.808, 24.809), (32.876, 26.191)), ((32.236, 26.418), (31.665, 27), (31, 27)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e6', 'e4', closed=True)
        self.add_contour('c4', 'e5')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c4')
