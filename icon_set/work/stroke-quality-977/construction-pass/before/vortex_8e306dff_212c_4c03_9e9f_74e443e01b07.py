"""Vortex (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8e306dff-212c-4c03-9e9f-74e443e01b07'
SOURCE_PATH = 'pictographic-primitives/symbol/vortex_8e306dff-212c-4c03-9e9f-74e443e01b07.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Vortex(Solo48):
    icon_id = 'vortex'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('vortex', 'symbol')

    def build(self):
        self.add_line('sym-e0', (8, 4), (21, 40))
        self.add_arc('sym-e1', (21, 40), (24, 44), radius_x=4, sweep=False)
        self.add_arc('sym-e2', (24, 44), (27, 40), radius_x=4, sweep=False)
        self.add_line('sym-e3', (27, 40), (40, 4))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3')
