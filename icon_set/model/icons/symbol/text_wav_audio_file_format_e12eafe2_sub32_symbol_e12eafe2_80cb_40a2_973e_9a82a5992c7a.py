"""Independent 32px profile of text-wav-audio-file-format-e12eafe2.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = 'e12eafe2-80cb-40a2-973e-9a82a5992c7a'
SOURCE_PATH = 'icon_set/dist/text32/text-wav-audio-file-format-e12eafe2.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e12eafe2-80cb-40a2-973e-9a82a5992c7a', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/wav (text)_e12eafe2-80cb-40a2-973e-9a82a5992c7a.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-wav-audio-file-format-e12eafe2',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-w-uppercase', 'letter-a-uppercase', 'letter-v-uppercase')
REFERENCE_EXPORT_SHA256 = '7be1a01e833f348505ed56546b20882a0a63278c6a96d2a1b44fe8d28039a297'

class DrawingContainerSymbol(TextSub32):
    icon_id = 'text-wav-audio-file-format-e12eafe2-sub32-symbol'
    related_origin_icon_id = 'text-wav-audio-file-format-e12eafe2-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/text-wav-audio-file-format-e12eafe2-sub32'
    counterpart_icon_id = 'text-wav-audio-file-format-e12eafe2-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 91
    text_ink_bounds = (0.0, 0.0, 91.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (68, 2), (77, 28))
        self.add_bezier('p1-r1-2', (77, 28), ((77.66666666666667, 29.333333333333332), (78.33333333333333, 30), (79, 30)))
        self.add_bezier('p1-r1-3', (79, 30), ((79.66666666666667, 30), (80, 29.333333333333332), (80, 28)))
        self.add_line('p1-r1-4', (80, 28), (89, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (39, 30), (49, 3))
        self.add_bezier('p2-r1-2', (49, 3), ((49, 2.3333333333333335), (49.333333333333336, 2), (50, 2)))
        self.add_bezier('p2-r1-3', (50, 2), ((50, 2), (50.333333333333336, 2.3333333333333335), (51, 3)))
        self.add_line('p2-r1-4', (51, 3), (60, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (44, 18), (56, 18))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 2), (8, 28))
        self.add_bezier('p4-r1-2', (8, 28), ((8.666666666666666, 29.333333333333332), (9, 30), (9, 30)))
        self.add_bezier('p4-r1-3', (9, 30), ((9, 30), (9.333333333333334, 29.333333333333332), (10, 28)))
        self.add_line('p4-r1-4', (10, 28), (16, 4))
        self.add_bezier('p4-r1-5', (16, 4), ((16, 3.3333333333333335), (16.333333333333332, 3), (17, 3)))
        self.add_bezier('p4-r1-6', (17, 3), ((17, 3), (17.333333333333332, 3.3333333333333335), (18, 4)))
        self.add_line('p4-r1-7', (18, 4), (24, 28))
        self.add_bezier('p4-r1-8', (24, 28), ((24, 29.333333333333332), (24.333333333333332, 30), (25, 30)))
        self.add_bezier('p4-r1-9', (25, 30), ((25, 30), (25, 29.333333333333332), (25, 28)))
        self.add_line('p4-r1-10', (25, 28), (32, 2))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', 'p4-r1-6', 'p4-r1-7', 'p4-r1-8', 'p4-r1-9', 'p4-r1-10', closed=False)
