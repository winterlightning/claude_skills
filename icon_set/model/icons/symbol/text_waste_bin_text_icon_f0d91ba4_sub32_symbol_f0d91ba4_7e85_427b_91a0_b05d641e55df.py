"""Independent 32px profile of text-waste-bin-text-icon-f0d91ba4.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = 'f0d91ba4-7e85-427b-91a0-b05d641e55df'
SOURCE_PATH = 'icon_set/dist/text32/text-waste-bin-text-icon-f0d91ba4.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f0d91ba4-7e85-427b-91a0-b05d641e55df', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/bin (text)_f0d91ba4-7e85-427b-91a0-b05d641e55df.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-waste-bin-text-icon-f0d91ba4',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-b-uppercase', 'letter-i-uppercase', 'letter-n-uppercase')
REFERENCE_EXPORT_SHA256 = 'b49debb925037d1415269d911dcbc9dea0724ca23ce992e0707b3c794bd8de3b'

class DrawingContainerSymbol(TextSub32):
    icon_id = 'text-waste-bin-text-icon-f0d91ba4-sub32-symbol'
    related_origin_icon_id = 'text-waste-bin-text-icon-f0d91ba4-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/text-waste-bin-text-icon-f0d91ba4-sub32'
    counterpart_icon_id = 'text-waste-bin-text-icon-f0d91ba4-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 68
    text_ink_bounds = (0.0, 0.0, 68.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (46, 30), (46, 2))
        self.add_line('p1-r1-2', (46, 2), (66, 30))
        self.add_line('p1-r1-3', (66, 30), (66, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (29, 2), (38, 2))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (33, 2), (33, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (29, 30), (38, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (2, 30), (2, 2))
        self.add_line('p5-r1-2', (2, 2), (11, 2))
        self.add_bezier('p5-r1-3', (11, 2), ((17, 2), (20, 6), (20, 9)))
        self.add_bezier('p5-r1-4', (20, 9), ((20, 12), (17, 16), (11, 16)))
        self.add_line('p5-r1-5', (11, 16), (2, 16))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', 'p5-r1-5', closed=False)
        self.add_bezier('p6-r1-1', (11, 16), ((18, 16), (21, 20), (21, 23)))
        self.add_bezier('p6-r1-2', (21, 23), ((21, 26), (18, 30), (11, 30)))
        self.add_line('p6-r1-3', (11, 30), (2, 30))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', 'p6-r1-3', closed=False)
        self.relate('connect', 'p5-r1-1', 'p6-r1-3')
        self.relate('connect', 'p5-r1-4', 'p6-r1-1')
        self.relate('connect', 'p5-r1-5', 'p6-r1-1')
