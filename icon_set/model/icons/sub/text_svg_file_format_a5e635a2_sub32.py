"""Independent 32px profile of text-svg-file-format-a5e635a2.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'a5e635a2-0920-48ba-9eea-82070fddd821'
SOURCE_PATH = 'icon_set/dist/text32/text-svg-file-format-a5e635a2.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a5e635a2-0920-48ba-9eea-82070fddd821', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/svg (text)_a5e635a2-0920-48ba-9eea-82070fddd821.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-svg-file-format-a5e635a2',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-s-uppercase', 'letter-v-uppercase', 'letter-g-uppercase')
REFERENCE_EXPORT_SHA256 = 'f1bb94f357763ace7bcdbe94200623c2015c83fcadb116bb76879ee6a55981e4'

























TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'text-svg-file-format-a5e635a2-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 68
    text_canvas_height = 20
    text_ink_bounds = (2.0, 0.0, 68.00000000000009, 20.000587807857475)

    def build(self):
        """Source-native uppercase composition for 'SVG'; 4-unit letter spacing."""
        self.add_line('p1-r1-1', (15.9314, 2), (8.77906, 2))
        self.add_bezier('p1-r1-2', (8.77906, 2), ((3.70172, 2), (2.21029, 7.42857), (6.98284, 9.42857)))
        self.add_line('p1-r1-3', (6.98284, 9.42857), (13.4623, 11.608))
        self.add_bezier('p1-r1-4', (13.4623, 11.608), ((17.7211, 13.4286), (16.2526, 18), (11.7787, 18)))
        self.add_line('p1-r1-5', (11.7787, 18), (4, 18))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_bezier('p2-r1-1', (32.55127, 16.7027), ((32.704660000000004, 17.0778), (32.871719999999996, 17.3883), (33.04542, 17.617)))
        self.add_bezier('p2-r1-2', (33.04542, 17.617), ((33.20183, 17.7576), (33.44708, 17.8964), (33.70229, 17.9762)))
        self.add_bezier('p2-r1-3', (33.70229, 17.9762), ((33.95375, 18.0094), (34.137299999999996, 18.0049), (34.2933, 17.9853)))
        self.add_bezier('p2-r1-4', (34.2933, 17.9853), ((34.5154, 17.9252), (34.727000000000004, 17.828), (34.9257, 17.6775)))
        self.add_bezier('p2-r1-5', (34.9257, 17.6775), ((35.072, 17.5137), (35.1652, 17.3721), (35.2973, 17.1142)))
        self.add_line('p2-r1-6', (35.2973, 17.1142), (35.6865, 16.1038))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', closed=False)
        self.add_line('p3-r1-1', (27, 2.02786), (32.552080000000004, 16.7029))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (35.6865, 16.1039), (40.9998, 2.00055))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_bezier('p5-r1-1', (62.8699, 3.51954), ((61.5334, 2.56364), (59.8896, 2), (58.1123, 2)))
        self.add_bezier('p5-r1-2', (58.1123, 2), ((53.63199, 2), (50, 5.58172), (50, 10)))
        self.add_bezier('p5-r1-3', (50, 10), ((50, 14.4183), (53.63199, 18), (58.1123, 18)))
        self.add_bezier('p5-r1-4', (58.1123, 18), ((62.373599999999996, 18), (65.6686, 14.5166), (66, 10.3983)))
        self.add_line('p5-r1-5', (66, 10.3983), (59.9716, 10.3983))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', 'p5-r1-5', closed=False)
        self.relate("connect", 'path-2-1', 'path-3-1')
        self.relate("connect", 'path-2-1', 'path-4-1')
        self.relate("connect", 'path-3-1', 'path-4-1')
