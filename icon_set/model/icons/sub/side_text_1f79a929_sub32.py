"""Independent 32px profile of side-text-1f79a929.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '1f79a929-e6ab-47a9-8cee-07a575e91e9b'
SOURCE_PATH = 'icon_set/dist/text32/side-text-1f79a929.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1f79a929-e6ab-47a9-8cee-07a575e91e9b', 'icon_set/dist/gallery/combination-originals/1f79a929-e6ab-47a9-8cee-07a575e91e9b.svg'),)
PROFILE_SOURCE_KEYS = ('text/side-text-1f79a929',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-x-uppercase', 'letter-l-uppercase', 'letter-s-uppercase', 'letter-x-uppercase')
REFERENCE_EXPORT_SHA256 = 'ae861910b73bbf7ad951530799c19ff5dbd5d45829f79a669b87ff56346149e6'

class Drawing(TextSub32):
    icon_id = 'side-text-1f79a929-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 101
    text_ink_bounds = (0.0, 0.0, 101.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (79, 2), (99, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (99, 2), (79, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_bezier('p3-r1-1', (71, 6), ((70, 3), (66, 2), (63, 2)))
        self.add_bezier('p3-r1-2', (63, 2), ((59, 2), (55, 4), (54, 9)))
        self.add_bezier('p3-r1-3', (54, 9), ((54, 9), (54, 9), (54, 10)))
        self.add_bezier('p3-r1-4', (54, 10), ((54, 17), (71, 13), (71, 22)))
        self.add_bezier('p3-r1-5', (71, 22), ((71, 22), (71, 22), (71, 23)))
        self.add_bezier('p3-r1-6', (71, 23), ((71, 28), (67, 30), (62, 30)))
        self.add_bezier('p3-r1-7', (62, 30), ((58, 30), (55, 29), (53, 26)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', closed=False)
        self.add_line('p4-r1-1', (29, 2), (29, 30))
        self.add_line('p4-r1-2', (29, 30), (46, 30))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (2, 2), (22, 30))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (22, 2), (2, 30))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
