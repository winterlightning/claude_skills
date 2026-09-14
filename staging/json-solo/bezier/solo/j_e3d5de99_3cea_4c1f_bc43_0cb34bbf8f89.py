"""J (typeface), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e3d5de99-3cea-4c1f-bc43-0cb34bbf8f89'
SOURCE_PATH = 'icons-json/typeface/J_e3d5de99-3cea-4c1f-bc43-0cb34bbf8f89.json'
AUTHOR = 'json_to_solo'

class JTypeface(Solo48):
    icon_id = 'j-typeface'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('j', 'typeface')

    def build(self):
        self.add_line('e0', (16, 4), (40, 4))
        self.add_line('e1', (40, 4), (40, 38))
        self.add_bezier('e2', (40, 38), ((40, 38.082), (39.968, 37.8), (39.968, 37.882)), ((39.968, 38.436), (39.616, 39.055), (39.264, 39.573)), ((37.136, 42.7), (30.864, 43.982), (25.328, 43.982)), ((24.896, 43.982), (24.448, 44), (24, 44)), ((23.993, 44), (23.986, 44), (23.979, 44)), ((23.538, 44), (23.097, 43.982), (22.672, 43.982)), ((17.136, 43.982), (10.864, 42.7), (8.736, 39.573)), ((8.384, 39.055), (8.032, 38.436), (8.032, 37.882)), ((8.032, 37.8), (8, 37.727), (8, 37.655)), ((8, 37.645), (8, 38.009), (8, 38)))
        self.add_contour('c0', 'e0', 'e1', 'e2')
