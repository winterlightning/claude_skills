"""Transit gateway (programing), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ed53f150-82ce-586d-8d45-acbd76391d39'
SOURCE_PATH = 'pictographic-primitives/programing/transit gateway_ed53f150-82ce-586d-8d45-acbd76391d39.svg'
AUTHOR = 'gpt-6'

class TransitGateway(Solo48):
    icon_id = 'transit-gateway'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('transit', 'gateway', 'programing')

    def build(self):
        self.add_line('sym-e0', (20, 24), (4, 24))
        self.add_line('sym-e2', (44, 24), (30, 24))
        self.add_line('sym-e3', (30, 24), (30, 11))
        self.add_arc('sym-e4', (30, 11), (27, 8), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('sym-e6', (27, 8), (15, 8))
        self.add_arc('sym-e7', (15, 8), (14, 8), radius_x=18, radius_y=18, large_arc=False, sweep=True)
        self.add_line('sym-e11', (14, 8), (13, 8))
        self.add_arc('sym-e12', (13, 8), (10, 11), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('sym-e13', (10, 11), (10, 37))
        self.add_arc('sym-e17', (10, 37), (13, 40), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_arc('sym-e18', (13, 40), (14, 40), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_arc('sym-e22', (14, 40), (15, 40), radius_x=22, radius_y=22, large_arc=False, sweep=True)
        self.add_line('sym-e23', (15, 40), (27, 40))
        self.add_arc('sym-e25', (27, 40), (30, 37), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('sym-e26', (30, 37), (30, 24))
        self.add_line('sym-e27', (44, 24), (39, 19))
        self.add_line('sym-e28', (44, 24), (39, 29))
        self.add_contour('sym-c0', 'sym-e0', closed=False)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e6', 'sym-e7', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e17', 'sym-e18', 'sym-e22', 'sym-e23', 'sym-e25', 'sym-e26', closed=False)
        self.add_contour('sym-c2', 'sym-e27', closed=False)
        self.add_contour('sym-c3', 'sym-e28', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
