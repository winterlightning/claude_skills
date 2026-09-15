"""Sliced pie (business), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ffd66227-1225-4049-b2a4-f8abe7a156c5'
SOURCE_PATH = 'pictographic-primitives/business/sliced pie_ffd66227-1225-4049-b2a4-f8abe7a156c5.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class SlicedPie(Solo48):
    icon_id = 'sliced-pie'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('sliced', 'pie', 'business')

    def build(self):
        # Plan: exact integer circle attachments; split the receiving arcs at the real nodes.
        # Reference: circle geometry and the supplied subject.
        self.add_line('e0', (31, 24), (44, 24))
        self.add_line('e1', (12, 40), (19, 29))
        self.add_line('e2', (24, 17), (24, 4))
        self.add_arc('e3-top', (4, 24), (44, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e3-bottom-node-0', (44, 24), (12, 40), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e3-bottom-node-1', (12, 40), (4, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e4-top', (17, 24), (31, 24), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('e4-bottom', (31, 24), (17, 24), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_contour('c0', 'e0', closed=False)
        self.add_contour('c1', 'e1', closed=False)
        self.add_contour('c2', 'e2', closed=False)
        self.add_contour('e3', 'e3-top', 'e3-bottom-node-0', 'e3-bottom-node-1', closed=True)
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
        self.relate('connect', 'c0', 'e4')
        self.relate('connect', 'c0', 'e3')
        self.relate('connect', 'c1', 'e3')
        self.relate('connect', 'c1', 'e4')
        self.relate('connect', 'c2', 'e4')
        self.relate('connect', 'c2', 'e3')
