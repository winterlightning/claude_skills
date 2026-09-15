"""Peace (travel), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2cc0db6e-1e02-5564-9ad8-0cbb6bf60ced'
SOURCE_PATH = 'pictographic-primitives/travel/peace_2cc0db6e-1e02-5564-9ad8-0cbb6bf60ced.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Peace(Solo48):
    icon_id = 'peace'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'travel'
    aliases = ()
    keywords = ('peace', 'travel')

    def build(self):
        # Plan: exact integer circle attachments; split the receiving arcs at the real nodes.
        # Reference: circle geometry and the supplied subject.
        self.add_line('e0', (24, 44), (24, 23))
        self.add_line('e1', (24, 23), (12, 40))
        self.add_line('e2', (36, 40), (24, 23))
        self.add_line('e3', (24, 23), (24, 4))
        self.add_arc('e4-top', (4, 24), (44, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e4-bottom-node-0', (44, 24), (36, 40), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e4-bottom-node-1', (36, 40), (12, 40), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e4-bottom-node-2', (12, 40), (4, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_contour('c0', 'e0', 'e1', closed=False)
        self.add_contour('c1', 'e2', 'e3', closed=False)
        self.add_contour('e4', 'e4-top', 'e4-bottom-node-0', 'e4-bottom-node-1', 'e4-bottom-node-2', closed=True)
        self.relate('connect', 'c0', 'e4')
        self.relate('connect', 'c0', 'e4')
        self.relate('connect', 'c1', 'e4')
        self.relate('connect', 'c1', 'e4')
