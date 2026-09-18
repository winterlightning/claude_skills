"""Independent 32px profile of side-text-cc92659e.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'cc92659e-8528-43c1-b8cd-489fe1f8785e'
SOURCE_PATH = 'icon_set/dist/text32/side-text-cc92659e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('cc92659e-8528-43c1-b8cd-489fe1f8785e', 'icon_set/dist/gallery/combination-originals/cc92659e-8528-43c1-b8cd-489fe1f8785e.svg'),)
PROFILE_SOURCE_KEYS = ('text/side-text-cc92659e',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-a-uppercase', 'digit-3')
REFERENCE_EXPORT_SHA256 = 'e296819595145e337bc73ac4ede6fb8e9384ee5647971f256ba7e10ad5245696'

class Drawing(TextSub32):
    icon_id = 'side-text-cc92659e-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 50
    text_ink_bounds = (0.0, 0.0, 50.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (30, 2), (41, 2))
        self.add_bezier('p1-r1-2', (41, 2), ((45, 2), (48, 5), (48, 9)))
        self.add_bezier('p1-r1-3', (48, 9), ((48, 13), (45, 16), (41, 16)))
        self.add_line('p1-r1-4', (41, 16), (37, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (38, 16), (41, 16))
        self.add_bezier('p2-r1-2', (41, 16), ((45, 16), (48, 19), (48, 23)))
        self.add_bezier('p2-r1-3', (48, 23), ((48, 27), (45, 30), (41, 30)))
        self.add_line('p2-r1-4', (41, 30), (30, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (2, 30), (11, 3))
        self.add_bezier('p3-r1-2', (11, 3), ((11.666666666666666, 2.3333333333333335), (12, 2), (12, 2)))
        self.add_bezier('p3-r1-3', (12, 2), ((12.666666666666666, 2), (13.333333333333334, 2.3333333333333335), (14, 3)))
        self.add_line('p3-r1-4', (14, 3), (23, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (6, 18), (19, 18))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
        self.relate("connect", 'p1-r1-3', 'p2-r1-2')
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
        self.relate("connect", 'p1-r1-4', 'p2-r1-2')
