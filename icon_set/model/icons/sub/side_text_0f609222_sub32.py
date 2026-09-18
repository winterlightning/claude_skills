"""Independent 32px profile of side-text-0f609222.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '0f609222-6b88-41ee-98b6-46d2a4e33966'
SOURCE_PATH = 'icon_set/dist/text32/side-text-0f609222.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0f609222-6b88-41ee-98b6-46d2a4e33966', 'icon_set/dist/gallery/combination-originals/0f609222-6b88-41ee-98b6-46d2a4e33966.svg'),)
PROFILE_SOURCE_KEYS = ('text/side-text-0f609222',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-x-uppercase', 'digit-2')
REFERENCE_EXPORT_SHA256 = 'b5248ecc99e96c79c0645b015e0b236c156cdcee483f12f59884fe82598500b8'

class Drawing(TextSub32):
    icon_id = 'side-text-0f609222-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 51
    text_ink_bounds = (0.0, 0.0, 51.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (29, 2), (43, 2))
        self.add_bezier('p1-r1-2', (43, 2), ((47, 2), (49, 5), (49, 8)))
        self.add_bezier('p1-r1-3', (49, 8), ((49, 9), (48, 11), (47, 12)))
        self.add_line('p1-r1-4', (47, 12), (33, 21))
        self.add_bezier('p1-r1-5', (33, 21), ((31, 23), (29, 25), (29, 28)))
        self.add_line('p1-r1-6', (29, 28), (29, 29))
        self.add_bezier('p1-r1-7', (29, 29), ((29, 29), (30, 30), (31, 30)))
        self.add_line('p1-r1-8', (31, 30), (49, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (2, 2), (22, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (22, 2), (2, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
