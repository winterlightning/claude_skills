"""Astrology lilith (religion), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8fe41c51-86b1-5293-9e23-cf23e45a15fc'
SOURCE_PATH = 'icons-json/religion/astrology lilith_8fe41c51-86b1-5293-9e23-cf23e45a15fc.json'
AUTHOR = 'json_to_solo'

class AstrologyLilithReligion(Solo48):
    icon_id = 'astrology-lilith-religion'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'religion'
    aliases = ()
    keywords = ('astrology', 'lilith', 'religion')

    def build(self):
        self.add_line('e0', (25, 28), (25, 44))
        self.add_line('e1', (15, 36), (35, 36))
        self.add_bezier('e2', (33, 6), ((30.538, 5.136), (27.286, 4.009), (24.505, 4.009)), ((24.323, 4.009), (24.153, 4), (23.972, 4)), ((23.969, 4), (23.966, 4), (23.963, 4)), ((23.778, 4), (23.594, 4.009), (23.409, 4.009)), ((21.822, 4.009), (20.025, 4.427), (18.56, 4.873)), ((12.591, 6.682), (8.012, 10.882), (8.012, 15.773)), ((8.012, 15.844), (8, 15.907), (8, 15.978)), ((8, 15.98), (8, 15.981), (8, 15.982)), ((8.012, 16.118), (8.012, 16.255), (8.025, 16.391)), ((8.025, 18.1), (8.702, 19.845), (9.76, 21.355)), ((12.886, 25.864), (18.671, 27.582), (25.231, 27.636)), ((31.2, 27.682), (35.877, 26.164), (39.655, 22.718)), ((39.828, 22.555), (39.84, 22.173), (40, 22)))
        self.add_contour('c0', 'e2')
        self.add_contour('c1', 'e0')
        self.add_contour('c2', 'e1')
        self.relate('connect', 'c1', 'c0')
