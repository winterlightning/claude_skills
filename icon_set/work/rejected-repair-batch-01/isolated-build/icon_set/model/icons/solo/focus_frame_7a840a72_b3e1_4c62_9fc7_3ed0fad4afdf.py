"""Focus frame (photography), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7a840a72-b3e1-4c62-9fc7-3ed0fad4afdf'
SOURCE_PATH = 'pictographic-primitives/photography/focus frame_7a840a72-b3e1-4c62-9fc7-3ed0fad4afdf.svg'
AUTHOR = 'gpt-6'

class FocusFrame(Solo48):
    icon_id = 'focus-frame'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'photography'
    aliases = ()
    keywords = ('focus', 'frame', 'photography')

    def build(self):
        self.add_line('sym-e0', (12, 8), (6, 8))
        self.add_arc('sym-e1', (6, 8), (4, 10), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('sym-e2', (4, 10), (4, 38))
        self.add_arc('sym-e4', (4, 38), (6, 40), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('sym-e5', (6, 40), (12, 40))
        self.add_line('sym-e6', (36, 8), (43, 8))
        self.add_arc('sym-e8', (43, 8), (44, 10), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('sym-e9', (44, 10), (44, 38))
        self.add_arc('sym-e11', (44, 38), (43, 40), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('sym-e12', (43, 40), (36, 40))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e4', 'sym-e5', closed=False)
        self.add_contour('sym-c1', 'sym-e6', 'sym-e8', 'sym-e9', 'sym-e11', 'sym-e12', closed=False)
