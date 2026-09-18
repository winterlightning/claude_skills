"""Independent 32px profile of side-text-2f9175d4.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '2f9175d4-638c-4619-a72b-95215338f0fe'
SOURCE_PATH = 'icon_set/dist/text32/side-text-2f9175d4.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2f9175d4-638c-4619-a72b-95215338f0fe', 'icon_set/dist/gallery/combination-originals/2f9175d4-638c-4619-a72b-95215338f0fe.svg'),)
PROFILE_SOURCE_KEYS = ('text/side-text-2f9175d4',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-d-uppercase', 'letter-m-uppercase', 'letter-g-uppercase')
REFERENCE_EXPORT_SHA256 = 'adb7e4d166946b87707aa822887d74dcf80bbba2a590158f23df2d78ac84a72e'

class Drawing(TextSub32):
    icon_id = 'side-text-2f9175d4-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 85
    text_ink_bounds = (0.0, 0.0, 85.0, 32.0)

    def build(self):
        self.add_bezier('p1-r1-1', (80, 6), ((78, 4), (75, 2), (73, 2)))
        self.add_bezier('p1-r1-2', (73, 2), ((68, 2), (62, 9), (62, 17)))
        self.add_bezier('p1-r1-3', (62, 17), ((62, 18), (63, 20), (63, 21)))
        self.add_bezier('p1-r1-4', (63, 21), ((65, 27), (68, 29), (72, 29)))
        self.add_bezier('p1-r1-5', (72, 29), ((77, 29), (83, 24), (83, 16)))
        self.add_line('p1-r1-6', (83, 16), (75, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (29, 30), (29, 2))
        self.add_line('p2-r1-2', (29, 2), (42, 20))
        self.add_line('p2-r1-3', (42, 20), (55, 2))
        self.add_line('p2-r1-4', (55, 2), (55, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (2, 2), (10, 2))
        self.add_bezier('p3-r1-2', (10, 2), ((18, 2), (21, 9), (21, 16)))
        self.add_bezier('p3-r1-3', (21, 16), ((21, 23), (18, 30), (10, 30)))
        self.add_line('p3-r1-4', (10, 30), (2, 30))
        self.add_line('p3-r1-5', (2, 30), (2, 2))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
