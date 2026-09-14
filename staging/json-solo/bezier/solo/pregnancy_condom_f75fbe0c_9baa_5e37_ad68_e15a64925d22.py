"""Pregnancy condom (health), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f75fbe0c-9baa-5e37-ad68-e15a64925d22'
SOURCE_PATH = 'icons-json/health/pregnancy condom_f75fbe0c-9baa-5e37-ad68-e15a64925d22.json'
AUTHOR = 'json_to_solo'

class PregnancyCondomHealth(Solo48):
    icon_id = 'pregnancy-condom-health'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('pregnancy', 'condom', 'health')

    def build(self):
        self.add_line('e0', (17, 40), (8, 31))
        self.add_line('e1', (8, 31), (26, 13))
        self.add_line('e2', (37, 20), (17, 40))
        self.add_line('e3', (17, 40), (19, 42))
        self.add_line('e4', (6, 29), (8, 31))
        self.add_bezier('e5', (26, 13), ((28.07, 11.02), (30.21, 8.373), (33.303, 8.111)), ((33.916, 8.062), (34.538, 8.103), (35.144, 8.225)), ((35.405, 8.275), (35.741, 8.455), (35.995, 8.455)), ((36.821, 8.455), (38.727, 6.008), (40.004, 6.008)), ((40.068, 6), (40.125, 6), (40.181, 6)), ((40.182, 6), (40.183, 6), (40.184, 6)), ((40.249, 6), (40.306, 6.008), (40.364, 6.008)), ((41.157, 6.008), (42, 6.867), (42, 7.685)), ((42, 7.686), (42, 7.687), (42, 7.688)), ((42, 7.736), (41.992, 7.784), (41.992, 7.833)), ((41.992, 9.183), (40.159, 10.156), (39.725, 11.384)), ((39.406, 12.3), (39.922, 13.405), (39.922, 14.354)), ((39.922, 16.62), (38.489, 18.445), (37, 20)))
        self.add_contour('c0', 'e0', 'e1', 'e5', 'e2', 'e3')
        self.add_contour('c1', 'e4')
