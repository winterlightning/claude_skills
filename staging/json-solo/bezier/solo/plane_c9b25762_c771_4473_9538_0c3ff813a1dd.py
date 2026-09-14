"""Plane (travel), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c9b25762-c771-4473-9538-0c3ff813a1dd'
SOURCE_PATH = 'icons-json/travel/plane_c9b25762-c771-4473-9538-0c3ff813a1dd.json'
AUTHOR = 'json_to_solo'

class PlaneC9b25762(Solo48):
    icon_id = 'plane-c9b25762'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'travel'
    aliases = ()
    keywords = ('plane', 'travel')

    def build(self):
        self.add_line('e0', (44, 8), (18, 37))
        self.add_line('e1', (7, 34), (4, 30))
        self.add_line('e2', (34, 19), (14, 8))
        self.add_bezier('e3', (18, 37), ((16.791, 38.312), (15.036, 39.984), (13.536, 39.984)), ((13.42, 39.984), (13.304, 40), (13.187, 40)), ((13.186, 40), (13.184, 40), (13.182, 40)), ((13.055, 39.984), (12.936, 39.984), (12.809, 39.968)), ((12.355, 39.968), (11.909, 39.664), (11.491, 39.392)), ((9.564, 38.112), (9.318, 36.912), (7.809, 34.832)), ((7.464, 34.352), (7.364, 34.416), (7, 34)))
        self.add_contour('c0', 'e0', 'e3', 'e1')
        self.add_contour('c1', 'e2')
        self.relate('connect', 'c1', 'c0')
