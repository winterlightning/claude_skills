"""Vertical (photography), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd58dfd2c-80d5-5864-aea1-9b4d6fb8eec3'
SOURCE_PATH = 'pictographic-primitives/photography/vertical_d58dfd2c-80d5-5864-aea1-9b4d6fb8eec3.svg'
AUTHOR = 'gpt-6'

class Vertical(Solo48):
    icon_id = 'vertical'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'photography'
    aliases = ()
    keywords = ('vertical', 'photography')

    def build(self):
        self.add_arc('sym-e0', (8, 4), (10, 11), radius_x=75, radius_y=75, large_arc=False, sweep=True)
        self.add_arc('sym-e1', (10, 11), (12, 24), radius_x=53, radius_y=53, large_arc=False, sweep=True)
        self.add_arc('sym-e2', (12, 24), (10, 37), radius_x=53, radius_y=53, large_arc=False, sweep=True)
        self.add_arc('sym-e3', (10, 37), (8, 44), radius_x=75, radius_y=75, large_arc=False, sweep=True)
        self.add_line('sym-e4', (8, 44), (40, 44))
        self.add_arc('sym-e6', (40, 44), (38, 37), radius_x=75, radius_y=75, large_arc=False, sweep=True)
        self.add_arc('sym-e7', (38, 37), (36, 24), radius_x=53, radius_y=53, large_arc=False, sweep=True)
        self.add_arc('sym-e8', (36, 24), (38, 11), radius_x=53, radius_y=53, large_arc=False, sweep=True)
        self.add_arc('sym-e9', (38, 11), (40, 4), radius_x=75, radius_y=75, large_arc=False, sweep=True)
        self.add_line('sym-e10', (40, 4), (8, 4))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', closed=True)
