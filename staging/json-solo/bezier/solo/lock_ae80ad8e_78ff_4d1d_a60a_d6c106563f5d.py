"""Lock (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ae80ad8e-78ff-4d1d-a60a-d6c106563f5d'
SOURCE_PATH = 'icons-json/interface-essential/lock_ae80ad8e-78ff-4d1d-a60a-d6c106563f5d.json'
AUTHOR = 'json_to_solo'

class Lock(Solo48):
    icon_id = 'lock'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('lock', 'interface-essential')

    def build(self):
        self.add_arc('sym-e0', (21, 32), (27, 32), radius_x=3, radius_y=4)
        self.add_arc('sym-e1', (27, 32), (21, 32), radius_x=3, radius_y=4)
        self.add_bezier('sym-e2', (24, 4), ((23.843, 4), (24.155, 4), (24, 4)))
        self.add_bezier('sym-e3', (24, 4), ((18.417, 4), (14, 9.218), (14, 15)))
        self.add_line('sym-e4', (14, 15), (14, 20))
        self.add_line('sym-e5', (14, 20), (12, 20))
        self.add_bezier('sym-e6', (12, 20), ((10.147, 20), (8, 21.755), (8, 24)))
        self.add_line('sym-e7', (8, 24), (8, 39))
        self.add_bezier('sym-e8', (8, 39), ((8, 39.118), (8, 38.882), (8, 39)))
        self.add_bezier('sym-e9', (8, 39), ((8, 39.109), (8, 38.891), (8, 39)))
        self.add_bezier('sym-e10', (8, 39), ((8, 39.6), (8, 40.436), (8, 41)))
        self.add_bezier('sym-e11', (8, 41), ((8.589, 42.518), (10.434, 44), (12, 44)))
        self.add_bezier('sym-e12', (12, 44), ((12.135, 44), (11.865, 43.991), (12, 44)))
        self.add_line('sym-e13', (12, 44), (24, 44))
        self.add_line('sym-e14', (24, 44), (36, 44))
        self.add_bezier('sym-e15', (36, 44), ((36.135, 43.991), (35.865, 44), (36, 44)))
        self.add_bezier('sym-e16', (36, 44), ((37.566, 44), (39.411, 42.518), (40, 41)))
        self.add_bezier('sym-e17', (40, 41), ((40, 40.436), (40, 39.6), (40, 39)))
        self.add_bezier('sym-e18', (40, 39), ((40, 38.891), (40, 39.109), (40, 39)))
        self.add_bezier('sym-e19', (40, 39), ((40, 38.882), (40, 39.118), (40, 39)))
        self.add_line('sym-e20', (40, 39), (40, 24))
        self.add_bezier('sym-e21', (40, 24), ((40, 21.755), (37.853, 20), (36, 20)))
        self.add_line('sym-e22', (36, 20), (34, 20))
        self.add_line('sym-e23', (34, 20), (34, 15))
        self.add_bezier('sym-e24', (34, 15), ((34, 9.218), (29.583, 4), (24, 4)))
        self.add_bezier('sym-e25', (24, 4), ((23.845, 4), (24.157, 4), (24, 4)))
        self.add_line('sym-e26', (14, 20), (24, 20))
        self.add_line('sym-e27', (24, 20), (34, 20))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', closed=True)
        self.add_contour('sym-c2', 'sym-e26', 'sym-e27')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
