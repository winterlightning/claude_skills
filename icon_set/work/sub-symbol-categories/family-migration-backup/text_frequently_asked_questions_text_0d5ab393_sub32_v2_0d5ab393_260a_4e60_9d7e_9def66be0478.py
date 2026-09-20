# Variant of text-frequently-asked-questions-text-0d5ab393-sub32; parent file remains unchanged.
"""Independent 32px profile of text-frequently-asked-questions-text-0d5ab393.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = '0d5ab393-260a-4e60-9d7e-9def66be0478'
SOURCE_PATH = 'icon_set/dist/text32/text-frequently-asked-questions-text-0d5ab393.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0d5ab393-260a-4e60-9d7e-9def66be0478', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/faq (text)_0d5ab393-260a-4e60-9d7e-9def66be0478.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-frequently-asked-questions-text-0d5ab393',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-f-uppercase', 'letter-a-uppercase', 'letter-q-uppercase')
REFERENCE_EXPORT_SHA256 = '93bea197e1b7530091de15fb2f7ad5f8b9dcf36d9a1e2005c5e79df419987788'

class DrawingVariant2(TextSub32):
    icon_id = 'text-frequently-asked-questions-text-0d5ab393-sub32-v2'
    variant_of = 'text-frequently-asked-questions-text-0d5ab393-sub32'
    variant_label = 'Record the actual joined strokes; preserve reviewed artwork'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 73
    text_ink_bounds = (0.0, 0.0, 73.0, 32.0)

    def build(self):
        self.add_arc('p1-r1-1', (51, 15), (69, 15), radius_x=9, radius_y=13, large_arc=True, sweep=True)
        self.add_arc('p1-r1-2', (69, 15), (51, 15), radius_x=9, radius_y=13, large_arc=True, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (63, 21), (71, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (25, 27), (33, 3))
        self.add_bezier('p3-r1-2', (33, 3), ((33.666666666666664, 2.3333333333333335), (34, 2), (34, 2)))
        self.add_bezier('p3-r1-3', (34, 2), ((34.666666666666664, 2), (35, 2.3333333333333335), (35, 3)))
        self.add_line('p3-r1-4', (35, 3), (44, 27))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (29, 16), (40, 16))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (17, 2), (2, 2))
        self.add_line('p5-r1-2', (2, 2), (2, 27))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.add_line('p6-r1-1', (2, 15), (15, 15))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.relate('connect', 'path-1-1', 'path-2-1')
