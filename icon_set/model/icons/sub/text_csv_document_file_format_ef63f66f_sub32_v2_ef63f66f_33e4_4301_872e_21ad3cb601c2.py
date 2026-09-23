"""Independent 32px profile of text-csv-document-file-format-ef63f66f.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = 'ef63f66f-33e4-4301-872e-21ad3cb601c2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/dist/text32/text-csv-document-file-format-ef63f66f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ef63f66f-33e4-4301-872e-21ad3cb601c2', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/CSV (text)_ef63f66f-33e4-4301-872e-21ad3cb601c2.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-csv-document-file-format-ef63f66f',)
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '472712d2f4953bd4249facf4d238de99cc84129ab0ee66a6601ffa68d56e4458'

TYPEFACE_GLYPH_IDS = ('letter-c-uppercase', 'letter-s-uppercase', 'letter-v-uppercase')
























TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class DrawingVariant2(TextSub32):
    icon_id = 'text-csv-document-file-format-ef63f66f-sub32-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 68
    text_canvas_height = 20
    text_ink_bounds = (2.0, 0.0, 66.9998, 20.000587807857475)

    def build(self):
        """Source-native uppercase composition for 'CSV'; 4-unit letter spacing."""
        self.add_bezier('p1-r1-1', (16, 2.6879), ((14.9406, 2.24575), (13.7674, 2), (12.533, 2)))
        self.add_bezier('p1-r1-2', (12.533, 2), ((7.82037, 2), (4, 5.58172), (4, 10)))
        self.add_bezier('p1-r1-3', (4, 10), ((4, 14.4183), (7.82037, 18), (12.533, 18)))
        self.add_bezier('p1-r1-4', (12.533, 18), ((13.7674, 18), (14.9406, 17.7543), (16, 17.3121)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (39.9314, 2), (32.77906, 2))
        self.add_bezier('p2-r1-2', (32.77906, 2), ((27.70172, 2), (26.21029, 7.42857), (30.98284, 9.42857)))
        self.add_line('p2-r1-3', (30.98284, 9.42857), (37.4623, 11.608))
        self.add_bezier('p2-r1-4', (37.4623, 11.608), ((41.7211, 13.4286), (40.2526, 18), (35.7787, 18)))
        self.add_line('p2-r1-5', (35.7787, 18), (28, 18))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
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
