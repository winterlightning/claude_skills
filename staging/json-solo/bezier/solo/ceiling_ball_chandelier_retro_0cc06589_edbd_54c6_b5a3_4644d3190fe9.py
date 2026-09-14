"""Ceiling ball chandelier retro (lamps), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0cc06589-edbd-54c6-b5a3-4644d3190fe9'
SOURCE_PATH = 'icons-json/lamps/ceiling ball chandelier retro_0cc06589-edbd-54c6-b5a3-4644d3190fe9.json'
AUTHOR = 'json_to_solo'

class CeilingBallChandelierRetroLamps(Solo48):
    icon_id = 'ceiling-ball-chandelier-retro-lamps'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'lamps'
    aliases = ()
    keywords = ('ceiling', 'ball', 'chandelier', 'retro', 'lamps')

    def build(self):
        self.add_arc('sym-e0', (19, 36), (24, 32), radius_x=5, radius_y=4)
        self.add_arc('sym-e1', (24, 32), (29, 36), radius_x=5, radius_y=4)
        self.add_arc('sym-e2', (29, 36), (19, 36), radius_x=5, radius_y=4)
        self.add_arc('sym-e3', (4, 36), (9, 32), radius_x=5, radius_y=4)
        self.add_arc('sym-e4', (9, 32), (13, 36), radius_x=5, radius_y=4)
        self.add_arc('sym-e5', (13, 36), (4, 36), radius_x=5, radius_y=4)
        self.add_arc('sym-e6', (44, 36), (39, 32), radius_x=5, radius_y=4, sweep=False)
        self.add_arc('sym-e7', (39, 32), (35, 36), radius_x=5, radius_y=4, sweep=False)
        self.add_arc('sym-e8', (35, 36), (44, 36), radius_x=5, radius_y=4, sweep=False)
        self.add_line('sym-e9', (29, 8), (24, 8))
        self.add_line('sym-e10', (24, 8), (19, 8))
        self.add_line('sym-e11', (24, 8), (24, 22))
        self.add_line('sym-e12', (24, 22), (24, 32))
        self.add_line('sym-e13', (5, 22), (9, 22))
        self.add_line('sym-e14', (9, 22), (24, 22))
        self.add_line('sym-e15', (24, 22), (39, 22))
        self.add_line('sym-e16', (39, 22), (43, 22))
        self.add_line('sym-e17', (9, 22), (9, 32))
        self.add_line('sym-e18', (39, 22), (39, 32))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', closed=True)
        self.add_contour('sym-c1', 'sym-e3', 'sym-e4', 'sym-e5', closed=True)
        self.add_contour('sym-c2', 'sym-e6', 'sym-e7', 'sym-e8', closed=True)
        self.add_contour('sym-c3', 'sym-e9', 'sym-e10')
        self.add_contour('sym-c4', 'sym-e11', 'sym-e12')
        self.add_contour('sym-c5', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16')
        self.add_contour('sym-c6', 'sym-e17')
        self.add_contour('sym-c7', 'sym-e18')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c1', 'sym-c6')
        self.relate('connect', 'sym-c2', 'sym-c7')
        self.relate('connect', 'sym-c3', 'sym-c4')
        self.relate('connect', 'sym-c4', 'sym-c5')
        self.relate('connect', 'sym-c5', 'sym-c6')
        self.relate('connect', 'sym-c5', 'sym-c7')
        self.relate('connect', 'sym-c3', 'sym-c4')
        self.relate('connect', 'sym-c3', 'sym-c4')
        self.relate('connect', 'sym-c4', 'sym-c5')
        self.relate('connect', 'sym-c4', 'sym-c5')
        self.relate('connect', 'sym-c4', 'sym-c5')
        self.relate('connect', 'sym-c4', 'sym-c5')
        self.relate('connect', 'sym-c5', 'sym-c7')
        self.relate('connect', 'sym-c5', 'sym-c6')
        self.relate('connect', 'sym-c2', 'sym-c7')
        self.relate('connect', 'sym-c1', 'sym-c6')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c4')
