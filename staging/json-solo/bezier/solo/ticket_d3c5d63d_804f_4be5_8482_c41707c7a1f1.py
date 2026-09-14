"""Ticket (entertainment), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd3c5d63d-804f-4be5-8482-c41707c7a1f1'
SOURCE_PATH = 'icons-json/entertainment/ticket_d3c5d63d-804f-4be5-8482-c41707c7a1f1.json'
AUTHOR = 'json_to_solo'

class Ticket(Solo48):
    icon_id = 'ticket'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'entertainment'
    aliases = ()
    keywords = ('ticket', 'entertainment')

    def build(self):
        self.add_line('sym-e0', (44, 17), (44, 8))
        self.add_line('sym-e1', (44, 8), (24, 8))
        self.add_line('sym-e2', (24, 8), (4, 8))
        self.add_line('sym-e3', (4, 8), (4, 17))
        self.add_bezier('sym-e4', (4, 17), ((7.653, 17.641), (9, 20.628), (9, 24)))
        self.add_bezier('sym-e5', (9, 24), ((9, 27.372), (7.653, 30.359), (4, 31)))
        self.add_line('sym-e6', (4, 31), (4, 40))
        self.add_line('sym-e7', (4, 40), (24, 40))
        self.add_line('sym-e8', (24, 40), (44, 40))
        self.add_line('sym-e9', (44, 40), (44, 31))
        self.add_bezier('sym-e10', (44, 31), ((40.347, 30.359), (39, 27.372), (39, 24)))
        self.add_bezier('sym-e11', (39, 24), ((39, 20.628), (40.347, 17.641), (44, 17)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', closed=True)
