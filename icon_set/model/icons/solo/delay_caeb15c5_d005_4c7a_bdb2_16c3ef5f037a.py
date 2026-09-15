"""Delay (diagrams), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'caeb15c5-d005-4c7a-bdb2-16c3ef5f037a'
SOURCE_PATH = 'pictographic-primitives/diagrams/delay_caeb15c5-d005-4c7a-bdb2-16c3ef5f037a.svg'
AUTHOR = 'gpt-6'

class Delay(Solo48):
    icon_id = 'delay'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'diagrams'
    aliases = ()
    keywords = ('delay', 'diagrams')

    def build(self):
        self.add_line('sym-e0', (4, 8), (4, 40))
        self.add_line('sym-e2', (4, 40), (27, 40))
        self.add_arc('sym-e3', (27, 40), (30, 40), radius_x=15, radius_y=15, large_arc=False, sweep=True)
        self.add_arc('sym-e4', (30, 40), (44, 25), radius_x=17, radius_y=17, large_arc=False, sweep=False)
        self.add_line('sym-e5', (44, 25), (44, 24))
        self.add_arc('sym-e6', (44, 24), (44, 23), radius_x=28, radius_y=28, large_arc=False, sweep=True)
        self.add_arc('sym-e7', (44, 23), (30, 8), radius_x=17, radius_y=17, large_arc=False, sweep=False)
        self.add_arc('sym-e8', (30, 8), (27, 8), radius_x=15, radius_y=15, large_arc=False, sweep=True)
        self.add_line('sym-e9', (27, 8), (4, 8))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', closed=True)
