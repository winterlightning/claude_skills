# Independent container symbol; edit separately from linked side sub-icon.
"""Independent 32px profile of text-m4v-video-format-5082511a.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = '5082511a-c4d5-4f3c-be72-f61c5ef1ad0b'
SOURCE_PATH = 'icon_set/dist/text32/text-m4v-video-format-5082511a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5082511a-c4d5-4f3c-be72-f61c5ef1ad0b', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/m4v (text)_5082511a-c4d5-4f3c-be72-f61c5ef1ad0b.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-m4v-video-format-5082511a',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-m-uppercase', 'digit-4', 'letter-v-uppercase')
REFERENCE_EXPORT_SHA256 = '069c20df116ae6d18553b913782c86f903b46af8dedc6b189d8024f302245ede'

class DrawingContainerSymbol(TextSub32):
    icon_id = 'text-m4v-video-format-5082511a-sub32-symbol'
    variant_of = 'text-m4v-video-format-5082511a-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/text-m4v-video-format-5082511a-sub32'
    counterpart_icon_id = 'text-m4v-video-format-5082511a-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 91
    text_ink_bounds = (0.0, 0.0, 91.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (68, 2), (77, 28))
        self.add_bezier('p1-r1-2', (77, 28), ((77.66666666666667, 29.333333333333332), (78, 30), (78, 30)))
        self.add_bezier('p1-r1-3', (78, 30), ((78.66666666666667, 30), (79.33333333333333, 29.333333333333332), (80, 28)))
        self.add_line('p1-r1-4', (80, 28), (89, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (36, 2), (36, 20))
        self.add_bezier('p2-r1-2', (36, 20), ((36, 20), (37, 20), (37, 20)))
        self.add_line('p2-r1-3', (37, 20), (60, 20))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (55, 2), (55, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 30), (2, 2))
        self.add_line('p4-r1-2', (2, 2), (15, 20))
        self.add_line('p4-r1-3', (15, 20), (28, 2))
        self.add_line('p4-r1-4', (28, 2), (28, 30))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
