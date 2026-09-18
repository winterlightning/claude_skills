"""Independent 32px profile of container-content-text-b6714fe0.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = None
SOURCE_PATH = 'icon_set/dist/text44/container-content-text-b6714fe0.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = ()
PROFILE_SOURCE_KEYS = ('text/container-content-text-b6714fe0',)
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '5cb9a9a974a4e8ca4e4d19866a5646b8e750951d97367d2e244bd5c6d9d474ec'

class Drawing(TextSub32):
    icon_id = 'container-content-text-b6714fe0-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 24
    text_ink_bounds = (0.0, 0.0, 24.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (22, 2))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_arc('p2-r1-1', (2, 7), (10, 7), radius_x=4, radius_y=5, large_arc=True, sweep=True)
        self.add_arc('p2-r1-2', (10, 7), (2, 7), radius_x=4, radius_y=5, large_arc=True, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_arc('p3-r1-1', (14, 25), (22, 25), radius_x=4, radius_y=5, large_arc=True, sweep=True)
        self.add_arc('p3-r1-2', (22, 25), (14, 25), radius_x=4, radius_y=5, large_arc=True, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
