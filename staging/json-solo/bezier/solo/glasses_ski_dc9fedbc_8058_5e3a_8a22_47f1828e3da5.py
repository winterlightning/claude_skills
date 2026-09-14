"""Batch-02/glasses ski (accessories), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dc9fedbc-8058-5e3a-8a22-47f1828e3da5'
SOURCE_PATH = 'icons-json/accessories/batch-02/glasses ski_dc9fedbc-8058-5e3a-8a22-47f1828e3da5.json'
AUTHOR = 'json_to_solo'

class Batch02GlassesSki(Solo48):
    icon_id = 'batch-02-glasses-ski'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'glasses', 'ski', 'accessories')

    def build(self):
        self.add_line('e0', (14, 40), (9, 38))
        self.add_line('e1', (5, 29), (4, 18))
        self.add_line('e2', (17, 8), (26, 8))
        self.add_line('e3', (44, 19), (43, 30))
        self.add_line('e4', (40, 38), (34, 40))
        self.add_bezier('e5', (9, 38), ((6.309, 37.216), (5.327, 32.984), (5, 29)))
        self.add_bezier('e6', (4, 18), ((4, 17.312), (4.018, 16.224), (4.018, 15.536)), ((4.018, 13.28), (5.382, 11.216), (6.518, 10.688)), ((8.755, 9.632), (11.036, 9.088), (13.327, 8.592)), ((14.364, 8.384), (15.436, 8.016), (16.473, 8.016)), ((16.555, 8.016), (16.918, 8), (17, 8)))
        self.add_bezier('e7', (26, 8), ((26.164, 8), (26.145, 8.016), (26.3, 8.016)), ((30.864, 8.016), (35.564, 9.056), (39.973, 11.088)), ((41.427, 11.76), (42.773, 12.288), (43.609, 14.72)), ((43.791, 15.216), (44, 15.904), (44, 16.512)), ((44, 16.768), (44, 17.024), (43.991, 17.28)), ((43.991, 17.536), (43.991, 17.792), (43.991, 18.048)), ((43.991, 18.176), (44, 18.304), (44, 18.432)), ((44, 18.688), (44, 18.744), (44, 19)))
        self.add_bezier('e8', (43, 30), ((42.755, 33.072), (42.218, 37.44), (40, 38)))
        self.add_bezier('e9', (34, 40), ((33.127, 40), (32.264, 40), (31.391, 40)), ((27.327, 40), (29.018, 26.192), (24.127, 26.064)), ((18.9, 25.936), (20.555, 39.984), (15.6, 39.984)), ((15.509, 39.984), (15.427, 40), (15.345, 40)), ((14.9, 40), (14.445, 40), (14, 40)))
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e6', 'e2', 'e7', 'e3', 'e8', 'e4', 'e9', closed=True)
