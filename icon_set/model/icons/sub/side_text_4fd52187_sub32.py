"""Independent 32px profile of side-text-4fd52187.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '4fd52187-1c97-4d8d-8d4a-93db88e7190c'
SOURCE_PATH = 'icon_set/dist/text32/side-text-4fd52187.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4fd52187-1c97-4d8d-8d4a-93db88e7190c', 'icon_set/dist/gallery/combination-originals/4fd52187-1c97-4d8d-8d4a-93db88e7190c.svg'),)
PROFILE_SOURCE_KEYS = ('text/side-text-4fd52187',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-0', 'symbol-percent')
REFERENCE_EXPORT_SHA256 = 'd4fb5af9e3e61ada488adc671a16034c63a8c62efdb9df0d630ada62ed80e35c'

class Drawing(TextSub32):
    icon_id = 'side-text-4fd52187-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 54
    text_ink_bounds = (0.0, 0.0, 53.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (31, 30), (51, 2))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_bezier('p2-r1-1', (31, 7), ((31, 4), (33, 2), (35, 2)))
        self.add_bezier('p2-r1-2', (35, 2), ((37, 2), (39, 4), (39, 7)))
        self.add_bezier('p2-r1-3', (39, 7), ((39, 10), (37, 13), (35, 13)))
        self.add_bezier('p2-r1-4', (35, 13), ((33, 13), (31, 10), (31, 7)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_bezier('p3-r1-1', (43, 25), ((43, 22), (45, 19), (47, 19)))
        self.add_bezier('p3-r1-2', (47, 19), ((49, 19), (51, 22), (51, 25)))
        self.add_bezier('p3-r1-3', (51, 25), ((51, 28), (49, 30), (47, 30)))
        self.add_bezier('p3-r1-4', (47, 30), ((45, 30), (43, 28), (43, 25)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_bezier('p4-r1-1', (2, 11), ((2, 7), (6, 3), (11, 3)))
        self.add_bezier('p4-r1-2', (11, 3), ((17, 3), (21, 7), (21, 11)))
        self.add_line('p4-r1-3', (21, 11), (21, 22))
        self.add_bezier('p4-r1-4', (21, 22), ((21, 27), (17, 30), (11, 30)))
        self.add_bezier('p4-r1-5', (11, 30), ((6, 30), (2, 27), (2, 22)))
        self.add_line('p4-r1-6', (2, 22), (2, 11))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', 'p4-r1-6', closed=False)
