"""P (typeface), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8caf81fe-c279-43b5-aea9-a67d5114c2e9'
SOURCE_PATH = 'icons-json/typeface/p_8caf81fe-c279-43b5-aea9-a67d5114c2e9.json'
AUTHOR = 'json_to_solo'

class PTypeface(Solo48):
    icon_id = 'p-typeface'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('p', 'typeface')

    def build(self):
        self.add_line('e0', (8, 10), (8, 44))
        self.add_bezier('e1', (8, 25), ((8, 25), (8.012, 24.918), (8.012, 24.927)), ((8.012, 25.236), (9.982, 26.727), (10.302, 26.955)), ((13.169, 29.073), (16.935, 30.555), (20.997, 30.873)), ((30.966, 31.645), (39.975, 25.918), (39.975, 18.491)), ((39.975, 18.291), (40, 18.082), (40, 17.882)), ((40, 17.877), (40, 17.872), (40, 17.867)), ((40, 17.554), (39.988, 17.241), (39.988, 16.936)), ((39.988, 11.191), (35.717, 6.509), (28.209, 4.736)), ((26.474, 4.327), (24.591, 4.009), (22.757, 4.009)), ((22.624, 4), (22.49, 4), (22.357, 4)), ((22.355, 4), (22.353, 4), (22.351, 4)), ((22.092, 4), (21.834, 4.009), (21.575, 4.009)), ((17.28, 4.009), (13.231, 5.782), (10.388, 8.045)), ((10.018, 8.336), (8.025, 9.945), (8.025, 10.336)), ((8.025, 10.345), (8, 9.991), (8, 10)))
        self.add_contour('c0', 'e1', 'e0')
