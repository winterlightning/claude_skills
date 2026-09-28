"""Cluster (programing), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'db5443e9-3ef0-5724-b357-1ff8c8cb3b7b'
SOURCE_PATH = 'pictographic-primitives/programing/cluster_db5443e9-3ef0-5724-b357-1ff8c8cb3b7b.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Cluster(Solo48):
    icon_id = 'cluster'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    categories = ('programing', 'primitives')
    aliases = ()
    keywords = ('cluster', 'programing')

    def build(self):
        # Plan: exact integer circle attachments; split the receiving arcs at the real nodes.
        # Reference: circle geometry and the supplied subject.
        self.add_line('e0', (24, 20), (24, 27))
        self.add_line('e1', (24, 27), (16, 34))
        self.add_line('e2', (24, 27), (32, 34))
        self.add_arc('e3-top', (32, 34), (44, 34), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('e3-bottom', (44, 34), (32, 34), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('e4-top', (4, 34), (16, 34), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('e4-bottom', (16, 34), (4, 34), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('e5-top', (18, 14), (30, 14), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('e5-bottom', (30, 14), (18, 14), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_contour('c0', 'e0', closed=False)
        self.add_contour('c1', 'e1', closed=False)
        self.add_contour('c2', 'e2', closed=False)
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
        self.add_contour('e5', 'e5-top', 'e5-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'e5')
        self.relate('connect', 'c1', 'e4')
        self.relate('connect', 'c2', 'e3')
