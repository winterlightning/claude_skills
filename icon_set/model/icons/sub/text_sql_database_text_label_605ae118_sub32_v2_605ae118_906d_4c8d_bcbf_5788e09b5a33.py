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

























TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class DrawingVariant2(TextSub32):
    icon_id = 'text-sql-database-text-label-605ae118-sub32-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 68
    text_canvas_height = 20
    text_ink_bounds = (2.0, 0.0, 65.0, 20.000000000000004)

    def build(self):
        """Source-native uppercase composition for 'SQL'; 4-unit letter spacing."""
        self.add_line('p1-r1-1', (15.9314, 2), (8.77906, 2))
        self.add_bezier('p1-r1-2', (8.77906, 2), ((3.70172, 2), (2.21029, 7.42857), (6.98284, 9.42857)))
        self.add_line('p1-r1-3', (6.98284, 9.42857), (13.4623, 11.608))
        self.add_bezier('p1-r1-4', (13.4623, 11.608), ((17.7211, 13.4286), (16.2526, 18), (11.7787, 18)))
        self.add_line('p1-r1-5', (11.7787, 18), (4, 18))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (35.143100000000004, 11.7143), (42.0002, 18))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_arc('p3-r1-1', (26.00049, 9.42857), (40.85763, 9.42857), radius_x=7.42857, radius_y=7.42857, large_arc=True, sweep=False)
        self.add_arc('p3-r1-2', (40.85763, 9.42857), (26.00049, 9.42857), radius_x=7.42857, radius_y=7.42857, large_arc=True, sweep=False)
        self.add_line('p3-r1-3', (26.00049, 9.42857), (26.00049, 9.42857))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_bezier('p4-r1-1', (63, 18), ((59.9428, 18), (52.23973, 18), (52, 18)))
        self.add_line('p4-r1-2', (52, 18), (52, 2))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.relate("connect", 'path-2-1', 'path-3-1')
