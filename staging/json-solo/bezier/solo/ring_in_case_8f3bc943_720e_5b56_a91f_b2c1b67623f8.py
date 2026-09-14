"""Batch-03/ring in case (accessories), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8f3bc943-720e-5b56-a91f-b2c1b67623f8'
SOURCE_PATH = 'icons-json/accessories/batch-03/ring in case_8f3bc943-720e-5b56-a91f-b2c1b67623f8.json'
AUTHOR = 'json_to_solo'

class Batch03RingInCase(Solo48):
    icon_id = 'batch-03-ring-in-case'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'ring', 'in', 'case', 'accessories')

    def build(self):
        self.add_line('e0', (23, 24), (17, 17))
        self.add_line('e1', (17, 17), (20, 13))
        self.add_line('e2', (20, 13), (27, 13))
        self.add_line('e3', (31, 17), (25, 24))
        self.add_line('e4', (40, 33), (40, 10))
        self.add_line('e5', (36, 6), (13, 6))
        self.add_line('e6', (8, 11), (8, 33))
        self.add_line('e7', (6, 33), (42, 33))
        self.add_line('e8', (42, 33), (42, 37))
        self.add_line('e9', (36, 42), (11, 42))
        self.add_bezier('e10', (31, 33), ((30.812, 29.735), (30.685, 26.855), (27.674, 24.982)), ((26.97, 24.54), (25.653, 24.008), (24.818, 24)), ((24.27, 24), (23.548, 24), (23, 24)))
        self.add_bezier('e11', (23, 24), ((22.018, 24.352), (21.079, 24.638), (20.195, 25.211)), ((18.379, 26.389), (17.054, 28.312), (16.685, 30.447)), ((16.538, 31.265), (16.992, 32.174), (17, 33)))
        self.add_bezier('e12', (27, 13), ((27.205, 13.123), (27.706, 13.527), (27.911, 13.683)), ((28.394, 14.051), (28.745, 14.836), (29.065, 15.335)), ((29.531, 16.064), (30.476, 16.313), (31, 17)))
        self.add_bezier('e13', (40, 10), ((40, 8.265), (38.695, 7.047), (37.156, 6.278)), ((36.878, 6.139), (36.319, 6), (36, 6)))
        self.add_bezier('e14', (13, 6), ((12.836, 6), (12.21, 6.016), (12.046, 6.016)), ((10.345, 6.016), (8.905, 7.366), (8.545, 8.97)), ((8.405, 9.575), (8, 10.386), (8, 11)))
        self.add_bezier('e15', (11, 42), ((11.139, 42), (10.631, 41.984), (10.492, 41.984)), ((8.144, 41.984), (6, 39.938), (6, 37.574)), ((6, 36.052), (6, 34.522), (6, 33)))
        self.add_bezier('e16', (42, 37), ((42, 37.131), (41.992, 37.345), (41.992, 37.475)), ((41.992, 39.439), (39.685, 41.984), (37.664, 41.984)), ((37.598, 41.992), (37.533, 41.992), (37.467, 42)), ((37.066, 42), (36.401, 42), (36, 42)))
        self.add_contour('c0', 'e10')
        self.add_contour('c1', 'e11')
        self.add_contour('c2', 'e0', 'e1', 'e2', 'e12', 'e3')
        self.add_contour('c3', 'e4', 'e13', 'e5', 'e14', 'e6')
        self.add_contour('c4', 'e15', 'e7', 'e8', 'e16', 'e9', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c0')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c4')
