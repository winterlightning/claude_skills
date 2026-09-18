"""Independent 32px profile of text-gdpr-data-privacy-text-602db514.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '602db514-f9ff-4dc0-874b-ecc9030684ee'
SOURCE_PATH = 'icon_set/dist/text32/text-gdpr-data-privacy-text-602db514.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('602db514-f9ff-4dc0-874b-ecc9030684ee', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/gdpr (text)_602db514-f9ff-4dc0-874b-ecc9030684ee.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-gdpr-data-privacy-text-602db514',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-g-uppercase', 'letter-d-uppercase', 'letter-p-uppercase', 'letter-r-uppercase')
REFERENCE_EXPORT_SHA256 = '26438886455d9fead2f05386555524816d1aef9c9400afbaceeedc941c393052'

class DrawingContainerSymbol(TextSub32):
    icon_id = 'text-gdpr-data-privacy-text-602db514-sub32-symbol'
    related_origin_icon_id = 'text-gdpr-data-privacy-text-602db514-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/text-gdpr-data-privacy-text-602db514-sub32'
    counterpart_icon_id = 'text-gdpr-data-privacy-text-602db514-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 107
    text_ink_bounds = (0.0, 0.0, 107.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (85, 30), (85, 2))
        self.add_line('p1-r1-2', (85, 2), (95, 2))
        self.add_bezier('p1-r1-3', (95, 2), ((101, 2), (104, 6), (104, 9)))
        self.add_bezier('p1-r1-4', (104, 9), ((104, 13), (101, 17), (95, 17)))
        self.add_line('p1-r1-5', (95, 17), (85, 17))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (95, 17), (105, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (57, 30), (57, 2))
        self.add_line('p3-r1-2', (57, 2), (67, 2))
        self.add_bezier('p3-r1-3', (67, 2), ((74, 2), (77, 6), (77, 9)))
        self.add_bezier('p3-r1-4', (77, 9), ((77, 13), (74, 17), (67, 17)))
        self.add_line('p3-r1-5', (67, 17), (57, 17))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
        self.add_line('p4-r1-1', (30, 2), (38, 2))
        self.add_bezier('p4-r1-2', (38, 2), ((46, 2), (50, 9), (50, 16)))
        self.add_bezier('p4-r1-3', (50, 16), ((50, 23), (46, 30), (38, 30)))
        self.add_line('p4-r1-4', (38, 30), (30, 30))
        self.add_line('p4-r1-5', (30, 30), (30, 2))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', closed=False)
        self.add_bezier('p5-r1-1', (19, 6), ((17, 4), (15, 2), (13, 2)))
        self.add_bezier('p5-r1-2', (13, 2), ((7, 2), (2, 9), (2, 17)))
        self.add_bezier('p5-r1-3', (2, 17), ((2, 18), (2, 20), (3, 21)))
        self.add_bezier('p5-r1-4', (3, 21), ((4, 27), (8, 29), (12, 29)))
        self.add_bezier('p5-r1-5', (12, 29), ((17, 29), (22, 24), (22, 16)))
        self.add_line('p5-r1-6', (22, 16), (14, 16))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', 'p5-r1-5', 'p5-r1-6', closed=False)
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
