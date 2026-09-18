"""Independent 32px profile of text-csv-document-file-format-ef63f66f.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = 'ef63f66f-33e4-4301-872e-21ad3cb601c2'
SOURCE_PATH = 'icon_set/dist/text32/text-csv-document-file-format-ef63f66f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ef63f66f-33e4-4301-872e-21ad3cb601c2', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/CSV (text)_ef63f66f-33e4-4301-872e-21ad3cb601c2.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-csv-document-file-format-ef63f66f',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-c-uppercase', 'letter-s-uppercase', 'letter-v-uppercase')
REFERENCE_EXPORT_SHA256 = '472712d2f4953bd4249facf4d238de99cc84129ab0ee66a6601ffa68d56e4458'

class DrawingContainerSymbol(TextSub32):
    icon_id = 'text-csv-document-file-format-ef63f66f-sub32-symbol'
    related_origin_icon_id = 'text-csv-document-file-format-ef63f66f-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/text-csv-document-file-format-ef63f66f-sub32'
    counterpart_icon_id = 'text-csv-document-file-format-ef63f66f-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 77
    text_ink_bounds = (0.001457877762348403, 0.0, 77.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (53, 2), (62, 28))
        self.add_bezier('p1-r1-2', (62, 28), ((62.666666666666664, 29.333333333333332), (63.333333333333336, 30), (64, 30)))
        self.add_bezier('p1-r1-3', (64, 30), ((64.66666666666667, 30), (65, 29.333333333333332), (65, 28)))
        self.add_line('p1-r1-4', (65, 28), (75, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_bezier('p2-r1-1', (45, 6), ((44, 3), (40, 2), (37, 2)))
        self.add_bezier('p2-r1-2', (37, 2), ((33, 2), (29, 4), (28, 9)))
        self.add_bezier('p2-r1-3', (28, 9), ((28, 9), (28, 9), (28, 10)))
        self.add_bezier('p2-r1-4', (28, 10), ((28, 17), (45, 13), (45, 22)))
        self.add_bezier('p2-r1-5', (45, 22), ((46, 22), (46, 22), (46, 23)))
        self.add_bezier('p2-r1-6', (46, 23), ((46, 28), (41, 30), (36, 30)))
        self.add_bezier('p2-r1-7', (36, 30), ((32, 30), (29, 29), (27, 26)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', closed=False)
        self.add_arc('p3-r1-1', (19, 6), (19, 26), radius_x=10, radius_y=14, large_arc=True, sweep=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
