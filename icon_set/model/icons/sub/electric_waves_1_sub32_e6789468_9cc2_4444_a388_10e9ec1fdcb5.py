"""Independent 32px profile of electric-waves-1.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'e6789468-9cc2-4444-a388-10e9ec1fdcb5'
SOURCE_PATH = 'pictographic-primitives/state/electric waves 1_e6789468-9cc2-4444-a388-10e9ec1fdcb5.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e6789468-9cc2-4444-a388-10e9ec1fdcb5', 'pictographic-primitives/state/electric waves 1_e6789468-9cc2-4444-a388-10e9ec1fdcb5.svg'),)
PROFILE_SOURCE_KEYS = ('solo/electric-waves-1',)
SOLO_SOURCE_ICON_IDS = ('electric-waves-1',)
REFERENCE_EXPORT_SHA256 = '881a581a00a906eed54f90344ffc38c3a3805d31f6febfbd161e6e588a59eda0'

class Drawing(Sub32):
    icon_id = 'electric-waves-1-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (2, 12), ((6, 8), (11, 5), (16, 5)))
        self.add_bezier('p1-r1-2', (16, 5), ((21, 5), (26, 8), (30, 12)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_bezier('p2-r1-1', (8, 19), ((10, 16), (13, 15), (16, 15)))
        self.add_bezier('p2-r1-2', (16, 15), ((19, 15), (22, 16), (24, 19)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (16, 27), (16, 27))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
