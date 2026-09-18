"""Independent 32px profile of side-text-ef2194cc.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'ef2194cc-7bad-4582-aa73-5f86c985b28b'
SOURCE_PATH = 'icon_set/dist/text32/side-text-ef2194cc.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ef2194cc-7bad-4582-aa73-5f86c985b28b', 'icon_set/dist/gallery/combination-originals/ef2194cc-7bad-4582-aa73-5f86c985b28b.svg'),)
PROFILE_SOURCE_KEYS = ('text/side-text-ef2194cc',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-u-uppercase', 'letter-v-uppercase')
REFERENCE_EXPORT_SHA256 = 'c00906fe433a3807bea147a281cefae6a77b3422ce7931c00136c03fc198442d'

class Drawing(TextSub32):
    icon_id = 'side-text-ef2194cc-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 52
    text_ink_bounds = (0.0, 0.0, 52.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (29, 2), (38, 28))
        self.add_bezier('p1-r1-2', (38, 28), ((38.666666666666664, 29.333333333333332), (39.333333333333336, 30), (40, 30)))
        self.add_bezier('p1-r1-3', (40, 30), ((40.666666666666664, 30), (41, 29.333333333333332), (41, 28)))
        self.add_line('p1-r1-4', (41, 28), (50, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (2, 2), (2, 20))
        self.add_bezier('p2-r1-2', (2, 20), ((2, 27), (7, 30), (12, 30)))
        self.add_bezier('p2-r1-3', (12, 30), ((17, 30), (22, 27), (22, 20)))
        self.add_line('p2-r1-4', (22, 20), (22, 2))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
