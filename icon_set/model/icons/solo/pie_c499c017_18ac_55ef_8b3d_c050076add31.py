"""Pie (food), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c499c017-18ac-55ef-8b3d-c050076add31'
SOURCE_PATH = 'pictographic-primitives/food/pie_c499c017-18ac-55ef-8b3d-c050076add31.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class PieFood(Solo48):
    icon_id = 'pie-food'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('pie', 'food')

    def build(self):
        # Plan: exact integer circle attachments; split the receiving arcs at the real nodes.
        # Reference: circle geometry and the supplied subject.
        self.add_line('e0', (36, 40), (26, 25))
        self.add_line('e1', (24, 23), (24, 4))
        self.add_arc('e2-top', (4, 24), (44, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e2-bottom-node-0', (44, 24), (36, 40), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e2-bottom-node-1', (36, 40), (4, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_line('e3', (26, 25), (24, 23))
        self.add_contour('c0', 'e0', 'e3', 'e1', closed=False)
        self.add_contour('e2', 'e2-top', 'e2-bottom-node-0', 'e2-bottom-node-1', closed=True)
        self.relate('connect', 'c0', 'e2')
        self.relate('connect', 'c0', 'e2')
