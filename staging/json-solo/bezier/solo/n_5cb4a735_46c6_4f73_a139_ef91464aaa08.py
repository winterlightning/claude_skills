"""N (typeface), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5cb4a735-46c6-4f73-a139-ef91464aaa08'
SOURCE_PATH = 'icons-json/typeface/n_5cb4a735-46c6-4f73-a139-ef91464aaa08.json'
AUTHOR = 'json_to_solo'

class N5cb4a735(Solo48):
    icon_id = 'n-5cb4a735'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('n', 'typeface')

    def build(self):
        self.add_line('e0', (8, 5), (8, 44))
        self.add_line('e1', (40, 16), (40, 44))
        self.add_bezier('e2', (8, 14), ((8, 13.982), (8.02, 13.964), (8.02, 13.955)), ((8.02, 13.164), (9.46, 11.009), (9.93, 10.373)), ((12.86, 6.373), (17.92, 4.009), (23.21, 4.009)), ((23.466, 4.009), (23.732, 4), (23.988, 4)), ((23.992, 4), (23.996, 4), (24, 4)), ((24.24, 4), (24.48, 4.009), (24.71, 4.009)), ((30.61, 4.009), (36.86, 6.536), (39.14, 11.764)), ((39.6, 12.836), (39.98, 14.073), (39.98, 15.236)), ((39.98, 15.427), (40, 15.809), (40, 16)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e2', 'e1')
        self.relate('connect', 'c1', 'c0')
