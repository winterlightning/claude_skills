"""Independent 32px profile of text-aif-text-icon-160d4fd7.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '160d4fd7-2412-44db-98f1-535785768595'
SOURCE_PATH = 'icon_set/dist/text32/text-aif-text-icon-160d4fd7.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('160d4fd7-2412-44db-98f1-535785768595', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/AIF (text)_160d4fd7-2412-44db-98f1-535785768595.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-aif-text-icon-160d4fd7',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-a-uppercase', 'letter-i-uppercase', 'letter-f-uppercase')
REFERENCE_EXPORT_SHA256 = 'e8bb5fc497e00f39957c1239ff8c4f2ff4135dcb63c560eb53c485a38a10a791'































TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'text-aif-text-icon-160d4fd7-sub32'
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
        """Source-native uppercase composition for 'AIF'; 4-unit letter spacing."""
        self.add_bezier('p1-r1-1', (4, 18), ((4, 18), (5.26667, 2), (10.1333, 2)))
        self.add_bezier('p1-r1-2', (10.1333, 2), ((15, 2), (16, 18), (16, 18)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p1-r2-1', (4.49782, 13.9921), (15.5709, 14.0032))
        self.add_contour('path-1-2', 'p1-r2-1', closed=False)
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
