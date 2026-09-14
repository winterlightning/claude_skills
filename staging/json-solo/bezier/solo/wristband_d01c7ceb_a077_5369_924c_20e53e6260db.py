"""Wristband (events), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd01c7ceb-a077-5369-924c-20e53e6260db'
SOURCE_PATH = 'icons-json/events/wristband_d01c7ceb-a077-5369-924c-20e53e6260db.json'
AUTHOR = 'json_to_solo'

class WristbandEvents(Solo48):
    icon_id = 'wristband-events'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'events'
    aliases = ()
    keywords = ('wristband', 'events')

    def build(self):
        self.add_bezier('sym-e0', (31, 38), ((30.218, 38.88), (29.236, 40), (28, 40)))
        self.add_bezier('sym-e1', (28, 40), ((27.909, 40), (28.091, 40), (28, 40)))
        self.add_bezier('sym-e2', (28, 40), ((27.236, 40), (26.755, 40), (26, 40)))
        self.add_bezier('sym-e3', (26, 40), ((25.399, 39.948), (24.604, 40), (24, 40)))
        self.add_bezier('sym-e4', (24, 40), ((23.396, 40), (22.601, 39.948), (22, 40)))
        self.add_bezier('sym-e5', (22, 40), ((21.245, 40), (20.764, 40), (20, 40)))
        self.add_bezier('sym-e6', (20, 40), ((19.909, 40), (20.091, 40), (20, 40)))
        self.add_bezier('sym-e7', (20, 40), ((18.764, 40), (17.782, 38.88), (17, 38)))
        self.add_line('sym-e8', (17, 38), (17, 25))
        self.add_bezier('sym-e9', (17, 25), ((13.436, 24.53), (8.945, 23.35), (6, 21)))
        self.add_bezier('sym-e10', (6, 21), ((5.336, 20.47), (5.636, 19.57), (5, 19)))
        self.add_bezier('sym-e11', (5, 19), ((4.991, 18.99), (4, 19), (4, 19)))
        self.add_bezier('sym-e12', (4, 19), ((4, 17.98), (4, 17.02), (4, 16)))
        self.add_bezier('sym-e13', (4, 16), ((4, 13.99), (6.555, 11.8), (8, 11)))
        self.add_bezier('sym-e14', (8, 11), ((12.5, 8.55), (18.027, 8), (23, 8)))
        self.add_bezier('sym-e15', (23, 8), ((23.455, 8), (23.545, 8), (24, 8)))
        self.add_bezier('sym-e16', (24, 8), ((24.455, 8), (24.545, 8), (25, 8)))
        self.add_bezier('sym-e17', (25, 8), ((29.973, 8), (35.5, 8.55), (40, 11)))
        self.add_bezier('sym-e18', (40, 11), ((41.445, 11.8), (44, 13.99), (44, 16)))
        self.add_bezier('sym-e19', (44, 16), ((44, 17.02), (44, 17.98), (44, 19)))
        self.add_bezier('sym-e20', (44, 19), ((44, 19), (43.009, 18.99), (43, 19)))
        self.add_bezier('sym-e21', (43, 19), ((42.364, 19.57), (42.664, 20.47), (42, 21)))
        self.add_bezier('sym-e22', (42, 21), ((39.055, 23.35), (34.564, 24.53), (31, 25)))
        self.add_bezier('sym-e23', (31, 25), ((29.873, 22.97), (29.218, 22), (27, 22)))
        self.add_line('sym-e24', (27, 22), (24, 22))
        self.add_line('sym-e25', (24, 22), (21, 22))
        self.add_bezier('sym-e26', (21, 22), ((18.782, 22), (18.127, 22.97), (17, 25)))
        self.add_line('sym-e27', (31, 25), (31, 38))
        self.add_bezier('sym-e28', (31, 38), ((34.691, 37.39), (44, 35.6), (44, 30)))
        self.add_bezier('sym-e29', (44, 30), ((44, 29.91), (44, 30.09), (44, 30)))
        self.add_line('sym-e30', (44, 30), (44, 19))
        self.add_bezier('sym-e31', (17, 38), ((13.309, 37.39), (4, 35.6), (4, 30)))
        self.add_bezier('sym-e32', (4, 30), ((4, 29.91), (4, 30.09), (4, 30)))
        self.add_line('sym-e33', (4, 30), (4, 19))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26')
        self.add_contour('sym-c1', 'sym-e27', 'sym-e28', 'sym-e29', 'sym-e30')
        self.add_contour('sym-c2', 'sym-e31', 'sym-e32', 'sym-e33')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
