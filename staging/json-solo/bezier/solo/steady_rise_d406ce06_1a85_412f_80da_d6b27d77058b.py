"""Steady rise (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd406ce06-1a85-412f-80da-d6b27d77058b'
SOURCE_PATH = 'icons-json/arrows/steady rise_d406ce06-1a85-412f-80da-d6b27d77058b.json'
AUTHOR = 'json_to_solo'

class SteadyRiseArrows(Solo48):
    icon_id = 'steady-rise-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('steady', 'rise', 'arrows')

    def build(self):
        self.add_line('e0', (39, 8), (44, 14))
        self.add_line('e1', (4, 40), (15, 40))
        self.add_line('e2', (20, 34), (20, 22))
        self.add_line('e3', (26, 14), (44, 14))
        self.add_line('e4', (39, 20), (44, 14))
        self.add_bezier('e5', (15, 40), ((16.909, 40), (19.436, 37.194), (20.091, 34.831)), ((20.155, 34.597), (20, 34.185), (20, 34)))
        self.add_bezier('e6', (20, 22), ((20, 21.84), (20.536, 20.886), (20.582, 20.677)), ((21.127, 17.588), (23.473, 14), (26, 14)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e5', 'e2', 'e6', 'e3')
        self.add_contour('c2', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
