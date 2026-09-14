"""Small office building (office), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9c7516ea-d9d2-5a2b-b1d3-b657095841fa'
SOURCE_PATH = 'icons-json/office/small office building_9c7516ea-d9d2-5a2b-b1d3-b657095841fa.json'
AUTHOR = 'json_to_solo'

class SmallOfficeBuildingOffice(Solo48):
    icon_id = 'small-office-building-office'
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
        self.add_bezier('sym-e6', (29, 30), ((29, 26.778), (26.664, 24.796), (24, 25)))
        self.add_bezier('sym-e7', (24, 25), ((21.336, 24.796), (19, 26.778), (19, 30)))
        self.add_line('sym-e8', (19, 30), (19, 40))
        self.add_line('sym-e9', (41, 40), (41, 17))
        self.add_line('sym-e10', (41, 17), (24, 17))
        self.add_line('sym-e11', (24, 17), (7, 17))
        self.add_line('sym-e12', (7, 17), (7, 40))
        self.add_bezier('sym-e13', (41, 17), ((42.464, 17), (44, 15.71), (44, 14)))
        self.add_bezier('sym-e14', (44, 14), ((44, 13.9), (44, 14.1), (44, 14)))
        self.add_line('sym-e15', (44, 14), (44, 10))
        self.add_bezier('sym-e16', (44, 10), ((44, 9.2), (42.791, 8), (42, 8)))
        self.add_bezier('sym-e17', (42, 8), ((41.936, 8), (42.064, 8), (42, 8)))
        self.add_line('sym-e18', (42, 8), (24, 8))
        self.add_line('sym-e19', (24, 8), (6, 8))
        self.add_bezier('sym-e20', (6, 8), ((5.936, 8), (6.064, 8), (6, 8)))
        self.add_bezier('sym-e21', (6, 8), ((5.209, 8), (4, 9.2), (4, 10)))
        self.add_line('sym-e22', (4, 10), (4, 14))
        self.add_bezier('sym-e23', (4, 14), ((4, 14.1), (4, 13.9), (4, 14)))
        self.add_bezier('sym-e24', (4, 14), ((4, 15.71), (5.536, 17), (7, 17)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4')
        self.add_contour('sym-c1', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8')
        self.add_contour('sym-c2', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12')
        self.add_contour('sym-c3', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24')
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
