"""Independent 32px profile of text-bold-sold-text-indicator-f65bbafd.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'f65bbafd-a164-45e3-85b4-a08690a4a3b5'
SOURCE_PATH = 'icon_set/dist/text32/text-bold-sold-text-indicator-f65bbafd.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f65bbafd-a164-45e3-85b4-a08690a4a3b5', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/sold (text)_f65bbafd-a164-45e3-85b4-a08690a4a3b5.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-bold-sold-text-indicator-f65bbafd',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-s-uppercase', 'letter-o-uppercase', 'letter-l-uppercase', 'letter-d-uppercase')
REFERENCE_EXPORT_SHA256 = '47cf2c501814db46175cdc3023324050d98d7b1876551213dc94a0c618c835db'































TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'text-bold-sold-text-indicator-f65bbafd-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 92
    text_canvas_height = 20
    text_ink_bounds = (2.0, 0.0, 90.00000000000003, 20.000000000000004)

    def build(self):
        """Source-native uppercase composition for 'SOLD'; 4-unit letter spacing."""
        self.add_line('p1-r1-1', (15.9314, 2), (8.77906, 2))
        self.add_bezier('p1-r1-2', (8.77906, 2), ((3.70172, 2), (2.21029, 7.42857), (6.98284, 9.42857)))
        self.add_line('p1-r1-3', (6.98284, 9.42857), (13.4623, 11.608))
        self.add_bezier('p1-r1-4', (13.4623, 11.608), ((17.7211, 13.4286), (16.2526, 18), (11.7787, 18)))
        self.add_line('p1-r1-5', (11.7787, 18), (4, 18))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_arc('p2-r1-1', (26, 10), (42, 10), radius_x=8, radius_y=8, large_arc=True, sweep=False)
        self.add_arc('p2-r1-2', (42, 10), (26, 10), radius_x=8, radius_y=8, large_arc=True, sweep=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_bezier('p3-r1-1', (63, 18), ((59.9428, 18), (52.23973, 18), (52, 18)))
        self.add_line('p3-r1-2', (52, 18), (52, 2))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (76, 2), (80.88681, 2))
        self.add_bezier('p4-r1-2', (80.88681, 2), ((84.81530000000001, 2), (88, 5.58172), (88, 10)))
        self.add_bezier('p4-r1-3', (88, 10), ((88, 14.4183), (84.81530000000001, 18), (80.88681, 18)))
        self.add_line('p4-r1-4', (80.88681, 18), (76, 18))
        self.add_line('p4-r1-5', (76, 18), (76, 2))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', closed=False)
