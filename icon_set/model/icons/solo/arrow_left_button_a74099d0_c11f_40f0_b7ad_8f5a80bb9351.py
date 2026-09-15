"""Arrow left button (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a74099d0-c11f-40f0-b7ad-8f5a80bb9351'
SOURCE_PATH = 'icons-json/symbol/arrow left button_a74099d0-c11f-40f0-b7ad-8f5a80bb9351.json'
AUTHOR = 'gpt-6'

class ArrowLeftButton(Solo48):
    icon_id = 'arrow-left-button'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('arrow', 'left', 'button', 'symbol')

    def build(self):
        self.add_arc('sym-e1', (8, 24), (10, 27), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('sym-e2', (10, 27), (27, 44))
        self.add_line('sym-e4', (27, 44), (40, 44))
        self.add_line('sym-e7', (40, 44), (21, 25))
        self.add_arc('sym-e8', (21, 25), (21, 24), radius_x=1, radius_y=1, large_arc=False, sweep=False)
        self.add_arc('sym-e9', (21, 24), (21, 23), radius_x=1, radius_y=1, large_arc=False, sweep=False)
        self.add_line('sym-e10', (21, 23), (40, 4))
        self.add_line('sym-e11', (40, 4), (27, 4))
        self.add_line('sym-e14', (27, 4), (10, 21))
        self.add_arc('sym-e16', (10, 21), (8, 24), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_contour('sym-c0', 'sym-e1', 'sym-e2', 'sym-e4', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e14', 'sym-e16', closed=True)
