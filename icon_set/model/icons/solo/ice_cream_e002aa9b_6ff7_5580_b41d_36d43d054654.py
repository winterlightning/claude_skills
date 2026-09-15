"""Ice cream (food), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e002aa9b-6ff7-5580-b41d-36d43d054654'
SOURCE_PATH = 'icons-json/food/ice cream_e002aa9b-6ff7-5580-b41d-36d43d054654.json'
AUTHOR = 'gpt-6'

class IceCream(Solo48):
    icon_id = 'ice-cream'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('ice', 'cream', 'food')

    def build(self):
        self.add_line('sym-e0', (14, 25), (16, 25))
        self.add_line('sym-e1', (16, 25), (18, 24))
        self.add_arc('sym-e2', (18, 24), (24, 25), radius_x=18, radius_y=18, large_arc=False, sweep=False)
        self.add_arc('sym-e5', (24, 25), (30, 24), radius_x=18, radius_y=18, large_arc=False, sweep=False)
        self.add_line('sym-e6', (30, 24), (32, 25))
        self.add_line('sym-e7', (32, 25), (34, 25))
        self.add_line('sym-e8', (34, 25), (30, 34))
        self.add_line('sym-e9', (30, 34), (27, 40))
        self.add_arc('sym-e10', (27, 40), (26, 43), radius_x=24, radius_y=24, large_arc=False, sweep=True)
        self.add_line('sym-e11', (26, 43), (24, 44))
        self.add_line('sym-e12', (24, 44), (22, 43))
        self.add_arc('sym-e13', (22, 43), (21, 40), radius_x=25, radius_y=25, large_arc=False, sweep=True)
        self.add_line('sym-e14', (21, 40), (18, 34))
        self.add_line('sym-e15', (18, 34), (14, 25))
        self.add_arc('sym-e16', (14, 25), (12, 24), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_arc('sym-e17', (12, 24), (8, 20), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('sym-e20', (8, 20), (9, 17))
        self.add_line('sym-e21', (9, 17), (10, 17))
        self.add_line('sym-e22', (10, 17), (10, 15))
        self.add_arc('sym-e23', (10, 15), (10, 12), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('sym-e24-1', (10, 12), (14, 7), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_arc('sym-e24-2', (14, 7), (23, 4), radius_x=16, radius_y=16, large_arc=False, sweep=True)
        self.add_arc('sym-e25', (23, 4), (24, 4), radius_x=69, radius_y=69, large_arc=False, sweep=False)
        self.add_arc('sym-e28', (24, 4), (25, 4), radius_x=76, radius_y=76, large_arc=False, sweep=False)
        self.add_arc('sym-e29-1', (25, 4), (34, 7), radius_x=16, radius_y=16, large_arc=False, sweep=True)
        self.add_arc('sym-e29-2', (34, 7), (38, 12), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_line('sym-e30', (38, 12), (38, 17))
        self.add_line('sym-e32', (38, 17), (39, 17))
        self.add_line('sym-e33', (39, 17), (40, 20))
        self.add_arc('sym-e36', (40, 20), (36, 24), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('sym-e37', (36, 24), (34, 25), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24-1', 'sym-e24-2', 'sym-e25', 'sym-e28', 'sym-e29-1', 'sym-e29-2', 'sym-e30', 'sym-e32', 'sym-e33', 'sym-e36', 'sym-e37', closed=False)
