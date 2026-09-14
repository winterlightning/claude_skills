"""Sagemaker (artificial-intelligence), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
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
        self.add_arc('e22', (25, 39), (28, 42), radius_x=24, sweep=False)
        self.add_arc('e23-1', (41, 28), (42, 28), radius_x=1)
        self.add_arc('e23-2', (42, 28), (42, 27), radius_x=30)
        self.add_line('e24', (20, 22), (21, 21))
        self.add_arc('e25', (24, 18), (24, 17), radius_x=18)
        self.add_arc('e26', (11, 12), (12, 11), radius_x=8)
        self.add_arc('e27', (31, 15), (31, 14), radius_x=20)
        self.add_arc('e28', (35, 24), (35, 23), radius_x=25)
        self.add_arc('e29', (31, 35), (31, 34), radius_x=34, sweep=False)
        self.add_contour('c0', 'e22', 'e0', 'e1', 'e2', 'e23-1', 'e23-2', 'e3', 'e4', 'e5', 'e6', 'e7')
        self.add_contour('c1', 'e8', 'e9', 'e10', 'e24', 'e11', 'e25', 'e12')
        self.add_contour('c2', 'e13', 'e14', 'e15', 'e16', 'e17', 'e18', 'e19', 'e26', 'e20', 'e21')
        self.add_contour('c3', 'e27')
        self.add_contour('c4', 'e28')
        self.add_contour('c5', 'e29')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
