"""C (typeface), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0097c435-6367-4391-b64a-a9c79558dfd5'
SOURCE_PATH = 'icons-json/typeface/c_0097c435-6367-4391-b64a-a9c79558dfd5.json'
AUTHOR = 'json_to_solo'

class CTypeface(Solo48):
    icon_id = 'c-typeface'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('c', 'typeface')

    def build(self):
        self.add_line('e0', (8, 14), (8, 35))
        self.add_bezier('e1', (40, 10), ((37.424, 6.645), (32.096, 4.009), (25.168, 4.009)), ((24.916, 4.009), (24.664, 4), (24.412, 4)), ((24.408, 4), (24.404, 4), (24.4, 4)), ((24.144, 4), (23.888, 4.009), (23.616, 4.018)), ((15.472, 4.018), (8.032, 9.073), (8.032, 13.545)), ((8.016, 13.7), (8.016, 13.845), (8, 14)))
        self.add_bezier('e2', (8, 35), ((8, 39.5), (15.312, 43.982), (23.408, 43.982)), ((23.664, 43.991), (23.92, 43.991), (24.176, 44)), ((24.182, 44), (24.188, 44), (24.194, 44)), ((24.572, 44), (24.95, 43.982), (25.344, 43.982)), ((32.016, 43.982), (37.68, 41.309), (40, 38)))
        self.add_contour('c0', 'e1', 'e0', 'e2')
