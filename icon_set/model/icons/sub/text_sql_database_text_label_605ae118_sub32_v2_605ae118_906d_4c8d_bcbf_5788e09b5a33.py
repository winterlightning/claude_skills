# Variant of text-sql-database-text-label-605ae118-sub32; parent file remains unchanged.
"""Independent 32px profile of text-sql-database-text-label-605ae118.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = '605ae118-906d-4c8d-bcbf-5788e09b5a33'
SOURCE_PATH = 'icon_set/dist/text32/text-sql-database-text-label-605ae118.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('605ae118-906d-4c8d-bcbf-5788e09b5a33', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/sql (text)_605ae118-906d-4c8d-bcbf-5788e09b5a33.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-sql-database-text-label-605ae118',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-s-uppercase', 'letter-q-uppercase', 'letter-l-uppercase')
REFERENCE_EXPORT_SHA256 = '554161d8553e308f8380a918c87e4e3377f42c3c3f272fcb0512cb62e51989d4'

class DrawingVariant2(TextSub32):
    icon_id = 'text-sql-database-text-label-605ae118-sub32-v2'
    variant_of = 'text-sql-database-text-label-605ae118-sub32'
    variant_label = 'Record the actual joined strokes; preserve reviewed artwork'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 70
    text_ink_bounds = (0.0, 0.0, 70.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (53, 2), (53, 27))
        self.add_line('p1-r1-2', (53, 27), (68, 27))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_arc('p2-r1-1', (26, 15), (44, 15), radius_x=9, radius_y=13, large_arc=True, sweep=True)
        self.add_arc('p2-r1-2', (44, 15), (26, 15), radius_x=9, radius_y=13, large_arc=True, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (38, 21), (46, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_bezier('p4-r1-1', (18, 5), ((17, 3), (14, 2), (11, 2)))
        self.add_bezier('p4-r1-2', (11, 2), ((7, 2), (3, 4), (3, 8)))
        self.add_bezier('p4-r1-3', (3, 8), ((3, 8), (3, 9), (3, 9)))
        self.add_bezier('p4-r1-4', (3, 9), ((3, 16), (18, 12), (19, 20)))
        self.add_bezier('p4-r1-5', (19, 20), ((19, 20), (19, 20), (19, 21)))
        self.add_bezier('p4-r1-6', (19, 21), ((19, 25), (14, 27), (10, 27)))
        self.add_bezier('p4-r1-7', (10, 27), ((7, 27), (3, 26), (2, 23)))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', 'p4-r1-6', 'p4-r1-7', closed=False)
        self.relate('connect', 'path-2-1', 'path-3-1')
