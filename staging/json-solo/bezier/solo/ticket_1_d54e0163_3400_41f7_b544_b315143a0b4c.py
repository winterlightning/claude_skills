"""Ticket 1 (container), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd54e0163-3400-41f7-b544-b315143a0b4c'
SOURCE_PATH = 'icons-json/container/ticket 1_d54e0163-3400-41f7-b544-b315143a0b4c.json'
AUTHOR = 'json_to_solo'

class Ticket1D54e0163(Solo48):
    icon_id = 'ticket-1-d54e0163'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    aliases = ()
    keywords = ('ticket', 'container')

    def build(self):
        self.add_bezier('sym-e0', (39, 24), ((39, 24.007), (39, 23.993), (39, 24)))
        self.add_bezier('sym-e1', (39, 24), ((39, 27.2), (40.343, 30.415), (44, 31)))
        self.add_line('sym-e2', (44, 31), (44, 40))
        self.add_line('sym-e3', (44, 40), (4, 40))
        self.add_line('sym-e4', (4, 40), (4, 31))
        self.add_bezier('sym-e5', (4, 31), ((4.627, 30.9), (5.418, 31.28), (6, 31)))
        self.add_bezier('sym-e6', (6, 31), ((8.42, 29.862), (8.999, 26.703), (9, 24)))
        self.add_bezier('sym-e7', (9, 24), ((8.999, 21.297), (8.42, 18.138), (6, 17)))
        self.add_bezier('sym-e8', (6, 17), ((5.418, 16.72), (4.627, 17.1), (4, 17)))
        self.add_line('sym-e9', (4, 17), (4, 8))
        self.add_line('sym-e10', (4, 8), (44, 8))
        self.add_line('sym-e11', (44, 8), (44, 17))
        self.add_bezier('sym-e12', (44, 17), ((40.343, 17.585), (39, 20.8), (39, 24)))
        self.add_bezier('sym-e13', (39, 24), ((39, 24.007), (39, 23.993), (39, 24)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', closed=True)
