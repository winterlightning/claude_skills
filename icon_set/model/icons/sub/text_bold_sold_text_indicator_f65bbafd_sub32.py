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

class Drawing(TextSub32):
    icon_id = 'text-bold-sold-text-indicator-f65bbafd-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 102
    text_ink_bounds = (0.0, 0.0, 102.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (81, 2), (88, 2))
        self.add_bezier('p1-r1-2', (88, 2), ((96, 2), (100, 9), (100, 16)))
        self.add_bezier('p1-r1-3', (100, 16), ((100, 23), (96, 30), (88, 30)))
        self.add_line('p1-r1-4', (88, 30), (81, 30))
        self.add_line('p1-r1-5', (81, 30), (81, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (56, 2), (56, 30))
        self.add_line('p2-r1-2', (56, 30), (73, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_arc('p3-r1-1', (28, 16), (48, 16), radius_x=10, radius_y=14, large_arc=True, sweep=True)
        self.add_arc('p3-r1-2', (48, 16), (28, 16), radius_x=10, radius_y=14, large_arc=True, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_bezier('p4-r1-1', (20, 6), ((19, 3), (15, 2), (12, 2)))
        self.add_bezier('p4-r1-2', (12, 2), ((8, 2), (4, 4), (3, 9)))
        self.add_bezier('p4-r1-3', (3, 9), ((3, 9), (3, 9), (3, 10)))
        self.add_bezier('p4-r1-4', (3, 10), ((3, 17), (20, 13), (20, 22)))
        self.add_bezier('p4-r1-5', (20, 22), ((20, 22), (20, 22), (20, 23)))
        self.add_bezier('p4-r1-6', (20, 23), ((20, 28), (16, 30), (11, 30)))
        self.add_bezier('p4-r1-7', (11, 30), ((7, 30), (4, 29), (2, 26)))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', 'p4-r1-6', 'p4-r1-7', closed=False)
