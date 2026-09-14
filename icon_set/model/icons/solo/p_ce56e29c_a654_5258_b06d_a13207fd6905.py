"""P (typeface), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ce56e29c-a654-5258-b06d-a13207fd6905'
SOURCE_PATH = 'icons-json/typeface/P_ce56e29c-a654-5258-b06d-a13207fd6905.json'
AUTHOR = 'json_to_solo'

class P(Solo48):
    icon_id = 'p'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('p', 'typeface')

    def build(self):
        self.add_line('e0', (8, 26), (26, 26))
        self.add_line('e1', (25, 4), (8, 4))
        self.add_line('e2', (8, 4), (8, 44))
        self.add_bezier('e3', (26, 26), ((26.825, 26), (28.308, 25.555), (29.108, 25.4)), ((35.372, 24.209), (39.988, 19.909), (39.988, 15.082)), ((39.988, 15.01), (40, 14.93), (40, 14.858)), ((40, 14.857), (40, 14.856), (40, 14.855)), ((40, 14.782), (39.988, 14.709), (39.988, 14.636)), ((39.988, 12.745), (39.36, 10.518), (37.969, 8.909)), ((35.397, 5.927), (29.738, 4), (25, 4)))
        self.add_contour('c0', 'e0', 'e3', 'e1', 'e2')
