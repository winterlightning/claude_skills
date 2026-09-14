"""Spoilt (smileys), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3386f387-266e-5903-a940-474434b6b765'
SOURCE_PATH = 'icons-json/smileys/spoilt_3386f387-266e-5903-a940-474434b6b765.json'
AUTHOR = 'json_to_solo'

class SpoiltSmileys(Solo48):
    icon_id = 'spoilt-smileys'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('spoilt', 'smileys')

    def build(self):
        self.add_line('e0', (5, 29), (4, 24))
        self.add_bezier('e1', (8, 12), ((8.594, 11.397), (9.001, 11.098), (9.595, 10.495)), ((10.288, 9.793), (10.972, 9.055), (11.738, 8.424)), ((14.988, 6.145), (19.354, 4.547), (23.316, 4.211)), ((23.532, 4.211), (23.739, 4.193), (23.955, 4.193)), ((24.234, 4.193), (24.513, 4.211), (24.792, 4.211)), ((33.41, 6.352), (41.594, 14.49), (43.789, 23.091)), ((43.789, 23.298), (43.807, 23.505), (43.807, 23.712)), ((43.807, 23.991), (43.789, 24.261), (43.789, 24.54)), ((41.685, 33.341), (33.605, 41.543), (24.828, 43.798)), ((24.621, 43.798), (24.414, 43.807), (24.207, 43.807)), ((23.865, 43.807), (23.523, 43.789), (23.181, 43.789)), ((16.371, 42.488), (9.359, 37.625), (5.876, 31.662)), ((5.606, 30.951), (5.126, 29.756), (5, 29)))
        self.add_bezier('e2', (4, 24), ((4.003, 23.631), (4.202, 23.262), (4.202, 22.893)), ((4.488, 19.608), (6.085, 15.109), (7.794, 12.296)), ((8.298, 11.63), (9.397, 10.585), (10, 10)))
        self.add_bezier('e3', (29, 19), ((30.828, 21.053), (33.263, 21.045), (36, 21)))
        self.add_bezier('e4', (12, 21), ((14.719, 21.045), (17.154, 20.99), (19, 19)))
        self.add_bezier('e5', (17, 25), ((17, 25.297), (17, 25.703), (17, 26)))
        self.add_bezier('e6', (30, 25), ((30.036, 25), (30.365, 24.9), (30.401, 24.9)), ((30.365, 25.197), (30.036, 25.703), (30, 26)))
        self.add_bezier('e7', (18, 35), ((21.736, 31.093), (26.3, 30.985), (30, 35)))
        self.add_contour('c0', 'e1', 'e0', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e5')
        self.add_contour('c4', 'e6')
        self.add_contour('c5', 'e7')
