"""20 (text) (other), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '11778f43-e4ae-47e0-a607-32a2e3ab7086'
SOURCE_PATH = 'icons-json/other/20 (text)_11778f43-e4ae-47e0-a607-32a2e3ab7086.json'
AUTHOR = 'json_to_solo'

class Icon20TextOther(Solo48):
    icon_id = 'icon-20-text-other'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('text', 'other')

    def build(self):
        self.add_line('e0', (15, 24), (4, 40))
        self.add_line('e1', (4, 40), (18, 40))
        self.add_bezier('e2', (5, 14), ((6.455, 11.231), (8.5, 8.012), (11.255, 8.012)), ((11.335, 8), (11.416, 8), (11.496, 8)), ((11.497, 8), (11.499, 8), (11.5, 8)), ((11.582, 8), (11.655, 8.012), (11.736, 8.012)), ((12.627, 8.012), (13.564, 8.505), (14.336, 9.058)), ((18.455, 12.049), (17.764, 19.938), (15, 24)))
        self.add_bezier('e3', (28, 24), ((28.064, 17.735), (29.427, 8.012), (35.264, 8.012)), ((35.364, 8), (35.455, 8), (35.545, 8)), ((35.636, 8), (35.736, 8), (35.827, 8.012)), ((40.864, 8.012), (43.982, 16.234), (43.982, 22.314)), ((43.982, 22.769), (44, 23.237), (44, 23.692)), ((44, 23.701), (44, 23.71), (44, 23.718)), ((44, 24.264), (43.982, 24.821), (43.982, 25.366)), ((43.982, 31.286), (41.391, 39.988), (36.291, 39.988)), ((36.191, 40), (36.1, 40), (36.009, 40)), ((35.918, 40), (35.818, 40), (35.727, 39.988)), ((29.782, 39.988), (28.036, 30.548), (28, 24)))
        self.add_contour('c0', 'e2', 'e0', 'e1')
        self.add_contour('c1', 'e3', closed=True)
