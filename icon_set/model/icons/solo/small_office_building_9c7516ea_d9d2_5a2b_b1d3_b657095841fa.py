"""Small office building (office), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9c7516ea-d9d2-5a2b-b1d3-b657095841fa'
SOURCE_PATH = 'icons-json/office/small office building_9c7516ea-d9d2-5a2b-b1d3-b657095841fa.json'
AUTHOR = 'json_to_solo'

class SmallOfficeBuilding(Solo48):
    icon_id = 'small-office-building'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('small', 'office', 'building')

    def build(self):
        self.add_line('sym-e0', (4, 40), (7, 40))
        self.add_line('sym-e1', (7, 40), (19, 40))
        self.add_line('sym-e2', (19, 40), (29, 40))
        self.add_line('sym-e3', (29, 40), (41, 40))
        self.add_line('sym-e4', (41, 40), (44, 40))
        self.add_line('sym-e5', (29, 40), (29, 30))
        self.add_arc('sym-e6', (29, 30), (24, 25), radius_x=4, sweep=False)
        self.add_arc('sym-e7', (24, 25), (19, 30), radius_x=4, sweep=False)
        self.add_line('sym-e8', (19, 30), (19, 40))
        self.add_line('sym-e9', (41, 40), (41, 17))
        self.add_line('sym-e10', (41, 17), (24, 17))
        self.add_line('sym-e11', (24, 17), (7, 17))
        self.add_line('sym-e12', (7, 17), (7, 40))
        self.add_arc('sym-e13', (41, 17), (44, 14), radius_x=3, sweep=False)
        self.add_line('sym-e15', (44, 14), (44, 10))
        self.add_arc('sym-e16', (44, 10), (42, 8), radius_x=2, sweep=False)
        self.add_line('sym-e18', (42, 8), (24, 8))
        self.add_line('sym-e19', (24, 8), (6, 8))
        self.add_arc('sym-e21', (6, 8), (4, 10), radius_x=2, sweep=False)
        self.add_line('sym-e22', (4, 10), (4, 14))
        self.add_arc('sym-e24', (4, 14), (7, 17), radius_x=3, sweep=False)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4')
        self.add_contour('sym-c1', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8')
        self.add_contour('sym-c2', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12')
        self.add_contour('sym-c3', 'sym-e13', 'sym-e15', 'sym-e16', 'sym-e18', 'sym-e19', 'sym-e21', 'sym-e22', 'sym-e24')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c2', 'sym-c3')
