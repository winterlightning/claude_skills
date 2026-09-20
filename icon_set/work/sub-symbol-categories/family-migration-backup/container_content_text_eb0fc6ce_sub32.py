"""Independent 32px profile of container-content-text-eb0fc6ce.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = None
SOURCE_PATH = 'icon_set/dist/text44/container-content-text-eb0fc6ce.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = ()
PROFILE_SOURCE_KEYS = ('text/container-content-text-eb0fc6ce',)
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '5940da061a1f64db3909173731bbb04a3496b9afe0272591fa14c286ce796609'

class Drawing(TextSub32):
    icon_id = 'container-content-text-eb0fc6ce-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 22
    text_ink_bounds = (0.0, 0.0, 22.0, 32.0)

    def build(self):
        self.add_bezier('p1-r1-1', (2, 9), ((2, 4), (6, 2), (11, 2)))
        self.add_bezier('p1-r1-2', (11, 2), ((15, 2), (20, 4), (20, 9)))
        self.add_bezier('p1-r1-3', (20, 9), ((20, 16), (11, 16), (11, 22)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (11, 30), (11, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
