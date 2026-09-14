"""Slice (state), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a004a57a-6eea-490b-8683-cc169050a26a'
SOURCE_PATH = 'icons-json/state/slice_a004a57a-6eea-490b-8683-cc169050a26a.json'
AUTHOR = 'json_to_solo'

class SliceState(Solo48):
    icon_id = 'slice-state'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('slice', 'state')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('e1', (33, 19), ((33.355, 19.664), (33.836, 19.873), (34.073, 20.591)), ((35.436, 24.791), (33.264, 29.209), (30, 32)))
        self.add_bezier('e2', (21, 34), ((17.445, 32.945), (15.591, 31.327), (14, 28)))
        self.add_bezier('e3', (14, 19), ((16.036, 15.918), (18.309, 13.545), (22, 13)))
        self.add_contour('c0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
