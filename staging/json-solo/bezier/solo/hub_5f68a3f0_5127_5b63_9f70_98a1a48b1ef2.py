"""Hub (programing), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5f68a3f0-5127-5b63-9f70-98a1a48b1ef2'
SOURCE_PATH = 'icons-json/programing/hub_5f68a3f0-5127-5b63-9f70-98a1a48b1ef2.json'
AUTHOR = 'json_to_solo'

class HubPrograming(Solo48):
    icon_id = 'hub-programing'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('hub', 'programing')

    def build(self):
        self.add_line('e0', (35, 31), (28, 28))
        self.add_line('e1', (13, 36), (22, 41))
        self.add_line('e2', (26, 41), (35, 36))
        self.add_line('e3', (39, 30), (39, 18))
        self.add_line('e4', (37, 17), (28, 11))
        self.add_line('e5', (9, 30), (9, 18))
        self.add_line('e6', (11, 17), (20, 11))
        self.add_line('e7', (28, 28), (28, 23))
        self.add_line('e8', (20, 28), (13, 31))
        self.add_line('e9', (20, 28), (20, 22))
        self.add_line('e10', (20, 22), (24, 20))
        self.add_line('e11', (24, 20), (24, 14))
        self.add_arc('e12-top', (34, 34), (42, 34), radius_x=4)
        self.add_arc('e12-bottom', (42, 34), (34, 34), radius_x=4)
        self.add_arc('e13-top', (6, 34), (14, 34), radius_x=4)
        self.add_arc('e13-bottom', (14, 34), (6, 34), radius_x=4)
        self.add_arc('e14-top', (20, 10), (28, 10), radius_x=4)
        self.add_arc('e14-bottom', (28, 10), (20, 10), radius_x=4)
        self.add_bezier('e15', (22, 41), ((22.393, 41.213), (23.362, 41.984), (23.828, 41.984)), ((23.877, 41.992), (23.933, 42), (23.981, 42)), ((23.982, 42), (23.983, 42), (23.984, 42)), ((24.041, 41.992), (24.09, 41.992), (24.147, 41.984)), ((24.622, 41.984), (25.599, 41.221), (26, 41)))
        self.add_bezier('e16', (39, 18), ((39, 17.255), (37.491, 17.311), (37, 17)))
        self.add_bezier('e17', (9, 18), ((9, 17.305), (10.525, 17.303), (11, 17)))
        self.add_bezier('e18', (28, 28), ((27.035, 28.532), (26.168, 29.195), (25.186, 29.686)), ((23.534, 30.529), (23.247, 29.981), (21.595, 29.056)), ((21.03, 28.745), (20.556, 28.327), (20, 28)))
        self.add_bezier('e19', (28, 23), ((26.969, 21.625), (25.497, 20.851), (24, 20)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e15', 'e2')
        self.add_contour('c2', 'e3', 'e16', 'e4')
        self.add_contour('c3', 'e5', 'e17', 'e6')
        self.add_contour('c4', 'e18')
        self.add_contour('c5', 'e7', 'e19')
        self.add_contour('c6', 'e8')
        self.add_contour('c7', 'e9', 'e10')
        self.add_contour('c8', 'e11')
        self.add_contour('e14', 'e14-top', 'e14-bottom', closed=True)
        self.add_contour('e13', 'e13-top', 'e13-bottom', closed=True)
        self.add_contour('e12', 'e12-top', 'e12-bottom', closed=True)
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c4', 'c7')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c5', 'c7')
        self.relate('connect', 'c5', 'c8')
        self.relate('connect', 'c7', 'c8')
        self.relate('connect', 'c0', 'e12')
        self.relate('connect', 'c1', 'e13')
        self.relate('connect', 'c1', 'e12')
        self.relate('connect', 'c2', 'e12')
        self.relate('connect', 'c2', 'e14')
        self.relate('connect', 'c3', 'e13')
        self.relate('connect', 'c3', 'e14')
        self.relate('connect', 'c6', 'e13')
        self.relate('connect', 'c8', 'e14')
