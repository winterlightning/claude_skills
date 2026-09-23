"""Independent 32px profile of text-flv-video-file-format-e3a73450.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'e3a73450-19cc-4412-8089-8b72325dc6cb'
SOURCE_PATH = 'icon_set/dist/text32/text-flv-video-file-format-e3a73450.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e3a73450-19cc-4412-8089-8b72325dc6cb', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/flv (text)_e3a73450-19cc-4412-8089-8b72325dc6cb.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-flv-video-file-format-e3a73450',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-f-uppercase', 'letter-l-uppercase', 'letter-v-uppercase')
REFERENCE_EXPORT_SHA256 = '8b329b99f5d5c777967a665dca5e754da1c8060940178d80f98888d6170bbf61'

























TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'text-flv-video-file-format-e3a73450-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 68
    text_canvas_height = 20
    text_ink_bounds = (2.2099599999999997, -1.3322676295501878e-15, 66.9998, 20.0024)

    def build(self):
        """Source-native uppercase composition for 'FLV'; 4-unit letter spacing."""
        self.add_line('p1-r1-1', (4.21094, 10.4907), (14.2337, 10.4907))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (4.20996, 18.0024), (4.20996, 2.3249))
        self.add_bezier('p2-r1-2', (4.20996, 2.3249), ((4.20996, 2.14546), (4.35542, 2), (4.53486, 2)))
        self.add_line('p2-r1-3', (4.53486, 2), (16.21, 2))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_bezier('p3-r1-1', (39, 18), ((35.9428, 18), (28.23973, 18), (28, 18)))
        self.add_line('p3-r1-2', (28, 18), (28, 2))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_bezier('p4-r1-1', (56.55127, 16.7027), ((56.704660000000004, 17.0778), (56.871719999999996, 17.3883), (57.04542, 17.617)))
        self.add_bezier('p4-r1-2', (57.04542, 17.617), ((57.20183, 17.7576), (57.44708, 17.8964), (57.70229, 17.9762)))
        self.add_bezier('p4-r1-3', (57.70229, 17.9762), ((57.95375, 18.0094), (58.137299999999996, 18.0049), (58.2933, 17.9853)))
        self.add_bezier('p4-r1-4', (58.2933, 17.9853), ((58.5154, 17.9252), (58.727000000000004, 17.828), (58.9257, 17.6775)))
        self.add_bezier('p4-r1-5', (58.9257, 17.6775), ((59.072, 17.5137), (59.1652, 17.3721), (59.2973, 17.1142)))
        self.add_line('p4-r1-6', (59.2973, 17.1142), (59.6865, 16.1038))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', 'p4-r1-6', closed=False)
        self.add_line('p5-r1-1', (51, 2.02786), (56.552080000000004, 16.7029))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (59.6865, 16.1039), (64.9998, 2.00055))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.relate("connect", 'path-1-1', 'path-2-1')
        self.relate("connect", 'path-4-1', 'path-5-1')
        self.relate("connect", 'path-4-1', 'path-6-1')
        self.relate("connect", 'path-5-1', 'path-6-1')
