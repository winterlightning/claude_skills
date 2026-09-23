"""Independent 32px profile of text-wav-audio-file-format-e12eafe2.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = 'e12eafe2-80cb-40a2-973e-9a82a5992c7a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/wav (text)_e12eafe2-80cb-40a2-973e-9a82a5992c7a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e12eafe2-80cb-40a2-973e-9a82a5992c7a', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/wav (text)_e12eafe2-80cb-40a2-973e-9a82a5992c7a.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-wav-audio-file-format-e12eafe2',)
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '7be1a01e833f348505ed56546b20882a0a63278c6a96d2a1b44fe8d28039a297'

TYPEFACE_GLYPH_IDS = ('letter-w-uppercase', 'letter-a-uppercase', 'letter-v-uppercase')
























TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class DrawingVariant3(TextSub32):
    icon_id = 'text-wav-audio-file-format-e12eafe2-sub32-v3'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 68
    text_canvas_height = 20
    text_ink_bounds = (0.0004900000000001015, 0.0, 66.9998, 20.000587807857475)

    def build(self):
        """Source-native uppercase composition for 'WAV'; 4-unit letter spacing."""
        self.add_line('p1-r1-1', (18.0005, 2.00052), (13.6033, 18.0005))
        self.add_line('p1-r1-2', (13.6033, 18.0005), (10.5005, 8.28623))
        self.add_line('p1-r1-3', (10.5005, 8.28623), (6.83221, 18.0005))
        self.add_line('p1-r1-4', (6.83221, 18.0005), (2.00049, 2.00052))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_bezier('p2-r1-1', (28, 18), ((28, 18), (29.26667, 2), (34.1333, 2)))
        self.add_bezier('p2-r1-2', (34.1333, 2), ((39, 2), (40, 18), (40, 18)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p2-r2-1', (28.49782, 13.9921), (39.5709, 14.0032))
        self.add_contour('path-2-2', 'p2-r2-1', closed=False)
        self.add_bezier('p3-r1-1', (56.55127, 16.7027), ((56.704660000000004, 17.0778), (56.871719999999996, 17.3883), (57.04542, 17.617)))
        self.add_bezier('p3-r1-2', (57.04542, 17.617), ((57.20183, 17.7576), (57.44708, 17.8964), (57.70229, 17.9762)))
        self.add_bezier('p3-r1-3', (57.70229, 17.9762), ((57.95375, 18.0094), (58.137299999999996, 18.0049), (58.2933, 17.9853)))
        self.add_bezier('p3-r1-4', (58.2933, 17.9853), ((58.5154, 17.9252), (58.727000000000004, 17.828), (58.9257, 17.6775)))
        self.add_bezier('p3-r1-5', (58.9257, 17.6775), ((59.072, 17.5137), (59.1652, 17.3721), (59.2973, 17.1142)))
        self.add_line('p3-r1-6', (59.2973, 17.1142), (59.6865, 16.1038))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', closed=False)
        self.add_line('p4-r1-1', (51, 2.02786), (56.552080000000004, 16.7029))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (59.6865, 16.1039), (64.9998, 2.00055))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate("connect", 'path-3-1', 'path-4-1')
        self.relate("connect", 'path-3-1', 'path-5-1')
        self.relate("connect", 'path-4-1', 'path-5-1')
