"""Ticket (entertainment), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd3c5d63d-804f-4be5-8482-c41707c7a1f1'
SOURCE_PATH = 'pictographic-primitives/entertainment/ticket_d3c5d63d-804f-4be5-8482-c41707c7a1f1.svg'
AUTHOR = 'gpt-6'

class Ticket(Solo48):
    icon_id = 'ticket-entertainment'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'entertainment'
    categories = ('entertainment', 'primitives')
    aliases = ()
    keywords = ('ticket', 'entertainment')

    def build(self):
        self.add_line('sym-e0', (44, 17), (44, 8))
        self.add_line('sym-e1', (44, 8), (4, 8))
        self.add_line('sym-e3', (4, 8), (4, 17))
        self.add_arc('sym-e4', (4, 17), (9, 24), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('sym-e5', (9, 24), (4, 31), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_line('sym-e6', (4, 31), (4, 40))
        self.add_line('sym-e7', (4, 40), (44, 40))
        self.add_line('sym-e9', (44, 40), (44, 31))
        self.add_arc('sym-e10', (44, 31), (39, 24), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('sym-e11', (39, 24), (44, 17), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e9', 'sym-e10', 'sym-e11', closed=True)
