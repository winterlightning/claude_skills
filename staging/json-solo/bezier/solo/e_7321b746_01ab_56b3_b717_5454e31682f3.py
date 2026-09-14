"""E (typeface), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7321b746-01ab-56b3-b717-5454e31682f3'
SOURCE_PATH = 'icons-json/typeface/E_7321b746-01ab-56b3-b717-5454e31682f3.json'
AUTHOR = 'json_to_solo'

class E7321b746(Solo48):
    icon_id = 'e-7321b746'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('e', 'typeface')

    def build(self):
        self.add_line('e0', (40, 4), (9, 4))
        self.add_line('e1', (8, 5), (8, 43))
        self.add_line('e2', (9, 44), (40, 44))
        self.add_line('e3', (33, 24), (8, 24))
        self.add_bezier('e4', (9, 4), ((8.545, 4.209), (8.012, 4.173), (8.012, 4.764)), ((8.012, 4.818), (8, 4.955), (8, 5)))
        self.add_bezier('e5', (8, 43), ((8, 43.045), (8.012, 43.191), (8.012, 43.236)), ((8.012, 43.582), (8.566, 43.982), (9.022, 43.982)), ((9.095, 43.991), (8.926, 43.991), (9, 44)))
        self.add_contour('c0', 'e0', 'e4', 'e1', 'e5', 'e2')
        self.add_contour('c1', 'e3')
        self.relate('connect', 'c1', 'c0')
