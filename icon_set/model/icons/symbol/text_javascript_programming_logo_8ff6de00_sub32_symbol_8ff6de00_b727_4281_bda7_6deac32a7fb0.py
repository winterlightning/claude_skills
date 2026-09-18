"""Independent 32px profile of text-javascript-programming-logo-8ff6de00.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '8ff6de00-b727-4281-bda7-6deac32a7fb0'
SOURCE_PATH = 'icon_set/dist/text32/text-javascript-programming-logo-8ff6de00.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('8ff6de00-b727-4281-bda7-6deac32a7fb0', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/js (text)_8ff6de00-b727-4281-bda7-6deac32a7fb0.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-javascript-programming-logo-8ff6de00',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-j-uppercase', 'letter-s-uppercase')
REFERENCE_EXPORT_SHA256 = '5e0ecd4c3d314804827a566eddad5c2fd44e61ec535a2c7befd7c361e2261e4c'

class DrawingContainerSymbol(TextSub32):
    icon_id = 'text-javascript-programming-logo-8ff6de00-sub32-symbol'
    related_origin_icon_id = 'text-javascript-programming-logo-8ff6de00-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/text-javascript-programming-logo-8ff6de00-sub32'
    counterpart_icon_id = 'text-javascript-programming-logo-8ff6de00-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 46
    text_ink_bounds = (0.0, 0.0, 46.0, 32.0)

    def build(self):
        self.add_bezier('p1-r1-1', (43, 6), ((42, 3), (39, 2), (35, 2)))
        self.add_bezier('p1-r1-2', (35, 2), ((31, 2), (27, 4), (26, 9)))
        self.add_bezier('p1-r1-3', (26, 9), ((26, 9), (26, 9), (26, 10)))
        self.add_bezier('p1-r1-4', (26, 10), ((26, 17), (43, 13), (44, 22)))
        self.add_bezier('p1-r1-5', (44, 22), ((44, 22), (44, 22), (44, 23)))
        self.add_bezier('p1-r1-6', (44, 23), ((44, 28), (39, 30), (35, 30)))
        self.add_bezier('p1-r1-7', (35, 30), ((31, 30), (27, 29), (26, 26)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_line('p2-r1-1', (6, 2), (18, 2))
        self.add_line('p2-r1-2', (18, 2), (18, 21))
        self.add_bezier('p2-r1-3', (18, 21), ((18, 27), (14, 30), (9, 30)))
        self.add_bezier('p2-r1-4', (9, 30), ((6, 30), (3, 28), (2, 24)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
