"""Independent 32px profile of text-gif-file-format-icon-3d3b075e.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '3d3b075e-c8d1-4ff5-82d7-2b5904b06c7d'
SOURCE_PATH = 'icon_set/dist/text32/text-gif-file-format-icon-3d3b075e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3d3b075e-c8d1-4ff5-82d7-2b5904b06c7d', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/gif (text)_3d3b075e-c8d1-4ff5-82d7-2b5904b06c7d.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-gif-file-format-icon-3d3b075e',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-g-uppercase', 'letter-i-uppercase', 'letter-f-uppercase')
REFERENCE_EXPORT_SHA256 = 'eccc894f9f66c7b38cbdad8993491e94f30ca4890b1cb0183a63f7070b56c38f'

























TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'text-gif-file-format-icon-3d3b075e-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 68
    text_canvas_height = 20
    text_ink_bounds = (0.0, -1.3322676295501878e-15, 66.21000000000001, 20.0024)

    def build(self):
        """Source-native uppercase composition for 'GIF'; 4-unit letter spacing."""
        self.add_bezier('p1-r1-1', (14.8699, 3.51954), ((13.5334, 2.56364), (11.8896, 2), (10.1123, 2)))
        self.add_bezier('p1-r1-2', (10.1123, 2), ((5.63199, 2), (2, 5.58172), (2, 10)))
        self.add_bezier('p1-r1-3', (2, 10), ((2, 14.4183), (5.63199, 18), (10.1123, 18)))
        self.add_bezier('p1-r1-4', (10.1123, 18), ((14.3736, 18), (17.6686, 14.5166), (18, 10.3983)))
        self.add_line('p1-r1-5', (18, 10.3983), (11.9716, 10.3983))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (40, 18), (28, 18))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (40, 2), (28, 2))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (34, 2), (34, 18))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (52.21094, 10.4907), (62.2337, 10.4907))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (52.20996, 18.0024), (52.20996, 2.3249))
        self.add_bezier('p6-r1-2', (52.20996, 2.3249), ((52.20996, 2.14546), (52.35542, 2), (52.53486, 2)))
        self.add_line('p6-r1-3', (52.53486, 2), (64.21000000000001, 2))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', 'p6-r1-3', closed=False)
        self.relate("connect", 'path-2-1', 'path-3-1')
        self.relate("connect", 'path-2-1', 'path-4-1')
        self.relate("connect", 'path-3-1', 'path-4-1')
        self.relate("connect", 'path-5-1', 'path-6-1')
