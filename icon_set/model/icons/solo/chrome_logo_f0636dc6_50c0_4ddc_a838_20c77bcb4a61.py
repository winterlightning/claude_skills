"""Chrome logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f0636dc6-50c0-4ddc-a838-20c77bcb4a61'
SOURCE_PATH = 'pictographic-primitives/logos/chrome logo_f0636dc6-50c0-4ddc-a838-20c77bcb4a61.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class ChromeLogo(Solo48):
    icon_id = 'chrome-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('chrome', 'logo', 'logos')

    def build(self):
        # Plan: exact integer circle attachments; split the receiving arcs at the real nodes.
        # Reference: circle geometry and the supplied subject.
        self.add_line('e0', (18, 19), (12, 8))
        self.add_line('e1', (19, 43), (24, 32))
        self.add_line('e2', (43, 19), (30, 19))
        self.add_arc('e3-top', (16, 24), (32, 24), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('e3-bottom-node-0', (32, 24), (24, 32), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('e3-bottom-node-1', (24, 32), (16, 24), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('e4-top-node-0', (4, 24), (12, 8), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e4-top-node-1', (12, 8), (44, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e4-bottom', (44, 24), (4, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_contour('c0', 'e0', closed=False)
        self.add_contour('c1', 'e1', closed=False)
        self.add_contour('c2', 'e2', closed=False)
        self.add_contour('e3', 'e3-top', 'e3-bottom-node-0', 'e3-bottom-node-1', closed=True)
        self.add_contour('e4', 'e4-top-node-0', 'e4-top-node-1', 'e4-bottom', closed=True)
        self.relate('connect', 'c0', 'e3')
        self.relate('connect', 'c0', 'e4')
        self.relate('connect', 'c1', 'e4')
        self.relate('connect', 'c1', 'e3')
        self.relate('connect', 'c2', 'e4')
        self.relate('connect', 'c2', 'e3')
