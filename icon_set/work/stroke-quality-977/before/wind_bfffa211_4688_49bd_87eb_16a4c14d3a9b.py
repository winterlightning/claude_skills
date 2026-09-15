"""Wind (state), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bfffa211-4688-49bd-87eb-16a4c14d3a9b'
SOURCE_PATH = 'pictographic-primitives/state/wind_bfffa211-4688-49bd-87eb-16a4c14d3a9b.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Wind(Solo48):
    icon_id = 'wind-state'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('wind', 'state')

    def build(self):
        self.add_bezier('e0', (4, 23), ((4.009, 23), (4.009, 22.99), (4.018, 22.99)), ((4.018, 22.96), (4.236, 22.85), (4.255, 22.84)), ((4.982, 22.41), (5.755, 22.07), (6.518, 21.75)), ((9.327, 20.57), (12.327, 19.89), (15.345, 20.16)), ((17.264, 20.33), (19.164, 20.83), (20.936, 21.66)), ((22.8, 22.52), (24.364, 23.94), (26.191, 24.86)), ((30.473, 27), (40.255, 27.9), (43.327, 22.95)), ((43.709, 22.32), (43.827, 21.71), (44, 21)))
        self.add_bezier('e1', (7, 36), ((11.473, 33.58), (16.982, 33.38), (21.609, 35.39)), ((23.109, 36.05), (24.373, 37.07), (25.773, 37.93)), ((27.927, 39.25), (30.573, 39.99), (33.045, 39.99)), ((33.26, 39.99), (33.475, 40), (33.69, 40)), ((33.693, 40), (33.697, 40), (33.7, 40)), ((33.991, 40), (34.282, 39.98), (34.573, 39.98)), ((37.1, 39.98), (41.009, 39.14), (42.527, 36.65)), ((42.845, 36.12), (42.845, 35.59), (43, 35)))
        self.add_bezier('e2', (8, 10), ((10.355, 8.73), (12.636, 8.02), (15.273, 8.02)), ((15.595, 8.02), (15.917, 8), (16.239, 8)), ((16.244, 8), (16.249, 8), (16.255, 8)), ((16.591, 8), (16.927, 8.02), (17.264, 8.02)), ((19.064, 8.02), (20.909, 8.45), (22.582, 9.14)), ((24.391, 9.88), (25.864, 11.18), (27.573, 12.11)), ((31.364, 14.16), (40.555, 15.19), (43.373, 10.78)), ((43.736, 10.21), (43.836, 9.65), (44, 9)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
