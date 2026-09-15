"""Eggplant (food), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '37dde66a-a1c3-4b6d-bf1d-a49fc7e5c370'
SOURCE_PATH = 'pictographic-primitives/food/eggplant_37dde66a-a1c3-4b6d-bf1d-a49fc7e5c370.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Eggplant(Solo48):
    icon_id = 'eggplant'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('eggplant', 'food')

    def build(self):
        self.add_line('e0', (44, 8), (41, 11))
        self.add_line('e1', (34, 31), (39, 25))
        self.add_line('e2', (39, 25), (40, 26))
        self.add_bezier('e3', (27, 14), ((28.655, 15.036), (29.945, 15.865), (32, 15.941)), ((32.536, 15.958), (33.073, 15.907), (33.6, 15.815)), ((34.1, 15.722), (34.6, 15.638), (35.091, 15.545)), ((35.055, 15.891), (35.018, 16.244), (34.973, 16.598)), ((34.873, 17.423), (34.855, 18.274), (34.964, 19.107)), ((35.318, 21.785), (36.982, 23.173), (39, 25)))
        self.add_bezier('e4', (27, 14), ((24.845, 16.989), (22.1, 19.663), (18.318, 20.926)), ((15.882, 21.735), (14.382, 21.541), (12.009, 21.853)), ((8.6, 22.307), (5.791, 24), (4.582, 27.082)), ((4.255, 27.924), (4.009, 28.876), (4.009, 29.777)), ((4.009, 29.835), (4, 29.901), (4, 29.959)), ((4, 29.96), (4, 29.961), (4, 29.962)), ((4, 30.189), (4.009, 30.408), (4.009, 30.636)), ((4.009, 35.84), (9.155, 39.992), (14.627, 39.992)), ((14.726, 39.992), (14.824, 40), (14.923, 40)), ((14.924, 40), (14.926, 40), (14.927, 40)), ((15.255, 40), (15.591, 39.992), (15.918, 39.992)), ((20.682, 39.992), (26.427, 36.792), (30.055, 34.122)), ((31.427, 33.112), (32.964, 32.339), (34, 31)))
        self.add_bezier('e5', (27, 14), ((26.727, 13.579), (25.709, 12.64), (26.036, 12.034)), ((26.627, 10.947), (28.827, 10.114), (30.009, 9.718)), ((32.745, 8.783), (36.091, 8.766), (38.764, 9.903)), ((39.682, 10.299), (40.191, 10.461), (41, 11)))
        self.add_bezier('e6', (40, 26), ((42.645, 23.137), (44, 18.274), (43.355, 14.535)), ((42.909, 13.314), (41.845, 12.002), (41, 11)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4', 'e1')
        self.add_contour('c3', 'e5')
        self.add_contour('c4', 'e2', 'e6')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c4')
