"""Obstruction (transportation), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '77ce8c19-d748-4677-9097-15486e0a1c5b'
SOURCE_PATH = 'icons-json/transportation/obstruction_77ce8c19-d748-4677-9097-15486e0a1c5b.json'
AUTHOR = 'json_to_solo'

class ObstructionTransportation(Solo48):
    icon_id = 'obstruction-transportation'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('obstruction', 'transportation')

    def build(self):
        self.add_line('e0', (33, 27), (33, 40))
        self.add_line('e1', (31, 42), (17, 42))
        self.add_line('e2', (15, 40), (15, 27))
        self.add_line('e3', (33, 27), (26, 27))
        self.add_line('e4', (33, 27), (41, 27))
        self.add_line('e5', (42, 26), (42, 15))
        self.add_line('e6', (42, 15), (34, 15))
        self.add_line('e7', (33, 16), (29, 22))
        self.add_line('e8', (29, 22), (26, 27))
        self.add_line('e9', (15, 27), (26, 27))
        self.add_line('e10', (15, 27), (13, 27))
        self.add_line('e11', (13, 27), (21, 15))
        self.add_line('e12', (13, 27), (7, 27))
        self.add_line('e13', (6, 26), (6, 17))
        self.add_line('e14', (7, 15), (15, 15))
        self.add_line('e15', (21, 15), (33, 15))
        self.add_line('e16', (33, 15), (33, 8))
        self.add_line('e17', (31, 6), (17, 6))
        self.add_line('e18', (15, 8), (15, 15))
        self.add_line('e19', (21, 15), (15, 15))
        self.add_bezier('e20', (33, 40), ((32.746, 40.425), (32.321, 41.738), (31.83, 41.926)), ((31.781, 41.926), (31.724, 41.926), (31.675, 41.926)), ((31.568, 41.951), (31.106, 41.975), (31, 42)))
        self.add_bezier('e21', (17, 42), ((16.869, 41.943), (16.35, 41.975), (16.211, 41.918)), ((15.491, 41.632), (15.286, 40.638), (15, 40)))
        self.add_bezier('e22', (41, 27), ((41.393, 26.525), (42, 26.43), (42, 25.775)), ((42, 25.735), (42, 26.049), (42, 26)))
        self.add_bezier('e23', (34, 15), ((33.984, 15.008), (33.785, 15.025), (33.777, 15.033)), ((33.515, 15.295), (33.262, 15.738), (33, 16)))
        self.add_bezier('e24', (7, 27), ((6.828, 26.894), (6.155, 26.978), (6.098, 26.741)), ((6.065, 26.643), (6.033, 26.098), (6, 26)))
        self.add_bezier('e25', (6, 17), ((6, 16.926), (6, 16.489), (6, 16.415)), ((6, 16.162), (6.196, 15.483), (6.311, 15.344)), ((6.475, 15.229), (6.828, 15.115), (7, 15)))
        self.add_bezier('e26', (33, 8), ((32.435, 6.838), (32.186, 6.515), (31, 6)))
        self.add_bezier('e27', (17, 6), ((16.861, 6.065), (16.334, 6.049), (16.186, 6.106)), ((15.524, 6.393), (15.278, 7.411), (15, 8)))
        self.add_contour('c0', 'e0', 'e20', 'e1', 'e21', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4', 'e22', 'e5', 'e6', 'e23', 'e7', 'e8')
        self.add_contour('c3', 'e9')
        self.add_contour('c4', 'e10')
        self.add_contour('c5', 'e11')
        self.add_contour('c6', 'e12', 'e24', 'e13', 'e25', 'e14')
        self.add_contour('c7', 'e15', 'e16', 'e26', 'e17', 'e27', 'e18')
        self.add_contour('c8', 'e19')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c5', 'c7')
        self.relate('connect', 'c5', 'c8')
        self.relate('connect', 'c7', 'c8')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c6', 'c8')
        self.relate('connect', 'c7', 'c8')
