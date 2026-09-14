"""Al (text u) (text), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c2306778-41d5-4836-93a4-7175608aabed'
SOURCE_PATH = 'icons-json/text/al (text u)_c2306778-41d5-4836-93a4-7175608aabed.json'
AUTHOR = 'json_to_solo'

class AlTextUText(Solo48):
    icon_id = 'al-text-u-text'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'text'
    aliases = ()
    keywords = ('al', 'text', 'u')

    def build(self):
        self.add_line('e0', (22, 27), (16, 6))
        self.add_line('e1', (14, 5), (8, 27))
        self.add_line('e2', (11, 19), (20, 19))
        self.add_line('e3', (32, 4), (32, 21))
        self.add_line('e4', (8, 44), (40, 44))
        self.add_bezier('e5', (16, 6), ((15.823, 5.364), (15.975, 4.009), (15.175, 4.009)), ((15.082, 4.009), (14.998, 4), (14.905, 4)), ((14.863, 4), (14.821, 4.009), (14.787, 4.009)), ((14.392, 4.009), (14.101, 4.636), (14, 5)))
        self.add_bezier('e6', (32, 21), ((32, 23.491), (33.036, 26.1), (35.781, 26.164)), ((36.876, 26.191), (37.979, 25.827), (38.981, 25.4)), ((39.411, 25.218), (39.992, 24.918), (39.992, 24.918)), ((39.992, 24.909), (40, 25), (40, 25)))
        self.add_contour('c0', 'e0', 'e5', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3', 'e6')
        self.add_contour('c3', 'e4')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
