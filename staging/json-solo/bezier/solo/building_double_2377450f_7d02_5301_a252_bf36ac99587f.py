"""Building double (office), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2377450f-7d02-5301-a252-bf36ac99587f'
SOURCE_PATH = 'icons-json/office/building double_2377450f-7d02-5301-a252-bf36ac99587f.json'
AUTHOR = 'json_to_solo'

class BuildingDoubleOffice(Solo48):
    icon_id = 'building-double-office'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('building', 'double', 'office')

    def build(self):
        self.add_line('e0', (31, 42), (31, 8))
        self.add_line('e1', (29, 6), (8, 6))
        self.add_line('e2', (6, 8), (6, 42))
        self.add_line('e3', (6, 42), (42, 42))
        self.add_line('e4', (42, 42), (42, 24))
        self.add_line('e5', (40, 21), (31, 21))
        self.add_line('e6', (19, 32), (19, 42))
        self.add_line('e7', (13, 13), (13, 17))
        self.add_line('e8', (24, 13), (24, 17))
        self.add_bezier('e9', (31, 8), ((31, 6.887), (30.807, 6.008), (29.49, 6.008)), ((29.425, 6.008), (29.359, 6), (29.294, 6)), ((29.171, 6), (29.131, 6), (29, 6)))
        self.add_bezier('e10', (8, 6), ((7.509, 6), (7.473, 6.016), (6.982, 6.016)), ((6.278, 6.016), (6, 7.476), (6, 8)))
        self.add_bezier('e11', (42, 24), ((42, 23.746), (41.992, 23.485), (41.992, 23.231)), ((41.992, 22.094), (41.563, 21), (40, 21)))
        self.add_contour('c0', 'e0', 'e9', 'e1', 'e10', 'e2', 'e3', 'e4', 'e11', 'e5')
        self.add_contour('c1', 'e6')
        self.add_contour('c2', 'e7')
        self.add_contour('c3', 'e8')
        self.relate('connect', 'c1', 'c0')
