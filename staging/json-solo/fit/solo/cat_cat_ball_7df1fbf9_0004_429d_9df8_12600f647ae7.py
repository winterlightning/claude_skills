"""Cat cat ball (pets), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7df1fbf9-0004-429d-9df8-12600f647ae7'
SOURCE_PATH = 'icons-json/pets/cat cat ball_7df1fbf9-0004-429d-9df8-12600f647ae7.json'
AUTHOR = 'json_to_solo'

class CatCatBallPets(Solo48):
    icon_id = 'cat-cat-ball-pets'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'pets'
    aliases = ()
    keywords = ('cat', 'ball', 'pets')

    def build(self):
        self.add_arc('sym-e0', (4, 24), (24, 4), radius_x=20)
        self.add_arc('sym-e1', (24, 4), (44, 24), radius_x=20)
        self.add_arc('sym-e2', (44, 24), (24, 44), radius_x=20)
        self.add_arc('sym-e3', (24, 44), (4, 24), radius_x=20)
        self.add_line('sym-e4', (44, 24), (33, 24))
        self.add_line('sym-e5', (33, 24), (24, 24))
        self.add_line('sym-e6', (24, 24), (15, 24))
        self.add_line('sym-e7', (15, 24), (4, 24))
        self.add_line('sym-e8', (24, 4), (24, 24))
        self.add_line('sym-e9', (24, 24), (24, 44))
        self.add_arc('sym-e10', (33, 24), (38, 10), radius_x=17)
        self.add_arc('sym-e11', (15, 24), (10, 10), radius_x=17, sweep=False)
        self.add_arc('sym-e12', (33, 24), (38, 38), radius_x=17, sweep=False)
        self.add_arc('sym-e13', (15, 24), (10, 38), radius_x=17)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', closed=True)
        self.add_contour('sym-c1', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7')
        self.add_contour('sym-c2', 'sym-e8', 'sym-e9')
        self.add_contour('sym-c3', 'sym-e10')
        self.add_contour('sym-c4', 'sym-e11')
        self.add_contour('sym-c5', 'sym-e12')
        self.add_contour('sym-c6', 'sym-e13')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c3', 'sym-c5')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c4', 'sym-c6')
        self.relate('connect', 'sym-c1', 'sym-c5')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c4')
        self.relate('connect', 'sym-c1', 'sym-c6')
        self.relate('connect', 'sym-c1', 'sym-c5')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c4')
        self.relate('connect', 'sym-c1', 'sym-c6')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c5')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c6')
