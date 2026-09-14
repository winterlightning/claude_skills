"""Fishing line (outdoors), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd931a080-b0aa-5280-b50e-074e997cbca4'
SOURCE_PATH = 'icons-json/outdoors/fishing line_d931a080-b0aa-5280-b50e-074e997cbca4.json'
AUTHOR = 'json_to_solo'

class FishingLineOutdoors(Solo48):
    icon_id = 'fishing-line-outdoors'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('fishing', 'line', 'outdoors')

    def build(self):
        self.add_line('e0', (33, 4), (33, 13))
        self.add_line('e1', (13, 34), (8, 30))
        self.add_line('e2', (8, 30), (8, 37))
        self.add_line('e3', (33, 37), (33, 20))
        self.add_arc('e4-top', (26, 17), (40, 17), radius_x=7, radius_y=4)
        self.add_arc('e4-bottom', (40, 17), (26, 17), radius_x=7, radius_y=4)
        self.add_bezier('e5', (8, 37), ((8, 37.355), (8.036, 37.436), (8.036, 37.791)), ((8.036, 40.745), (14.24, 43.991), (20.071, 43.991)), ((20.194, 43.991), (20.333, 44), (20.473, 44)), ((20.476, 44), (20.478, 44), (20.48, 44)), ((20.747, 43.991), (21.031, 43.991), (21.316, 43.982)), ((22.844, 43.982), (24.516, 43.627), (25.849, 43.282)), ((31.396, 41.864), (33, 40), (33, 37)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e5', 'e3')
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
        self.relate('connect', 'c0', 'e4')
        self.relate('connect', 'c1', 'e4')
