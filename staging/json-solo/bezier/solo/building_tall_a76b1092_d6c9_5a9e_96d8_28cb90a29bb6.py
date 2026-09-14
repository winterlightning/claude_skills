"""Building tall (office), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a76b1092-d6c9-5a9e-96d8-28cb90a29bb6'
SOURCE_PATH = 'icons-json/office/building tall_a76b1092-d6c9-5a9e-96d8-28cb90a29bb6.json'
AUTHOR = 'json_to_solo'

class BuildingTallOffice(Solo48):
    icon_id = 'building-tall-office'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('building', 'tall', 'office')

    def build(self):
        self.add_line('sym-e0', (42, 42), (38, 42))
        self.add_line('sym-e1', (38, 42), (28, 42))
        self.add_line('sym-e2', (28, 42), (20, 42))
        self.add_line('sym-e3', (20, 42), (10, 42))
        self.add_line('sym-e4', (10, 42), (6, 42))
        self.add_bezier('sym-e5', (24, 32), ((21.918, 32), (20, 32.51), (20, 35)))
        self.add_line('sym-e6', (20, 35), (20, 42))
        self.add_line('sym-e7', (24, 6), (12, 6))
        self.add_bezier('sym-e8', (12, 6), ((11.656, 6.115), (11.344, 6), (11, 6)))
        self.add_bezier('sym-e9', (11, 6), ((10.869, 6.065), (10, 7.804), (10, 8)))
        self.add_line('sym-e10', (10, 8), (10, 42))
        self.add_line('sym-e11', (20, 13), (20, 16))
        self.add_line('sym-e12', (20, 22), (20, 26))
        self.add_bezier('sym-e13', (24, 32), ((26.082, 32), (28, 32.51), (28, 35)))
        self.add_line('sym-e14', (28, 35), (28, 42))
        self.add_line('sym-e15', (24, 6), (36, 6))
        self.add_bezier('sym-e16', (36, 6), ((36.344, 6.115), (36.656, 6), (37, 6)))
        self.add_bezier('sym-e17', (37, 6), ((37.131, 6.065), (38, 7.804), (38, 8)))
        self.add_line('sym-e18', (38, 8), (38, 42))
        self.add_line('sym-e19', (28, 13), (28, 16))
        self.add_line('sym-e20', (28, 22), (28, 26))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4')
        self.add_contour('sym-c1', 'sym-e5', 'sym-e6')
        self.add_contour('sym-c2', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10')
        self.add_contour('sym-c3', 'sym-e11')
        self.add_contour('sym-c4', 'sym-e12')
        self.add_contour('sym-c5', 'sym-e13', 'sym-e14')
        self.add_contour('sym-c6', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18')
        self.add_contour('sym-c7', 'sym-e19')
        self.add_contour('sym-c8', 'sym-e20')
        self.relate('connect', 'sym-c0', 'sym-c6')
        self.relate('connect', 'sym-c0', 'sym-c5')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c5')
        self.relate('connect', 'sym-c2', 'sym-c6')
        self.relate('connect', 'sym-c0', 'sym-c5')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c5')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c6')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c6')
        self.relate('connect', 'sym-c0', 'sym-c2')
