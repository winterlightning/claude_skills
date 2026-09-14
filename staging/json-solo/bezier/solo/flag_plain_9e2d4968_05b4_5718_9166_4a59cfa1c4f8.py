"""Flag plain (social), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9e2d4968-05b4-5718-9166-4a59cfa1c4f8'
SOURCE_PATH = 'icons-json/social/flag plain_9e2d4968-05b4-5718-9166-4a59cfa1c4f8.json'
AUTHOR = 'json_to_solo'

class FlagPlain(Solo48):
    icon_id = 'flag-plain'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'social'
    aliases = ()
    keywords = ('flag', 'plain', 'social')

    def build(self):
        self.add_line('e0', (40, 7), (40, 26))
        self.add_line('e1', (8, 29), (14, 27))
        self.add_line('e2', (8, 4), (8, 44))
        self.add_bezier('e3', (8, 9), ((8.11, 8.918), (8.22, 9.3), (8.33, 9.218)), ((8.77, 9.036), (9.26, 8.955), (9.7, 8.782)), ((14.19, 6.964), (18.8, 5.336), (23.81, 5.618)), ((27.57, 5.827), (30.75, 7.664), (34.36, 7.927)), ((36.16, 8.045), (37.99, 7.582), (39.65, 6.991)), ((39.76, 6.9), (39.88, 7.091), (40, 7)))
        self.add_bezier('e4', (14, 27), ((17.6, 25.909), (21.54, 25.009), (25.32, 25.464)), ((27.78, 25.764), (30.02, 26.891), (32.49, 27.173)), ((35.16, 27.473), (37.64, 27.027), (40, 26)))
        self.add_contour('c0', 'e3', 'e0')
        self.add_contour('c1', 'e1', 'e4')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
