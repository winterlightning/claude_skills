"""Moon and cancel (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '487fd90e-ac2a-4467-9057-edc666b22495'
SOURCE_PATH = 'icons-json/symbol/moon and cancel_487fd90e-ac2a-4467-9057-edc666b22495.json'
AUTHOR = 'json_to_solo'

class MoonAndCancel(Solo48):
    icon_id = 'moon-and-cancel'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('moon', 'and', 'cancel', 'symbol')

    def build(self):
        self.add_line('e0', (42, 18), (35, 26))
        self.add_line('e1', (35, 18), (42, 26))
        self.add_line('e2', (32, 40), (26, 37))
        self.add_bezier('e3', (26, 37), ((24.323, 36.28), (22.781, 33.385), (21.987, 31.789)), ((18.952, 25.628), (19.639, 17.913), (24.245, 12.709)), ((25.735, 11.032), (27.674, 10.017), (29.654, 9.044)), ((30.161, 8.798), (30.676, 8.553), (31.184, 8.307)), ((31.306, 8.242), (31.429, 8.185), (31.552, 8.127)), ((31.552, 8.119), (30.259, 7.653), (29.613, 7.424)), ((27.641, 6.728), (25.579, 6.008), (23.46, 6.008)), ((23.404, 6.008), (23.339, 6), (23.275, 6)), ((23.274, 6), (23.273, 6), (23.272, 6)), ((22.977, 6), (22.691, 6.016), (22.396, 6.016)), ((14.64, 6.016), (8.504, 11.793), (6.63, 19.042)), ((6.303, 20.302), (6.008, 21.693), (6.008, 23.002)), ((6.008, 23.179), (6, 23.356), (6, 23.533)), ((6, 23.536), (6, 23.539), (6, 23.542)), ((6, 23.853), (6.008, 24.164), (6.008, 24.475)), ((6.008, 31.887), (11.146, 39.079), (18.224, 41.28)), ((19.508, 41.681), (20.907, 41.984), (22.249, 41.984)), ((22.445, 41.984), (22.634, 42), (22.822, 42)), ((22.825, 42), (22.828, 42), (22.831, 42)), ((23.024, 42), (23.209, 41.984), (23.403, 41.984)), ((26.397, 41.984), (29.235, 40.957), (32, 40)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3', closed=True)
