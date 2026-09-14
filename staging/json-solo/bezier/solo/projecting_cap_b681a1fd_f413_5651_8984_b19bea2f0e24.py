"""Projecting cap (construction), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b681a1fd-f413-5651-8984-b19bea2f0e24'
SOURCE_PATH = 'icons-json/construction/projecting cap_b681a1fd-f413-5651-8984-b19bea2f0e24.json'
AUTHOR = 'json_to_solo'

class ProjectingCapConstruction(Solo48):
    icon_id = 'projecting-cap-construction'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'construction'
    aliases = ()
    keywords = ('projecting', 'cap', 'construction')

    def build(self):
        self.add_line('e0', (44, 8), (4, 8))
        self.add_line('e1', (4, 8), (4, 40))
        self.add_line('e2', (4, 40), (44, 40))
        self.add_line('e3', (44, 24), (19, 24))
        self.add_arc('e4-top', (12, 24), (20, 24), radius_x=4, radius_y=5)
        self.add_arc('e4-bottom', (20, 24), (12, 24), radius_x=4, radius_y=5)
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
        self.relate('connect', 'c1', 'e4')
