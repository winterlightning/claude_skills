"""Pi (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2d02ee84-d369-4690-b442-c33909f4220f'
SOURCE_PATH = 'icons-json/symbol/pi_2d02ee84-d369-4690-b442-c33909f4220f.json'
AUTHOR = 'json_to_solo'

class PiSymbol(Solo48):
    icon_id = 'pi-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('pi', 'symbol')

    def build(self):
        self.add_line('e0', (13, 8), (44, 8))
        self.add_line('e1', (32, 28), (34, 8))
        self.add_bezier('e2', (4, 16), ((5.218, 12.682), (7.664, 9.196), (11.482, 8.286)), ((12, 8.16), (12.473, 8), (13, 8)))
        self.add_bezier('e3', (9, 40), ((10.291, 37.381), (11.836, 34.737), (12.718, 31.975)), ((14.173, 27.402), (14.718, 22.375), (15.373, 17.659)), ((15.827, 14.434), (16.645, 11.234), (17, 8)))
        self.add_bezier('e4', (42, 37), ((40.818, 38.617), (39.382, 39.992), (37.064, 39.992)), ((36.982, 39.992), (36.9, 40), (36.818, 40)), ((36.691, 40), (36.564, 39.983), (36.445, 39.983)), ((35.855, 39.983), (35.236, 39.781), (34.709, 39.545)), ((30.909, 37.794), (31.709, 31.242), (32, 28)))
        self.add_contour('c0', 'e2', 'e0')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4', 'e1')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c0')
