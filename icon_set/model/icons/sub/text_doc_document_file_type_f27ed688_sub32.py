"""Independent 32px profile of text-doc-document-file-type-f27ed688.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'f27ed688-cc0b-4a36-83e6-2b70c6de0e5c'
SOURCE_PATH = 'icon_set/dist/text32/text-doc-document-file-type-f27ed688.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f27ed688-cc0b-4a36-83e6-2b70c6de0e5c', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/doc (text)_f27ed688-cc0b-4a36-83e6-2b70c6de0e5c.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-doc-document-file-type-f27ed688',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-d-uppercase', 'letter-o-uppercase', 'letter-c-uppercase')
REFERENCE_EXPORT_SHA256 = 'dccf22f77d37e1aaf6d229b4e63aa44987a554ec84aa60606b2ee596fb8f4087'

























TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'text-doc-document-file-type-f27ed688-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 68
    text_canvas_height = 20
    text_ink_bounds = (2.0, 0.0, 66.0, 20.0)

    def build(self):
        """Source-native uppercase composition for 'DOC'; 4-unit letter spacing."""
        self.add_line('p1-r1-1', (4, 2), (8.88681, 2))
        self.add_bezier('p1-r1-2', (8.88681, 2), ((12.8153, 2), (16, 5.58172), (16, 10)))
        self.add_bezier('p1-r1-3', (16, 10), ((16, 14.4183), (12.8153, 18), (8.88681, 18)))
        self.add_line('p1-r1-4', (8.88681, 18), (4, 18))
        self.add_line('p1-r1-5', (4, 18), (4, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_arc('p2-r1-1', (26, 10), (42, 10), radius_x=8, radius_y=8, large_arc=True, sweep=False)
        self.add_arc('p2-r1-2', (42, 10), (26, 10), radius_x=8, radius_y=8, large_arc=True, sweep=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_bezier('p3-r1-1', (64, 2.6879), ((62.9406, 2.24575), (61.7674, 2), (60.533, 2)))
        self.add_bezier('p3-r1-2', (60.533, 2), ((55.82037, 2), (52, 5.58172), (52, 10)))
        self.add_bezier('p3-r1-3', (52, 10), ((52, 14.4183), (55.82037, 18), (60.533, 18)))
        self.add_bezier('p3-r1-4', (60.533, 18), ((61.7674, 18), (62.9406, 17.7543), (64, 17.3121)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
