"""Independent 32px profile of text-html-text-label-149e1bb4.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '149e1bb4-7caa-4573-92e8-c2528ea99ca1'
SOURCE_PATH = 'icon_set/dist/text32/text-html-text-label-149e1bb4.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('149e1bb4-7caa-4573-92e8-c2528ea99ca1', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/html (text)_149e1bb4-7caa-4573-92e8-c2528ea99ca1.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-html-text-label-149e1bb4',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-h-uppercase', 'letter-t-uppercase', 'letter-m-uppercase', 'letter-l-uppercase')
REFERENCE_EXPORT_SHA256 = 'd477a4a303d3b7100be7fbe03fe31251250ddd398c07604e20ed3d5fc8ec735b'

























TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'text-html-text-label-149e1bb4-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 92
    text_canvas_height = 20
    text_ink_bounds = (2.0, -1.9539862061712654e-06, 89.0, 20.0)

    def build(self):
        """Source-native uppercase composition for 'HTML'; 4-unit letter spacing."""
        self.add_line('p1-r1-1', (15.9998, 10), (4, 10))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (16, 18), (15.9998, 2))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p2-r2-1', (4.00021, 18), (4, 2))
        self.add_contour('path-2-2', 'p2-r2-1', closed=False)
        self.add_line('p3-r1-1', (28, 2), (40, 2))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (34, 18), (34.0064, 2))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (50, 18), (50, 2.4248))
        self.add_bezier('p5-r1-2', (50, 2.4248), ((50, 2.01632), (50.53474, 1.84408), (50.78474, 2.17204)))
        self.add_line('p5-r1-3', (50.78474, 2.17204), (57.65053, 11.1787))
        self.add_bezier('p5-r1-4', (57.65053, 11.1787), ((57.82456, 11.407), (58.175399999999996, 11.407), (58.3495, 11.1787)))
        self.add_line('p5-r1-5', (58.3495, 11.1787), (65.2153, 2.17204))
        self.add_bezier('p5-r1-6', (65.2153, 2.17204), ((65.4653, 1.84408), (66, 2.01632), (66, 2.4248)))
        self.add_line('p5-r1-7', (66, 2.4248), (66, 18))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', 'p5-r1-5', 'p5-r1-6', 'p5-r1-7', closed=False)
        self.add_bezier('p6-r1-1', (87, 18), ((83.9428, 18), (76.23973, 18), (76, 18)))
        self.add_line('p6-r1-2', (76, 18), (76, 2))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', closed=False)
        self.relate("connect", 'path-1-1', 'path-2-1')
        self.relate("connect", 'path-3-1', 'path-4-1')
