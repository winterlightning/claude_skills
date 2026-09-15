"""Amazon managed blockchain (programing), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '881f4502-fae5-4c7e-99a9-18cf1f644952'
SOURCE_PATH = 'icons-json/programing/amazon managed blockchain_881f4502-fae5-4c7e-99a9-18cf1f644952.json'
AUTHOR = 'gpt-6'

class AmazonManagedBlockchain(Solo48):
    icon_id = 'amazon-managed-blockchain'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('amazon', 'managed', 'blockchain', 'programing')

    def build(self):
        self.add_line('sym-e0', (19, 24), (29, 24))
        self.add_line('sym-e1', (29, 24), (29, 8))
        self.add_line('sym-e4', (29, 8), (42, 8))
        self.add_arc('sym-e6', (42, 8), (44, 10), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('sym-e7', (44, 10), (44, 38))
        self.add_arc('sym-e9', (44, 38), (42, 40), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('sym-e11', (42, 40), (29, 40))
        self.add_line('sym-e13', (29, 40), (29, 24))
        self.add_line('sym-e15', (19, 24), (19, 12))
        self.add_arc('sym-e16', (19, 12), (19, 9), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('sym-e17', (19, 9), (19, 8))
        self.add_line('sym-e18', (19, 8), (5, 8))
        self.add_arc('sym-e19', (5, 8), (4, 11), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_line('sym-e20', (4, 11), (4, 37))
        self.add_arc('sym-e24', (4, 37), (5, 40), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_line('sym-e25', (5, 40), (19, 40))
        self.add_line('sym-e26', (19, 40), (19, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e4', 'sym-e6', 'sym-e7', 'sym-e9', 'sym-e11', 'sym-e13', closed=False)
        self.add_contour('sym-c1', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e24', 'sym-e25', 'sym-e26', closed=True)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
