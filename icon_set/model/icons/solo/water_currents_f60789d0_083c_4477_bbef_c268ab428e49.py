"""Water currents (weather), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f60789d0-083c-4477-bbef-c268ab428e49'
SOURCE_PATH = 'icons-json/weather/water currents_f60789d0-083c-4477-bbef-c268ab428e49.json'
AUTHOR = 'json_to_solo'

class WaterCurrents(Solo48):
    icon_id = 'water-currents'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'weather'
    aliases = ()
    keywords = ('water', 'currents', 'weather')

    def build(self):
        self.add_line('sym-e0', (8, 8), (4, 12))
        self.add_line('sym-e1', (4, 12), (8, 16))
        self.add_arc('sym-e3', (19, 21), (15, 13), radius_x=7, sweep=False)
        self.add_line('sym-e4', (15, 13), (12, 12))
        self.add_line('sym-e5', (12, 12), (4, 12))
        self.add_arc('sym-e7', (4, 25), (11, 29), radius_x=5, sweep=False)
        self.add_line('sym-e8', (11, 29), (14, 27))
        self.add_arc('sym-e9', (14, 26), (16, 28), radius_x=11)
        self.add_line('sym-e10', (16, 28), (19, 29))
        self.add_line('sym-e11', (19, 29), (22, 28))
        self.add_line('sym-e12', (22, 28), (23, 27))
        self.add_arc('sym-e13', (23, 27), (24, 26), radius_x=1, sweep=False)
        self.add_arc('sym-e16', (24, 26), (25, 27), radius_x=1, sweep=False)
        self.add_line('sym-e17', (25, 27), (26, 28))
        self.add_line('sym-e18', (26, 28), (29, 29))
        self.add_line('sym-e19', (29, 29), (32, 28))
        self.add_arc('sym-e20', (32, 28), (34, 26), radius_x=12)
        self.add_arc('sym-e22-1', (4, 36), (6, 39), radius_x=4, sweep=False)
        self.add_line('sym-e22-2', (6, 39), (9, 40))
        self.add_arc('sym-e25', (9, 40), (13, 38), radius_x=6, sweep=False)
        self.add_arc('sym-e26', (13, 38), (14, 37), radius_x=4)
        self.add_line('sym-e27', (14, 37), (15, 38))
        self.add_arc('sym-e28', (15, 38), (16, 39), radius_x=4, sweep=False)
        self.add_line('sym-e29-1', (16, 39), (19, 40))
        self.add_line('sym-e29-2', (19, 40), (22, 39))
        self.add_arc('sym-e30', (22, 39), (24, 37), radius_x=11)
        self.add_line('sym-e31', (24, 37), (26, 39))
        self.add_line('sym-e32-1', (26, 39), (29, 40))
        self.add_line('sym-e32-2', (29, 40), (32, 39))
        self.add_arc('sym-e33', (32, 39), (33, 38), radius_x=4, sweep=False)
        self.add_line('sym-e34', (33, 38), (34, 37))
        self.add_line('sym-e35', (34, 37), (35, 38))
        self.add_arc('sym-e36', (35, 38), (39, 40), radius_x=5, sweep=False)
        self.add_line('sym-e39-1', (39, 40), (42, 39))
        self.add_arc('sym-e39-2', (42, 39), (44, 36), radius_x=4, sweep=False)
        self.add_line('sym-e41', (40, 8), (44, 12))
        self.add_line('sym-e42', (44, 12), (40, 16))
        self.add_arc('sym-e44', (29, 21), (33, 13), radius_x=7)
        self.add_line('sym-e45', (33, 13), (36, 12))
        self.add_line('sym-e46', (36, 12), (44, 12))
        self.add_arc('sym-e48', (44, 25), (37, 29), radius_x=5)
        self.add_line('sym-e49', (37, 29), (34, 27))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e3', 'sym-e4', 'sym-e5')
        self.add_contour('sym-c2', 'sym-e7', 'sym-e8')
        self.add_contour('sym-c3', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20')
        self.add_contour('sym-c4', 'sym-e22-1', 'sym-e22-2', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29-1', 'sym-e29-2', 'sym-e30', 'sym-e31', 'sym-e32-1', 'sym-e32-2', 'sym-e33', 'sym-e34', 'sym-e35', 'sym-e36', 'sym-e39-1', 'sym-e39-2')
        self.add_contour('sym-c5', 'sym-e41', 'sym-e42')
        self.add_contour('sym-c6', 'sym-e44', 'sym-e45', 'sym-e46')
        self.add_contour('sym-c7', 'sym-e48', 'sym-e49')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c5', 'sym-c6')
        self.relate('connect', 'sym-c5', 'sym-c6')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c5', 'sym-c6')
        self.relate('connect', 'sym-c0', 'sym-c1')
