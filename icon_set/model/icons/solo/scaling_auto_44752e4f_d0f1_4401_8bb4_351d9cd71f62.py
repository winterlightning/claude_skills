"""Scaling auto (programing), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '44752e4f-d0f1-4401-8bb4-351d9cd71f62'
SOURCE_PATH = 'icons-json/programing/scaling auto_44752e4f-d0f1-4401-8bb4-351d9cd71f62.json'
AUTHOR = 'json_to_solo'

class ScalingAuto(Solo48):
    icon_id = 'scaling-auto'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('scaling', 'auto', 'programing')

    def build(self):
        self.add_line('e0', (20, 10), (24, 6))
        self.add_line('e1', (24, 16), (24, 6))
        self.add_line('e2', (28, 10), (24, 6))
        self.add_line('e3', (10, 20), (6, 24))
        self.add_line('e4', (10, 28), (6, 24))
        self.add_line('e5', (15, 24), (6, 24))
        self.add_line('e6', (38, 20), (42, 24))
        self.add_line('e7', (33, 24), (42, 24))
        self.add_line('e8', (38, 28), (42, 24))
        self.add_line('e9', (24, 32), (24, 42))
        self.add_line('e10', (20, 38), (24, 42))
        self.add_line('e11', (28, 39), (24, 42))
        self.add_line('e12', (17, 20), (17, 28))
        self.add_line('e13', (20, 30), (28, 30))
        self.add_line('e14', (31, 28), (31, 20))
        self.add_line('e15', (28, 18), (19, 18))
        self.add_line('e16', (17, 28), (20, 30))
        self.add_line('e17', (28, 30), (31, 28))
        self.add_line('e18', (31, 20), (28, 18))
        self.add_line('e19', (19, 18), (17, 20))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.add_contour('c6', 'e6')
        self.add_contour('c7', 'e7')
        self.add_contour('c8', 'e8')
        self.add_contour('c9', 'e9')
        self.add_contour('c10', 'e10')
        self.add_contour('c11', 'e11')
        self.add_contour('c12', 'e12', 'e16', 'e13', 'e17', 'e14', 'e18', 'e15', 'e19', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c6', 'c8')
        self.relate('connect', 'c7', 'c8')
        self.relate('connect', 'c10', 'c11')
        self.relate('connect', 'c10', 'c9')
        self.relate('connect', 'c11', 'c9')
