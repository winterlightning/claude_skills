"""Independent 32px profile of text-dxf-file-format-symbol-ef7bb64f.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'ef7bb64f-2ca6-4de8-80aa-37d95ecbe745'
SOURCE_PATH = 'icon_set/dist/text32/text-dxf-file-format-symbol-ef7bb64f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ef7bb64f-2ca6-4de8-80aa-37d95ecbe745', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/dxf (text)_ef7bb64f-2ca6-4de8-80aa-37d95ecbe745.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-dxf-file-format-symbol-ef7bb64f',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-d-uppercase', 'letter-x-uppercase', 'letter-f-uppercase')
REFERENCE_EXPORT_SHA256 = '2645e115a3138228491aa650a5f1adc89dab9ef8c9887e264aa973b68e9626fa'

























TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'text-dxf-file-format-symbol-ef7bb64f-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 68
    text_canvas_height = 20
    text_ink_bounds = (2.0, -1.3322676295501878e-15, 66.21000000000001, 20.0024)

    def build(self):
        """Source-native uppercase composition for 'DXF'; 4-unit letter spacing."""
        self.add_line('p1-r1-1', (4, 2), (8.88681, 2))
        self.add_bezier('p1-r1-2', (8.88681, 2), ((12.8153, 2), (16, 5.58172), (16, 10)))
        self.add_bezier('p1-r1-3', (16, 10), ((16, 14.4183), (12.8153, 18), (8.88681, 18)))
        self.add_line('p1-r1-4', (8.88681, 18), (4, 18))
        self.add_line('p1-r1-5', (4, 18), (4, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (27, 2.00003), (41, 17.9909))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (27.02295, 18), (40.9638, 2.04587))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (52.21094, 10.4907), (62.2337, 10.4907))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (52.20996, 18.0024), (52.20996, 2.3249))
        self.add_bezier('p5-r1-2', (52.20996, 2.3249), ((52.20996, 2.14546), (52.35542, 2), (52.53486, 2)))
        self.add_line('p5-r1-3', (52.53486, 2), (64.21000000000001, 2))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', closed=False)
        self.relate("connect", 'path-2-1', 'path-3-1')
        self.relate("connect", 'path-4-1', 'path-5-1')
