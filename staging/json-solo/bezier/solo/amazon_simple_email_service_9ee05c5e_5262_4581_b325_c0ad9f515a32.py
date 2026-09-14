"""Amazon simple email service (_uncategorized_02), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9ee05c5e-5262-4581-b325-c0ad9f515a32'
SOURCE_PATH = 'icons-json/_uncategorized_02/amazon simple email service_9ee05c5e-5262-4581-b325-c0ad9f515a32.json'
AUTHOR = 'json_to_solo'

class AmazonSimpleEmailServiceUncategorized02(Solo48):
    icon_id = 'amazon-simple-email-service-uncategorized-02'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_02'
    aliases = ()
    keywords = ('amazon', 'simple', 'email', 'service', '_uncategorized_02')

    def build(self):
        self.add_line('e0', (36, 31), (24, 31))
        self.add_line('e1', (12, 31), (24, 31))
        self.add_line('e2', (24, 35), (24, 31))
        self.add_line('e3', (9, 7), (23, 17))
        self.add_line('e4', (25, 17), (39, 7))
        self.add_line('e5', (9, 7), (9, 22))
        self.add_line('e6', (11, 24), (24, 24))
        self.add_line('e7', (9, 7), (11, 6))
        self.add_line('e8', (11, 6), (37, 6))
        self.add_line('e9', (37, 6), (39, 7))
        self.add_line('e10', (39, 7), (39, 22))
        self.add_line('e11', (37, 24), (24, 24))
        self.add_line('e12', (24, 24), (24, 31))
        self.add_arc('e13-top', (36, 39), (42, 39), radius_x=3)
        self.add_arc('e13-bottom', (42, 39), (36, 39), radius_x=3)
        self.add_arc('e14-top', (6, 39), (12, 39), radius_x=3)
        self.add_arc('e14-bottom', (12, 39), (6, 39), radius_x=3)
        self.add_arc('e15-top', (21, 39), (27, 39), radius_x=3)
        self.add_arc('e15-bottom', (27, 39), (21, 39), radius_x=3)
        self.add_bezier('e16', (39, 35), ((39.614, 32.66), (38.258, 31.9), (36, 31)))
        self.add_bezier('e17', (9, 35), ((8.46, 32.619), (9.644, 31.892), (12, 31)))
        self.add_bezier('e18', (24, 35), ((24, 34.73), (24, 35.27), (24, 35)))
        self.add_bezier('e19', (23, 17), ((23.614, 17.082), (24.386, 17.074), (25, 17)))
        self.add_bezier('e20', (9, 22), ((9.008, 22.074), (9.215, 21.758), (9.232, 21.873)), ((9.379, 22.912), (10.174, 23.476), (11, 24)))
        self.add_bezier('e21', (39, 22), ((39, 23.301), (38.137, 23.452), (37, 24)))
        self.add_contour('c0', 'e16', 'e0')
        self.add_contour('c1', 'e17', 'e1')
        self.add_contour('c2', 'e18', 'e2')
        self.add_contour('c3', 'e3', 'e19', 'e4')
        self.add_contour('c4', 'e5', 'e20', 'e6')
        self.add_contour('c5', 'e7', 'e8', 'e9')
        self.add_contour('c6', 'e10', 'e21', 'e11')
        self.add_contour('c7', 'e12')
        self.add_contour('e14', 'e14-top', 'e14-bottom', closed=True)
        self.add_contour('e13', 'e13-top', 'e13-bottom', closed=True)
        self.add_contour('e15', 'e15-top', 'e15-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c7')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c7')
        self.relate('connect', 'c2', 'c7')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c4', 'c7')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c0', 'e13')
        self.relate('connect', 'c1', 'e14')
        self.relate('connect', 'c2', 'e15')
