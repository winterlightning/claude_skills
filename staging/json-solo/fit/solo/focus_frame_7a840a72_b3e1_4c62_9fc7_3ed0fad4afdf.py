"""Focus frame (photography), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7a840a72-b3e1-4c62-9fc7-3ed0fad4afdf'
SOURCE_PATH = 'icons-json/photography/focus frame_7a840a72-b3e1-4c62-9fc7-3ed0fad4afdf.json'
AUTHOR = 'json_to_solo'

class FocusFramePhotography(Solo48):
    icon_id = 'focus-frame-photography'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'photography'
    aliases = ()
    keywords = ('focus', 'frame', 'photography')

    def build(self):
        self.add_line('sym-e0', (12, 8), (6, 8))
        self.add_arc('sym-e1', (6, 8), (4, 10), radius_x=2, sweep=False)
        self.add_line('sym-e2', (4, 10), (4, 24))
        self.add_line('sym-e3', (4, 24), (4, 38))
        self.add_arc('sym-e4', (4, 38), (6, 40), radius_x=2, sweep=False)
        self.add_line('sym-e5', (6, 40), (12, 40))
        self.add_line('sym-e6', (36, 8), (42, 8))
        self.add_line('sym-e7', (42, 8), (43, 8))
        self.add_arc('sym-e8', (43, 8), (44, 10), radius_x=3, sweep=False)
        self.add_line('sym-e9', (44, 10), (44, 24))
        self.add_line('sym-e10', (44, 24), (44, 38))
        self.add_arc('sym-e11', (44, 38), (43, 40), radius_x=3, sweep=False)
        self.add_line('sym-e12', (43, 40), (42, 40))
        self.add_line('sym-e13', (42, 40), (36, 40))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5')
        self.add_contour('sym-c1', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13')
