"""Independent 32px profile of text-waste-bin-text-icon-f0d91ba4.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'f0d91ba4-7e85-427b-91a0-b05d641e55df'
SOURCE_PATH = 'icon_set/dist/text32/text-waste-bin-text-icon-f0d91ba4.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f0d91ba4-7e85-427b-91a0-b05d641e55df', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/bin (text)_f0d91ba4-7e85-427b-91a0-b05d641e55df.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-waste-bin-text-icon-f0d91ba4',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-b-uppercase', 'letter-i-uppercase', 'letter-n-uppercase')
REFERENCE_EXPORT_SHA256 = 'b49debb925037d1415269d911dcbc9dea0724ca23ce992e0707b3c794bd8de3b'

























TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'text-waste-bin-text-icon-f0d91ba4-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 68
    text_canvas_height = 20
    text_ink_bounds = (2.0, 0.0, 67.0, 20.000000000000007)

    def build(self):
        """Source-native uppercase composition for 'BIN'; 4-unit letter spacing."""
        self.add_line('p1-r1-1', (4, 2), (10.1362, 2))
        self.add_bezier('p1-r1-2', (10.1362, 2), ((12.3453, 2), (14.1362, 3.79086), (14.1362, 6)))
        self.add_bezier('p1-r1-3', (14.1362, 6), ((14.1362, 8.20914), (12.3453, 10), (10.1362, 10)))
        self.add_line('p1-r1-4', (10.1362, 10), (4, 10))
        self.add_line('p1-r1-5', (4, 10), (4, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (4, 10.0101), (12.005, 10.0101))
        self.add_bezier('p2-r1-2', (12.005, 10.0101), ((14.2114, 10.0101), (16, 11.7987), (16, 14.005)))
        self.add_bezier('p2-r1-3', (16, 14.005), ((16, 16.2114), (14.2114, 18), (12.005, 18)))
        self.add_line('p2-r1-4', (12.005, 18), (4, 18))
        self.add_line('p2-r1-5', (4, 18), (4, 10.0101))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_line('p3-r1-1', (40, 18), (28, 18))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (40, 2), (28, 2))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (34, 2), (34, 18))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (51, 18), (51, 2.21987))
        self.add_bezier('p6-r1-2', (51, 2.21987), ((51, 1.97187), (51.77876, 1.91394), (51.95982, 2.14847)))
        self.add_line('p6-r1-3', (51.95982, 2.14847), (64.0402, 17.7968))
        self.add_bezier('p6-r1-4', (64.0402, 17.7968), ((64.2212, 18.0313), (65, 17.9734), (65, 17.7254)))
        self.add_line('p6-r1-5', (65, 17.7254), (65, 2.02527))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', 'p6-r1-3', 'p6-r1-4', 'p6-r1-5', closed=False)
        self.relate("connect", 'path-1-1', 'path-2-1')
        self.relate("connect", 'path-3-1', 'path-4-1')
        self.relate("connect", 'path-3-1', 'path-5-1')
        self.relate("connect", 'path-4-1', 'path-5-1')
