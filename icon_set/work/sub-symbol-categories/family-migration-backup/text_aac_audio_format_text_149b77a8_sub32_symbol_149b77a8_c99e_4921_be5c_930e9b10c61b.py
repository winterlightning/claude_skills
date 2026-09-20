# Independent container symbol; edit separately from linked side sub-icon.
"""Independent 32px profile of text-aac-audio-format-text-149b77a8.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = '149b77a8-c99e-4921-be5c-930e9b10c61b'
SOURCE_PATH = 'icon_set/dist/text32/text-aac-audio-format-text-149b77a8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('149b77a8-c99e-4921-be5c-930e9b10c61b', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/acc (text)_149b77a8-c99e-4921-be5c-930e9b10c61b.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-aac-audio-format-text-149b77a8',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-a-uppercase', 'letter-a-uppercase', 'letter-c-uppercase')
REFERENCE_EXPORT_SHA256 = '5f83298b2b9a9115a4f5a4d97d61792d4634c8ee29e9e59bdafc5956630e624b'

class DrawingContainerSymbol(TextSub32):
    icon_id = 'text-aac-audio-format-text-149b77a8-sub32-symbol'
    variant_of = 'text-aac-audio-format-text-149b77a8-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/text-aac-audio-format-text-149b77a8-sub32'
    counterpart_icon_id = 'text-aac-audio-format-text-149b77a8-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 79
    text_ink_bounds = (0.0, 0.0, 79.0, 32.0)

    def build(self):
        self.add_arc('p1-r1-1', (77, 6), (77, 26), radius_x=10, radius_y=14, large_arc=True, sweep=False)
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (31, 30), (40, 3))
        self.add_bezier('p2-r1-2', (40, 3), ((40.666666666666664, 2.3333333333333335), (41, 2), (41, 2)))
        self.add_bezier('p2-r1-3', (41, 2), ((41.666666666666664, 2), (42, 2.3333333333333335), (42, 3)))
        self.add_line('p2-r1-4', (42, 3), (52, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (35, 18), (48, 18))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 30), (11, 3))
        self.add_bezier('p4-r1-2', (11, 3), ((11.666666666666666, 2.3333333333333335), (12, 2), (12, 2)))
        self.add_bezier('p4-r1-3', (12, 2), ((12.666666666666666, 2), (13.333333333333334, 2.3333333333333335), (14, 3)))
        self.add_line('p4-r1-4', (14, 3), (23, 30))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
        self.add_line('p5-r1-1', (6, 18), (19, 18))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
