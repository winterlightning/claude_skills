"""Science momentum (science), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '176d1a87-f7f0-5ee9-b933-4e9e4d66edaf'
SOURCE_PATH = 'pictographic-primitives/science/science momentum_176d1a87-f7f0-5ee9-b933-4e9e4d66edaf.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class ScienceMomentum(Solo48):
    icon_id = 'science-momentum'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'science'
    categories = ('science', 'primitives')
    aliases = ()
    keywords = ('science', 'momentum')

    def build(self):
        # Plan: exact integer circle attachments; split the receiving arcs at the real nodes.
        # Reference: circle geometry and the supplied subject.
        self.add_line('e0', (22, 24), (42, 6))
        self.add_line('e1', (42, 6), (35, 7))
        self.add_line('e2', (41, 13), (42, 6))
        self.add_arc('e3-top-node-0', (6, 32), (22, 24), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('e3-top-node-1', (22, 24), (26, 32), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('e3-bottom', (26, 32), (6, 32), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_contour('c0', 'e0', 'e1', closed=False)
        self.add_contour('c1', 'e2', closed=False)
        self.add_contour('e3', 'e3-top-node-0', 'e3-top-node-1', 'e3-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'e3')
