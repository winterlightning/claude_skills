"""Ticket 1 (container), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7598ef67-d9e2-48eb-bc31-cab0bc1372b2'
SOURCE_PATH = 'icons-json/container/ticket 1_7598ef67-d9e2-48eb-bc31-cab0bc1372b2.json'
AUTHOR = 'json_to_solo'

class Ticket1(Solo48):
    icon_id = 'ticket-1'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    aliases = ()
    keywords = ('ticket', 'container')

    def build(self):
        self.add_arc('sym-e1', (39, 24), (44, 31), radius_x=6, sweep=False)
        self.add_line('sym-e2', (44, 31), (44, 40))
        self.add_line('sym-e3', (44, 40), (4, 40))
        self.add_line('sym-e4', (4, 40), (4, 31))
        self.add_line('sym-e5', (4, 31), (6, 31))
        self.add_arc('sym-e6', (6, 31), (9, 24), radius_x=7, sweep=False)
        self.add_arc('sym-e7', (9, 24), (6, 17), radius_x=7, sweep=False)
        self.add_line('sym-e8', (6, 17), (4, 17))
        self.add_line('sym-e9', (4, 17), (4, 8))
        self.add_line('sym-e10', (4, 8), (44, 8))
        self.add_line('sym-e11', (44, 8), (44, 17))
        self.add_arc('sym-e12', (44, 17), (39, 24), radius_x=6, sweep=False)
        self.add_contour('sym-c0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', closed=True)
