"""Text bold (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8004bf6f-3430-545f-9b06-3c0cc0268453'
SOURCE_PATH = 'icons-json/interface-essential/text bold_8004bf6f-3430-545f-9b06-3c0cc0268453.json'
AUTHOR = 'json_to_solo'

class TextBoldInterfaceEssential(Solo48):
    icon_id = 'text-bold-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('text', 'bold', 'interface-essential')

    def build(self):
        self.add_line('e0', (30, 44), (8, 44))
        self.add_line('e1', (8, 44), (8, 4))
        self.add_line('e2', (8, 4), (28, 4))
        self.add_line('e3', (30, 24), (8, 24))
        self.add_bezier('e4', (28, 4), ((29.21, 4), (30.57, 4.391), (31.68, 4.782)), ((33.22, 5.327), (34.71, 6.073), (35.88, 7.145)), ((39.38, 10.373), (39.59, 16.109), (36.8, 19.755)), ((35.74, 21.145), (34.14, 22.036), (32.54, 22.827)), ((31.83, 23.173), (31.11, 23.509), (30.38, 23.836)), ((30.25, 23.891), (30.13, 23.945), (30, 24)), ((30, 24), (31.06, 24.382), (31.16, 24.418)), ((32.47, 24.891), (33.89, 25.291), (35.11, 25.955)), ((38.19, 27.636), (39.99, 30.464), (39.99, 33.764)), ((39.99, 33.982), (40, 34.191), (40, 34.409)), ((40, 34.41), (40, 34.411), (40, 34.412)), ((40, 34.475), (40, 34.547), (40, 34.618)), ((40, 38.773), (36.31, 42.609), (32, 43.591)), ((31.67, 43.664), (30.78, 44), (30.53, 44)), ((30.36, 44), (30.18, 44), (30, 44)))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e4', closed=True)
        self.add_contour('c1', 'e3')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
