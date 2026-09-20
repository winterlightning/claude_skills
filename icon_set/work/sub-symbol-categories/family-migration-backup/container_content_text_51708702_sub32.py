"""Independent 32px profile of container-content-text-51708702.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = None
SOURCE_PATH = 'icon_set/dist/text44/container-content-text-51708702.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = ()
PROFILE_SOURCE_KEYS = ('text/container-content-text-51708702',)
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '9966bd1f2b343fc5a42f51e3527659add148a19781cbf913df71d807e67b3099'

class Drawing(TextSub32):
    icon_id = 'container-content-text-51708702-sub32'
    keyshape = Keyshape.HRECT_S
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    STROKE_WIDTH = 32  # Proportional dot-only text: its cap is the entire glyph.
    text_canvas_width = 256
    text_ink_bounds = (0, 0, 256, 32)

    def build(self):
        self.add_line('p1-r1-1', (16, 16), (16, 16))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (128, 16), (128, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (240, 16), (240, 16))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
