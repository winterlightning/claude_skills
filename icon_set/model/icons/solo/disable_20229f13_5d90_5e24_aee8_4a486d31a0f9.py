"""Disable (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '20229f13-5d90-5e24-aee8-4a486d31a0f9'
SOURCE_PATH = 'pictographic-primitives/interface-essential/disable_20229f13-5d90-5e24-aee8-4a486d31a0f9.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Disable(Solo48):
    icon_id = 'disable'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('disable', 'interface-essential')

    def build(self):
        # Plan: exact integer circle attachments; split the receiving arcs at the real nodes.
        # Reference: circle geometry and the supplied subject.
        self.add_line('e0', (36, 8), (12, 40))
        self.add_arc('e1-top-node-0', (4, 24), (36, 8), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e1-top-node-1', (36, 8), (44, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e1-bottom-node-0', (44, 24), (12, 40), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e1-bottom-node-1', (12, 40), (4, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_contour('c0', 'e0', closed=False)
        self.add_contour('e1', 'e1-top-node-0', 'e1-top-node-1', 'e1-bottom-node-0', 'e1-bottom-node-1', closed=True)
        self.relate('connect', 'c0', 'e1')
        self.relate('connect', 'c0', 'e1')
