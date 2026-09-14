"""Ge (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6a1cef81-74dd-4aac-86f0-786b211f3267'
SOURCE_PATH = 'icons-json/symbol/ge (text u)_6a1cef81-74dd-4aac-86f0-786b211f3267.json'
AUTHOR = 'json_to_solo'

class GeTextUSymbol(Solo48):
    icon_id = 'ge-text-u-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('ge', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (21, 19), (21, 16))
        self.add_line('e1', (21, 16), (16, 16))
        self.add_line('e2', (8, 44), (40, 44))
        self.add_bezier('e3', (21, 8), ((20.082, 5.873), (18.164, 4.018), (15.848, 4.018)), ((15.741, 4.009), (15.633, 4), (15.525, 4)), ((15.523, 4), (15.522, 4), (15.52, 4)), ((15.335, 4), (15.149, 4.018), (14.964, 4.018)), ((14.181, 4.018), (13.423, 4.273), (12.699, 4.555)), ((8.758, 6.1), (8.008, 10.764), (8.008, 14.773)), ((8.008, 15.018), (8, 15.255), (8, 15.5)), ((8, 15.945), (8.017, 16.4), (8.017, 16.855)), ((8.017, 19.582), (8.632, 22.764), (10.619, 24.618)), ((13.297, 27.127), (17.987, 27.2), (20.194, 23.955)), ((21.28, 22.373), (21, 20.909), (21, 19)))
        self.add_bezier('e4', (30, 19), ((31.566, 19.2), (33.027, 19.809), (34.611, 19.836)), ((35.84, 19.855), (37.642, 20.055), (38.754, 19.336)), ((40, 18.327), (39.579, 14.864), (38.627, 13.673)), ((36.682, 11.245), (33.204, 11.845), (31.377, 14.064)), ((28.893, 17.082), (29.053, 24.909), (33.272, 26.155)), ((35.318, 26.764), (38.417, 26.109), (39.629, 24.055)), ((39.764, 23.818), (39.992, 23.436), (39.992, 23.145)), ((39.992, 23.127), (40, 23.018), (40, 23)))
        self.add_contour('c0', 'e3', 'e0', 'e1')
        self.add_contour('c1', 'e4')
        self.add_contour('c2', 'e2')
