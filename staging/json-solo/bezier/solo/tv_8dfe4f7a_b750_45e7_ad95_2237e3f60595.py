"""Tv (tv), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8dfe4f7a-b750-45e7-ad95-2237e3f60595'
SOURCE_PATH = 'icons-json/tv/tv_8dfe4f7a-b750-45e7-ad95-2237e3f60595.json'
AUTHOR = 'json_to_solo'

class Tv8dfe4f7a(Solo48):
    icon_id = 'tv-8dfe4f7a'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'tv'
    aliases = ()
    keywords = ('tv',)

    def build(self):
        self.add_line('e0', (16, 4), (23, 12))
        self.add_line('e1', (14, 44), (17, 38))
        self.add_line('e2', (34, 44), (31, 38))
        self.add_line('e3', (32, 4), (25, 12))
        self.add_line('e4', (25, 12), (33, 12))
        self.add_line('e5', (16, 12), (23, 12))
        self.add_bezier('e6', (25, 12), ((24.436, 11.991), (23.556, 12), (23, 12)))
        self.add_bezier('e7', (33, 12), ((34.541, 12), (36.876, 12.473), (38.046, 13.655)), ((40, 15.627), (39.992, 20.636), (39.992, 23.418)), ((39.992, 23.651), (40, 23.875), (40, 24.107)), ((40, 24.111), (40, 24.114), (40, 24.118)), ((40, 24.727), (39.992, 25.345), (39.992, 25.955)), ((39.992, 29), (40, 34.145), (37.684, 36.109)), ((36.042, 37.427), (32.987, 37.836), (31, 38)))
        self.add_bezier('e8', (31, 38), ((26.503, 38.282), (21.488, 38.282), (17, 38)))
        self.add_bezier('e9', (17, 38), ((15.004, 37.818), (11.891, 37.445), (10.265, 36.091)), ((8.017, 34.209), (8.017, 29.355), (8.017, 26.482)), ((8.017, 25.936), (8, 25.399), (8, 24.853)), ((8, 24.845), (8, 24.836), (8, 24.827)), ((8, 24.3), (8.017, 23.773), (8.017, 23.245)), ((8.017, 20.345), (8, 14.882), (10.568, 13.282)), ((11.966, 12.418), (14.408, 12), (16, 12)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e6')
        self.add_contour('c4', 'e4', 'e7')
        self.add_contour('c5', 'e8')
        self.add_contour('c6', 'e9', 'e5')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c6')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c1', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c4', 'c5')
