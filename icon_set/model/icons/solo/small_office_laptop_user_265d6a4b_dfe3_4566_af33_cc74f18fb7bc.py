"""Small office laptop user (office), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '265d6a4b-dfe3-4566-af33-cc74f18fb7bc'
SOURCE_PATH = 'icons-json/office/small office laptop user_265d6a4b-dfe3-4566-af33-cc74f18fb7bc.json'
AUTHOR = 'json_to_solo'

class SmallOfficeLaptopUser(Solo48):
    icon_id = 'small-office-laptop-user'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('small', 'office', 'laptop', 'user')

    def build(self):
        self.add_line('e0', (26, 35), (26, 34))
        self.add_line('e1', (38, 37), (38, 42))
        self.add_line('e2', (26, 35), (27, 42))
        self.add_line('e3', (26, 35), (25, 33))
        self.add_line('e4', (23, 32), (13, 32))
        self.add_line('e5', (12, 33), (14, 42))
        self.add_line('e6', (38, 42), (27, 42))
        self.add_line('e7', (38, 42), (41, 42))
        self.add_line('e8', (42, 41), (42, 21))
        self.add_line('e9', (41, 20), (24, 6))
        self.add_line('e10', (23, 6), (7, 20))
        self.add_line('e11', (6, 21), (6, 41))
        self.add_line('e12', (7, 42), (14, 42))
        self.add_line('e13', (27, 42), (14, 42))
        self.add_arc('e14-top', (26, 24), (36, 24), radius_x=5)
        self.add_arc('e14-bottom', (36, 24), (26, 24), radius_x=5)
        self.add_arc('e15', (26, 34), (38, 37), radius_x=8)
        self.add_line('e16', (25, 33), (23, 32))
        self.add_line('e17', (13, 32), (12, 33))
        self.add_arc('e18', (41, 42), (42, 41), radius_x=1, sweep=False)
        self.add_arc('e19', (42, 21), (41, 20), radius_x=1, sweep=False)
        self.add_line('e20', (24, 6), (23, 6))
        self.add_arc('e21', (7, 20), (6, 21), radius_x=1, sweep=False)
        self.add_arc('e22', (6, 41), (7, 42), radius_x=1, sweep=False)
        self.add_contour('c0', 'e0', 'e15', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3', 'e16', 'e4', 'e17', 'e5')
        self.add_contour('c3', 'e6')
        self.add_contour('c4', 'e7', 'e18', 'e8', 'e19', 'e9', 'e20', 'e10', 'e21', 'e11', 'e22', 'e12')
        self.add_contour('c5', 'e13')
        self.add_contour('e14', 'e14-top', 'e14-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c4', 'c5')
