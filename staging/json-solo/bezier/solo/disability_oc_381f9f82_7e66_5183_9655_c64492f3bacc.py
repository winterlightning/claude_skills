"""Disability oc (wayfinding), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '381f9f82-7e66-5183-9655-c64492f3bacc'
SOURCE_PATH = 'icons-json/wayfinding/disability oc_381f9f82-7e66-5183-9655-c64492f3bacc.json'
AUTHOR = 'json_to_solo'

class DisabilityOcWayfinding(Solo48):
    icon_id = 'disability-oc-wayfinding'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    aliases = ()
    keywords = ('disability', 'oc', 'wayfinding')

    def build(self):
        self.add_line('e0', (30, 16), (30, 33))
        self.add_line('e1', (19, 31), (19, 16))
        self.add_line('e2', (4, 17), (4, 31))
        self.add_bezier('e3', (44, 13), ((43.909, 12.78), (43.918, 12.55), (43.8, 12.34)), ((42.6, 10.04), (40.509, 8.01), (37.955, 8.01)), ((37.811, 8.01), (37.668, 8), (37.525, 8)), ((37.523, 8), (37.52, 8), (37.518, 8)), ((37.373, 8.01), (37.227, 8.01), (37.082, 8.02)), ((33.391, 8.02), (30, 12.14), (30, 16)))
        self.add_bezier('e4', (30, 33), ((30, 33.34), (30.509, 33.79), (30.582, 34.12)), ((31.218, 37.25), (33.836, 39.98), (36.836, 39.98)), ((37.055, 39.98), (37.264, 40), (37.482, 40)), ((37.484, 40), (37.486, 40), (37.489, 40)), ((37.632, 40), (37.766, 39.99), (37.909, 39.99)), ((40.518, 39.99), (42.518, 38), (43.791, 35.68)), ((43.909, 35.46), (43.9, 35.22), (44, 35)))
        self.add_bezier('e5', (4, 31), ((4, 31), (4, 31), (4, 31)), ((4, 35.28), (7.264, 39.99), (11.373, 39.99)), ((11.509, 39.99), (11.655, 40), (11.791, 40)), ((11.936, 39.99), (12.082, 39.99), (12.218, 39.98)), ((16.255, 39.98), (19, 35.13), (19, 31)))
        self.add_bezier('e6', (19, 16), ((19, 15.37), (19.182, 14.56), (18.991, 13.97)), ((17.945, 10.87), (15.309, 8.01), (12.118, 8.01)), ((11.973, 8.01), (11.827, 8), (11.682, 8)), ((11.536, 8.01), (11.391, 8.01), (11.245, 8.02)), ((7.336, 8.02), (4.009, 12.39), (4.009, 16.53)), ((4, 16.61), (4, 16.69), (4, 16.76)), ((4, 16.84), (4, 16.92), (4, 17)))
        self.add_contour('c0', 'e3', 'e0', 'e4')
        self.add_contour('c1', 'e5', 'e1', 'e6', 'e2', closed=True)
