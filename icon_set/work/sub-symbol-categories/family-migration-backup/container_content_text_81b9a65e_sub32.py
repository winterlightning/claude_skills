"""Independent 32px profile of container-content-text-81b9a65e.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = None
SOURCE_PATH = 'icon_set/dist/text44/container-content-text-81b9a65e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = ()
PROFILE_SOURCE_KEYS = ('text/container-content-text-81b9a65e',)
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '867946dfcd260a21239ee63e777b67132715dd4f279262d206438167be3b335c'

class Drawing(TextSub32):
    icon_id = 'container-content-text-81b9a65e-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 15
    text_ink_bounds = (0.0, 0.0, 15.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (4, 30), (11, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (2, 7), (13, 7))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (7, 2), (7, 13))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
