"""Independent 32px profile of text-automatic-camera-flash-6d9d5bd7.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = None
SOURCE_PATH = 'icon_set/dist/text28/text-automatic-camera-flash-6d9d5bd7.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = ()
PROFILE_SOURCE_KEYS = ('text/text-automatic-camera-flash-6d9d5bd7',)
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = 'c19c4b587346a7b131934b964f7acec0d9fabe6d0045c59f63c559f21bedfb90'

class Drawing(TextSub32):
    icon_id = 'text-automatic-camera-flash-6d9d5bd7-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 51
    text_ink_bounds = (0.0, 0.0, 51.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (28, 30), (37, 3))
        self.add_bezier('p1-r1-2', (37, 3), ((37.666666666666664, 2.3333333333333335), (38, 2), (38, 2)))
        self.add_bezier('p1-r1-3', (38, 2), ((38.666666666666664, 2), (39, 2.3333333333333335), (39, 3)))
        self.add_line('p1-r1-4', (39, 3), (49, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (32, 18), (44, 18))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (17, 2), (2, 18))
        self.add_line('p3-r1-2', (2, 18), (15, 18))
        self.add_line('p3-r1-3', (15, 18), (8, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
