# Independent container symbol; edit separately from linked side sub-icon.
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

class DrawingContainerSymbol(TextSub32):
    icon_id = 'text-doc-document-file-type-f27ed688-sub32-symbol'
    variant_of = 'text-doc-document-file-type-f27ed688-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/text-doc-document-file-type-f27ed688-sub32'
    counterpart_icon_id = 'text-doc-document-file-type-f27ed688-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 77
    text_ink_bounds = (0.0, 0.0, 77.0, 32.0)

    def build(self):
        self.add_arc('p1-r1-1', (75, 6), (75, 26), radius_x=10, radius_y=14, large_arc=True, sweep=False)
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_bezier('p2-r1-1', (29, 16), ((29, 8), (34, 2), (39, 2)))
        self.add_bezier('p2-r1-2', (39, 2), ((45, 2), (50, 8), (50, 16)))
        self.add_bezier('p2-r1-3', (50, 16), ((50, 24), (45, 30), (39, 30)))
        self.add_bezier('p2-r1-4', (39, 30), ((34, 30), (29, 24), (29, 16)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (2, 2), (10, 2))
        self.add_bezier('p3-r1-2', (10, 2), ((18, 2), (21, 9), (21, 16)))
        self.add_bezier('p3-r1-3', (21, 16), ((21, 23), (18, 30), (10, 30)))
        self.add_line('p3-r1-4', (10, 30), (2, 30))
        self.add_line('p3-r1-5', (2, 30), (2, 2))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
