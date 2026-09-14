"""Instagram logo 1 (logos), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5f62be60-64f8-4b4b-b867-a302f8b567b1'
SOURCE_PATH = 'icons-json/logos/instagram logo 1_5f62be60-64f8-4b4b-b867-a302f8b567b1.json'
AUTHOR = 'json_to_solo'

class InstagramLogo1Logos(Solo48):
    icon_id = 'instagram-logo-1-logos'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('instagram', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (35, 42), (13, 42))
        self.add_line('e1', (6, 35), (6, 13))
        self.add_line('e2', (14, 6), (35, 6))
        self.add_line('e3', (42, 13), (42, 35))
        self.add_arc('e4-top', (16, 24), (32, 24), radius_x=8)
        self.add_arc('e4-bottom', (32, 24), (16, 24), radius_x=8)
        self.add_bezier('e5', (13, 42), ((12.967, 41.992), (13.29, 41.992), (13.257, 41.984)), ((9.976, 41.984), (6, 38.256), (6, 35)))
        self.add_bezier('e6', (6, 13), ((6.008, 12.967), (6.008, 13.298), (6.016, 13.265)), ((6.016, 10.205), (9.96, 6.016), (13.053, 6.016)), ((13.274, 6.016), (13.486, 6), (13.707, 6)), ((13.863, 6), (13.845, 6), (14, 6)))
        self.add_bezier('e7', (35, 6), ((38.117, 6), (41.992, 10.115), (41.992, 13.257)), ((41.992, 13.29), (42, 12.967), (42, 13)))
        self.add_bezier('e8', (42, 35), ((41.992, 35.041), (41.992, 34.718), (41.984, 34.759)), ((41.984, 37.934), (37.95, 41.984), (34.759, 41.984)), ((34.718, 41.992), (35.041, 41.992), (35, 42)))
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e6', 'e2', 'e7', 'e3', 'e8', closed=True)
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
