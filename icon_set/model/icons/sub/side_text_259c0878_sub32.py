"""Independent 32px profile of side-text-259c0878.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '259c0878-528e-42fb-8d9f-56fe04a84b03'
SOURCE_PATH = 'icon_set/dist/text32/side-text-259c0878.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('259c0878-528e-42fb-8d9f-56fe04a84b03', 'icon_set/dist/gallery/combination-originals/259c0878-528e-42fb-8d9f-56fe04a84b03.svg'),)
PROFILE_SOURCE_KEYS = ('text/side-text-259c0878',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-c-uppercase', 'digit-5')
REFERENCE_EXPORT_SHA256 = '7d73023e55ea0339c8806a39d5a0673a19066453881a7bcd0ab8904f4e188d50'

class Drawing(TextSub32):
    icon_id = 'side-text-259c0878-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 48
    text_ink_bounds = (0.001457877762348403, 0.0, 48.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (44, 2), (27, 2))
        self.add_bezier('p1-r1-2', (27, 2), ((27, 2), (26, 2), (26, 3)))
        self.add_line('p1-r1-3', (26, 3), (26, 13))
        self.add_bezier('p1-r1-4', (26, 13), ((26, 13), (27, 14), (27, 14)))
        self.add_line('p1-r1-5', (27, 14), (38, 14))
        self.add_bezier('p1-r1-6', (38, 14), ((43, 14), (46, 18), (46, 22)))
        self.add_bezier('p1-r1-7', (46, 22), ((46, 24), (45, 26), (44, 28)))
        self.add_bezier('p1-r1-8', (44, 28), ((42, 29), (40, 30), (38, 30)))
        self.add_line('p1-r1-9', (38, 30), (27, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', closed=False)
        self.add_arc('p2-r1-1', (19, 6), (19, 26), radius_x=10, radius_y=14, large_arc=True, sweep=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
