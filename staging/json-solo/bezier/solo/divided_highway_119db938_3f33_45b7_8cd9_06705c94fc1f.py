"""Divided highway (transportation), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '119db938-3f33-45b7-8cd9-06705c94fc1f'
SOURCE_PATH = 'icons-json/transportation/divided highway_119db938-3f33-45b7-8cd9-06705c94fc1f.json'
AUTHOR = 'json_to_solo'

class DividedHighwayTransportation(Solo48):
    icon_id = 'divided-highway-transportation'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('divided', 'highway', 'transportation')

    def build(self):
        self.add_line('sym-e0', (40, 4), (40, 27))
        self.add_bezier('sym-e1', (40, 27), ((40, 27.682), (38.46, 28.445), (38, 29)))
        self.add_line('sym-e2', (38, 29), (35, 33))
        self.add_bezier('sym-e3', (35, 33), ((34.37, 33.764), (34, 35.055), (34, 36)))
        self.add_line('sym-e4', (34, 36), (34, 44))
        self.add_line('sym-e5', (34, 44), (37, 41))
        self.add_line('sym-e6', (31, 41), (34, 44))
        self.add_bezier('sym-e7', (24, 20), ((25.579, 20), (27.009, 19.29), (28, 18)))
        self.add_bezier('sym-e8', (28, 18), ((28.38, 17.509), (29, 16.618), (29, 16)))
        self.add_line('sym-e9', (29, 16), (29, 7))
        self.add_line('sym-e10', (8, 4), (8, 27))
        self.add_bezier('sym-e11', (8, 27), ((8, 27.682), (9.54, 28.445), (10, 29)))
        self.add_line('sym-e12', (10, 29), (13, 33))
        self.add_bezier('sym-e13', (13, 33), ((13.63, 33.764), (14, 35.055), (14, 36)))
        self.add_line('sym-e14', (14, 36), (14, 44))
        self.add_line('sym-e15', (14, 44), (11, 41))
        self.add_line('sym-e16', (17, 41), (14, 44))
        self.add_bezier('sym-e17', (24, 20), ((22.421, 20), (20.991, 19.29), (20, 18)))
        self.add_bezier('sym-e18', (20, 18), ((19.62, 17.509), (19, 16.618), (19, 16)))
        self.add_line('sym-e19', (19, 16), (19, 7))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5')
        self.add_contour('sym-c1', 'sym-e6')
        self.add_contour('sym-c2', 'sym-e7', 'sym-e8', 'sym-e9')
        self.add_contour('sym-c3', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15')
        self.add_contour('sym-c4', 'sym-e16')
        self.add_contour('sym-c5', 'sym-e17', 'sym-e18', 'sym-e19')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c2', 'sym-c5')
        self.relate('connect', 'sym-c3', 'sym-c4')
        self.relate('connect', 'sym-c3', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c3', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c1')
