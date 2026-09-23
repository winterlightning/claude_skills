"""V2 typeface composition for Emergency 911 Number."""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '53668ec4-a104-4d57-8154-81e216c068e3'
SOURCE_PATH = 'published/gallery/combination-originals/53668ec4-a104-4d57-8154-81e216c068e3.svg'
AUTHOR = 'codex'
SOURCE_REFERENCES = (('53668ec4-a104-4d57-8154-81e216c068e3', 'published/gallery/combination-originals/53668ec4-a104-4d57-8154-81e216c068e3.svg'),)
PROFILE_SOURCE_KEYS = ('text/side-text-53668ec4',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-9', 'digit-1', 'digit-1')


REFERENCE_EXPORT_SHA256 = 'e09cedbab9c18256817ef26410d1f26d42380ccf6038a14d2a990edb53661299'






















TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'text-emergency-911-number-53668ec4-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 68
    text_canvas_height = 20
    text_ink_bounds = (2.0, 0.0, 66.0, 20.00000000000001)

    def build(self):
        """Source-native uppercase composition for '911'; 4-unit letter spacing."""
        self.add_line('p1-r1-1', (16.0005, 6.72498), (16.0005, 13.1172))
        self.add_bezier('p1-r1-2', (16.0005, 13.1172), ((16.0005, 15.8139), (13.8144, 18), (11.1177, 18)))
        self.add_line('p1-r1-3', (11.1177, 18), (5.62988, 18))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_arc('p2-r1-1', (4, 6.80433), (16, 6.80433), radius_x=6, radius_y=4.80433, large_arc=True, sweep=False)
        self.add_arc('p2-r1-2', (16, 6.80433), (4, 6.80433), radius_x=6, radius_y=4.80433, large_arc=True, sweep=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (34.4, 18), (34.4, 2.40859))
        self.add_bezier('p3-r1-2', (34.4, 2.40859), ((34.4, 2.18293), (34.2171, 2), (33.99141, 2)))
        self.add_line('p3-r1-3', (33.99141, 2), (28, 2))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_line('p3-r2-1', (28.85714, 18), (40, 18))
        self.add_contour('path-3-2', 'p3-r2-1', closed=False)
        self.add_line('p4-r1-1', (58.4, 18), (58.4, 2.40859))
        self.add_bezier('p4-r1-2', (58.4, 2.40859), ((58.4, 2.18293), (58.2171, 2), (57.99141, 2)))
        self.add_line('p4-r1-3', (57.99141, 2), (52, 2))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', closed=False)
        self.add_line('p4-r2-1', (52.85714, 18), (64, 18))
        self.add_contour('path-4-2', 'p4-r2-1', closed=False)
        self.relate("connect", 'path-1-1', 'path-2-1')
