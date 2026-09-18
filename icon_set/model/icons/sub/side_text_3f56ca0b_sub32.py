"""Independent 32px profile of side-text-3f56ca0b.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '3f56ca0b-8416-402d-aabd-eff420b147d9'
SOURCE_PATH = 'icon_set/dist/text32/side-text-3f56ca0b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3f56ca0b-8416-402d-aabd-eff420b147d9', 'icon_set/dist/gallery/combination-originals/3f56ca0b-8416-402d-aabd-eff420b147d9.svg'),)
PROFILE_SOURCE_KEYS = ('text/side-text-3f56ca0b',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-3', 'letter-d-uppercase', 'letter-s-uppercase')
REFERENCE_EXPORT_SHA256 = '9c45702055ac1889aa1603544ffcc1050a961b0ec0775c9c5b0a9f68e38eba43'

class Drawing(TextSub32):
    icon_id = 'side-text-3f56ca0b-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 74
    text_ink_bounds = (0.0, 0.0, 74.0, 32.0)

    def build(self):
        self.add_bezier('p1-r1-1', (72, 6), ((71, 3), (67, 2), (64, 2)))
        self.add_bezier('p1-r1-2', (64, 2), ((60, 2), (56, 4), (55, 9)))
        self.add_bezier('p1-r1-3', (55, 9), ((55, 9), (55, 9), (55, 10)))
        self.add_bezier('p1-r1-4', (55, 10), ((55, 17), (72, 13), (72, 22)))
        self.add_bezier('p1-r1-5', (72, 22), ((72, 22), (72, 22), (72, 23)))
        self.add_bezier('p1-r1-6', (72, 23), ((72, 28), (68, 30), (63, 30)))
        self.add_bezier('p1-r1-7', (63, 30), ((59, 30), (56, 29), (54, 26)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_line('p2-r1-1', (27, 2), (35, 2))
        self.add_bezier('p2-r1-2', (35, 2), ((43, 2), (47, 9), (47, 16)))
        self.add_bezier('p2-r1-3', (47, 16), ((47, 23), (43, 30), (35, 30)))
        self.add_line('p2-r1-4', (35, 30), (27, 30))
        self.add_line('p2-r1-5', (27, 30), (27, 2))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_line('p3-r1-1', (2, 2), (13, 2))
        self.add_bezier('p3-r1-2', (13, 2), ((17, 2), (20, 5), (20, 9)))
        self.add_bezier('p3-r1-3', (20, 9), ((20, 13), (17, 16), (13, 16)))
        self.add_line('p3-r1-4', (13, 16), (9, 16))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (10, 16), (13, 16))
        self.add_bezier('p4-r1-2', (13, 16), ((17, 16), (20, 19), (20, 23)))
        self.add_bezier('p4-r1-3', (20, 23), ((20, 27), (17, 30), (13, 30)))
        self.add_line('p4-r1-4', (13, 30), (2, 30))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
        self.relate("connect", 'p3-r1-3', 'p4-r1-1')
        self.relate("connect", 'p3-r1-3', 'p4-r1-2')
        self.relate("connect", 'p3-r1-4', 'p4-r1-1')
        self.relate("connect", 'p3-r1-4', 'p4-r1-2')
