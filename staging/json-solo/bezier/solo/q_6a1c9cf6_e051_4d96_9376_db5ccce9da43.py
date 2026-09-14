"""Q (typeface), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6a1c9cf6-e051-4d96-9376-db5ccce9da43'
SOURCE_PATH = 'icons-json/typeface/q_6a1c9cf6-e051-4d96-9376-db5ccce9da43.json'
AUTHOR = 'json_to_solo'

class Q6a1c9cf6(Solo48):
    icon_id = 'q-6a1c9cf6'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('q', 'typeface')

    def build(self):
        self.add_line('e0', (40, 10), (40, 44))
        self.add_bezier('e1', (40, 25), ((40, 25), (39.988, 24.918), (39.988, 24.927)), ((39.988, 25.236), (38.018, 26.727), (37.698, 26.955)), ((34.831, 29.073), (31.065, 30.555), (27.003, 30.873)), ((17.034, 31.645), (8.025, 25.918), (8.025, 18.491)), ((8.025, 18.291), (8, 18.082), (8, 17.882)), ((8, 17.876), (8, 17.87), (8, 17.865)), ((8, 17.507), (8.025, 17.158), (8.025, 16.809)), ((8.025, 11.118), (12.406, 6.482), (19.791, 4.736)), ((21.526, 4.327), (23.409, 4.009), (25.243, 4.009)), ((25.376, 4), (25.51, 4), (25.643, 4)), ((25.645, 4), (25.647, 4), (25.649, 4)), ((25.908, 4), (26.166, 4.009), (26.425, 4.009)), ((30.72, 4.009), (34.769, 5.782), (37.612, 8.045)), ((37.982, 8.336), (39.975, 9.945), (39.975, 10.336)), ((39.975, 10.345), (40, 9.991), (40, 10)))
        self.add_contour('c0', 'e1', 'e0')
