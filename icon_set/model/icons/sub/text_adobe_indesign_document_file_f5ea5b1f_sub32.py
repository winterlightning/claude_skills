"""Independent 32px profile of text-adobe-indesign-document-file-f5ea5b1f.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'f5ea5b1f-a0c0-4aab-b396-16942d8b27ce'
SOURCE_PATH = 'icon_set/dist/text32/text-adobe-indesign-document-file-f5ea5b1f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f5ea5b1f-a0c0-4aab-b396-16942d8b27ce', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/indd (text)_f5ea5b1f-a0c0-4aab-b396-16942d8b27ce.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-adobe-indesign-document-file-f5ea5b1f',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-i-uppercase', 'letter-n-uppercase', 'letter-d-uppercase', 'letter-d-uppercase')
REFERENCE_EXPORT_SHA256 = '0ca1b4a0da39e8dc6429562113bd3b4d61d82e7a7c5a550d0c3f80e3bce97dec'































TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'text-adobe-indesign-document-file-f5ea5b1f-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 92
    text_canvas_height = 20
    text_ink_bounds = (2.0, 0.0, 90.00000000000003, 20.0)

    def build(self):
        """Source-native uppercase composition for 'INDD'; 4-unit letter spacing."""
        self.add_line('p1-r1-1', (16, 18), (4, 18))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (16, 2), (4, 2))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (10, 2), (10, 18))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (27, 18), (27, 2.21987))
        self.add_bezier('p4-r1-2', (27, 2.21987), ((27, 1.97187), (27.77876, 1.91394), (27.95982, 2.14847)))
        self.add_line('p4-r1-3', (27.95982, 2.14847), (40.0402, 17.7968))
        self.add_bezier('p4-r1-4', (40.0402, 17.7968), ((40.221199999999996, 18.0313), (41, 17.9734), (41, 17.7254)))
        self.add_line('p4-r1-5', (41, 17.7254), (41, 2.02527))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', closed=False)
        self.add_line('p5-r1-1', (52, 2), (56.88681, 2))
        self.add_bezier('p5-r1-2', (56.88681, 2), ((60.8153, 2), (64, 5.58172), (64, 10)))
        self.add_bezier('p5-r1-3', (64, 10), ((64, 14.4183), (60.8153, 18), (56.88681, 18)))
        self.add_line('p5-r1-4', (56.88681, 18), (52, 18))
        self.add_line('p5-r1-5', (52, 18), (52, 2))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', 'p5-r1-5', closed=False)
        self.add_line('p6-r1-1', (76, 2), (80.88681, 2))
        self.add_bezier('p6-r1-2', (80.88681, 2), ((84.81530000000001, 2), (88, 5.58172), (88, 10)))
        self.add_bezier('p6-r1-3', (88, 10), ((88, 14.4183), (84.81530000000001, 18), (80.88681, 18)))
        self.add_line('p6-r1-4', (80.88681, 18), (76, 18))
        self.add_line('p6-r1-5', (76, 18), (76, 2))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', 'p6-r1-3', 'p6-r1-4', 'p6-r1-5', closed=False)
        self.relate("connect", 'path-1-1', 'path-2-1')
        self.relate("connect", 'path-1-1', 'path-3-1')
        self.relate("connect", 'path-2-1', 'path-3-1')
