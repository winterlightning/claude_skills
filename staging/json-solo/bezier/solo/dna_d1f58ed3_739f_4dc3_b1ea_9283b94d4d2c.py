"""Dna (artificial-intelligence), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd1f58ed3-739f-4dc3-b1ea-9283b94d4d2c'
SOURCE_PATH = 'icons-json/artificial-intelligence/dna_d1f58ed3-739f-4dc3-b1ea-9283b94d4d2c.json'
AUTHOR = 'json_to_solo'

class Dna(Solo48):
    icon_id = 'dna'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'artificial-intelligence'
    aliases = ()
    keywords = ('dna', 'artificial-intelligence')

    def build(self):
        self.add_line('e0', (29, 16), (30, 17))
        self.add_line('e1', (30, 17), (26, 17))
        self.add_line('e2', (17, 25), (18, 34))
        self.add_line('e3', (35, 18), (30, 18))
        self.add_bezier('e4', (31, 6), ((30.386, 6.843), (30.725, 6.687), (30.349, 7.244)), ((28.426, 10.14), (28.517, 12.695), (29, 16)))
        self.add_bezier('e5', (26, 17), ((22.261, 17), (18.224, 18.412), (17.005, 22.437)), ((16.784, 23.149), (16.869, 24.264), (17, 25)))
        self.add_bezier('e6', (18, 34), ((18.556, 37.035), (17.872, 39.161), (16.211, 41.665)), ((16.105, 41.82), (16.115, 41.861), (16, 42)))
        self.add_bezier('e7', (42, 15), ((41.869, 15.139), (41.853, 15.319), (41.705, 15.45)), ((40.004, 16.931), (37.348, 18), (35, 18)))
        self.add_bezier('e8', (30, 18), ((30.262, 19.759), (30.382, 21.905), (30.292, 23.697)), ((30.087, 27.968), (27.125, 30.709), (22.879, 30.742)), ((19.942, 30.766), (16.988, 30.055), (14.075, 29.801)), ((12.701, 29.678), (11.294, 29.564), (9.935, 29.891)), ((8.594, 30.21), (7.375, 30.922), (6.303, 31.773)), ((6.155, 31.887), (6.131, 31.877), (6, 32)))
        self.add_contour('c0', 'e4', 'e0', 'e1', 'e5', 'e2', 'e6')
        self.add_contour('c1', 'e7', 'e3', 'e8')
