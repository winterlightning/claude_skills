"""Independent 32px profile of container-content-text-1469716c.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = None
SOURCE_PATH = 'icon_set/dist/text44/container-content-text-1469716c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = ()
PROFILE_SOURCE_KEYS = ('text/container-content-text-1469716c',)
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = 'cb2079a7be26c40747eb209de1b28b13cfb2d96858520110ca73ea5cb7dfc5b8'

class Drawing(TextSub32):
    icon_id = 'container-content-text-1469716c-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 35
    text_ink_bounds = (0.0, 0.0, 35.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (33, 2), (16, 2))
        self.add_line('p1-r1-2', (16, 2), (16, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (16, 16), (30, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_arc('p3-r1-1', (2, 5), (8, 5), radius_x=3, radius_y=3, large_arc=True, sweep=True)
        self.add_arc('p3-r1-2', (8, 5), (2, 5), radius_x=3, radius_y=3, large_arc=True, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
