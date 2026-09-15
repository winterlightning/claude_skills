"""Controls stop (video), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '35a7506d-5335-584d-86b3-1dce1f10167e'
SOURCE_PATH = 'icons-json/video/controls stop_35a7506d-5335-584d-86b3-1dce1f10167e.json'
AUTHOR = 'gpt-6'

class ControlsStop(Solo48):
    icon_id = 'controls-stop'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video'
    aliases = ()
    keywords = ('controls', 'stop', 'video')

    def build(self):
        self.add_line('sym-e0', (24, 6), (40, 6))
        self.add_arc('sym-e2', (40, 6), (42, 8), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('sym-e5', (42, 8), (42, 40))
        self.add_arc('sym-e9', (42, 40), (40, 42), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('sym-e11', (40, 42), (8, 42))
        self.add_arc('sym-e14', (8, 42), (6, 40), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('sym-e17', (6, 40), (6, 8))
        self.add_arc('sym-e21', (6, 8), (8, 6), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('sym-e23', (8, 6), (24, 6))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e2', 'sym-e5', 'sym-e9', 'sym-e11', 'sym-e14', 'sym-e17', 'sym-e21', 'sym-e23', closed=True)
