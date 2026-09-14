"""Sagemaker (artificial-intelligence), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ca669b8d-03d5-4a83-b8c3-f45526ed6922'
SOURCE_PATH = 'icons-json/artificial-intelligence/sagemaker_ca669b8d-03d5-4a83-b8c3-f45526ed6922.json'
AUTHOR = 'json_to_solo'

class SagemakerArtificialIntelligence(Solo48):
    icon_id = 'sagemaker-artificial-intelligence'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'artificial-intelligence'
    aliases = ()
    keywords = ('sagemaker', 'artificial-intelligence')

    def build(self):
        self.add_line('e0', (28, 42), (37, 37))
        self.add_line('e1', (37, 37), (37, 31))
        self.add_line('e2', (37, 31), (41, 28))
        self.add_line('e3', (42, 27), (42, 20))
        self.add_line('e4', (42, 20), (37, 17))
        self.add_line('e5', (37, 17), (37, 11))
        self.add_line('e6', (37, 11), (28, 6))
        self.add_line('e7', (28, 6), (24, 8))
        self.add_line('e8', (25, 39), (25, 27))
        self.add_line('e9', (25, 27), (20, 23))
        self.add_line('e10', (20, 23), (20, 22))
        self.add_line('e11', (21, 21), (24, 18))
        self.add_line('e12', (24, 17), (24, 8))
        self.add_line('e13', (25, 39), (20, 42))
        self.add_line('e14', (20, 42), (11, 36))
        self.add_line('e15', (11, 36), (11, 31))
        self.add_line('e16', (11, 31), (6, 27))
        self.add_line('e17', (6, 27), (6, 20))
        self.add_line('e18', (6, 20), (11, 17))
        self.add_line('e19', (11, 17), (11, 12))
        self.add_line('e20', (12, 11), (20, 6))
        self.add_line('e21', (20, 6), (24, 8))
        self.add_bezier('e22', (25, 39), ((26.031, 40.129), (26.781, 41.067), (28, 42)))
        self.add_bezier('e23', (41, 28), ((41.27, 27.877), (41.73, 27.837), (42, 27.715)), ((42, 27.567), (42, 27.147), (42, 27)))
        self.add_bezier('e24', (20, 22), ((20.27, 21.73), (20.73, 21.27), (21, 21)))
        self.add_bezier('e25', (24, 18), ((24, 17.73), (24, 17.27), (24, 17)))
        self.add_bezier('e26', (11, 12), ((11.27, 11.73), (11.73, 11.27), (12, 11)))
        self.add_bezier('e27', (31, 15), ((31, 14.73), (31, 14.27), (31, 14)))
        self.add_bezier('e28', (35, 24), ((35, 23.73), (35, 23.27), (35, 23)))
        self.add_bezier('e29', (31, 35), ((31, 34.73), (31, 34.27), (31, 34)))
        self.add_contour('c0', 'e22', 'e0', 'e1', 'e2', 'e23', 'e3', 'e4', 'e5', 'e6', 'e7')
        self.add_contour('c1', 'e8', 'e9', 'e10', 'e24', 'e11', 'e25', 'e12')
        self.add_contour('c2', 'e13', 'e14', 'e15', 'e16', 'e17', 'e18', 'e19', 'e26', 'e20', 'e21')
        self.add_contour('c3', 'e27')
        self.add_contour('c4', 'e28')
        self.add_contour('c5', 'e29')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
