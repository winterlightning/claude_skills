"""Independent 32px profile of side-text-03f5123c.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '03f5123c-4121-4c9f-8ffb-3c6f68958ad0'
SOURCE_PATH = 'icon_set/dist/text32/side-text-03f5123c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('03f5123c-4121-4c9f-8ffb-3c6f68958ad0', 'icon_set/dist/gallery/combination-originals/03f5123c-4121-4c9f-8ffb-3c6f68958ad0.svg'),)
PROFILE_SOURCE_KEYS = ('text/side-text-03f5123c',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-a-uppercase', 'letter-i-uppercase')
REFERENCE_EXPORT_SHA256 = '842efe2e4d987c9b0d67ddf1b503236da2c6628f7a7b646d90a444bfb5068e8e'

class Drawing(TextSub32):
    icon_id = 'side-text-03f5123c-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 41
    text_ink_bounds = (0.0, 0.0, 41.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (30, 2), (39, 2))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (35, 2), (35, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (30, 30), (39, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 30), (11, 3))
        self.add_bezier('p4-r1-2', (11, 3), ((11.666666666666666, 2.3333333333333335), (12, 2), (12, 2)))
        self.add_bezier('p4-r1-3', (12, 2), ((12.666666666666666, 2), (13.333333333333334, 2.3333333333333335), (14, 3)))
        self.add_line('p4-r1-4', (14, 3), (23, 30))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
        self.add_line('p5-r1-1', (6, 18), (19, 18))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
