"""Focus frame (photography), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('sym-e1', (6, 8), ((4.691, 8.62), (4.564, 8.55), (4, 10)))
        self.add_line('sym-e2', (4, 10), (4, 24))
        self.add_line('sym-e3', (4, 24), (4, 38))
        self.add_bezier('sym-e4', (4, 38), ((4.564, 39.45), (4.691, 39.38), (6, 40)))
        self.add_line('sym-e5', (6, 40), (12, 40))
        self.add_line('sym-e6', (36, 8), (42, 8))
        self.add_bezier('sym-e7', (42, 8), ((42.182, 8.11), (42.818, 8), (43, 8)))
        self.add_bezier('sym-e8', (43, 8), ((43.691, 8.47), (43.655, 9.27), (44, 10)))
        self.add_line('sym-e9', (44, 10), (44, 24))
        self.add_line('sym-e10', (44, 24), (44, 38))
        self.add_bezier('sym-e11', (44, 38), ((43.655, 38.73), (43.691, 39.53), (43, 40)))
        self.add_bezier('sym-e12', (43, 40), ((42.818, 40), (42.182, 39.89), (42, 40)))
        self.add_line('sym-e13', (42, 40), (36, 40))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5')
        self.add_contour('sym-c1', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13')
