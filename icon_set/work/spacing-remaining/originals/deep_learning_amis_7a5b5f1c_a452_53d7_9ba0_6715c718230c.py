"""Deep learning amis (programing), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7a5b5f1c-a452-53d7-9ba0-6715c718230c'
SOURCE_PATH = 'icons-json/programing/deep learning amis_7a5b5f1c-a452-53d7-9ba0-6715c718230c.json'
AUTHOR = 'json_to_solo'

class DeepLearningAmis(Solo48):
    icon_id = 'deep-learning-amis'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('deep', 'learning', 'amis', 'programing')

    def build(self):
        self.add_arc('sym-e0', (20, 36), (24, 32), radius_x=4)
        self.add_arc('sym-e1', (24, 32), (28, 36), radius_x=4)
        self.add_arc('sym-e2', (28, 36), (20, 36), radius_x=4)
        self.add_arc('sym-e3', (20, 25), (24, 21), radius_x=4)
        self.add_arc('sym-e4', (24, 21), (28, 25), radius_x=4)
        self.add_arc('sym-e5', (28, 25), (24, 29), radius_x=4)
        self.add_arc('sym-e6', (24, 29), (20, 25), radius_x=4)
        self.add_arc('sym-e7', (20, 13), (28, 13), radius_x=4)
        self.add_arc('sym-e8', (28, 13), (24, 17), radius_x=4)
        self.add_arc('sym-e9', (24, 17), (20, 13), radius_x=4)
        self.add_arc('sym-e10', (24, 17), (24, 18), radius_x=18, sweep=False)
        self.add_line('sym-e11', (24, 18), (24, 21))
        self.add_arc('sym-e12', (24, 29), (24, 30), radius_x=30, sweep=False)
        self.add_line('sym-e13', (24, 30), (24, 32))
        self.add_line('sym-e14', (24, 42), (10, 42))
        self.add_arc('sym-e16', (10, 42), (6, 38), radius_x=4)
        self.add_line('sym-e18', (6, 38), (6, 37))
        self.add_line('sym-e19', (6, 37), (6, 10))
        self.add_line('sym-e21-1', (6, 10), (7, 7))
        self.add_line('sym-e21-2', (7, 7), (11, 6))
        self.add_line('sym-e23', (11, 6), (12, 6))
        self.add_line('sym-e24', (12, 6), (24, 6))
        self.add_line('sym-e25', (24, 6), (36, 6))
        self.add_line('sym-e26', (36, 6), (37, 6))
        self.add_line('sym-e28-1', (37, 6), (41, 7))
        self.add_line('sym-e28-2', (41, 7), (42, 10))
        self.add_line('sym-e30', (42, 10), (42, 37))
        self.add_arc('sym-e31', (42, 37), (42, 38), radius_x=38, sweep=False)
        self.add_arc('sym-e33', (42, 38), (38, 42), radius_x=4)
        self.add_line('sym-e35', (38, 42), (24, 42))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', closed=True)
        self.add_contour('sym-c1', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', closed=True)
        self.add_contour('sym-c2', 'sym-e7', 'sym-e8', 'sym-e9', closed=True)
        self.add_contour('sym-c3', 'sym-e10', 'sym-e11')
        self.add_contour('sym-c4', 'sym-e12', 'sym-e13')
        self.add_contour('sym-c5', 'sym-e14', 'sym-e16', 'sym-e18', 'sym-e19', 'sym-e21-1', 'sym-e21-2', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e28-1', 'sym-e28-2', 'sym-e30', 'sym-e31', 'sym-e33', 'sym-e35', closed=True)
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c4')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c4')
        self.relate('connect', 'sym-c1', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c4')
