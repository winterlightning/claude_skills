"""Eye 1 (container), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8a93bf49-363b-48fa-94da-6dbc6570089f'
SOURCE_PATH = 'pictographic-primitives/container/eye 1_8a93bf49-363b-48fa-94da-6dbc6570089f.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Eye1Container(Solo48):
    icon_id = 'eye-1-container'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    aliases = ()
    keywords = ('eye', 'container')

    def build(self):
        self.add_bezier('e0', (4, 25), ((4.009, 25.01), (4.009, 25.02), (4.018, 25.03)), ((4.018, 25.16), (4.8, 26.21), (4.891, 26.35)), ((5.691, 27.54), (6.509, 28.72), (7.355, 29.87)), ((11.2, 35.05), (17.491, 39.99), (23.836, 39.99)), ((23.988, 39.99), (24.141, 40), (24.293, 40)), ((24.295, 40), (24.298, 40), (24.3, 40)), ((24.527, 40), (24.755, 39.99), (24.982, 39.99)), ((29.173, 39.99), (34.709, 37.02), (37.882, 34.1)), ((39.064, 33.02), (40.1, 31.72), (41.045, 30.38)), ((41.427, 29.84), (43.982, 26.04), (43.982, 25.48)), ((43.991, 25.47), (43.991, 25.46), (44, 25.45)), ((44, 25.45), (44, 25.45), (44, 25.45)), ((44, 25.44), (43.991, 25.43), (43.991, 25.42)), ((43.991, 24.6), (42.291, 20.86), (41.927, 20.05)), ((40.955, 17.93), (39.827, 15.81), (38.327, 14.08)), ((35.227, 10.5), (29.673, 8.01), (25.191, 8.01)), ((24.985, 8.01), (24.77, 8), (24.564, 8)), ((24.561, 8), (24.558, 8), (24.555, 8)), ((24.255, 8), (23.955, 8.02), (23.664, 8.02)), ((15.391, 8.02), (11.891, 11.81), (7.364, 19)), ((6.464, 20.43), (5.609, 21.88), (4.818, 23.38)), ((4.682, 23.64), (4.009, 24.71), (4.009, 24.97)), ((4.009, 24.98), (4, 24.99), (4, 25)))
        self.add_contour('c0', 'e0', closed=True)
