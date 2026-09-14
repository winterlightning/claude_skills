"""Plurk logo (logos), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '84175448-d777-471c-9cf7-aab8a04d553d'
SOURCE_PATH = 'icons-json/logos/plurk logo_84175448-d777-471c-9cf7-aab8a04d553d.json'
AUTHOR = 'json_to_solo'

class PlurkLogo(Solo48):
    icon_id = 'plurk-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('plurk', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (25, 24), (17, 24))
        self.add_line('e1', (17, 24), (17, 32))
        self.add_line('e2', (17, 32), (17, 40))
        self.add_line('e3', (8, 40), (8, 18))
        self.add_line('e4', (26, 32), (17, 32))
        self.add_bezier('e5', (17, 24), ((17, 22.109), (16.74, 19.873), (17.12, 17.927)), ((17.38, 16.609), (18.04, 15.318), (19.02, 14.327)), ((19.84, 13.482), (20.85, 12.891), (22, 12.5)), ((25.84, 11.182), (30.4, 13.427), (30.81, 17.236)), ((31.1, 19.909), (29.09, 22.636), (26.4, 23.636)), ((26, 23.791), (25.44, 24), (25, 24)))
        self.add_bezier('e6', (17, 40), ((17, 41.718), (14.59, 43.991), (12.77, 43.991)), ((12.681, 43.991), (12.603, 44), (12.524, 44)), ((12.523, 44), (12.521, 44), (12.52, 44)), ((12.44, 44), (12.36, 43.991), (12.28, 43.991)), ((10.58, 43.991), (8.01, 42.145), (8.01, 40.491)), ((8, 40.445), (8, 40.045), (8, 40)))
        self.add_bezier('e7', (8, 18), ((8, 16.964), (8.47, 15.373), (8.84, 14.4)), ((11.01, 8.682), (17.03, 4.009), (23.9, 4.009)), ((24.008, 4.009), (24.117, 4), (24.225, 4)), ((24.227, 4), (24.228, 4), (24.23, 4)), ((24.5, 4), (24.77, 4.009), (25.04, 4.009)), ((32.82, 4.009), (39.99, 10.018), (39.99, 17.209)), ((39.99, 17.352), (40, 17.495), (40, 17.639)), ((40, 17.641), (40, 17.643), (40, 17.645)), ((40, 17.9), (39.99, 18.145), (39.99, 18.4)), ((39.99, 24.036), (35.44, 29.445), (29.71, 31.382)), ((28.57, 31.773), (27.23, 32), (26, 32)))
        self.add_contour('c0', 'e5', 'e0', closed=True)
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e6', 'e3', 'e7', 'e4', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c1', 'c2')
