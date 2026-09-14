"""Lead nuturing plant (nature), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4f10974a-d5b4-43a2-b15c-1c1fd7f01497'
SOURCE_PATH = 'icons-json/nature/lead nuturing plant_4f10974a-d5b4-43a2-b15c-1c1fd7f01497.json'
AUTHOR = 'json_to_solo'

class LeadNuturingPlant(Solo48):
    icon_id = 'lead-nuturing-plant'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature'
    aliases = ()
    keywords = ('lead', 'nuturing', 'plant', 'nature')

    def build(self):
        self.add_line('e0', (23, 37), (25, 37))
        self.add_bezier('e1', (36, 21), ((33.273, 23.44), (31.136, 25.91), (29, 29)))
        self.add_bezier('e2', (11, 18), ((14.391, 20.75), (16.764, 24.1), (19, 28)))
        self.add_bezier('e3', (9, 40), ((13.345, 38.08), (18.327, 37.16), (23, 37)))
        self.add_bezier('e4', (39, 40), ((34.318, 38.04), (30.018, 37.01), (25, 37)))
        self.add_bezier('e5', (23, 37), ((22.136, 33.77), (20.464, 30.94), (19, 28)))
        self.add_bezier('e6', (25, 37), ((26.073, 34.24), (27.582, 31.57), (29, 29)))
        self.add_bezier('e7', (29, 29), ((28.318, 27.59), (27.2, 26.26), (26.982, 24.67)), ((26.064, 17.75), (32.073, 13.81), (37.027, 11.51)), ((38.555, 10.8), (40.145, 10.22), (41.736, 9.7)), ((42.036, 9.6), (43.218, 9.14), (43.327, 9.2)), ((43.391, 9.24), (43.518, 10.37), (43.564, 10.65)), ((43.782, 12.13), (43.991, 13.65), (43.991, 15.16)), ((43.991, 15.278), (44, 15.406), (44, 15.524)), ((44, 15.526), (44, 15.528), (44, 15.53)), ((44, 15.97), (43.991, 16.42), (43.991, 16.86)), ((43.991, 23.06), (41.264, 29.39), (35.3, 30.66)), ((34.055, 30.93), (32.673, 30.98), (31.436, 30.64)), ((30.336, 30.33), (29.936, 29.68), (29, 29)))
        self.add_bezier('e8', (19, 29), ((19.664, 27.54), (20.782, 26.19), (21.036, 24.57)), ((22.3, 16.48), (17.082, 12.71), (11.064, 10.11)), ((9.755, 9.54), (6.127, 8), (4.773, 8)), ((4.772, 8), (4.772, 8), (4.771, 8)), ((4.73, 8), (4.545, 9.303), (4.518, 9.5)), ((4.255, 11.16), (4.009, 12.91), (4.009, 14.6)), ((4.009, 14.718), (4, 14.846), (4, 14.964)), ((4, 14.966), (4, 14.968), (4, 14.97)), ((4, 15.46), (4.009, 15.94), (4.009, 16.43)), ((4.009, 19.24), (4.655, 22.27), (6.064, 24.63)), ((8.236, 28.26), (13.018, 30.85), (16.973, 29.53)), ((17.918, 29.21), (18.2, 28.61), (19, 28)))
        self.add_contour('c0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e5')
        self.add_contour('c5', 'e0')
        self.add_contour('c6', 'e6')
        self.add_contour('c7', 'e7', closed=True)
        self.add_contour('c8', 'e8')
        self.relate('connect', 'c0', 'c6')
        self.relate('connect', 'c0', 'c7')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c1', 'c8')
        self.relate('connect', 'c4', 'c8')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c5', 'c6')
