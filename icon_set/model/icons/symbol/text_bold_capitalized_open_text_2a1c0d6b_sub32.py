"""Independent 32px profile of text-bold-capitalized-open-text-2a1c0d6b.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '2a1c0d6b-91c3-4bcc-9330-99a425f9b10b'
SOURCE_PATH = 'icon_set/dist/text32/text-bold-capitalized-open-text-2a1c0d6b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2a1c0d6b-91c3-4bcc-9330-99a425f9b10b', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/open (text)_2a1c0d6b-91c3-4bcc-9330-99a425f9b10b.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-bold-capitalized-open-text-2a1c0d6b',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-o-uppercase', 'letter-p-uppercase', 'letter-e-uppercase', 'letter-n-uppercase')
REFERENCE_EXPORT_SHA256 = '8af484f64c79108fc87721adbb83587e220ba53d815d9492aa293a2a7d2a91f0'

class Drawing(TextSub32):
    icon_id = 'text-bold-capitalized-open-text-2a1c0d6b-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 105
    text_ink_bounds = (0.0, 0.0, 105.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (82, 30), (82, 2))
        self.add_line('p1-r1-2', (82, 2), (103, 30))
        self.add_line('p1-r1-3', (103, 30), (103, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (74, 2), (57, 2))
        self.add_line('p2-r1-2', (57, 2), (57, 30))
        self.add_line('p2-r1-3', (57, 30), (74, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (57, 16), (71, 16))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (30, 30), (30, 2))
        self.add_line('p4-r1-2', (30, 2), (40, 2))
        self.add_bezier('p4-r1-3', (40, 2), ((46, 2), (50, 6), (50, 9)))
        self.add_bezier('p4-r1-4', (50, 9), ((50, 13), (46, 17), (40, 17)))
        self.add_line('p4-r1-5', (40, 17), (30, 17))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', closed=False)
        self.add_arc('p5-r1-1', (2, 16), (22, 16), radius_x=10, radius_y=14, large_arc=True, sweep=True)
        self.add_arc('p5-r1-2', (22, 16), (2, 16), radius_x=10, radius_y=14, large_arc=True, sweep=True)
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
