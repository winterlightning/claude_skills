"""Earth (maps), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '862e1938-ba92-42a6-be54-909eda881f11'
SOURCE_PATH = 'pictographic-primitives/maps/earth_862e1938-ba92-42a6-be54-909eda881f11.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class EarthMaps(Solo48):
    icon_id = 'earth-maps'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'maps'
    aliases = ()
    keywords = ('earth', 'maps')

    def build(self):
        # Plan: exact integer ellipse attachments; split the receiving arcs at the real nodes.
        # Reference: circle geometry and the supplied subject.
        self.add_arc('e0-top-node-0', (4, 24), (8, 12), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e0-top-node-1', (8, 12), (36, 8), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e0-top-node-2', (36, 8), (44, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e0-bottom-node-0', (44, 24), (12, 40), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e0-bottom-node-1', (12, 40), (4, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e1-1', (12, 40), (21, 28), radius_x=9, radius_y=9, large_arc=False, sweep=False)
        self.add_line('e1-2', (21, 28), (15, 26))
        self.add_arc('e1-3', (15, 26), (13, 24), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('e1-4', (13, 24), (15, 16))
        self.add_arc('e1-5', (15, 16), (8, 12), radius_x=10, radius_y=10, large_arc=False, sweep=False)
        self.add_arc('e2-1', (43, 29), (34, 27), radius_x=16, radius_y=16, large_arc=False, sweep=True)
        self.add_line('e2-2', (34, 27), (33, 22))
        self.add_line('e2-3', (33, 22), (27, 18))
        self.add_arc('e2-4', (27, 18), (27, 15), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('e2-5', (27, 15), (36, 8), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_contour('c0', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', closed=False)
        self.add_contour('c1', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', closed=False)
        self.add_contour('e0', 'e0-top-node-0', 'e0-top-node-1', 'e0-top-node-2', 'e0-bottom-node-0', 'e0-bottom-node-1', closed=True)
        self.relate('connect', 'c0', 'e0')
        self.relate('connect', 'c0', 'e0')
        self.relate('connect', 'c1', 'e0')
        self.relate('connect', 'c1', 'e0')
